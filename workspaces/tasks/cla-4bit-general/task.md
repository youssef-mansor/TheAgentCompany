# Verilog 4-bit Carry Lookahead Adder Implementation and Testing

## Step 1: Implement a 4-bit Carry Lookahead Adder
Design a 4-bit CLA in Verilog with the following interface:
- `A` (4-bit input)
- `B` (4-bit input)
- `cin` (carry-in)
- `S` (4-bit sum output)
- `cout` (carry-out)

The CLA should use generate (G) and propagate (P) signals for implementation of lookahead logic

## Step 2: Create a Self-Checking Testbench
- Develop a comprehensive testbench for the CLA modulewith asserstions that covers all possible cases.  
- If a case fails, the assertion should stop the testbench execution

Ensure to Test random combinations of inputs (A, B, cin)

Ensure to test edge cases (e.g. zero, 15)

## Step 3: Debug and Fix Issues
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.

## Step 4: `run_test.sh` File Creation
- Create a shel script `run_test.sh` that contains the command to only run the testbench.
- execute the `run_test.sh` to make sure it successfully runs the testbench.