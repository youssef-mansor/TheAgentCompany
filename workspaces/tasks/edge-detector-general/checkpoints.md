
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
   
---

## Testbench Comprehensiveness checkpoints - Total 3 pts (grade_checkpoint3)

Ensure the following points are addressed within the test bench 

### Edge Detection: (1 pts)
   - Verify that `signal_out` is `1` only when there is a rising edge on `signal_in`.

### Multiple Edges: (1 pts)
   - Apply multiple rising edges on `signal_in` and confirm that `signal_out` is asserted for one clock cycle for each rising edge.

### No False Positives: (1 pts)
   - Ensure that `signal_out` remains `0` when `signal_in` remains stable (high or low) between clock cycles.

---
