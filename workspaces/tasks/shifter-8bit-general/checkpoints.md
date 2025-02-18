## Action Checkpoints - Total 3 pts (grade_checkpoint1)

### File creation shifter.v: (1 pts)
   - A file is created for the shifter module `shifter.v` (1 pts)

### File creation shifter_tb.v: (1 pts)
   - A testbench file is created for the shifter module `shifter_tb.v` (1 pts)

### File creation report.md: (1 pts)
   - A test file is created for the output of the testbench `report.md` (1 pts)

---

## Main Module Checkpoints - Total 20 pts (grade_checkpoint2)

### 1. Shift Logic (5 pts)
   - The code implements shift operations:
     - The code performs left shift when direction is 1 (1 pts)
     - The code performs right shift when direction is 0 (1 pts)
     - The code shifts on rising clock edge (1 pts)
     - The code maintains proper bit order (1 pts)
     - The code handles direction changes properly (1 pts)

### 2. Register Implementation (5 pts)
   - The code implements 8-bit register:
     - The code maintains 8-bit width properly (1 pts)
     - The code discards shifted-out bits correctly (1 pts)
     - The code inserts new bits at proper position (1 pts)
     - The code preserves unshifted bits (1 pts)
     - The code prevents data corruption (1 pts)

### 3. Reset Logic (5 pts)
   - The code implements reset functionality:
     - The code resets register to zero when active (1 pts)
     - The code maintains reset priority over clock (1 pts)
     - The code handles asynchronous reset properly (1 pts)
     - The code maintains reset until deasserted (1 pts)
     - The code resumes operation after reset (1 pts)

### 4. Interface (5 pts)
   - The code implements module ports:
     - The code defines clock and reset inputs properly (1 pts)
     - The code defines 8-bit shift_in input properly (1 pts)
     - The code defines direction input properly (1 pts)
     - The code defines 8-bit shift_out output properly (1 pts)
     - The code uses correct port directions (1 pts)

---

## Testbench Comprehensiveness checkpoints - Total 28 pts (grade_checkpoint3)

### Left Shift Operations: (4 pts)
   - The testbench code tests:
     - The code tests basic left shift operation (1 pts)
     - The code verifies MSB handling (1 pts)
     - The code tests consecutive left shifts (1 pts)
     - The code checks timing requirements (1 pts)

### Right Shift Operations: (4 pts)
   - The testbench code tests:
     - The code tests basic right shift operation (1 pts)
     - The code verifies LSB handling (1 pts)
     - The code tests consecutive right shifts (1 pts)
     - The code checks timing requirements (1 pts)

### Direction Control: (4 pts)
   - The testbench code tests:
     - The code tests direction changes (1 pts)
     - The code verifies direction timing (1 pts)
     - The code tests alternating directions (1 pts)
     - The code checks direction stability (1 pts)

### Reset Behavior: (4 pts)
   - The testbench code tests:
     - The code tests reset during shifts (1 pts)
     - The code verifies reset priority (1 pts)
     - The code tests reset release behavior (1 pts)
     - The code checks multiple reset scenarios (1 pts)

### Data Patterns: (4 pts)
   - The testbench code tests:
     - The code tests alternating patterns (1 pts)
     - The code tests walking ones (1 pts)
     - The code tests walking zeros (1 pts)
     - The code tests random patterns (1 pts)

### Timing Verification: (4 pts)
   - The testbench code tests:
     - The code tests clock to output delay (1 pts)
     - The code verifies setup/hold times (1 pts)
     - The code tests back-to-back operations (1 pts)
     - The code checks clock edge sensitivity (1 pts)

### Boundary Cases: (4 pts)
   - The testbench code tests:
     - The code tests maximum shift sequences (1 pts)
     - The code verifies bit preservation (1 pts)
     - The code tests edge conditions (1 pts)
     - The code checks corner cases (1 pts)

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## shifter.v

---

## Testbench Comprehensiveness checkpoints - Total 28 pts (grade_checkpoint3)

### Left Shift Operations: (4 pts)
    Verify that when `direction = 1`, the register contents shift left, and `shift_out` holds the correct value after the shift.

### Right Shift Operations: (4 pts)
    Verify that when `direction = 0`, the register contents shift right, and `shift_out` holds the correct value after the shift.

### Direction Control: (4 pts)
    Verify that bits shifted out of the register are discarded, and verify that no unexpected data appears at the empty positions.

### Reset Behavior: (4 pts)
    Verify that the reset functionality is implemented correctly.

### Data Patterns: (4 pts)
    Verify that the data patterns are handled correctly.

### Timing Verification: (4 pts)
    Verify that the clock to output delay is within acceptable limits.

### Boundary Cases: (4 pts)
    Verify that the code handles edge conditions and corner cases correctly.

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)

Returns the count of passed test cases in the `report.md` file and the total number of cases in the file in the specific format: 

**Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## shifter_tb.v

## report.md