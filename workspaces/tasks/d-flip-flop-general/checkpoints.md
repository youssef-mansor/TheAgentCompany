
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
   - `clk` 
   - `reset`
   - `d`
   - `q`

---

### Testbench Comprehensiveness checkpoints - Total 1 pts (grade_checkpoint3)

Ensure the following points are addressed within the test bench 

### Normal Operation: (1 pts)
   - Different test cases with different values of `d` at different time intervals are applied.

---
