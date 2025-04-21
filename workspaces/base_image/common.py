import base64
import os
import logging
import urllib
import subprocess
import functools
import re
import requests
import xml.etree.ElementTree as ET


import litellm
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET

from config import *

logging.basicConfig(level=logging.INFO)

def extract_test_results(xml_file):
    """
    Parses a cocotb XML file and returns a tuple:
    (number of test cases, number of failures)
    
    If the file is not a valid XML, it notifies the user and returns None.
    
    Args:
        xml_file (str): Path to the XML file.
    
    Returns:
        tuple or None: (num_testcases, num_failures) if successful, else None.
    """
    try:
        tree = ET.parse(xml_file)
    except FileNotFoundError:
        print(f"Error: The file '{xml_file}' does not exist.")
        return None
    except ET.ParseError as e:
        print(f"Error: The file '{xml_file}' is not a valid XML file. {e}")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return None

    root = tree.getroot()
    
    # Count the <testcase> elements
    test_cases = root.findall(".//testcase")
    num_testcases = len(test_cases)
    
    # Count the <failure> elements within the testcases
    failures = root.findall(".//failure")
    num_failures = len(failures)
    
    return num_testcases, num_failures



def grader(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result is None:
                logging.warning(f"Grader returns None, using False instead")
                return False
            return result
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {str(e)}")
            return False
    return wrapper
    

# messages: a list of message.
# example [{ "content": "Hello, how are you?","role": "user"}]
def modify_messages(checkpoints_list_msg, file_content):

    # messages original content are the checkpoints
    messages = checkpoints_list_msg[:]
    EVAL_JUDGE = """
        You are a judge evaluating a file content against predefined checkpoints.  
        Each checkpoint has an assigned score.

        Task:  
        1. Analyze the file based on the given checkpoints.  
        2. If a checkpoint is met, assign the corresponding score else assign zero. 
        3. Generate a detailed report with the following format:  
            - Clearly list each checkpoint and the corresponding score assigned.  
            - Conclude the report with the final score in the format:  
                **Final Score: <score>/<total>**
        Don't make introduction or conclusion just respond directly with the report in the format specified above.

    """
    CHEKCPOINTS_INTRO = """

        # Checkpoints

    """

    FILE_SPECIFICATION = """

        Listed below are the contents for all files in the workspace. You are required to evaluate only the file that is
        relevant to the defined checkpoints.

    """

    # Prepend the EVAL_JUDGE and CHEKCPOINTS_INTRO to the messages and append the file content
    messages[0]["content"] = f"{EVAL_JUDGE}{CHEKCPOINTS_INTRO}{checkpoints_list_msg[0]['content']}{FILE_SPECIFICATION}{file_content}"

    return messages


def llm_complete(checkpoints_list_msg, file_content=None):
    if TEST_MODE:
        return {'choices': [{'message': {"content": "Hello, how are you?","role": "user"}}]}
    
    messages = modify_messages(checkpoints_list_msg, file_content)


    return litellm.completion(
        api_key=LITELLM_API_KEY,
        base_url=LITELLM_BASE_URL,
        model=LITELLM_MODEL,
        messages=messages
    ).json()



def llm_confirm(script=None, cocotb_test=False, verilog_tb_files_dict=None, python_files_dict=None, logs=None): # the function confirms the contents of sh script are used to run the testbench and that the testbench has assertions that stop execution on a failed test.
    # user assert to raise smooth error if any dict is empty such that if both is empty error is raised
    assert verilog_tb_files_dict or python_files_dict, "No verilog or python files found in the workspace."
    # make warning if cocotb_test is true but python_files_Dict is empty or if python_files_dict is not empty but cocotb_test is false. pritn meaninful message
    if cocotb_test and not python_files_dict:
        print("Warning: cocotb_test is true but no python files found in the workspace.")
    elif not cocotb_test and python_files_dict:
        print("Warning: cocotb_test is false but python files found in the workspace.")    
    
    workspace_content_truncated = None

    # instead workspace_content_truncated, will be assigned such that if cocotb_test is true, the build function will be passed the python_files_dict else the verilog_tb_files_dict  will be assigned
    if cocotb_test:
        workspace_content_truncated = build_workspace_content_truncated(python_files_dict, "python", 1000)
    else:
        workspace_content_truncated = build_workspace_content_truncated(verilog_tb_files_dict, "verilog", 1000)


    if TEST_MODE:
        return {'choices': [{'message': {"content": "Hello, how are you?","role": "user"}}]}
    
    messages = [
        {
            "content": f"Answer only yes or no. Given that the workspace contains the following files and their contents (only part of each file is shown): \n---\n{workspace_content_truncated}\n---\n, is the following script:\n```bash\n{script}\n```\nused to run the testbench?"  ,
            "role": "user"}
    ]

    # report messages in logs[3]
    logs[3] += f"\n## LLM Confirmation Prompt (Used to run testbench?):\n"
    logs[3] += f"{messages[0]['content']}\n"

    llm_response =  litellm.completion(
        api_key=LITELLM_API_KEY,
        base_url=LITELLM_BASE_URL,
        model=LITELLM_MODEL,
        messages=messages
    ).json()

    return llm_response

def execute_testbench(shell_script_path, files_dict,verilog_tb_files_dict, python_files_dict, logs):

    # Assigning the boolean fatal_macro true if $fatal macro is found in the content of any file in the verilog_tb_files_dict by looping over the dictionary
    fatal_macro = any("$fatal" in content for content in verilog_tb_files_dict.values())

    # Assigning the boolean cocotb_test true if test_runner.py is found as the name of one of the files in files_dict
    cocotb_test = any("test_runner.py" in content for content in files_dict.keys())

    # report boolean variables in logs[3]
    logs[3] += f"\n## Boolean Variables:\n"
    logs[3] += f"- fatal_macro: {fatal_macro}\n"
    logs[3] += f"- cocotb_test: {cocotb_test}\n"

    # if verilog_tb_files_dict is empty and cocotb_test is false print appropriate message and return (0,1)
    if not verilog_tb_files_dict and not cocotb_test:
        print("No verilog  testbench files found in the workspace.")
        return (0, 1)
    
    if shell_script_path:
        # report shell script path in logs[3]
        logs[3] += f"\n## Shell Script Path:\n"
        logs[3] += f"{shell_script_path}\n"
        
        try:
            # Read the file content
            with open(shell_script_path, 'r') as file:
                script = file.read()
                # report script in logs[3]
                logs[3] += f"\n## Shell Script Content:\n"
                logs[3] += f"```bash\n{script}\n```\n"
        except Exception as e:
            print(f"Error reading file: {e}")
            return (0, 1)

        # Pass the file content to llm_confirm() and get the response
        llm_response = llm_confirm(script, cocotb_test, verilog_tb_files_dict, python_files_dict, logs) # is the script used to run a testbench?


        # Extract the confirmation text and check for 'yes'
        confirmation_text = llm_response['choices'][0]['message']['content'].lower()
        # report llm response in logs[3]
        logs[3] += f"\n## LLM Confirmation on the shell script (Used to run testbench?):\n"
        logs[3] += f"{confirmation_text}\n"

        if "yes" in confirmation_text:
            try:
                # Run the shell script with a timeout of 250 seconds
                result = subprocess.run(
                    shell_script_path,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=250  # Timeout after 250 seconds
                )
                # Check if the exit code indicates success
                # report result.returncode in logs[3]
                logs[3] += f"\n## Return Code of Testbench Execution:\n"
                logs[3] += f"{result.returncode}\n"
                
                if result.returncode == 0:
                    # check if cocotb_test is true 
                    if cocotb_test:
                        # check if the resultant xml indeed does not have any failures
                        _, num_failures = extract_test_results(find_file_path("results.xml"))
                        # report results.xml content in logs[3]
                        logs[3] += f"\n## Results.xml Content:\n"
                        # read file content and report it
                        with open(find_file_path("results.xml"), 'r') as file:
                            logs[3] += f"```xml\n{file.read()}\n```\n"
                        # report num_failures in logs[3]
                        logs[3] += f"\n## Number of Failures:\n"
                        logs[3] += f"{num_failures}\n"
                        if num_failures == 0:
                            # report testbench execution status
                            logs[3] += f"\n## Testbench Execution Status:\n"
                            logs[3] += f"Testbench execution successful.\n"
                            return (1, 1)
                        else:
                            # report testbench execution status
                            logs[3] += f"\n## Testbench Execution Status:\n"
                            logs[3] += f"Testbench execution failed with {num_failures} failures.\n"
                            return (0, 1)
                    else: # then it is a verilog testbench
                        #check if the fatal macro is used in the testbench
                        if fatal_macro:
                            # report testbench execution status
                            logs[3] += f"\n## Testbench Execution Status:\n"
                            logs[3] += f"Testbench execution successful.\n"
                            return (1, 1)
                        else:
                            # report testbench execution status
                            logs[3] += f"\n## Testbench Execution Status:\n"
                            logs[3] += f"Testbench execution not trustworthy as $fatal macro is not used in the testbench.\n"
                            # pass the result of running the command above to the llm with the question of wether this text indicates that all test cases has been passed and only ask the llm to answer only with yes or no
                            messages = [ 
                                { "content": f"Answer only yes or no. Given the following output:\n```{result.stdout}```\n, does the output indicate that all test cases have passed?",
                                "role": "user"}
                            ]
                            # report result.stdout in logs[3]
                            logs[3] += f"\n## stdout of testbench execution:\n"
                            logs[3] += f"```{result.stdout}\n```\n"
                            llm_response = litellm.completion(
                                api_key=LITELLM_API_KEY,
                                base_url=LITELLM_BASE_URL,
                                model=LITELLM_MODEL,
                                messages=messages
                            ).json()
                            confirmation_text = llm_response['choices'][0]['message']['content'].lower()

                            # report llm response in logs[3]
                            logs[3] += f"\n## LLM Confirmation (stdout indicates successful execution?):\n"
                            logs[3] += f"{confirmation_text}\n"
                            if "yes" in confirmation_text:
                                return (1, 1)
                            else:
                                return (0, 1)                            
                else:
                    return (0, 1)
            except subprocess.TimeoutExpired:
                print("Testbench execution timed out after 250 seconds.")
                return (0, 1)
            except Exception as e:
                print(f"Error executing testbench: {e}")
                return (0, 1)
        else: # script is not used to run the testbench
            return (0, 1)
    else:
        # report no shell script in logs[3]
        logs[3] += f"\n## Shell Script Path:\n"
        logs[3] += f"No shell script found in the workspace.\n"
        return (0, 1)


def find_files(pattern=None, search_paths=None, command=None, first_match_only=False):
    """Unified function for finding files in the system.
    
    Args:
        pattern (str, optional): File pattern to search for (e.g. "run_test.sh")
        search_paths (list, optional): List of paths to search in. Defaults to common paths.
        command (str, optional): Direct find command to execute. Takes precedence over pattern/paths.
        first_match_only (bool): Return only the first match found. Defaults to False.
    
    Returns:
        Union[str, List[str], None]: Found file path(s) or None if nothing found
    """
    try:
        if command:
            # Direct command execution mode
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, text=True)
        else:
            # Pattern-based search mode
            if search_paths is None:
                search_paths = ["/workspace", "/outputs", "/openhands/workspace"]
            
            for path in search_paths:
                try:
                    cmd = ["find", path]
                    if pattern:
                        cmd.extend(["-path", f"*/{pattern}"])
                    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
                    if result.stdout.strip():
                        break
                except subprocess.CalledProcessError:
                    continue
            else:
                return None if first_match_only else []
        
        lines = result.stdout.strip().splitlines()
        if not lines:
            return None if first_match_only else []
            
        return lines[0] if first_match_only else lines
            
    except Exception as e:
        logging.error(f"Error in find_files: {e}")
        return None if first_match_only else []

