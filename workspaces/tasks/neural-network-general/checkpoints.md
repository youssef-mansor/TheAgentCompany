## Action Checkpoints - Total 3 pt (grade_checkpoint1)

### File creation neural_network.v: (1 pts)
   - A file is created for the neural network module `neural_network.v`

### File creation neural_network_tb.v: (1 pts)
   - A testbench file is created for the neural network module `neural_network_tb.v`

### File creation report.md: (1 pts)
   - A test report file is created `report.md`

---

## Main Module Checkpoints - Total 4 pts (grade_checkpoint2)

### 1. Interface & Modularity (1 pts)
   - The module correctly implements all required ports:
     - Clock and reset signals (clk, rst)
     - Wishbone interface (addr_in, data_in, we, data_out, ack_o)
     - Control signals (start, ready)
   - Design is modular with separate units for:
     - Input interface (Wishbone)
     - Hidden layer neurons
     - Output layer neuron
     - Output interface

### 2. Neural Network Architecture (1 pts)
   - Implements correct network structure:
     - 2-input, 2-neuron hidden layer
     - 1-neuron output layer
     - Sigmoid activation function
   - Proper weight and bias initialization
   - Correct data flow between layers

### 3. IEEE 754 & Wishbone Compliance (1 pts)
   - IEEE 754 single-precision floating point:
     - All computations use 32-bit floating point
     - Proper handling of special values
   - Wishbone protocol implementation:
     - Memory-mapped I/O for weights/biases
     - Correct acknowledge signal handling
     - Proper address decoding

### 4. Hardware Optimization (1 pts)
   - Efficient parallel processing:
     - Concurrent hidden layer neuron computation
     - Pipelined data flow
   - Resource utilization:
     - Shared activation function units
     - Efficient memory access
   - Control signal optimization

---

## Testbench Comprehensiveness - Total 7 pts (grade_checkpoint3)

### Basic Operations: (1 pts)
   - Test input loading
   - Test weight initialization
   - Test bias loading
   - Test computation flow

### Python Model Validation: (1 pts)
   - Test against Python outputs
   - Verify computation accuracy
   - Compare activation function results
   - Validate final outputs

### Wishbone Protocol: (1 pts)
   - Test memory write operations
   - Test memory read operations
   - Verify acknowledge signal
   - Test address decoding

### Control Flow: (1 pts)
   - Test start signal handling
   - Test ready signal assertion
   - Test computation timing
   - Test pipeline stages

### Edge Cases: (1 pts)
   - Test boundary values
   - Test special IEEE 754 values
   - Test overflow conditions
   - Test underflow conditions

### Parallel Processing: (1 pts)
   - Test concurrent operations
   - Test pipeline efficiency
   - Test resource sharing
   - Test timing constraints

### Reset Behavior: (1 pts)
   - Test synchronous reset
   - Test state clearing
   - Test initialization sequence
   - Test recovery from reset

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**



