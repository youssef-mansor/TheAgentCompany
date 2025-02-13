## Action Checkpoints - Total 3 pt (grade_checkpoint1)

### File creation vending_machine.v: (1 pts)
   - A file is created for the vending machine FSM module `vending_machine.v`

### File creation vending_machine_tb.v: (1 pts)
   - A testbench file is created for the vending machine FSM module `vending_machine_tb.v`

### File creation report.md: (1 pts)
   - A test file is created for the output of the testbench `report.md`

---

## Main Module Checkpoints - Total 4 pts (grade_checkpoint2)

### 1. Input Interface (1 pts)
   - The module correctly implements all required input ports:
     - Clock and reset signals
     - Coin input for multiple denominations
     - Keypad input for product selection

### 2. Output Interface (1 pts)
   - The module correctly implements all required output ports:
     - Change return amount
     - Product dispensed signal
     - Error condition signal
     - Current balance

### 3. FSM States (1 pts)
   - The FSM implements all required states:
     - Idle (waiting for input)
     - Coin Inserted (updating balance)
     - Product Selection (validating selection)
     - Dispense Product (with change calculation)
     - Error State (handling invalid inputs)
     - Reset State

### 4. Interface (1 pts)
   - The module header correctly defines the required ports:
   ```verilog
   input wire clk,                  // Clock signal
   input wire reset,                // Reset signal
   input wire [2:0] coin_in,       // Coin input ($0.05, $0.10, $0.25)
   input wire [3:0] keypad_in,     // Product selection input
   output reg [7:0] change_out,    // Change to return
   output reg product_dispensed,    // Product dispensed signal
   output reg error,               // Error condition signal
   output reg [7:0] balance        // Current balance
   ```

# File Content

## vending_machine.v

---

## Testbench Comprehensiveness checkpoints - Total 7 pts (grade_checkpoint3)

Ensure the following points are addressed within the test bench:

### Reset Behavior: (1 pts)
   - Verify FSM resets all outputs (balance, change) to zero upon reset.

### Valid Coin Handling: (1 pts)
   - Test acceptance of valid coin denominations and correct balance updates.

### Invalid Operations: (1 pts)
   - Test invalid coins, insufficient payments, and invalid product selections.

### Change Calculation: (1 pts)
   - Verify correct change return for payments exceeding product price.

### Partial Payments: (1 pts)
   - Test accumulation of multiple payments until product price is met.

### Edge Cases: (1 pts)
   - Test exact payment amount, maximum payment scenarios, and boundary conditions.

### State Coverage: (1 pts)
   - Verify all FSM states are reached and transitions are correct.

# File Content

## vending_machine_tb.v

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md