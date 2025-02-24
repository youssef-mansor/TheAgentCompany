
---

## Main Module Checkpoints - Total 4 pts (grade_checkpoint2)

### 1. Increment Logic  (1 pts)
    Adds 1 to the count on each rising edge of `clk`. 

### 2. Width Constraint  (1 pts)
    Limits the counter to a range of 0 to 15 (4 bits).

### 3. Interface  (1 pts)
    The module header correctly defines the required ports:  
- `clk`
- `reset`
- `count` (4 bits)

---

## Testbench Comprehensiveness checkpoints - Total 2 pts (grade_checkpoint3)

Ensure the following points are addressed within the test bench 

### Normal Increment: (1 pts)
     After resetting, the simulation waits long enough to test counter increments at the triggering edge.
### Wrap-Around: (1 pts)
     Ensure the counter wraps back to 0 after reaching 15 (4-bit overflow).

---





