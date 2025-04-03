import os
import ast
import sys
import logging
import subprocess
import time
import re
from typing import List, Dict, Tuple
from abc import ABC, abstractmethod

from scoring import Result, Checkpoint
from common import grade_checkpoint_llm, execute_testbench, find_file_path

class BaseEvaluator(ABC):
    REPO_DIR = '/workspace/openhands/'
    UT_FILE = REPO_DIR + 'tests/unit/test_agent_skill.py'
    COV_FILE = REPO_DIR + 'tests/unit/test_agent_skill_coverage.xml'
    UTILS_DIR = '/utils'  # Base directory for utilities in the container
    
    def __init__(self):
        self.load_checkpoints()
        
    def load_checkpoints(self):
        """Load checkpoints from the markdown file"""
        with open('/instruction/checkpoints.md', 'r') as f:
            content = f.read()
        
        # Split by lines containing only hyphens (allowing extra dashes)
        sections = re.split(r'\n\s*-{3,}\s*\n', content)
        
        # sections[0]: Action Checkpoints (ignored)
        # sections[1]: Main Module Checkpoints
        # sections[2]: Testbench Comprehensiveness
        # sections[3]: Functionality
        self.CHECK_POINTS_MODULE = sections[1].strip()
        self.CHECK_POINTS_TB = sections[2].strip()
    
    def config_env(self, dir_path: str) -> bool:
        """Configure environment with poetry dependencies"""
        try:
            os.chdir(dir_path)
            subprocess.run(["poetry", "--version"], check=True, capture_output=True)
        except Exception as e:
            logging.warning(f"is_test_run configure step 1. {e}")
            subprocess.run([sys.executable, "-m", "pip", "install", "poetry"], check=True)
            time.sleep(5)

        logging.info("Installing dependencies...")
        try:
            result = subprocess.run(["poetry", "install"], capture_output=True, text=True)
        except Exception as e:
            logging.warning(f"is_test_run configure step 2. {e}")
            return False

        if result.returncode != 0:
            logging.warning(f"Error installing dependencies.")
            logging.warning(f"{result.stderr}")
            return False
        
        logging.info("Dependencies installed successfully.")
        return True

    def get_default_weights(self) -> Dict[str, int]:
        """Get default weights for each checkpoint category"""
        return {
            'module': 30,  # W_M
            'testbench': 30,  # W_T
            'functionality': 40,  # W_F
        }

    def calculate_score(self, score: Tuple[float, float], weight: int) -> float:
        """Calculate weighted score"""
        if score[1] != 0:
            return (score[0] / score[1]) * weight
        return 0

    def grade_checkpoints(self, trajectory: str = "") -> Result:
        """Grade all checkpoints and return final result"""
        checkpoints: List[Checkpoint] = []
        weights = self.get_default_weights()

        # Get scores for each checkpoint
        scores = {
            'checkpoint_llm_module': grade_checkpoint_llm(self.CHECK_POINTS_MODULE, 'verilog'),
            'checkpoint_llm_tb': grade_checkpoint_llm(self.CHECK_POINTS_TB, 'verilog/python'),
            'checkpoint_llm_functionality': execute_testbench(find_file_path("run_test.sh"))
        }

        # Calculate weighted scores
        weighted_scores = {
            'checkpoint_llm_module': (
                self.calculate_score(scores['checkpoint_llm_module'], weights['module']),
                weights['module']
            ),
            'checkpoint_llm_tb': (
                self.calculate_score(scores['checkpoint_llm_tb'], weights['testbench']),
                weights['testbench']
            ),
            'checkpoint_llm_functionality': (
                self.calculate_score(scores['checkpoint_llm_functionality'], weights['functionality']),
                weights['functionality']
            )
        }

        # Create checkpoints
        for _, (score, total) in weighted_scores.items():
            checkpoints.append(Checkpoint(int(total), int(score)))

        return Result(checkpoints)

    @abstractmethod
    def custom_evaluation(self) -> None:
        """Override this method to add task-specific evaluation logic"""
        pass
