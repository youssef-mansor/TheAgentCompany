from base_evaluator import BaseEvaluator
from common import grade_checkpoint_llm, execute_testbench, find_file_path
from scoring import Result, Checkpoint

import subprocess
import logging
import os
from typing import Tuple, List, Dict


class MemoryBugFixEvaluator(BaseEvaluator):
    """Evaluator for the Memory Bug Fix task"""

    def __init__(self):
        super().__init__()
        # Initialize with the base evaluator
        # The logs variable is already initialized in BaseEvaluator as an empty list
        # and is accessible to all BaseEvaluator instances and subclasses
        
    def custom_evaluation(self, trajectory: str) -> Result:
        """Custom evaluation logic for the Memory Bug Fix task
        
        Args:
            trajectory: Path to the trajectory file
            
        Returns:
            Result object containing evaluation results
        """
        # Initialize result with default values
        result = Result()
        
        # TODO: Add custom evaluation logic specific to memory bug fix task
        # This will be implemented later
        
        return result

    def get_default_weights(self) -> Dict[str, int]:
        """Override weights for memory bug fix task"""
        return {
            'module': 40,      # W_M - Weight for module implementation (bug fix)
            'functionality': 60 # W_F - Weight for functionality (most important for bug fix)
        }

    def grade_checkpoints(self, trajectory: str = "") -> Tuple[Result, List[str]]:
        """Grade all checkpoints and return final result
        
        For the memory-bug-fix task, we need to:
        1. Check if the bug in the memory module was correctly identified and fixed
        2. Verify that the testbench runs successfully with the fixed module
        3. Validate that the memory read/write operations work as expected
        """
        checkpoints = []
        weights = self.get_default_weights()

        # TODO: Implement specialized grading logic for memory bug fix
        # This will differ from standard tasks because we're specifically looking for:
        # 1. Correct identification of the bug in the memory module
        # 2. Proper fix implementation
        # 3. Successful execution of the testbench with expected outputs
        
        # Combine the verilog_tb_files_dict and python_files_dict into a single dictionary
        testbench_files_dict = {**self.verilog_tb_files_dict, **self.python_files_dict}
        
        # Get scores for each checkpoint
        scores = {
            'checkpoint_llm_module': grade_checkpoint_llm(self.CHECK_POINTS_MODULE, 'verilog', self.files_dict, self.logs),
            'checkpoint_llm_functionality': execute_testbench(find_file_path("run_test.sh"), self.files_dict, self.verilog_tb_files_dict, self.python_files_dict, self.logs)
        }

        # TODO: Add additional memory-specific evaluation logic here
        # For example, check if the specific bug in the memory module was fixed correctly
        # This could involve parsing simulation outputs or checking specific patterns in the code

        # Calculate weighted scores
        weighted_scores = {
            'checkpoint_llm_module': (
                self.calculate_score(scores['checkpoint_llm_module'], weights['module']),
                weights['module']
            ),
            'checkpoint_llm_functionality': (
                self.calculate_score(scores['checkpoint_llm_functionality'], weights['functionality']),
                weights['functionality']            )
        }

        # Create checkpoints
        for _, (score, total) in weighted_scores.items():
            checkpoints.append(Checkpoint(int(total), int(score)))

        return Result(checkpoints=checkpoints), self.logs


# Create a singleton instance
evaluator = MemoryBugFixEvaluator()

# Function to be called by the evaluation system
def grade_checkpoints(trajectory: str = "") -> Tuple[Result, List[str]]:
    return evaluator.grade_checkpoints(trajectory)