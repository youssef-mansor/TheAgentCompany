## Action Checkpoints - Total 3 pt (grade_checkpoint1)

### File creation cla.v: (1 pts)
   - A file is created for the CLA module `cla.v`

### File creation cla_tb.v: (1 pts)
   - A testbench file is created for the CLA module `cla_tb.v`

### File creation report.md: (1 pts)
   - A test file is created for the output of the testbench `report.md`

---

## Main Module Checkpoints - Total 4 pts (grade_checkpoint2)

### 1. Input/Output Interface (1 pts)
   - The module correctly implements all required ports:
     - 4-bit inputs A and B
     - Carry-in signal cin
     - 4-bit sum output S
     - Carry-out signal cout

### 2. Generate and Propagate Logic (1 pts)
   - Correctly implements:
     - Generate signals (G[i] = A[i] AND B[i])
     - Propagate signals (P[i] = A[i] XOR B[i])

### 3. Carry Lookahead Logic (1 pts)
   - Implements carry lookahead equations:
     - C1 = G0 + P0 * cin
     - C2 = G1 + P1 * C1
     - C3 = G2 + P2 * C2
     - C4 = G3 + P3 * C3 (cout)

### 4. Interface (1 pts)
   - The module header correctly defines the required ports:
   ```verilog
   input wire [3:0] A,      // 4-bit input A
   input wire [3:0] B,      // 4-bit input B
   input wire cin,          // Carry-in
   output wire [3:0] S,     // 4-bit sum
   output wire cout         // Carry-out
   ```

# File Content

## cla.v

---

## Testbench Comprehensiveness checkpoints - Total 7 pts (grade_checkpoint3)

Ensure the following points are addressed within the test bench:

### Full Combinatorial Test: (1 pts)
   - Test all possible combinations of inputs (A, B, cin).

### Edge Cases: (1 pts)
   - Test boundary conditions:
     - A = 0, B = 0, cin = 0
     - A = 15, B = 15, cin = 1
     - A = 8, B = 7, cin = 1

### Carry Propagation: (1 pts)
   - Verify correct carry propagation through all bits.

### Lookahead Logic: (1 pts)
   - Validate proper implementation of generate and propagate signals.

### Random Tests: (1 pts)
   - Perform randomized testing of inputs.

### Performance: (1 pts)
   - Verify carry lookahead behavior vs ripple carry.

### Error Cases: (1 pts)
   - Test overflow conditions and boundary scenarios.

# File Content

## cla_tb.v

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md