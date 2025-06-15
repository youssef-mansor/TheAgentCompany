from base_evaluator import BaseEvaluator
from common import grade_checkpoint_llm, execute_testbench, find_file_path
from scoring import Result, Checkpoint

import subprocess
import logging
import os
from typing import Tuple, List


class UARTIntegrationEvaluator(BaseEvaluator):
    """Evaluator for the UART Integration Caravel task"""

    def __init__(self):
        super().__init__()
        
    def custom_evaluation(self, trajectory: str) -> Result:
        """Custom evaluation logic for the UART Integration task
        
        Args:
            trajectory: Path to the trajectory file
            
        Returns:
            Result object containing evaluation results
        """
        # Initialize result with default values
        result = Result()
        return result

    def get_default_weights(self):
        """Override weights for UART Integration evaluation"""
        return {
            'action_points': 10,     # Weight for basic file existence checks
            'module': 20,            # Weight for user_project_wrapper implementation
            'testbench': 20,         # Weight for test implementation
            'functionality': 50        # Weight for functionality (handled separately)
        }

    def grade_action_points(self):
        """Grade action points - checking file existence"""
        score = 0
        max_score = 2  # 1 point each for uart/.git and user_project_wrapper.v

        # Check for uart/.git
        git_dir = find_file_path("uart/.git")
        if git_dir:
            self.logs[0] += "\nuart/.git directory found\n"
            score += 1
        else:
            self.logs[0] += "\nuart/.git directory not found\n"
            logging.warning("uart/.git directory not found")

        # Check for user_project_wrapper.v
        wrapper_file = find_file_path("user_project_wrapper.v")
        if wrapper_file:
            self.logs[0] += "user_project_wrapper.v file found\n"
            score += 1
        else:
            self.logs[0] += "user_project_wrapper.v file not found\n"
            logging.warning("user_project_wrapper.v file not found")

        return (score, max_score)

    def grade_checkpoints(self, trajectory="") -> Tuple[Result, List[str]]:
        """Override to implement UART Integration evaluation"""
        checkpoints = []
        weights = self.get_default_weights()

        # Combine testbench files
        testbench_files_dict = {**self.verilog_tb_files_dict, **self.python_files_dict}
        
        # Get scores for each checkpoint
        scores = {
            'checkpoint_action_points': self.grade_action_points(),
            'checkpoint_llm_module': grade_checkpoint_llm(self.CHECK_POINTS_MODULE, 'verilog', 
                                                        {k: v for k, v in self.files_dict.items() if k.endswith('user_project_wrapper.v')} 
                                                        if any(k.endswith('user_project_wrapper.v') for k in self.files_dict) 
                                                        else {}, self.logs),
            'checkpoint_llm_tb': grade_checkpoint_llm(self.CHECK_POINTS_TB, 'verilog/python', testbench_files_dict, self.logs),
            'checkpoint_llm_functionality': execute_testbench(find_file_path("run_test.sh"), self.files_dict, self.verilog_tb_files_dict, self.python_files_dict, self.logs)
        }

        # Calculate weighted scores
        weighted_scores = {
            'checkpoint_action_points': (
                self.calculate_score(scores['checkpoint_action_points'], weights['action_points']),
                weights['action_points']
            ),
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

# Create a singleton instance
evaluator = UARTIntegrationEvaluator()

# Function to be called by the evaluation system
def grade_checkpoints(trajectory="") -> Tuple[Result, List[str]]:
    return evaluator.grade_checkpoints(trajectory)