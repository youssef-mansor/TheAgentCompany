## Action Checkpoints - Total 3 pt (grade_checkpoint1)

### File creation vending_machine.v: (1 pts)
   - A file is created for the vending machine FSM module `vending_machine.v`

### File creation vending_machine_tb.v: (1 pts)
   - A testbench file is created for the vending machine FSM module `vending_machine_tb.v`

### File creation report.md: (1 pts)
   - A test file is created for the output of the testbench `report.md`

---

## Main Module Checkpoints - Total 4 pts (grade_checkpoint2)

### 1. Interface & Inputs (1 pts)
   - The code implements the following components:
     - The code has clock and reset inputs
     - The code has coin inputs (nickel, dime, quarter)
     - The code has product selection input
     - The code has cancel transaction input
     - The code has output signals for:
       - Product dispensed
       - Change returned
       - Current amount display
       - Error conditions

### 2. State Machine Design (1 pts)
   - The code implements FSM architecture:
     - The code defines states:
       - IDLE: waiting for coins
       - COLLECTING: accepting coins
       - DISPENSING: giving product
       - RETURNING: giving change
       - ERROR: handling invalid conditions
     - The code implements state transitions
     - The code handles state encoding
     - The code manages state registers

### 3. Money Handling (1 pts)
   - The code implements transaction logic:
     - The code tracks accumulated amount
     - The code calculates required change
     - The code handles coin combinations:
       - Nickel (5¢)
       - Dime (10¢)
       - Quarter (25¢)
     - The code manages maximum amount
     - The code handles invalid amounts

### 4. Product & Change Control (1 pts)
   - The code implements dispensing logic:
     - The code verifies sufficient funds
     - The code manages product inventory
     - The code calculates optimal change combination
     - The code handles transaction completion
     - The code manages error conditions:
       - Insufficient funds
       - Invalid selection
       - No change available
       - Out of stock

---

## Testbench Comprehensiveness checkpoints - Total 7 pts (grade_checkpoint3)

### Basic Operation: (1 pts)
   - The testbench code tests:
     - The code tests coin insertion sequence
     - The code verifies product selection
     - The code checks change return
     - The code validates state transitions

### Money Handling: (1 pts)
   - The testbench code tests:
     - The code tests different coin combinations
     - The code verifies amount accumulation
     - The code tests change calculation
     - The code checks maximum amount handling

### Product Selection: (1 pts)
   - The testbench code tests:
     - The code tests valid product selection
     - The code verifies price checking
     - The code tests inventory management
     - The code checks dispensing signals

### Change Return: (1 pts)
   - The testbench code tests:
     - The code tests exact change scenarios
     - The code verifies change combinations
     - The code tests cancel operation
     - The code checks change timing

### Error Handling: (1 pts)
   - The testbench code tests:
     - The code tests insufficient funds
     - The code verifies invalid selections
     - The code tests timeout conditions
     - The code checks error recovery

### State Transitions: (1 pts)
   - The testbench code tests:
     - The code tests all state transitions
     - The code verifies illegal transitions
     - The code tests reset behavior
     - The code checks state persistence

### Complete Transactions: (1 pts)
   - The testbench code tests:
     - The code tests full transaction cycles
     - The code verifies concurrent operations
     - The code tests back-to-back transactions
     - The code checks system stability

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md