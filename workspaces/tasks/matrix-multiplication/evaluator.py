from base_evaluator import BaseEvaluator
from scoring import Result
from typing import Tuple, List

class MatrixMultiplicationEvaluator(BaseEvaluator):
    """Evaluator for the Matrix Multiplication task"""
    
    def __init__(self):
        super().__init__()
    
    def get_default_weights(self):
        """Override weights for matrix multiplication evaluation"""
        return {
            'module': 35,      # W_M - Weight for module implementation
            'testbench': 35,   # W_T - Weight for testbench
            'functionality': 30 # W_F - Weight for functionality
        }
    
    def custom_evaluation(self, trajectory: str) -> Result:
        """Custom evaluation logic for the matrix multiplication task
        
        Args:
            trajectory: Path to the trajectory file
            
        Returns:
            Result object containing evaluation results
        """
        # Initialize result with default values
        result = Result()
        
        # Add custom evaluation logic here if needed
        # For now returning an empty result since we're using the base evaluator's functionality
        return result

# Create a singleton instance
evaluator = MatrixMultiplicationEvaluator()

# Function to be called by the evaluation system
def grade_checkpoints(trajectory="") -> Tuple[Result, List[str]]:
    return evaluator.grade_checkpoints(trajectory)