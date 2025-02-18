## Action Checkpoints - Total 3 pts (grade_checkpoint1)

### File creation fpu.v: (1 pts)
   - A file is created for the FPU module `fpu.v` (1 pts)

### File creation fpu_tb.v: (1 pts)
   - A testbench file is created for the FPU module `fpu_tb.v` (1 pts)

### File creation report.md: (1 pts)
   - A test report file is created `report.md` (1 pts)

---

## Main Module Checkpoints - Total 20 pts (grade_checkpoint2)

### 1. Interface & Modularity (5 pts)
   - The code implements module ports:
     - The code defines clock and control inputs properly (1 pts)
     - The code defines operand inputs correctly (1 pts)
     - The code defines result output properly (1 pts)
     - The code defines exception outputs properly (1 pts)
     - The code uses correct port directions and types (1 pts)

### 2. Operations Support (5 pts)
   - The code implements IEEE-754 operations:
     - The code implements addition/subtraction correctly (1 pts)
     - The code implements multiplication correctly (1 pts)
     - The code implements division correctly (1 pts)
     - The code implements int-to-float conversion (1 pts)
     - The code implements float-to-int conversion (1 pts)

### 3. IEEE 754 Compliance (5 pts)
   - The code implements standard features:
     - The code handles special values (NaN, Infinity, Zero) (1 pts)
     - The code implements all rounding modes (1 pts)
     - The code detects overflow and underflow (1 pts)
     - The code handles division by zero (1 pts)
     - The code detects invalid operations (1 pts)

### 4. Pipeline Implementation (5 pts)
   - The code implements pipelining:
     - The code implements decode stage properly (1 pts)
     - The code implements execute stage properly (1 pts)
     - The code implements result stage properly (1 pts)
     - The code handles pipeline stalls correctly (1 pts)
     - The code maintains consistent latency (1 pts)

---

## Testbench Comprehensiveness checkpoints - Total 28 pts (grade_checkpoint3)

### Basic Operations: (4 pts)
   - The testbench code tests:
     - The code tests addition operations (1 pts)
     - The code tests subtraction operations (1 pts)
     - The code tests multiplication operations (1 pts)
     - The code tests division operations (1 pts)

### Special Values: (4 pts)
   - The testbench code tests:
     - The code tests NaN handling (1 pts)
     - The code tests infinity handling (1 pts)
     - The code tests zero handling (1 pts)
     - The code tests denormalized numbers (1 pts)

### Rounding Modes: (4 pts)
   - The testbench code tests:
     - The code tests round to nearest even (1 pts)
     - The code tests round toward zero (1 pts)
     - The code tests round toward +∞ (1 pts)
     - The code tests round toward -∞ (1 pts)

### Exceptions: (4 pts)
   - The testbench code tests:
     - The code tests overflow conditions (1 pts)
     - The code tests underflow conditions (1 pts)
     - The code tests division by zero (1 pts)
     - The code tests invalid operations (1 pts)

### Conversions: (4 pts)
   - The testbench code tests:
     - The code tests positive int-to-float conversion (1 pts)
     - The code tests negative int-to-float conversion (1 pts)
     - The code tests positive float-to-int conversion (1 pts)
     - The code tests negative float-to-int conversion (1 pts)

### Edge Cases: (4 pts)
   - The testbench code tests:
     - The code tests maximum float values (1 pts)
     - The code tests minimum float values (1 pts)
     - The code tests power of 2 boundaries (1 pts)
     - The code tests normalization cases (1 pts)

### Pipeline: (4 pts)
   - The testbench code tests:
     - The code tests operation sequences (1 pts)
     - The code tests mixed operations (1 pts)
     - The code tests data dependencies (1 pts)
     - The code tests pipeline throughput (1 pts)

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**



