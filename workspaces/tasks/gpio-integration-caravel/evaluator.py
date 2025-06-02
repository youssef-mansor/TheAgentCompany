from base_evaluator import BaseEvaluator
from scoring import Result, Checkpoint
from common import find_file_path, grade_checkpoint_llm
import subprocess
import logging
import os
import re
from typing import List, Tuple


class GPIOCaravelEvaluator(BaseEvaluator):
    """Evaluator for the GPIO Caravel Integration task"""

    def __init__(self):
        super().__init__()
        # Initialize Caravel-specific variables
        self.wrapper_path = "caravel_user_project_ol2/verilog/rtl/user_project_wrapper.v"
        self.CHECK_POINTS_INTEGRATION = self.load_checkpoints()
        
    def get_default_weights(self):
        """Override weights for Caravel evaluation"""
        return {
            'module': 70,      # Weight for integration implementation (W_M)
            'template': 30,     # Weight for template structure (W_A)
        }

    def check_template_structure(self) -> Tuple[float, float]:
        """Check if the required Caravel template files exist"""
        score = 0.0
        max_score = 2.0
        print("why the heck not writting into logs[5]")
        self.logs[5] += "\n## Checking Caravel template structure"

        try:
            wrapper_path = find_file_path(self.wrapper_path)
            if wrapper_path and os.path.isfile(wrapper_path):
                score += 2
                self.logs[5] += "\nFound user_project_wrapper.v in Caravel template structure"
            else:
                self.logs[5] += "\nuser_project_wrapper.v not found in Caravel template"
                # Check alternative locations
                try:
                    alt_paths = [
                        find_file_path("user_proj_wrapper.v"),
                        find_file_path("user_project_wrapper.v")
                    ]
                    if any(path and os.path.isfile(path) for path in alt_paths if path):
                        score += 1
                        self.logs[5] += "\nFound wrapper file in alternative location"
                    else:
                        self.logs[5] += "\nNo wrapper file found in any location"
                except Exception as alt_err:
                    logging.warning(f"Error checking alternative paths: {alt_err}")
                    self.logs[5] += "\nError occurred while checking alternative locations"
        except Exception as e:
            logging.warning(f"Error checking template structure: {e}")
            self.logs[5] += "\nError occurred while checking template structure"
            # Return 0 score but don't fail the evaluation
            self.logs[5] += "\nError occurred while checking template structure"

            return (0, max_score)

        return (score, max_score)

    def grade_checkpoints(self, trajectory="") -> Tuple[Result, List[str]]:
        """Override to implement Caravel-specific grading"""
        checkpoints = []
        weights = self.get_default_weights()

        # Get scores for each checkpoint
        scores = {
            'template': self.check_template_structure(),
            'module': grade_checkpoint_llm(self.CHECK_POINTS_INTEGRATION, 'verilog', self.files_dict, self.logs)
        }

        # Calculate weighted scores
        weighted_scores = {
            'template': (
                self.calculate_score(scores['template'], weights['template']),
                weights['template']
            ),
            'module': (
                self.calculate_score(scores['module'], weights['module']),
                weights['module']
            )
        }

        # Create checkpoints
        for _, (score, total) in weighted_scores.items():
            checkpoints.append(Checkpoint(int(total), int(score)))

        return Result(checkpoints=checkpoints), self.logs

    def custom_evaluation(self, trajectory: str) -> Result:
        """Custom evaluation logic for GPIO Caravel integration"""
        # This can be implemented if additional custom evaluation is needed
        return Result()


    def load_checkpoints(self):
        with open('/instruction/checkpoints.md', 'r') as f:
            content = f.read()

        # Split by lines containing only hyphens (allowing extra dashes)
        sections = re.split(r'\n\s*-{3,}\s*\n', content)

        # sections[0]: Action Checkpoints (ignored)
        # sections[1]: Integration Checkpoints

        CHECK_POINTS_INTEGRATION = sections[1].strip()
        return CHECK_POINTS_INTEGRATION


# Create a singleton instance
evaluator = GPIOCaravelEvaluator()

# Function to be called by the evaluation system
def grade_checkpoints(trajectory="") -> Tuple[Result, List[str]]:
    return evaluator.grade_checkpoints(trajectory)