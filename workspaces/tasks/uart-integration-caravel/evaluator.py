import logging
from typing import Dict, Tuple
from common import find_file_path
from base_evaluator import BaseEvaluator



def is_file_exist(file_path):
    """
     Check if a file exists at the given path.
    """
    if not file_path:
        logging.warning("is_file_exist: Empty path provided")
        return False

    abs_path = os.path.abspath(file_path)

    try:
        return os.path.isfile(abs_path)
    except Exception as e:
        logging.warning(f"Error in is_file_exist: {e}")
        return False

class UartIntegrationEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__()

    def get_default_weights(self) -> Dict[str, Tuple[float, float]]:
        """Override default weights for this task"""
        return {
            'checkpoint1': (10, 2),  # (weight, total points)
            'checkpoint_llm_module': (20, None),  # None means use computed total from LLM
            'checkpoint_llm_tb': (20, None),
            'checkpoint_llm_functionality': (50, None)
        }

    def grade_checkpoint1(self) -> Tuple[float, float]:
        """Grade checkpoint 1 - Check for required files"""
        score = 0.0
        total_points = 2.0
        
        if is_file_exist(find_file_path("uart/.git/HEAD")):
            score += 1
            self.logs[0] += "\n- Found uart/.git/HEAD"
        else:
            self.logs[0] += "\n- Missing uart/.git/HEAD"
            logging.warning("file uart/.git/HEAD not found")

        if is_file_exist(find_file_path("user_project_wrapper*.v")):
            score += 1
            self.logs[0] += "\n- Found user_project_wrapper.v"
        else:
            self.logs[0] += "\n- Missing user_project_wrapper.v"
            logging.warning("file user_project_wrapper.v not found")

        return score, total_points


def grade_checkpoints(trajectory="") -> Result:
    evaluator = UartIntegrationEvaluator()
    return evaluator.grade_checkpoints(trajectory)
