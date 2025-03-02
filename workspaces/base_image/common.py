import base64
import os
import logging
import urllib
import subprocess
import functools
import re
import requests

import litellm
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET

from config import *

logging.basicConfig(level=logging.INFO)

IMAGE_JPEG = 'image/jpeg'
IMAGE_PNG = 'image/png'

workspace_files = None #all verilog and python files in the workspace names


class MockRocketChatClient:

    class JsonResponse:
        def json(self):
            return {'users': [], 'messages': []}

    def __getattr__(self, name):
        def method(*args, **kwargs):
            return self.JsonResponse()
        return method


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

def llm_confirm(file_content=None):
    if TEST_MODE:
        return {'choices': [{'message': {"content": "Hello, how are you?","role": "user"}}]}
    
    print(f"file content to confirm:\n{file_content}\n")

    messages = [
        {
            "content": f"Given that the workspace contains the following files: {workspace_files}, is the following script:\n```bash\n{file_content}\n```\nused to run the testbench?"  ,
            "role": "user"}
    ]

    return litellm.completion(
        api_key=LITELLM_API_KEY,
        base_url=LITELLM_BASE_URL,
        model=LITELLM_MODEL,
        messages=messages
    ).json()

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
                # Run the shell script
                result = subprocess.run(
                    shell_script_path,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                # Check if the exit code indicates success
                if result.returncode == 0:
                    return (1, 1)
                else:
                    return (0, 1)
            except Exception as e:
                print(f"Error executing testbench: {e}")
                return (0, 1)
        else:
            print("Testbench execution not confirmed by LLM.")
            return (0, 1)
    else:
        return (0, 1)

def find_file_path(file_path):
    search_paths = ["/workspace", "/home", "/outputs", "/openhands"]
    for path in search_paths:
        print(f"current path: {path}")
        try:
            command = ["find", path, "-path", f"*/{file_path}"]
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
            lines = result.stdout.splitlines()
            # if lines:
            #     print(f"I will return lines[0]: {lines[0]} from this list {lines}")
            # print(f"lines: \n{lines}")
            if lines:
                return lines[0]
        except subprocess.CalledProcessError:
            continue  # If no results are found in this path, continue to the next

def run_find_command(find_cmd):
    """Run a find command and return a list of file paths."""
    try:
        result = subprocess.run(find_cmd, shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout.strip().splitlines()
        else:
            return []
    except Exception as e:
        print(f"Error running command '{find_cmd}': {e}")
        return []

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
        workspace_content += f"```{file_type}\n{content}\n```\n"
    return workspace_content

def check_with_llm_F(checkpoints, file_content): # to handle the case of functinality score

    if len(checkpoints) == 0:
        print(f"position 1: returning {(0, 0)}")
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
        return (int(score.group(1)), int(total_score.group(1)))
    else:
        print(f"position 3: returning {(0, 0)}")
        return (0, 0)

@grader
def grade_checkpoint_llm(CHECK_POINTS, file_type):
    # List of substrings to exclude from file names
    global workspace_files
    exclude = ['test_runner.py', 'cocotb_iverilog_dump.v', 'openhands/miniforge3']
    
    files = {}
    search_paths = ["/workspace", "/outputs", "/openhands/workspace/"]

    # Collect Verilog files (.v and .sv) from each search path
    for directory in search_paths:
        verilog_cmd = f"find {directory} -type f \\( -name '*.v' -o -name '*.sv' \\)"
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
        return check_with_llm_F(CHECK_POINTS, workspace_content)
    else:
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
    
    