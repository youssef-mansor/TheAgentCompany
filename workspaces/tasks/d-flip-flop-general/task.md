# Verilog D Flip-Flop Implementation and Testing  

## Step 0: Files creation
Create the following files
- `/workspace/report.md`
- `/workspace/dff.v` 
- `/workspace/dff_tb.v`

## Step 1: Implement a D Flip-Flop  
Design a D flip-flop in Verilog with the following interface:  
- `clk`  
- `reset`  
- `d`  
- `q`  

Place the implemented flip-flop into `/workspace/dff.v`  

## Step 2: Create a Self-Checking Testbench  
- Develop a comprehensive testbench for the D Flip Flop module that covers all possible cases.  
- Save the output in a Markdown file with:  
  - **Test title**  
  - **Pass/Fail status**  

Ensure the testbench prints each test's pass/fail status directly into `/workspace/report.md` using Verilog file operations, with one line per test indicating "pass" or "fail."

Place the implemented testbench into `/workspace/dff_tb.v`  

## Step 3: Debug and Fix Issues  
- If the module does not pass all test cases, revisit and refine the Verilog code.  
- Modify the design until all test cases pass successfully.  