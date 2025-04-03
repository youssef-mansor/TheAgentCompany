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

IMAGE_JPEG = 'image/jpeg'
IMAGE_PNG = 'image/png'

workspace_files = None #all verilog and python files in the workspace names
workspace_content = None #all verilog and python files in the workspace content
cocotb_test = None # boolean to check if cocotb test is used
fatal_macro = None # boolean to check if $fatal macro is used

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



def llm_confirm(file_content=None): # the function confirms the contents of sh script are used to run the testbench and that the testbench has assertions that stop execution on a failed test.

    # make the logic to add the rest of the files here
    files = {}
    search_paths = ["/workspace", "/outputs", "/openhands/workspace/"]
    exclude = ['cocotb_iverilog_dump.v', 'openhands/miniforge3', 'runs']

    for directory in search_paths:
        file_cmd = f"find {directory} -type f \\( -name '*.bash' -o -name '*.sh' -o -name '*.py' -o -name '*.v' -o -name '*.sv' -o -iname 'makefile*' \\)"
        files.update(collect_files(file_cmd, exclude))

    workspace_content = build_workspace_content_truncated(files, "any", 1000)


    if TEST_MODE:
        return {'choices': [{'message': {"content": "Hello, how are you?","role": "user"}}]}
    
    print(f"file content to confirm:\n{file_content}\n")

    messages = [
        {
            "content": f"Answer only yes or no. Given that the workspace contains the following files and their contents: \n---\n{workspace_content}\n---\n, is the following script:\n```bash\n{file_content}\n```\nused to run the testbench?"  ,
            "role": "user"}
    ]

    llm_response =  litellm.completion(
        api_key=LITELLM_API_KEY,
        base_url=LITELLM_BASE_URL,
        model=LITELLM_MODEL,
        messages=messages
    ).json()

    return llm_response

def execute_testbench(shell_script_path):
    if shell_script_path:
        try:
            # Read the file content
            with open(shell_script_path, 'r') as file:
                file_content = file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return (0, 1)

        # Pass the file content to llm_confirm() and get the response
        llm_response = llm_confirm(file_content)

        # Extract the confirmation text and check for 'yes'
        confirmation_text = llm_response['choices'][0]['message']['content'].lower()
        print(f"confirmation_text: {confirmation_text}\n")
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
                if result.returncode == 0:
                    # check if coco_tb test is true 
                    if cocotb_test:
                        # check if the resultant xml indeed does not have any failures
                        _, num_failures = extract_test_results(find_file_path("results.xml"))
                        if num_failures == 0:
                            print("Testbench execution successful.")
                            return (1, 1)
                        else:
                            print(f"Testbench execution failed with {num_failures} failures.")
                            return (0, 1)
                    else: # then it is a verilog testbench
                        #check if the fatal macro is used in the testbench
                        if fatal_macro:
                            print("Testbench execution successful.")
                            return (1, 1)
                        else:
                            print("Testbench execution not trustworthy as $fatal macro is not used in the testbench.")
                            # pass the result of running the command above to the llm with the question of wether this text indicates that all test cases has been passed and only ask the llm to answer only with yes or no
                            messages = [ 
                                { "content": f"Answer only yes or no. Given the following output:\n```{result.stdout}```\n, does the output indicate that all test cases have passed?",
                                "role": "user"}
                            ]
                            print(f"messages for checking the stdout of running the testbench: {messages}")
                            llm_response = litellm.completion(
                                api_key=LITELLM_API_KEY,
                                base_url=LITELLM_BASE_URL,
                                model=LITELLM_MODEL,
                                messages=messages
                            ).json()
                            confirmation_text = llm_response['choices'][0]['message']['content'].lower()
                            if "yes" in confirmation_text:
                                print("Testbench execution successful and all test cases have passed.") 
                                return (1, 1)
                            else:
                                print("Some test cases didn't pass")
                                return (0, 1)                            
                else:
                    print(f"Testbench execution failed with exit code {result.returncode}")
                    return (0, 1)
            except subprocess.TimeoutExpired:
                print("Testbench execution timed out after 250 seconds.")
                return (0, 1)
            except Exception as e:
                print(f"Error executing testbench: {e}")
                return (0, 1)
        else:
            print("script is not used to run the testbench")
            return (0, 1)
    else:
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
    workspace_content = ""
    for file_name, content in files.items():
        workspace_content += f"\n# {file_name}\n"
        if file_type == "any":
            workspace_content += f"```\n{content}\n```\n"
        else:   
            workspace_content += f"```{file_type}\n{content}\n```\n"
    return workspace_content

def build_workspace_content_truncated(files, file_type, n):
    """
    Build a workspace content string that lists each file and its content
    in the given markdown format.
    """
    workspace_content = ""
    for file_name, content in files.items():
        workspace_content += f"\n# {file_name}\n"
        if file_type == "any":
            workspace_content += f"```\n{content[0:n]}\n```\n"
        else:   
            workspace_content += f"```{file_type}\n{content[0:n]}\n```\n"
    return workspace_content

def check_with_llm_F(checkpoints, file_content): # to handle the case of functinality score

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

    print("\n************************************Evaluation Report*******************************************")
    llm_response_txt = llm_response['choices'][0]['message']['content'].lower()
    print(llm_response_txt)
    print("*************************************************************************************************\n")


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

@grader
def grade_checkpoint_llm(CHECK_POINTS, file_type):
    # List of substrings to exclude from file names
    global workspace_files
    global workspace_content
    global cocotb_test
    global fatal_macro

    exclude = ['test_runner.py', 'cocotb_iverilog_dump.v', 'openhands/miniforge3']
    
    files = {}
    search_paths = ["/workspace", "/outputs", "/openhands/workspace/"]

    # Collect Verilog files (.v and .sv) from each search path
    for directory in search_paths:
        verilog_cmd = f"find {directory} -type f \\( -name '*.v' -o -name '*.sv' \\) -not -path '*/runs/*'"
        files.update(collect_files(verilog_cmd, exclude))
    
    # Optionally include Python files if file_type is 'verilog/python'
    if file_type == 'verilog/python':
        for directory in search_paths:
            python_cmd = f"find {directory} -type f -name '*.py'"
            files.update(collect_files(python_cmd, exclude))

    
    workspace_files = list(files.keys())
    print(f"workspace files are assigned: {workspace_files}")
    # Build workspace content and send to the LLM if any files are found
    if files:
        workspace_content = build_workspace_content(files, file_type)
        # Logic for checking if test_runner.py exists (cocotb testing is used) in workspace_files and if no, checking for $fatal macro in the workspace_content
        cocotb_test = any(f.endswith(".py") for f in workspace_files)
        fatal_macro = "$fatal" in workspace_content
        print(f"cocotb_test: {cocotb_test}")
        print(f"fatal_macro: {fatal_macro}")
        print("calling check_with_llm_F function within grade_checkpoint_llm") 
        return check_with_llm_F(CHECK_POINTS, workspace_content)
    else:
        print("Finished grade_checkpoint_llm function")
        print("workspace is empty")
        return (0, 0)



def check_repo_exists(project_name: str):
    try:
        if project_name not in PROJECT_FILES:
            logging.warning(f"Unknown project: {project_name}")
            return False
            
        file_path = os.path.join('/workspace', project_name, PROJECT_FILES[project_name])
        return os.path.isfile(file_path)
    except Exception as e:
        logging.warning(f"Error checking file: {e}")
        return False
    
    
