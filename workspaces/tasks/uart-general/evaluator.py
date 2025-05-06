from base_evaluator import BaseEvaluator
from scoring import Result

class UARTEvaluator(BaseEvaluator):
    """Evaluator for the UART task"""
    
    def custom_evaluation(self, trajectory: str) -> Result:
        """Custom evaluation logic for the UART task
        
        Args:
            trajectory: Path to the trajectory file
            
        Returns:
            Result object containing evaluation results
        """
        # Initialize result with default values
        result = Result()
        
        # Add custom evaluation logic here
        # For now returning an empty result since we need to implement specific UART evaluation logic
        return result

# Create a singleton instance
evaluator = UARTEvaluator()

# Function to be called by the evaluation system
def grade_checkpoints(trajectory="") -> Result:
    return evaluator.grade_checkpoints(trajectory)