# Legacy function maintained for backward compatibility
def find_file_path(file_path):
    return find_files(pattern=file_path, first_match_only=True)

# Legacy function maintained for backward compatibility
def run_find_command(find_cmd):
    """Run a find command and return a list of file paths."""
    return find_files(command=find_cmd) or []

def collect_files(find_cmd, exclude):
    """
    Run a find command and collect files that do not contain any of the
    excluded substrings. Returns a dictionary mapping file paths to their content.
    """
    files = {}
    file_paths = run_find_command(find_cmd)
    for file_path in file_paths:
        # Skip files that contain any substring from the exclude list
        if any(sub in file_path for sub in exclude):
            continue
        try:
            with open(file_path, 'r') as f:
                files[file_path] = f.read()
        except Exception as e:
            print(f"Could not read file {file_path}: {e}")
    return files

def build_workspace_content(files, file_type):
    """
    Build a workspace content string that lists each file and its content
    in the given markdown format.
    """
    # content = "Content Gamma"
    workspace_content = ""
    for file_name, file_content in files.items():
        workspace_content += f"\n#### {file_name}\n"
        if file_type == "any":
            workspace_content += f"```\n{file_content}\n```\n"
        else:   
            workspace_content += f"```{file_type}\n{file_content}\n```\n"
    
    return workspace_content

