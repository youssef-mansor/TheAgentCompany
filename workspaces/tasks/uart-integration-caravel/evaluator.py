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


REPO_DIR = '/workspace/openhands/'
UT_FILE = REPO_DIR + 'tests/unit/test_agent_skill.py'
COV_FILE = REPO_DIR + 'tests/unit/test_agent_skill_coverage.xml'

with open('/instruction/checkpoints.md', 'r') as f:
    content = f.read()

# Split by lines containing only hyphens (allowing extra dashes)

print("************************************************************************************************* inside evaluator.py *********************")

sections = re.split(r'\n\s*-{3,}\s*\n', content)

# sections[0]: Action Checkpoints (ignored)
# sections[1]: Main Module Checkpoints
# sections[2]: Testbench Comprehensiveness
# sections[3]: Functionality
print(f"content: {content}")
print(f"Sections: {sections}")

CHECK_POINTS_MODULE = sections[1].strip()
CHECK_POINTS_TB = sections[2].strip()

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
    if is_file_exist(find_file_path("uart/.git/HEAD")):
        score += 1
    else:
        print("file uart/.git/HEAD not found")

    if is_file_exist(find_file_path("user_project_wrapper*.v")): #wild card in case the agent produced user_project_wrapper.new.v for example
        score += 1
    else:
        print("file user_proj_wrapper.v not found")

    # round score to the nearest integer
    return int(score)


def grade_checkpoints(trajectory="") -> Result:
    checkpoints: List[Checkpoint] = []
    result = Result(checkpoints)

    # Define the total scores corresponding to each checkpoint function with unique keys
    scores = {
        'checkpoint1': (grade_checkpoint1(), 2),
        'checkpoint_llm_module': grade_checkpoint_llm(CHECK_POINTS_MODULE, 'verilog'),
        'checkpoint_llm_tb': grade_checkpoint_llm(CHECK_POINTS_TB, 'verilog/python'),
        'checkpoint_llm_functionality': execute_testbench(find_file_path("run_test.sh")) #TODO update that to depend on the exit code.
    }

    W_A = 10
    W_M = 20
    W_T = 20
    W_F = 50
    Final = 0

    # Checkpoint 1
    if scores['checkpoint1'][1] != 0:
        A = scores['checkpoint1'][0] / scores['checkpoint1'][1]
    else:
        A = 0

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

    # Checkpoint LLM Functionality
    if scores['checkpoint_llm_functionality'][1] != 0:
        F = scores["checkpoint_llm_functionality"][0] / scores["checkpoint_llm_functionality"][1]
    else:
        F = 0

    scores_checkpoints = {
        'checkpoint1':(A*W_A, W_A),
        'checkpoint_llm_module':(M*W_M,W_M),
        'checkpoint_llm_tb':(T*W_T, W_T),
        'checkpoint_llm_functionality':(F*W_F, W_F),
    }

    for final_score_key, (final_score, total_score) in scores_checkpoints.items():
        # Append the checkpoint with the total score and the calculated score
        checkpoints.append(Checkpoint(int(total_score), int(final_score)))

    return result


