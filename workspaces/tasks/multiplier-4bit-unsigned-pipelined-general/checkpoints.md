
---

## Main Module Checkpoints - Total 7 pts (grade_checkpoint2)

### 1. Interface & Modularity (1 pts)
   - The code implements the following interface:
      - `clk`
      - `reset`
      - `a` (4-bit input)
      - `b` (4-bit input)
      - `product` (8-bit output)
      - `valid` (output)

### 2. Pipeline Stages (1 pts)
   - The code implements the pipeline structure.

### 3. Multiplication Logic (2 pts)
     - The code implements shifting for partial products (1 pts)
     - The code accumulates partial products correctly (1 pts)

### 4. Control Logic (3 pts)
   - The code implements control mechanisms:
     - The code tracks pipeline validity (1 pts)
     - The code handles stall conditions (1 pts)
     - The code manages data flow between stages (1 pts)
---

## Testbench Comprehensiveness checkpoints - Total 7 pts (grade_checkpoint3)

### Zero Multiplication: (1 pts)
     - The code tests zero multiplication


### Boundary Values: (3 pts)
   - The testbench code tests:
     - The code tests maximum values (15 x 15) (1 pts)
     - The code tests minimum values (0 x N) (1 pts)
     - The code tests single bit multiplications (1 pts)

### Pipeline Hazards: (2 pts)
   - The testbench code tests:
     - The code tests pipeline stalls (1 pts)
     - The code tests valid signal propagation (1 pts)

### Exhaustive Testing: (1 pts)
     - The code tests all input combinations.

---