def build_workspace_content_truncated(files, file_type, n):
    """
    Build a workspace content string that lists each file and its content
    in the given markdown format.
    """
    content_truncated = ""
    for file_name, content in files.items():
        content_truncated += f"\n#### {file_name}\n"
        if file_type == "any":
            content_truncated += f"```\n{content[0:n]}\n```\n"
        else:   
            content_truncated += f"```{file_type}\n{content[0:n]}\n```\n"
    return content_truncated

def check_with_llm_F(checkpoints, file_content, file_type, logs): # to handle the case of functinality score

    if len(checkpoints) == 0:
        print(f"position 1: returning {(0, 0)}")
        print("No checkpoints provided, Finished check_with_llm_F function called within grade_checkpoint_llm")
        return (0, 0)

    messages = [
        {
            "content": f"{checkpoints}",
            "role": "user"}
    ]

    llm_response = llm_complete(messages, file_content)
    llm_response_txt = llm_response['choices'][0]['message']['content'].lower()

    if (file_type == "verilog"):
        logs[1] += f"\n## Evaluation Report:\n"
        logs[1] += f"{llm_response_txt}"
    elif (file_type == "verilog/python"):
        logs[2] += f"\n## Evaluation Report:\n"
        logs[2] += f"{llm_response_txt}"



    score = re.search(r'(?i)final\s+score:\s*(\d{1,2})/\d{1,2}', llm_response_txt)
    total_score = re.search(r'(?i)final\s+score:\s*\d{1,2}/(\d{1,3})', llm_response_txt)
    if score:
        print(f"position 2: returning {(int(score.group(1)), int(total_score.group(1)))}")
        print("Finished check_with_llm_F function called within grade_checkpoint_llm")
        return (int(score.group(1)), int(total_score.group(1)))
    else:
        print(f"position 3: returning {(0, 0)}")
        print("Finished check_with_llm_F function called within grade_checkpoint_llm")
        return (0, 0)


