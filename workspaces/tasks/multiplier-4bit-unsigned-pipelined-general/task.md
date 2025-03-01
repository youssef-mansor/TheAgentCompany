# Verilog Four-Bit Pipelined Multiplier Implementation and Testing

## Step 1: Implement a Four-Bit Pipelined Multiplier
Design a 4-bit unsigned pipelined multiplier in Verilog with the following interface:
- `clk`
- `reset`
- `a` (4-bit input)
- `b` (4-bit input)
- `product` (8-bit output)
- `valid` (output)

The multiplier should have a three-cycle pipeline.

## Step 2: Create a Self-Checking Testbench
- Develop a comprehensive testbench for the multiplier module with asserstions that covers all possible cases.  
- If a case fails, the assertion should stop the testbench execution. 

Ensure the following points are addressed within the testbench:

### Pipeline Functionality: (1 pts)
   - Verify that the product is correctly calculated after exactly three clock cycles.
   - Include test cases to test pipeline functionality including stalling and valid signals.

### Input Combinations: (1 pts)
   - Test all possible input combinations (4-bit × 4-bit = 256 cases).


## Step 3: Debug and Fix Issues
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.

## Step 4: `run_test.sh` File Creation
- Create a shel script `run_test.sh` that contains the command to only run the testbench.
- execute the `run_test.sh` to make sure it successfully runs the testbench.