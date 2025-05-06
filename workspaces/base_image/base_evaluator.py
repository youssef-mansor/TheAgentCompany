import os
import ast
import sys
import logging
import subprocess
import time
import re
from typing import List, Dict, Tuple
from abc import ABC, abstractmethod
from enum import IntEnum


class GlobalVarIndices(IntEnum):
    WORKSPACE_FILES = 0
    WORKSPACE_CONTENT = 1
    COCOTB_TEST = 2
    FATAL_MACRO = 3

from scoring import Result, Checkpoint
from common import grade_checkpoint_llm, execute_testbench, find_file_path, collect_files, is_verilog_testbench

class BaseEvaluator(ABC):
    REPO_DIR = '/workspace/openhands/'
    UT_FILE = REPO_DIR + 'tests/unit/test_agent_skill.py'
    COV_FILE = REPO_DIR + 'tests/unit/test_agent_skill_coverage.xml'
    UTILS_DIR = '/utils'  # Base directory for utilities in the container
    
    def __init__(self):
        # Initialize with None values for each named index
        self.GLOBAL_VARS = [None] * len(GlobalVarIndices)
        self.files_dict = {}
        self.verilog_tb_files_dict = {}
        self.python_files_dict = {}
        self.logs = ["# General","\n# Main Module","\n# Testbench","\n# Functionality","\n# OpenLane"]
        self.load_checkpoints()
        self.populate_files_dict()
        self.identify_testbenches()
        
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
        
    def populate_files_dict(self, file_type='verilog/python'):
        """Populate the files_dict with Verilog and optionally Python files from specified paths"""
        exclude = ['test_runner.py', 'cocotb_iverilog_dump.v', 'openhands/miniforge3', 'parsetab.py']
        search_paths = ["/workspace", "/outputs", "/openhands/workspace/"]

        # Collect Verilog files (.v and .sv) from each search path
        for directory in search_paths:
            verilog_cmd = f"find {directory} -type f \( -name '*.v' -o -name '*.sv' \) -not -path '*/runs/*'"
            verilog_files = collect_files(verilog_cmd, exclude)
            self.files_dict.update(verilog_files)
        
        # Optionally include Python files if file_type is 'verilog/python'
        if file_type == 'verilog/python':
            for directory in search_paths:
                python_cmd = f"find {directory} -type f -name '*.py'"
                python_files = collect_files(python_cmd, exclude)
                self.files_dict.update(python_files)
                self.python_files_dict.update(python_files)
        
        # Append the files dict keys to the logs General part as  mardown list
        self.logs.append("Files Dict:")
        for filepath in self.files_dict.keys():
            self.logs.append(f"- {filepath}")
        self.logs.append("\n")
            

        
    def identify_testbenches(self):
        """Identify Verilog testbench files from files_dict and populate verilog_tb_files_dict"""
        for filepath, content in self.files_dict.items():
            # Only check Verilog/SystemVerilog files
            if filepath.endswith(('.v', '.sv')):
                if is_verilog_testbench(content):
                    self.verilog_tb_files_dict[filepath] = content

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

    def grade_checkpoints(self, trajectory: str = "") -> Tuple[Result, List[str]]:
        """Grade all checkpoints and return final result"""
        checkpoints: List[Checkpoint] = []
        weights = self.get_default_weights()

        # Get scores for each checkpoint
        # Each call to grade_checkpoint_llm builds the workspace_content out of the files_dict, this is not redundant, because in the first build we exclude python files.
        
        # Combine the verilog_tb_files_dict and python_files_dict into a single dictionary called testbench_files_dict
        testbench_files_dict = {**self.verilog_tb_files_dict, **self.python_files_dict}
        scores = {
            'checkpoint_llm_module': grade_checkpoint_llm(self.CHECK_POINTS_MODULE, 'verilog', self.files_dict, self.logs),
            'checkpoint_llm_tb': grade_checkpoint_llm(self.CHECK_POINTS_TB, 'verilog/python', testbench_files_dict, self.logs),
            'checkpoint_llm_functionality': execute_testbench(find_file_path("run_test.sh"), self.files_dict, self.verilog_tb_files_dict, self.python_files_dict, self.logs)
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

        return Result(checkpoints=checkpoints), self.logs

    @abstractmethod
    def custom_evaluation(self) -> None:
        """Override this method to add task-specific evaluation logic"""
        pass
