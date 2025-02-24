# Verilog Four-Bit Counter Implementation and Testing

## Step 1: Implement a Four-Bit Counter
Design a four-bit counter in Verilog with the following interface:  
- `clk` 
- `reset`
- `count` 

## Step 2: Create a Self-Checking Testbench  
- Develop a comprehensive testbench for the counter module with asserstions that covers all possible cases.  
- If a case fails, the assertion should stop the testbench execution. 

Ensure the following points are addressed within the test bench 

**Normal Increment:**
     Allow the counter to increment and observe proper functionality at trigerring edge.
**Wrap-Around:**
     Ensure the counter wraps back to 0 after reaching 15 (4-bit overflow).

## Step 3: Debug and Fix Issues  
- If the module does not pass all test cases, revisit and refine the Verilog code.  
- Modify the design until all test cases pass successfully.  

## Step 4: `run_test.sh` File Creation
- Create a shel script `run_test.sh` that contains the command to run the testbench.
- execute the `run_test.sh` to make sure it successfully runs the testbench.