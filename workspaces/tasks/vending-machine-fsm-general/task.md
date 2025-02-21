# Verilog Vending Machine FSM Implementation and Testing  

## Step 0: Files Creation  
Create the following files:  
- `/workspace/report.md`  
- `/workspace/vending_machine.v`  
- `/workspace/vending_machine_tb.v`  

## Step 1: Implement a Vending Machine FSM  
Design a vending machine FSM in Verilog with the following interface:  
- **Inputs:**  
  - `clk` (clock signal)  
  - `reset` (reset signal)  
  - `money` (inserted amount:  5,  10,  20)  
  - `select_product` (product selection: 2-bit input)  
  - `extra_cash` (additional money inserted)  

- **Outputs:**  
  - `prodA` (dispense product A)  
  - `prodB` (dispense product B)  
  - `prodC` (dispense product C)  
  - `balance` (remaining balance to return)  

The FSM should handle:  
- Selection of one of three products:  
  - **Product A:**  5  
  - **Product B:**  10  
  - **Product C:**  15  
- Money insertion in denominations of  5,  10, and  20.  
- Returning change when the inserted amount exceeds the product price.  
- Returning the full amount if the purchase is canceled before completion.  
- Waiting for additional money if the inserted amount is insufficient.  

Place the implemented FSM into `/workspace/vending_machine.v`.  

## Step 2: Create a Self-Checking Testbench  
- Develop a comprehensive testbench for the vending machine FSM that covers all possible cases.  
- Ensure it automatically verifies correctness and prints the results.  
- Save the output in a Markdown (test report) file with:  
  - **Test title**  
  - **Pass/Fail status**  

Ensure the testbench addresses the following points:  
- Tests with all possible money denominations.  
- Testing with all products.  
- Concise display of expected vs. actual result with pass/fail status by use of `$display` for output visualization. 
- The output for each run should be **directly written to `/workspace/report.md` as part of the testbench execution**.

Place the implemented testbench into `/workspace/vending_machine_tb.v`.  
Place the test report into `/workspace/report.md`.  

## Step 3: Debug and Fix Issues  
- If the module does not pass all test cases, revisit and refine the Verilog code.  
- Modify the design until all test cases pass successfully.  