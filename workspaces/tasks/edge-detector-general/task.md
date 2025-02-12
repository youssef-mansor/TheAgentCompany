# Verilog Rising-Edge Detector Implementation and Testing  

## Step 1: Implement a Rising-Edge Detector  
Design a rising-edge detector in Verilog with the following interface:  
- `clk`  
- `reset`  
- `signal_in`  
- `signal_out`  

Place the implemented edge detector into `/openhands/workspace/edge_detector.v`  

## Step 2: Create a Self-Checking Testbench  
- Develop a comprehensive testbench for the rising-edge detector module that covers all possible cases.  
- Ensure it automatically verifies correctness and prints the results.  
- Save the output in a Markdown file with:  
  - **Test title**  
  - **Pass/Fail status**  

Ensure the following points are addressed within the test bench 

### Edge Detection: (1 pts)
   - Verify that `signal_out` is `1` only when there is a rising edge on `signal_in`.

### Multiple Edges: (1 pts)
   - Apply multiple rising edges on `signal_in` and confirm that `signal_out` is asserted for one clock cycle for each rising edge.

### No False Positives: (1 pts)
   - Ensure that `signal_out` remains `0` when `signal_in` remains stable (high or low) between clock cycles.
   
Place the implemented testbench into `/openhands/workspace/edge_detector_tb.v`  
Place the test report into `/openhands/workspace/report.md`  

## Step 3: Debug and Fix Issues  
- If the module does not pass all test cases, revisit and refine the Verilog code.  
- Modify the design until all test cases pass successfully.  
