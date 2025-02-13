# Verilog Vending Machine FSM Implementation and Testing

## Step 1: Implement a Vending Machine FSM
Design a vending machine FSM in Verilog with the following interface:
- `clk`
- `reset`
- `coin_in` (for $0.05, $0.10, $0.25)
- `keypad_in` (for product selection)
- `change_out` (change to return)
- `product_dispensed` (output)
- `error` (error condition)
- `balance` (current balance)

The FSM should handle:
- Multiple coin denominations ($0.05, $0.10, $0.25)
- Partial payments with balance tracking
- Product selection via keypad
- Change calculation and return
- Error conditions (invalid coins, insufficient payment, invalid selection)

Place the implemented FSM into `/openhands/workspace/vending_machine.v`

## Step 2: Create a Self-Checking Testbench
- Develop a comprehensive testbench for the vending machine FSM that covers all possible cases.
- Ensure it automatically verifies correctness and prints the results.
- Save the output in a Markdown file with:
  - **Test title**
  - **Pass/Fail status**

Ensure the following points are addressed within the testbench:

### Reset Behavior: (1 pts)
   - Verify FSM resets all outputs (balance, change) to zero upon reset.

### Valid Operations: (1 pts)
   - Test valid coin inputs and product selections with correct balance updates.

### Error Handling: (1 pts)
   - Verify proper handling of invalid coins, insufficient payment, invalid selections.

### Change Calculation: (1 pts)
   - Test correct change return for payments exceeding product price.

### Partial Payments: (1 pts)
   - Verify accumulation of multiple payments until product price is met.

### Edge Cases: (1 pts)
   - Test exact payment, excess payment, insufficient payment scenarios.

### State Transitions: (1 pts)
   - Verify correct FSM state transitions through all operational modes.

Place the implemented testbench into `/openhands/workspace/vending_machine_tb.v`
Place the test report into `/openhands/workspace/report.md`

## Step 3: Debug and Fix Issues
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.
