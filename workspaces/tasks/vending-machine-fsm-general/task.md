# Verilog Vending Machine FSM Implementation and Testing  

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

## Step 2: Create a Self-Checking Testbench  
- Develop a comprehensive testbench for the vending machine FSM with asserstions that covers all possible cases.  
- If a case fails, the assertion should stop the testbench execution. 


Ensure the testbench addresses the following points:  
- Tests with all possible money denominations.  
- Testing with all products.  

## Step 3: Debug and Fix Issues  
- If the module does not pass all test cases, revisit and refine the Verilog code.  
- Modify the design until all test cases pass successfully.  

## Step 4: `run_test.sh` File Creation
- Create a shel script `run_test.sh` that contains the command to only run the testbench.
- execute the `run_test.sh` to make sure it successfully runs the testbench.