# Verilog Rising-Edge Detector Implementation and Testing  

## Step 0: Files creation
Create the following files
- `/workspace/report.md`
- `/workspace/edge_detector.v` 
- `/workspace/edge_detector_tb.v`

## Step 1: Implement a Rising-Edge Detector  
Design a rising-edge detector in Verilog with the following interface:  
- `clk`  
- `reset`  
- `signal_in`  
- `signal_out`  

Place the implemented edge detector into `/workspace/edge_detector.v`  

## Step 2: Create a Self-Checking Testbench  
- Develop a comprehensive testbench for the rising-edge detector module that covers all possible cases.  
- Ensure it automatically verifies correctness and prints the results.  
- Save the output in a Markdown file with:  
  - **Test title**  
  - **Pass/Fail status**  

Ensure the following points are addressed within the test bench 

### Edge Detection:
   - Verify that `signal_out` is `1` only when there is a rising edge on `signal_in`.

### Multiple Edges:
   - Apply multiple rising edges on `signal_in` and confirm that `signal_out` is asserted for one clock cycle for each rising edge.

### No False Positives:
   - Ensure that `signal_out` remains `0` when `signal_in` remains stable (high or low) between clock cycles.
   
Ensure the testbench prints each test's pass/fail status directly into `/workspace/report.md` using Verilog file operations, with one line per test indicating "pass" or "fail."

Place the implemented testbench into `/workspace/edge_detector_tb.v`  

## Step 3: Debug and Fix Issues  
- If the module does not pass all test cases, revisit and refine the Verilog code.  
- Modify the design until all test cases pass successfully.  
