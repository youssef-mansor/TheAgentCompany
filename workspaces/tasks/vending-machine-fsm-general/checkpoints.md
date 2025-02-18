## Action Checkpoints - Total 3 pts (grade_checkpoint1)

### File creation vending_machine.v: (1 pts)
   - A file is created for the vending machine FSM module `vending_machine.v` (1 pts)

### File creation vending_machine_tb.v: (1 pts)
   - A testbench file is created for the vending machine FSM module `vending_machine_tb.v` (1 pts)

### File creation report.md: (1 pts)
   - A test file is created for the output of the testbench `report.md` (1 pts)

---

## Main Module Checkpoints - Total 20 pts (grade_checkpoint2)

### 1. Interface & Inputs (5 pts)
   - The code implements the following components:
     - The code has clock and reset inputs (1 pts)
     - The code has coin inputs (nickel, dime, quarter) (1 pts)
     - The code has product selection input (1 pts)
     - The code has cancel transaction input (1 pts)
     - The code has output signals for: (1 pts)
       - Product dispensed
       - Change returned
       - Current amount display
       - Error conditions

### 2. State Machine Design (5 pts)
   - The code implements FSM architecture:
     - The code defines states: (1 pts)
       - IDLE: waiting for coins
       - COLLECTING: accepting coins
       - DISPENSING: giving product
       - RETURNING: giving change
       - ERROR: handling invalid conditions
     - The code implements state transitions (1 pts)
     - The code handles state encoding (1 pts)
     - The code manages state registers (1 pts)
     - The code implements proper state logic (1 pts)

### 3. Money Handling (5 pts)
   - The code implements transaction logic:
     - The code tracks accumulated amount (1 pts)
     - The code calculates required change (1 pts)
     - The code handles coin combinations: (1 pts)
       - Nickel (5¢)
       - Dime (10¢)
       - Quarter (25¢)
     - The code manages maximum amount (1 pts)
     - The code handles invalid amounts (1 pts)

### 4. Product & Change Control (5 pts)
   - The code implements dispensing logic:
     - The code verifies sufficient funds (1 pts)
     - The code manages product inventory (1 pts)
     - The code calculates optimal change combination (1 pts)
     - The code handles transaction completion (1 pts)
     - The code manages error conditions: (1 pts)
       - Insufficient funds
       - Invalid selection
       - No change available
       - Out of stock

---

## Testbench Comprehensiveness checkpoints - Total 28 pts (grade_checkpoint3)

### Basic Operation: (4 pts)
   - The testbench code tests:
     - The code tests coin insertion sequence (1 pts)
     - The code verifies product selection (1 pts)
     - The code checks change return (1 pts)
     - The code validates state transitions (1 pts)

### Money Handling: (4 pts)
   - The testbench code tests:
     - The code tests different coin combinations (1 pts)
     - The code verifies amount accumulation (1 pts)
     - The code tests change calculation (1 pts)
     - The code checks maximum amount handling (1 pts)

### Product Selection: (4 pts)
   - The testbench code tests:
     - The code tests valid product selection (1 pts)
     - The code verifies price checking (1 pts)
     - The code tests inventory management (1 pts)
     - The code checks dispensing signals (1 pts)

### Change Return: (4 pts)
   - The testbench code tests:
     - The code tests exact change scenarios (1 pts)
     - The code verifies change combinations (1 pts)
     - The code tests cancel operation (1 pts)
     - The code checks change timing (1 pts)

### Error Handling: (4 pts)
   - The testbench code tests:
     - The code tests insufficient funds (1 pts)
     - The code verifies invalid selections (1 pts)
     - The code tests timeout conditions (1 pts)
     - The code checks error recovery (1 pts)

### State Transitions: (4 pts)
   - The testbench code tests:
     - The code tests all state transitions (1 pts)
     - The code verifies illegal transitions (1 pts)
     - The code tests reset behavior (1 pts)
     - The code checks state persistence (1 pts)

### Complete Transactions: (4 pts)
   - The testbench code tests:
     - The code tests full transaction cycles (1 pts)
     - The code verifies concurrent operations (1 pts)
     - The code tests back-to-back transactions (1 pts)
     - The code checks system stability (1 pts)

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md