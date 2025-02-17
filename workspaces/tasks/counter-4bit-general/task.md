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

**Normal Increment: (1 pts)**
     Allow the counter to increment and observe proper functionality at trigerring edge.
**Wrap-Around: (1 pts)**
     Ensure the counter wraps back to 0 after reaching 15 (4-bit overflow).

Place the implemented testbench into `/workspace/counter_tb.v`
Place the implemented report into `/workspace/report.md`

## Step 3: Debug and Fix Issues  
- If the module does not pass all test cases, revisit and refine the Verilog code.  
- Modify the design until all test cases pass successfully.  