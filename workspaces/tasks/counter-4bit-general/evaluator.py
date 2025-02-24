import os
import ast
import sys
import logging
import subprocess
import time
import re


from typing import List
from scoring import Result, Checkpoint
from common import *

REPO_DIR = '/workspace/openhands/'
UT_FILE = REPO_DIR + 'tests/unit/test_agent_skill.py'
COV_FILE = REPO_DIR + 'tests/unit/test_agent_skill_coverage.xml'


with open('/instruction/checkpoints.md', 'r') as f:
    content = f.read()

# Split by lines containing only hyphens (allowing extra dashes)
sections = re.split(r'\n\s*-{3,}\s*\n', content)
testbench_path = None # holds the evaluated testbench path

# sections[0]: Action Checkpoints (ignored)
# sections[1]: Main Module Checkpoints
# sections[2]: Testbench Comprehensiveness
# sections[3]: Functionality

CHECK_POINTS_MODULE = sections[1].strip()
CHECK_POINTS_TB = sections[2].strip()
CHECK_POINTS_REPORT = sections[3].strip()


def config_env(dir_path):
    """configure enviroment"""
    try:
        os.chdir(dir_path)

        subprocess.run(["poetry", "--version"], check=True, capture_output=True)
    except Exception as e:
        logging.warning(f"is_test_run configure step 1. {e}")
        subprocess.run([sys.executable, "-m", "pip", "install", "poetry"], check=True)
        time.sleep(5)

    logging.info(f"Installing dependencies...")
    try:
        result = subprocess.run(["poetry", "install"], capture_output=True, text=True)
    except Exception as e:
        logging.warning(f"is_test_run configure step 2. {e}")
        return False

    if result.returncode != 0:
        logging.warning(f"Error installing dependencies. {e}")
        logging.warning(f"{result.stderr}")
        return False
    else:
        logging.info(f"Dependencies installed successfully.")

    
def check_with_llm_F(checkpoints, file_content): # to handle the case of functinality score

    if len(checkpoints) == 0:
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
        return (int(score.group(1)), int(total_score.group(1)))
    else:
        return (0, 0)
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

@grader
def grade_checkpoint_llm(CHECK_POINTS, file_type):
    # List of substrings to exclude from file names
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
    
    # Build workspace content and send to the LLM if any files are found
    if files:
        workspace_content = build_workspace_content(files, file_type)
        return check_with_llm_F(CHECK_POINTS, workspace_content)
    else:
        print("workspace is empty")
        return (0, 0)
    

def execute_testbench(shell_script_path):
    if shell_script_path:
        try:
            # Run the shell script
            result = subprocess.run(shell_script_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Check if the exit code indicates success
            if result.returncode == 0:
                return (1, 1)
            else:
                return (0, 1)
        except Exception as e:
            print(f"Error executing testbench: {e}")
            return (0, 1)
    else:
        return (0, 1)


def grade_checkpoints(trajectory="") -> Result:
    checkpoints: List[Checkpoint] = []
    result = Result(checkpoints)

    # Define the total scores corresponding to each checkpoint function with unique keys
    scores = {
        'checkpoint_llm_module': grade_checkpoint_llm(CHECK_POINTS_MODULE, 'verilog'),
        'checkpoint_llm_tb': grade_checkpoint_llm(CHECK_POINTS_TB, 'verilog/python'),
        'checkpoint_llm_functionality': execute_testbench(find_file_path("run_test.sh")) #TODO update that to depend on the exit code.
    }
    W_M = 30
    W_T = 30
    W_F = 40
    Final = 0

    # Checkpoint LLM Module
    if scores["checkpoint_llm_module"][1] != 0:
        M = scores["checkpoint_llm_module"][0] / scores["checkpoint_llm_module"][1]
    else:
        M = 0

    # Checkpoint LLM TB
    if scores["checkpoint_llm_tb"][1] != 0:
        T = scores["checkpoint_llm_tb"][0] / scores["checkpoint_llm_tb"][1]
    else:
        T = 0

    # Checkpoint LLM Report
    if scores['checkpoint_llm_functionality'][1] != 0:
        F = scores["checkpoint_llm_functionality"][0] / scores["checkpoint_llm_functionality"][1]
    else:
        F = 0


    scores_checkpoints = {
        'checkpoint_llm_module':(M*W_M,W_M),
        'checkpoint_llm_tb':(T*W_T, W_T),
        'checkpoint_llm_functionality':(((F + T) / 2)*W_F, W_F),
    }

    for final_score_key, (final_score, total_score) in scores_checkpoints.items():
        # Append the checkpoint with the total score and the calculated score
        checkpoints.append(Checkpoint(int(total_score), int(final_score)))

    return result


