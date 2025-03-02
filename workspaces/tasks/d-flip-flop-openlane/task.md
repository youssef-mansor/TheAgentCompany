# Verilog D Flip-Flop Implementation and Testing  

## Step 1: Implement a D Flip-Flop  
Design a D flip-flop in Verilog with the following interface:  
- `clk`  
- `reset`  
- `d`  
- `q`  

## Step 2: Create a Self-Checking Testbench  
- Develop a comprehensive testbench for the D Flip Flop module with asserstions that covers all possible cases.  
- If a case fails, the assertion should stop the testbench execution. 

## Step 3: Debug and Fix Issues  
- If the module does not pass all test cases, revisit and refine the Verilog code.  
- Modify the design until all test cases pass successfully.  

## Step 4: `run_test.sh` File Creation
- Create a shel script `run_test.sh` that contains the command to only run the testbench.
- execute the `run_test.sh` to make sure it successfully runs the testbench.


## Step 5: OpenLane Flow
- Harden the top module using the OpenLane flow.  
- Ensure the hardening process is power, performance, and area (PPA) efficient, leading to the successful generation of the final GDSII.