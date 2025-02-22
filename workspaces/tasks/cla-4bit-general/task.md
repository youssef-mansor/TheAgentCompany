# Verilog 4-bit Carry Lookahead Adder Implementation and Testing

## Step 0: Files creation
Create the following files
- `/workspace/report.md`
- `/workspace/cla.v`
- `/workspace/cla_tb.v`

## Step 1: Implement a 4-bit Carry Lookahead Adder
Design a 4-bit CLA in Verilog with the following interface:
- `A` (4-bit input)
- `B` (4-bit input)
- `cin` (carry-in)
- `S` (4-bit sum output)
- `cout` (carry-out)

The CLA should use generate (G) and propagate (P) signals for implementation of lookahead logic

Place the implemented CLA into `/workspace/cla.v`

## Step 2: Create a Self-Checking Testbench
- Develop a comprehensive testbench for the CLA module that covers all possible cases.
- Ensure it automatically verifies correctness and prints the results.
- Save the output in a Markdown file with:
  - **Test title**
  - **Pass/Fail status**

Ensure to Test all possible combinations of inputs (A, B, cin)
Ensure the testbench prints each test's pass/fail status directly into `/workspace/report.md` using Verilog file operations, with one line per test indicating "pass" or "fail."

Place the implemented testbench into `/workspace/cla_tb.v`

## Step 3: Debug and Fix Issues
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.
