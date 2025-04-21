from base_evaluator import BaseEvaluator
from common import grade_checkpoint_llm, execute_testbench, find_file_path
from scoring import Result, Checkpoint

import subprocess
import logging
import os
from typing import Tuple, List


class MultiplierPipelinedOpenLaneEvaluator(BaseEvaluator):
    """Evaluator for the 4-bit Unsigned Pipelined Multiplier OpenLane task"""

    def __init__(self):
        super().__init__()

    def custom_evaluation(self, trajectory: str) -> Result:
        """Custom evaluation logic for the Multiplier OpenLane task
        
        Args:
            trajectory: Path to the trajectory file
            
        Returns:
            Result object containing evaluation results
        """
        # Initialize result with default values
        result = Result()
        
        # Add custom evaluation logic here if needed
        # For now returning an empty result since we need to implement specific Multiplier evaluation logic
        return result

    def get_default_weights(self):
        """Override weights to include OpenLane evaluation"""
        return {
            'module': 15,      # W_M - Weight for module implementation
            'testbench': 15,   # W_T - Weight for testbench
            'functionality': 20,# W_F - Weight for functionality
            'openlane': 50     # W_O - Weight for OpenLane results
        }

    def grade_checkpoint_openlane(self):
        """Grade OpenLane specific checkpoints"""
        score = 0
        search_paths = ["/workspace", "/outputs", "/openhands/workspace/", "/tmp"]
        
        # Search for config.json outside any "runs" subdirectories
        config_found = False
        for path in search_paths:
            try:
                result = subprocess.run(
                    f'find {path} -type f -name "*config*json" ! -path "*/runs/*"',
                    shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
                )
                if result.stdout.strip():
                    config_found = True
                    break
            except Exception as e:
                logging.warning(f"Error searching for config.json: {e}")

        if config_found:
            score += 1
        else:
            logging.warning("config.json not found")

        # Search for .gds files within any "/final/gds/" directory
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
                logging.warning(f"Error searching for GDS: {e}")

        if gds_found:
            score += 1
        else:
            logging.warning("GDS file not found")

        return (score, 2)


    def grade_checkpoints(self, trajectory="") -> Tuple[Result, List[str]]:
        """Override to add OpenLane evaluation"""
        checkpoints = []
        weights = self.get_default_weights()

        # Get scores for each checkpoint
        scores = {
            'checkpoint_llm_module': grade_checkpoint_llm(self.CHECK_POINTS_MODULE, 'verilog', self.files_dict, self.logs),
            'checkpoint_llm_tb': grade_checkpoint_llm(self.CHECK_POINTS_TB, 'verilog/python', self.files_dict, self.logs),
            'checkpoint_llm_functionality': execute_testbench(find_file_path("run_test.sh"), self.files_dict, self.verilog_tb_files_dict, self.python_files_dict, self.logs),
            'checkpoint_llm_openlane': self.grade_checkpoint_openlane()
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
            ),
            'checkpoint_llm_openlane': (
                self.calculate_score(scores['checkpoint_llm_openlane'], weights['openlane']),
                weights['openlane']
            )
        }

        # Create checkpoints
        for _, (score, total) in weighted_scores.items():
            checkpoints.append(Checkpoint(int(total), int(score)))

        return Result(checkpoints), self.logs


# Create a singleton instance
evaluator = MultiplierPipelinedOpenLaneEvaluator()

# Function to be called by the evaluation system
def grade_checkpoints(trajectory="") -> Tuple[Result, List[str]]:
    # Test
    #check if the file /outputs/report_multiplier-4bit-unsigned-pipelined-openlane.md exists and print informative message
    #if it does exist append to it some text
    #TODO Print the path for report
    # path = find_file_path('report_multiplier-4bit-unsigned-pipelined-openlane.md')
    # print(f"Returned value of find_file_path function: {path} Returned type: {type(path)}")
    # if os.path.exists(path):
    #     with open(path, 'a') as f:
    #         f.write("This content is appended to the file")
    #         print("Content appended to the report file")
    # else:
    #     print("Report file does not exist")
    return evaluator.grade_checkpoints(trajectory)