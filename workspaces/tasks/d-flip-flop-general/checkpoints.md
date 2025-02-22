## Action Checkpoints - Total 3 pt (grade_checkpoint1)

### File creation dff.v: (1 pts)
   - A file is created for the D flip-flop module `dff.v`

### File creation dff_tb.v: (1 pts)
   - A testbench file is created for the D flip-flop module `dff_tb.v`

### File creation report.md: (1 pts)
   - A test file is created for the output of the testbench `report.md`

---

## Main Module Checkpoints - Total 4 pts (grade_checkpoint2)

### 1. D to Q Logic (1 pts)
   - The output `q` should follow the input `d` on each rising edge of `clk` when `reset` is inactive.

### 2. Reset Priority (1 pts)
   - The output `q` should be reset to 0 when the `reset` signal is active, regardless of the clock or `d` value.

### 3. Edge-Triggered Behavior (1 pts)
   - The flip-flop should be edge-triggered, updating `q` on the rising edge of `clk`.

### 4. Interface (1 pts)
   - The module header should correctly define the following ports:
   ```verilog
   input wire clk,    // Clock signal
   input wire reset,  // Reset signal
   input wire d,      // Data input
   output reg q       // Output q
   ```

# File Content

## dff.v

---

### Testbench Comprehensiveness checkpoints - Total 1 pts (grade_checkpoint3)

Ensure the following points are addressed within the test bench 

### Normal Operation: (1 pts)
   - Different test cases with different values of `d` at different time intervals are applied.


# File Content

## dff_tb.v

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md
