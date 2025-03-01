
---

## Main Module Checkpoints - Total 20 pts (grade_checkpoint2)

### 1. Interface & Memory (5 pts)
   - The code implements the following components:
     - The code has clock and reset inputs properly defined (1 pts)
     - The code has input data interface with 8-bit fixed point (1 pts)
     - The code has weight memory interface defined (1 pts)
     - The code has output interface with 8-bit fixed point (1 pts)
     - The code has control signals (start, done) are defined (1 pts)

### 2. Neural Network Structure (5 pts)
   - The code implements network architecture:
     - The code implements input layer with 4 neurons (1 pts)
     - The code implements hidden layer with 4 neurons (1 pts)
     - The code implements output layer with 2 neurons (1 pts)
     - The code implements weight connections properly (1 pts)
     - The code implements bias values properly (1 pts)

### 3. Processing Elements (4 pts)
   - The code implements neuron operations:
     - The code performs fixed-point multiplication correctly (1 pts)
     - The code accumulates weighted sums properly (1 pts)
     - The code implements ReLU activation function (1 pts)
     - The code handles fixed-point saturation (1 pts)

### 4. Control Unit (4 pts)
   - The code implements control logic:
     - The code sequences layer operations (1 pts)
     - The code manages memory access  (1 pts)
     - The code handles input loading and weight fetching (1 pts)
     - The code manages computation and output stages (1 pts)

---

## Testbench Comprehensiveness checkpoints - Total 15 pts (grade_checkpoint3)
   - The code verifies weight loading (1 pts)
   - The code tests multiple input patterns (1 pts)
   - The code tests bias loading (1 pts)
   - The code checks memory read patterns (1 pts)
   - The code tests start/done signaling (1 pts)
   - The code validates against python model (6 pts)
   - The code tests maximum input values (1 pts)
   - The code tests minimum input values (1 pts)
   - The code tests zero inputs (1 pts)

---
