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
- Ensure it automatically verifies correctness and prints the results.  
- Save the output in a Markdown file with:  
  - **Test title**  
  - **Pass/Fail status**  

Place the implemented testbench into `/workspace/dff_tb.v`  
Place the test report into `/workspace/report.md` even if not all tests passed. make sure to print testbench results into report.md

## Step 3: Debug and Fix Issues  
- If the module does not pass all test cases, revisit and refine the Verilog code.  
- Modify the design until all test cases pass successfully.  