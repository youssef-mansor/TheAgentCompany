from base_evaluator import BaseEvaluator
from common import grade_checkpoint_llm, find_files, collect_files
from scoring import Result, Checkpoint

import subprocess
import logging
import os
import glob
from typing import Tuple, List, Dict


class VerilogCppDPIEvaluator(BaseEvaluator):
    """Evaluator for the Verilog C++ DPI Validation 2-bit adder task"""

    def __init__(self):
        super().__init__()
        # Initialize with the base evaluator
        self.cpp_files_dict = {}
        self.populate_cpp_files()
        
    def populate_cpp_files(self):
        """Populate the cpp_files_dict with C++ files from specified paths"""
        exclude = ['cocotb_iverilog_dump.v', 'openhands/miniforge3']
        search_paths = ["/workspace", "/outputs", "/openhands/workspace/"]

        # Collect C++ files (.cpp and .cc) from each search path
        for directory in search_paths:
            cpp_cmd = f"find {directory} -type f \( -name '*.cpp' -o -name '*.cc' \)"
            cpp_files = collect_files(cpp_cmd, exclude)
            self.cpp_files_dict.update(cpp_files)
        
        # Append the cpp files dict keys to the logs General part as markdown list
        self.logs[0] += "\n\n## C++ Files:\n"
        for filepath in self.cpp_files_dict.keys():
            self.logs[0] += f"- {filepath}\n"
        
    def custom_evaluation(self, trajectory: str) -> Result:
        """Custom evaluation logic for the Verilog C++ DPI Validation task"""
        # Initialize result with default values
        result = Result()
        return result

    def get_default_weights(self) -> Dict[str, int]:
        """Override weights for Verilog C++ DPI validation task"""
        return {
            'module': 20,      # W_M - Weight for main module implementation
            'testbench': 20,   # W_T - Weight for testbench comprehensiveness
            'functionality': 60 # W_F - Weight for functionality (Verilator compilation and execution)
        }
    
    def run_verilator_test(self) -> Tuple[float, float]:
        """Run Verilator test with C++ testbench
        
        Returns:
            Tuple[float, float]: (score, total_score)
        """
        # Find Verilog and C++ files
        verilog_files = [f for f in self.files_dict.keys() if f.endswith(('.v', '.sv'))]
        cpp_files = list(self.cpp_files_dict.keys())
        
        if not verilog_files:
            self.logs[3] += "\n## Error: No Verilog files found\n"
            return 0, 60
            
        if not cpp_files:
            self.logs[3] += "\n## Error: No C++ files found\n"
            return 0, 60
        
        # Find the main Verilog module file (likely contains adder_2bit or similar)
        verilog_module_file = None
        for file in verilog_files:
            if 'adder' in file.lower() and file.endswith('.sv'):
                verilog_module_file = file
                break
        
        if not verilog_module_file:
            for file in verilog_files:
                if file.endswith('.sv'):
                    verilog_module_file = file
                    break
        
        if not verilog_module_file:
            verilog_module_file = verilog_files[0]
        
        # Find the C++ testbench file
        cpp_testbench_file = None
        for file in cpp_files:
            if 'tb' in os.path.basename(file).lower() or 'test' in os.path.basename(file).lower():
                cpp_testbench_file = file
                break
        
        if not cpp_testbench_file and cpp_files:
            cpp_testbench_file = cpp_files[0]
            
        if not cpp_testbench_file:
            self.logs[3] += "\n## Error: No C++ testbench file found\n"
            return 0, 60
            
        # Log the files we're using
        self.logs[3] += f"\n## Verilator Test Files:\n"
        self.logs[3] += f"- Verilog Module: {verilog_module_file}\n"
        self.logs[3] += f"- C++ Testbench: {cpp_testbench_file}\n"
        
        # Create a temporary directory for Verilator output
        os.makedirs("obj_dir", exist_ok=True)
        
        # Run Verilator commands
        try:
            # Change to the directory containing the files
            verilog_dir = os.path.dirname(verilog_module_file)
            if verilog_dir:
                os.chdir(verilog_dir)
                
            verilog_basename = os.path.basename(verilog_module_file)
            cpp_basename = os.path.basename(cpp_testbench_file)
            
            # Extract module name from the Verilog file (remove extension)
            module_name = os.path.splitext(verilog_basename)[0]
            
            # Run Verilator command
            self.logs[3] += "\n## Running Verilator Commands:\n"
            
            verilator_cmd = f"verilator -Wall --cc {verilog_basename} --exe {cpp_basename}"
            self.logs[3] += f"```\n{verilator_cmd}\n```\n"
            
            result = subprocess.run(verilator_cmd, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                self.logs[3] += f"\n## Verilator Error:\n```\n{result.stderr}\n```\n"
                return 0, 60
                
            # Run make command
            make_cmd = f"make -C obj_dir -f V{module_name}.mk V{module_name}"
            self.logs[3] += f"\n```\n{make_cmd}\n```\n"
            
            result = subprocess.run(make_cmd, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                self.logs[3] += f"\n## Make Error:\n```\n{result.stderr}\n```\n"
                return 0, 60
                
            # Run the executable
            run_cmd = f"./obj_dir/V{module_name}"
            self.logs[3] += f"\n```\n{run_cmd}\n```\n"
            
            result = subprocess.run(run_cmd, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                self.logs[3] += f"\n## Execution Error:\n```\n{result.stderr}\n```\n"
                return 0, 60
                
            # If we got here, all commands succeeded
            self.logs[3] += f"\n## Verilator Test Successful!\n"
            self.logs[3] += f"\n## Output:\n```\n{result.stdout}\n```\n"
            return 60, 60
            
        except Exception as e:
            self.logs[3] += f"\n## Exception during Verilator test: {str(e)}\n"
            return 0, 60

    def grade_checkpoints(self, trajectory: str = "") -> Tuple[Result, List[str]]:
        """Grade all checkpoints and return final result"""
        checkpoints = []
        weights = self.get_default_weights()

        # Combine the verilog_tb_files_dict and cpp_files_dict for testbench evaluation
        testbench_files_dict = {**self.verilog_tb_files_dict, **self.cpp_files_dict}
        
        # Get scores for each checkpoint
        scores = {
            'checkpoint_llm_module': grade_checkpoint_llm(self.CHECK_POINTS_MODULE, 'verilog', self.files_dict, self.logs),
            'checkpoint_llm_tb': grade_checkpoint_llm(self.CHECK_POINTS_TB, 'verilog/python', testbench_files_dict, self.logs),
            'verilator_test': self.run_verilator_test()
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
            'verilator_test': (
                scores['verilator_test'][0],  # Already weighted
                weights['functionality']
            )
        }

        # Create checkpoints
        for _, (score, total) in weighted_scores.items():
            checkpoints.append(Checkpoint(int(total), int(score)))

        return Result(checkpoints=checkpoints), self.logs


# Create a singleton instance
evaluator = VerilogCppDPIEvaluator()

# Function to be called by the evaluation system
def grade_checkpoints(trajectory: str = "") -> Tuple[Result, List[str]]:
    return evaluator.grade_checkpoints(trajectory)