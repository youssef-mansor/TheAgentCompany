import os
import ast
import sys
import logging
import subprocess
import time
import re
import subprocess



from typing import List
from scoring import Result, Checkpoint
from common import *


def find_file(file_name):
    try:
        result = subprocess.check_output(['find', '/', '-name', file_name], text=True).strip()
        return result
    except subprocess.CalledProcessError:
        return "File not found"
    except Exception as e:
        return f"Error: {e}"
    
# def find_file_specific(file_name):
#     try:
#         result = subprocess.check_output(['find', '/', '-name', file_name], text=True).strip()
#         lines = result.split("\n")  # Split the output into lines
#         for line in lines:
#             if "rtl/{file_name}" in line or "workspace/{file_name}" in line or "outputs/{file_name}":
#                 return line  # Return the first matching line
#         return "No matching file found"
#     except subprocess.CalledProcessError:
#         return "File not found"
#     except Exception as e:
#         return f"Error: {e}"
    

def find_file_specific(filename = "user_proj_wrapper.v"):
    search_paths = ["/openhands", "/home", "/outputs", "/workspace"]
    for path in search_paths:
        try:
            result = subprocess.check_output(['find', path, '-name', filename], text=True).strip()
            lines = result.split("\n")
            for line in lines:
                if line.strip():
                    return line  # Return the first matching result
        except subprocess.CalledProcessError:
            continue  # If no results are found in this path, continue to the next
    
    return "No matching file found"



REPO_DIR = '/workspace/openhands/'
UT_FILE = REPO_DIR + 'tests/unit/test_agent_skill.py'
COV_FILE = REPO_DIR + 'tests/unit/test_agent_skill_coverage.xml'

with open('/instruction/checkpoints.md', 'r') as f:
    content = f.read()

# Split by lines containing only hyphens (allowing extra dashes)
sections = re.split(r'\n\s*-{3,}\s*\n', content)

# sections[0]: Action Checkpoints (ignored)
# sections[1]: Integration Checkpoints

CHECK_POINTS_INTEGRATION = sections[1].strip()

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
        return 0

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
        return 0


def is_file_exist(file_path):
    """
     Check if a file exists at the given path.
    """
    if not file_path:
        logging.warning("is_file_exist: Empty path provided")
        return False

    abs_path = os.path.abspath(file_path)

    try:
        return os.path.isfile(abs_path)
    except Exception as e:
        logging.warning(f"Error in is_file_exist: {e}")
        return False

@grader
def grade_checkpoint1():
    score = 0.0
    if is_file_exist(find_file_path("caravel_user_project_ol2/verilog/rtl/user_proj_wrapper.v")):
        score += 1
    else:
        print("file user_proj_wrapper.v doesn't exist")
    if is_file_exist(find_file_path("report.md")):
        score += 1
    else:
        print("file report.md does not exist")        
    return score

@grader
def grade_checkpoint_llm(CHECK_POINTS, file_path, file_type):
    file_content = None
    # check if the file /openhands/workspace/shifter.v exists
    if is_file_exist(file_path):
        # read it content into file
        with open(file_path, 'r') as file:
            file_content = file.read()
            file_content = f"\n{file_type}```\n" + file_content + "\n```\n"

        return check_with_llm_F(CHECK_POINTS, file_content)
    
    else:
        print(f"{file_path} does not exist")
        return (0, 0)


def grade_checkpoints(trajectory="") -> Result:
    checkpoints: List[Checkpoint] = []
    result = Result(checkpoints)

    # Define the total scores corresponding to each checkpoint function with unique keys
    scores = {
        'checkpoint1': (grade_checkpoint1(), 2),
        'checkpoint_llm_integration': grade_checkpoint_llm(CHECK_POINTS_INTEGRATION, find_file_path("caravel_user_project_ol2/verilog/rtl/user_proj_wrapper.v"), 'verilog')
    }
    W_A = 30
    W_M = 70
    Final = 0

    # Checkpoint 1
    if scores['checkpoint1'][1] != 0:
        A = scores['checkpoint1'][0] / scores['checkpoint1'][1]
        print(f"A: {A}")
    else:
        A = 0

    print(f"find_file_specific('user_proj_wrapper.v'): {find_file_specific('user_proj_wrapper.v')}")
    print(f"find_file('user_proj_wrapper.v'): {find_file('user_proj_wrapper.v')}")


    # Checkpoint LLM Module
    if scores["checkpoint_llm_integration"][1] != 0:
        M = scores["checkpoint_llm_integration"][0] / scores["checkpoint_llm_integration"][1]
    else:
        M = 0

    scores_checkpoints = {
        'checkpoint1':(A*W_A, W_A),
        'checkpoint_llm_integration':(M*W_M,W_M)
    }

    print(find_file("user_proj_wrapper.v"))
    for final_score_key, (final_score, total_score) in scores_checkpoints.items():
        # Append the checkpoint with the total score and the calculated score
        checkpoints.append(Checkpoint(int(total_score), int(final_score)))

    return result


