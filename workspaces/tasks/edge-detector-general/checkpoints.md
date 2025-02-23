## Action Checkpoints - Total 3 pt (grade_checkpoint1)

### File creation edge_detector.v: (1 pts)
   - A file is created for the edge detector module `edge_detector.v`

### File creation edge_detector_tb.v: (1 pts)
   - A testbench file is created for the edge detector module `edge_detector_tb.v`

### File creation report.md: (1 pts)
   - A test file is created for the output of the testbench `report.md`

---

## Main Module Checkpoints - Total 4 pts (grade_checkpoint2)

### 1. Edge Detection Logic (1 pts)
   - The module should output `1` for one clock cycle when a rising edge of `signal_in` occurs.

### 2. Reset Priority (1 pts)
   - If `reset` is active, `signal_out` should be `0` regardless of the clock or `signal_in`.

### 3. Clock Behavior (1 pts)
   - The output `signal_out` should only be asserted high for one clock cycle on the rising edge of `signal_in`.

### 4. Interface (1 pts)
   - The module should define the ports appropriately, as specified in the prompt:
   - `clk`     
   - `reset`
   - `signal_in`
   - `signal_out`
   
# File Content

## edge_detector.v

---

## Testbench Comprehensiveness checkpoints - Total 3 pts (grade_checkpoint3)

Ensure the following points are addressed within the test bench 

### Edge Detection: (1 pts)
   - Verify that `signal_out` is `1` only when there is a rising edge on `signal_in`.

### Multiple Edges: (1 pts)
   - Apply multiple rising edges on `signal_in` and confirm that `signal_out` is asserted for one clock cycle for each rising edge.

### No False Positives: (1 pts)
   - Ensure that `signal_out` remains `0` when `signal_in` remains stable (high or low) between clock cycles.


# File Content

## edge_detector_tb.v

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md