## Action Checkpoints - Total 3 pts (grade_checkpoint1)

### File creation neural_network.v: (1 pts)
   - A file is created for the neural network module `neural_network.v` (1 pts)

### File creation neural_network_tb.v: (1 pts)
   - A testbench file is created for the neural network module `neural_network_tb.v` (1 pts)

### File creation report.md: (1 pts)
   - A test report file is created `report.md` (1 pts)

---

## Main Module Checkpoints - Total 20 pts (grade_checkpoint2)

### 1. Interface & Memory (5 pts)
   - The code implements the following components:
     - The code has clock and reset inputs properly defined (1 pts)
     - The code has input data interface with 8-bit fixed point (1 pts)
     - The code has weight memory interface properly defined (1 pts)
     - The code has output interface with 8-bit fixed point (1 pts)
     - The code has control signals (start, done) properly defined (1 pts)

### 2. Neural Network Structure (5 pts)
   - The code implements network architecture:
     - The code implements input layer with 4 neurons (1 pts)
     - The code implements hidden layer with 4 neurons (1 pts)
     - The code implements output layer with 2 neurons (1 pts)
     - The code implements weight connections properly (1 pts)
     - The code implements bias values properly (1 pts)

### 3. Processing Elements (5 pts)
   - The code implements neuron operations:
     - The code performs fixed-point multiplication correctly (1 pts)
     - The code accumulates weighted sums properly (1 pts)
     - The code implements ReLU activation function (1 pts)
     - The code handles fixed-point saturation (1 pts)
     - The code manages data flow between layers (1 pts)

### 4. Control Unit (5 pts)
   - The code implements control logic:
     - The code sequences layer operations properly (1 pts)
     - The code manages memory access timing (1 pts)
     - The code tracks computation progress (1 pts)
     - The code handles input loading and weight fetching (1 pts)
     - The code manages computation and output stages (1 pts)

---

## Testbench Comprehensiveness checkpoints - Total 28 pts (grade_checkpoint3)

### Basic Operation: (4 pts)
   - The testbench code tests:
     - The code tests single input propagation (1 pts)
     - The code verifies weight loading (1 pts)
     - The code checks activation function (1 pts)
     - The code validates output format (1 pts)

### Data Processing: (4 pts)
   - The testbench code tests:
     - The code tests multiple input patterns (1 pts)
     - The code verifies layer transitions (1 pts)
     - The code tests computation accuracy (1 pts)
     - The code checks fixed-point handling (1 pts)

### Memory Interface: (4 pts)
   - The testbench code tests:
     - The code tests weight loading sequence (1 pts)
     - The code verifies memory access timing (1 pts)
     - The code tests bias loading sequence (1 pts)
     - The code checks memory read patterns (1 pts)

### Control Flow: (4 pts)
   - The testbench code tests:
     - The code tests start/done signaling (1 pts)
     - The code verifies computation stages (1 pts)
     - The code tests reset behavior (1 pts)
     - The code checks pipeline operation (1 pts)

### Numerical Accuracy: (4 pts)
   - The testbench code tests:
     - The code tests fixed-point precision (1 pts)
     - The code verifies rounding behavior (1 pts)
     - The code tests overflow handling (1 pts)
     - The code validates against software model (1 pts)

### Edge Cases: (4 pts)
   - The testbench code tests:
     - The code tests maximum input values (1 pts)
     - The code tests minimum input values (1 pts)
     - The code tests zero inputs (1 pts)
     - The code verifies boundary conditions (1 pts)

### Performance: (4 pts)
   - The testbench code tests:
     - The code tests computation latency (1 pts)
     - The code verifies throughput (1 pts)
     - The code tests back-to-back operations (1 pts)
     - The code checks resource utilization (1 pts)

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**



