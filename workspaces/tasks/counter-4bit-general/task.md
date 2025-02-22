# Verilog Four-Bit Counter Implementation and Testing

## Step 0: Files creation
Create the following files
- `/workspace/report.md`
- `/workspace/counter.v`
- `/workspace/counter_tb.v`

## Step 1: Implement a Four-Bit Counter
Design a four-bit counter in Verilog with the following interface:  
- `clk` 
- `reset`
- `count` 
Place the implemented counter into `/workspace/counter.v`

## Step 2: Create a Self-Checking Testbench  
- Develop a comprehensive testbench for the counter module that covers all possible cases.  
- Ensure it automatically verifies correctness and prints the results.  
- Save the output in a Markdown file with:  
  - **Test title**  
  - **Pass/Fail status**  

Ensure the following points are addressed within the test bench 

**Normal Increment:**
     Allow the counter to increment and observe proper functionality at trigerring edge.
**Wrap-Around:**
     Ensure the counter wraps back to 0 after reaching 15 (4-bit overflow).

Ensure the testbench prints each test's pass/fail status directly into `/workspace/report.md` using Verilog file operations, with one line per test indicating "pass" or "fail."

Place the implemented testbench into `/workspace/counter_tb.v`

## Step 3: Debug and Fix Issues  
- If the module does not pass all test cases, revisit and refine the Verilog code.  
- Modify the design until all test cases pass successfully.  