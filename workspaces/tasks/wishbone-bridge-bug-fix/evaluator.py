from base_evaluator import BaseEvaluator
from common import grade_checkpoint_llm, execute_testbench, find_file_path
from scoring import Result, Checkpoint

import subprocess
import logging
import os
from typing import Tuple, List, Dict


class WishboneBridgeBugFixEvaluator(BaseEvaluator):
    """Evaluator for the Wishbone Bridge Bug Fix task"""

    def __init__(self):
        super().__init__()
        
    def custom_evaluation(self, trajectory: str) -> Result:
        """Custom evaluation logic for the Wishbone Bridge Bug Fix task
        
        Args:
            trajectory: Path to the trajectory file
            
        Returns:
            Result object containing evaluation results
        """
        # Initialize result with default values
        result = Result()
        
        # Add custom evaluation logic here if needed
        return result

    def get_default_weights(self) -> Dict[str, int]:
        """Override weights to match the task requirements"""
        return {
            'module': 40,      # W_M - Weight for module implementation (40%)
            'compilation': 60  # W_C - Weight for iverilog compilation check (60%)
        }
    
    def check_iverilog_compilation(self) -> Tuple[float, float]:
        """Run iverilog on the main module file and check the exit code
        
        Returns:
            Tuple of (score, total_possible_score)
        """
        score = 0
        total_score = 1
        
        # Find the main module file (bus_bridge.v)
        main_module_file = None
        for filepath, content in self.files_dict.items():
            if filepath.endswith('.v') and 'bus_bridge' in content:
                main_module_file = filepath
                break
        
        if not main_module_file:
            self.logs.append("\n# Compilation Check\nError: Could not find bus_bridge module file")
            return (score, total_score)
        
        # Run iverilog on the file
        try:
            result = subprocess.run(
                ['iverilog', '-o', '/tmp/bus_bridge_compiled', main_module_file],
                capture_output=True, text=True
            )
            
            # Check if compilation was successful
            if result.returncode == 0:
                score = 1
                self.logs.append(f"\n# Compilation Check\nSuccess: {main_module_file} compiled successfully with iverilog")
            else:
                self.logs.append(f"\n# Compilation Check\nFailed: {main_module_file} failed to compile with iverilog\nError: {result.stderr}")
        except Exception as e:
            self.logs.append(f"\n# Compilation Check\nError running iverilog: {str(e)}")
        
        return (score, total_score)

    def grade_checkpoints(self, trajectory="") -> Tuple[Result, List[str]]:
        """Override to include iverilog compilation check"""
        checkpoints = []
        weights = self.get_default_weights()

        # Get scores for each checkpoint
        scores = {
            'checkpoint_llm_module': grade_checkpoint_llm(self.CHECK_POINTS_MODULE, 'verilog', self.files_dict, self.logs),
            'checkpoint_iverilog_compilation': self.check_iverilog_compilation()
        }

        # Calculate weighted scores
        weighted_scores = {
            'checkpoint_llm_module': (
                self.calculate_score(scores['checkpoint_llm_module'], weights['module']),
                weights['module']
            ),
            'checkpoint_iverilog_compilation': (
                self.calculate_score(scores['checkpoint_iverilog_compilation'], weights['compilation']),
                weights['compilation']
            )
        }

        # Create checkpoints
        for _, (score, total) in weighted_scores.items():
            checkpoints.append(Checkpoint(int(total), int(score)))

        return Result(checkpoints=checkpoints), self.logs

# Create a singleton instance
evaluator = WishboneBridgeBugFixEvaluator()

# Function to be called by the evaluation system
def grade_checkpoints(trajectory="") -> Tuple[Result, List[str]]:
    return evaluator.grade_checkpoints(trajectory)