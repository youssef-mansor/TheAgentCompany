from base_evaluator import BaseEvaluator
from scoring import Result

class ShifterEvaluator(BaseEvaluator):
    """Evaluator for the 8-bit Shifter task"""
    
    def custom_evaluation(self, trajectory: str) -> Result:
        """Custom evaluation logic for the 8-bit Shifter task
        
        Args:
            trajectory: Path to the trajectory file
            
        Returns:
            Result object containing evaluation results
        """
        # Initialize result with default values
        result = Result()
        
        # Add custom evaluation logic here if needed
        # For now returning an empty result since we use the base evaluation logic
        return result

# Create a singleton instance
evaluator = ShifterEvaluator()

# Function to be called by the evaluation system
def grade_checkpoints(trajectory="") -> Result:
    return evaluator.grade_checkpoints(trajectory)