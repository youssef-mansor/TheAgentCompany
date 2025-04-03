from base_evaluator import BaseEvaluator
from scoring import Result
from common import grade_checkpoint_llm, execute_testbench, find_file_path
import subprocess
import logging

class DFlipFlopOpenLaneEvaluator(BaseEvaluator):
    """Evaluator for the D Flip-Flop OpenLane task"""

    def custom_evaluation(self, trajectory: str) -> Result:
        """Custom evaluation logic for the D Flip-Flop OpenLane task
        
        Args:
            trajectory: Path to the trajectory file
            
        Returns:
            Result object containing evaluation results
        """
        # Initialize result with default values
        result = Result()
        
        # Add custom evaluation logic here
        # For now returning an empty result since we need to implement specific D Flip-Flop evaluation logic
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

    def grade_checkpoints(self, trajectory="") -> Result:
        """Override to add OpenLane evaluation"""
        checkpoints = []
        weights = self.get_default_weights()

        # Get scores for each checkpoint
        scores = {
            'checkpoint_llm_module': grade_checkpoint_llm(self.CHECK_POINTS_MODULE, 'verilog'),
            'checkpoint_llm_tb': grade_checkpoint_llm(self.CHECK_POINTS_TB, 'verilog/python'),
            'checkpoint_llm_functionality': execute_testbench(find_file_path("run_test.sh")),
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

        return Result(checkpoints)

# Create a singleton instance
evaluator = DFlipFlopOpenLaneEvaluator()

# Function to be called by the evaluation system
def grade_checkpoints(trajectory="") -> Result:
    return evaluator.grade_checkpoints(trajectory)


    scores_checkpoints = {
        'checkpoint_llm_module':(M*W_M,W_M),
        'checkpoint_llm_tb':(T*W_T, W_T),
        'checkpoint_llm_functionality':(F*W_F, W_F),
        'checkpoint_llm_openlane':(O*W_O, W_O)
    }

    for final_score_key, (final_score, total_score) in scores_checkpoints.items():
        # Append the checkpoint with the total score and the calculated score
        checkpoints.append(Checkpoint(int(total_score), int(final_score)))

    return result