def is_verilog_testbench(content):
    """
    Checks if the given Verilog file content indicates a testbench.
    
    Heuristics used:
      1. A module declaration must exist.
      2. If the module's name includes typical testbench keywords (e.g., starts with "tb" or contains "test")
         then it is likely a testbench.
      3. If the module declaration has an empty port list, that's a strong testbench signal.
      4. If the file contains simulation-specific constructs (like $dumpfile, $monitor, or initial blocks)
         and the module name/port list do not strongly indicate a design module, then it may be a testbench.
    
    Args:
        content (str): The content of the Verilog file to check
    
    Returns:
        bool: True if the content indicates a testbench, False otherwise.
    """

    # Remove block comments (/* ... */)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # Remove single line comments (//...)
    content = re.sub(r'//.*', '', content)

    # Search for module declarations.
    # This regex looks for a line starting with the word "module",
    # followed by the module name (captured in group 1) and an optional port list (captured in group 2).
    module_pattern = re.compile(r'\bmodule\s+(\w+)\s*(\([^;]*\))?\s*;')
    modules = module_pattern.findall(content)

    if not modules:
        return False  # No module found

    # Look for simulation-specific constructs.
    sim_tasks = re.search(r'\$(dumpfile|monitor|display)\b', content)
    initial_block = re.search(r'\binitial\b', content)

    # Evaluate each module declaration.
    for module_name, port_list in modules:
        module_name_lower = module_name.lower()
        # Check if the module name clearly indicates a testbench.
        if module_name_lower.startswith("tb") or "test" in module_name_lower:
            return True

        # Check if the port list is present and empty.
        if port_list is not None:
            # Remove surrounding parentheses and whitespace.
            ports = port_list.strip()[1:-1].strip()
            if ports == "":
                return True
        else:
            # If there is no port list at all, that is also a common testbench indicator.
            return True

    # Even if the above checks didn't fire, simulation constructs may be a hint.
    # But to avoid false positives (like design modules that use initial blocks), require both:
    # - simulation constructs present AND a module with an empty port list or a testbench-like name.
    if (sim_tasks or initial_block):
        for module_name, port_list in modules:
            module_name_lower = module_name.lower()
            # If the module name doesn't strongly look like a design module
            # (i.e., it has a testbench-like name or an empty port list), then mark as testbench.
            if (module_name_lower.startswith("tb") or "test" in module_name_lower):
                return True
            if port_list is not None:
                ports = port_list.strip()[1:-1].strip()
                if ports == "":
                    return True
            else:
                return True

    # If none of the above conditions are met, we assume it's a design module.
    return False


@grader
def grade_checkpoint_llm(CHECK_POINTS, file_type, files_dict, logs):
    if files_dict:
        workspace_content = build_workspace_content(files_dict, file_type)
        # report workspace content if file_type is verilog/python to include all files.
        if file_type == 'verilog/python':
            logs[0] += "\n## Workspace Content:\n"
            # check if workspace_content is successfully returned
            if not workspace_content:
                logs[0] += "\n ### Workspace content is empty"
            else:
                # append workspace content to Main Module element in logs
                logs[0] += f"\n{workspace_content}"
        # just for debugging
        # return (0, 0) # TODO delete this.

        print("calling check_with_llm_F function within grade_checkpoint_llm") 
        return check_with_llm_F(CHECK_POINTS, workspace_content, file_type, logs)
    else:
        print("Finished grade_checkpoint_llm function")
        print("workspace is empty")
        return (0, 0)