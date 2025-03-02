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


@grader
def grade_checkpoint_openlane():
    score = 0
    search_paths = ["/workspace", "/outputs", "/openhands/workspace/"]

    # Search for config.json outside any "runs" subdirectories.
    config_found = False
    for path in search_paths:
        try:
            result = subprocess.run(
                f'find {path} -type f -name "config.json" ! -path "*/runs/*"',
                shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            if result.stdout.strip():
                config_found = True
                break
        except Exception as e:
            # TODO  log or handle exceptions here.
            pass

    if config_found:
        score += 1
    else:
        print("config.json not found")
        print(f"result: {result}")


    # Search for .gds files within any "/final/gds/" directory.
    gds_found = False
    for path in search_paths:
        try:
            result = subprocess.run(
                f'find {path} -type f -path "*/final/gds/*" -name "*.gds"',
                shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            if result.stdout.strip():
                gds_found = True
                break
        except Exception as e:
            # TODO log or handle exceptions here.
            pass

    if gds_found:
        score += 1
    else:
        print("gds not found")
        print(f"result: {result}")

    return (score, 2)



def grade_checkpoints(trajectory="") -> Result:
    checkpoints: List[Checkpoint] = []
    result = Result(checkpoints)

    # Define the total scores corresponding to each checkpoint function with unique keys
    scores = {
        'checkpoint_llm_module': grade_checkpoint_llm(CHECK_POINTS_MODULE, 'verilog'),
        'checkpoint_llm_tb': grade_checkpoint_llm(CHECK_POINTS_TB, 'verilog/python'),
        'checkpoint_llm_functionality': execute_testbench(find_file_path("run_test.sh")), #TODO update that to depend on the exit code.
        'checkpoint_llm_openlane':grade_checkpoint_openlane()
    }
    W_M = 15
    W_T = 15
    W_F = 20
    W_O = 50
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

    # Checkpoint LLM Functionality
    if scores['checkpoint_llm_functionality'][1] != 0:
        F = scores["checkpoint_llm_functionality"][0] / scores["checkpoint_llm_functionality"][1]
    else:
        F = 0

    # Checkpoint LLM Functionality
    if scores['checkpoint_llm_openlane'][1] != 0:
        O = scores["checkpoint_llm_openlane"][0] / scores["checkpoint_llm_openlane"][1]
    else:
        O = 0


    scores_checkpoints = {
        'checkpoint_llm_module':(M*W_M,W_M),
        'checkpoint_llm_tb':(T*W_T, W_T),
        'checkpoint_llm_functionality':(F*W_F, W_F),
        'checkpoint_llm_openlane':(O*W_O, W_O)
    }

    for final_score_key, (final_score, total_score) in scores_checkpoints.items():
        # Append the checkpoint with the total score and the calculated score
        checkpoints.append(Checkpoint(int(total_score), int(final_score)))

    return result


