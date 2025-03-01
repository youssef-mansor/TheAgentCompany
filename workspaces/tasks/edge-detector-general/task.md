# Verilog Rising-Edge Detector Implementation and Testing  

## Step 1: Implement a Rising-Edge Detector  
Design a rising-edge detector in Verilog with the following interface:  
- `clk`  
- `reset`  
- `signal_in`  
- `signal_out`  


## Step 2: Create a Self-Checking Testbench  
- Develop a comprehensive testbench for the rising-edge detector module  with asserstions that covers all possible cases.  
- If a case fails, the assertion should stop the testbench execution. 

Ensure the following points are addressed within the test bench 

### Edge Detection:
   - Verify that `signal_out` is `1` only when there is a rising edge on `signal_in`.

### Multiple Edges:
   - Apply multiple rising edges on `signal_in` and confirm that `signal_out` is asserted for one clock cycle for each rising edge.

### No False Positives:
   - Ensure that `signal_out` remains `0` when `signal_in` remains stable (high or low) between clock cycles.

## Step 3: Debug and Fix Issues  
- If the module does not pass all test cases, revisit and refine the Verilog code.  
- Modify the design until all test cases pass successfully.  

## Step 4: `run_test.sh` File Creation
- Create a shel script `run_test.sh` that contains the command to only run the testbench.
- execute the `run_test.sh` to make sure it successfully runs the testbench.