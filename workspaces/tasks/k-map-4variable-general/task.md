# Boolean Logic Simplification and Verilog Implementation

## Step 1: Simplify the Boolean Logic
- Simplify the following Boolean logic equation using the provided K-map:
  
  **K-map**:
  ```
          ab
   cd   | 00 | 01 | 11 | 10 |
  ----------------------------
   00   |  0 |  1 |  1 |  0 |  
   01   |  1 |  1 |  0 |  0 |  
   11   |  1 |  0 |  0 |  1 |  
   10   |  0 |  1 |  1 |  1 |  
  ```
- Implement the minimized Boolean logic as a Verilog module with the following interface:
  - Inputs: `a`, `b`, `c`, `d`
  - Output: `f`

## Step 2: Create a Self-Checking Testbench  
- Develop a comprehensive testbench for the module to verify its functionality with asserstions that covers all possible cases.  
- If a case fails, the assertion should stop the testbench execution. 


Ensure to Verify all 16 possible input combinations (2^4).

## Step 3: Debug and Fix Issues  
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.

## Step 4: `run_test.sh` File Creation
- Create a shel script `run_test.sh` that contains the command to only run the testbench.
- execute the `run_test.sh` to make sure it successfully runs the testbench.