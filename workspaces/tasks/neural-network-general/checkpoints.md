## Action Checkpoints - Total 3 pt (grade_checkpoint1)

### File creation neural_network.v: (1 pts)
   - A file is created for the neural network module `neural_network.v`

### File creation neural_network_tb.v: (1 pts)
   - A testbench file is created for the neural network module `neural_network_tb.v`

### File creation report.md: (1 pts)
   - A test report file is created `report.md`

---

## Main Module Checkpoints - Total 4 pts (grade_checkpoint2)

### 1. Interface & Memory (1 pts)
   - The code implements the following components:
     - The code has clock and reset inputs
     - The code has input data interface (8-bit fixed point)
     - The code has weight memory interface
     - The code has output interface (8-bit fixed point)
     - The code has control signals (start, done)

### 2. Neural Network Structure (1 pts)
   - The code implements network architecture:
     - The code has input layer (4 neurons)
     - The code has hidden layer (4 neurons)
     - The code has output layer (2 neurons)
     - The code implements weight connections
     - The code implements bias values

### 3. Processing Elements (1 pts)
   - The code implements neuron operations:
     - The code performs fixed-point multiplication
     - The code accumulates weighted sums
     - The code implements activation function:
       - ReLU: output = (input > 0) ? input : 0
       - Fixed-point saturation handling
     - The code handles timing between operations
     - The code manages data flow between layers

### 4. Control Unit (1 pts)
   - The code implements control logic:
     - The code sequences layer operations
     - The code manages memory access
     - The code tracks computation progress
     - The code handles pipeline stages:
       - Input loading
       - Weight fetching
       - Computation
       - Activation
       - Output generation

---

## Testbench Comprehensiveness checkpoints - Total 7 pts (grade_checkpoint3)

### Basic Operation: (1 pts)
   - The testbench code tests:
     - The code tests single input propagation
     - The code verifies weight loading
     - The code checks activation function
     - The code validates output format

### Data Processing: (1 pts)
   - The testbench code tests:
     - The code tests multiple input patterns
     - The code verifies layer transitions
     - The code tests computation accuracy
     - The code checks fixed-point handling

### Memory Interface: (1 pts)
   - The testbench code tests:
     - The code tests weight loading
     - The code verifies memory access timing
     - The code tests bias loading
     - The code checks memory read patterns

### Control Flow: (1 pts)
   - The testbench code tests:
     - The code tests start/done signaling
     - The code verifies computation stages
     - The code tests reset behavior
     - The code checks pipeline operation

### Numerical Accuracy: (1 pts)
   - The testbench code tests:
     - The code tests fixed-point precision
     - The code verifies rounding behavior
     - The code tests overflow handling
     - The code validates against software model

### Edge Cases: (1 pts)
   - The testbench code tests:
     - The code tests maximum input values
     - The code tests minimum input values
     - The code tests zero inputs
     - The code verifies boundary conditions

### Performance: (1 pts)
   - The testbench code tests:
     - The code tests computation latency
     - The code verifies throughput
     - The code tests back-to-back operations
     - The code checks resource utilization

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**



