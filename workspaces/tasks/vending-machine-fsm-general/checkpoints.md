
---

## Vending Machine FSM Checkpoints - Total 5 pts (grade_checkpoint2)  

### 1. Module Interface (1 pt)  
   Defines the required ports correctly:  
   ```verilog  
   input wire clk, reset;       // Clock and reset signals  
   input wire [x:x] money;      // Inserted money  
   input wire [x:x] select_product; // Product selection  
   input wire [x:x] extra_cash; // Additional inserted money  
   output reg prodA, prodB, prodC; // Product dispense signals  
   output reg [x:x] balance;    // Remaining balance  
   ```  

### 2. State Definition (1 pt)  
   Defines parameters for the different states of the vending machine.  

### 3. State Transitions (1 pt)  
   Implements a procedural block to handle transitions between states.  

### 4. Reset Behavior (1 pt)  
   Ensures that on reset, the machine returns to a void/default/initial state.  

### 5. State Transition Logic (1 pt)  
   Uses a `case` statement to transition between states based on inserted money and product selection.  

### 6. Output Handling (1 pt)  
   Defines machine output logic in a procedural block based on the current state and uses `$display` for output visualization.  

# File Content  

## vending_machine.v  

---

## Vending Machine Testbench Checkpoints - Total 3 pts (grade_checkpoint2)  

### 1. Money Denominations (1 pt)  
   - Tests all possible money denominations (5,  10,  20).  

### 2. Product Selection (1 pt)  
   - Tests vending for all products (prodA, prodB, prodC).  

### 3. Output Validation (1 pt)  
   - Displays expected vs. actual results concisely and determines pass/fail status.  

# File Content  

## vending_machine_tb.v  

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md