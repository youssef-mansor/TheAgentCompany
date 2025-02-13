# Verilog Neural Network Implementation and Testing

## Step 1: Implement a Neural Network in Verilog
Design a synthesizable neural network module in Verilog that implements the following Python model:

```python
import torch
import torch.nn as nn

class CustomNN(nn.Module):
    def __init__(self):
        super(CustomNN, self).__init__()
        # Define the layers
        self.hidden = nn.Linear(2, 2)  # Input to hidden layer (2 inputs -> 2 neurons)
        self.output = nn.Linear(2, 1)  # Hidden to output layer (2 neurons -> 1 output)

        # Manually set weights and biases for the hidden layer
        self.hidden.weight = nn.Parameter(torch.tensor([[4.0, 4.0], [-4.0, -4.0]]))
        self.hidden.bias = nn.Parameter(torch.tensor([-2.0, 6.0]))

        # Manually set weights and biases for the output layer
        self.output.weight = nn.Parameter(torch.tensor([[4.0, 4.0]]))
        self.output.bias = nn.Parameter(torch.tensor([-6.0]))

    def forward(self, x):
        x = self.hidden(x)  # Hidden layer transformation
        x = torch.sigmoid(x)  # Activation function (Sigmoid)
        x = self.output(x)  # Output layer transformation
        x = torch.sigmoid(x)
        return x
```

The Verilog implementation must have the following interface:
```verilog
module neural_network (
    // Clock and reset
    input wire clk,                  // Clock signal
    input wire rst,                  // Reset signal
    
    // Wishbone interface
    input wire [31:0] addr_in,       // Address input
    input wire [31:0] data_in,       // Data input
    input wire we,                   // Write enable
    output wire [31:0] data_out,     // Data output
    output wire ack_o,               // Acknowledge signal
    
    // Control interface
    input wire start,                // Start computation
    output wire ready                // Result ready
);
```

Requirements:
- IEEE-754 single precision floating point compliance
- Wishbone protocol for memory-mapped I/O
- Modular design with separate functional units
- Hardware parallelism for efficient computation
- Sigmoid activation function implementation
- Control signals for operation flow

Place the implemented neural network into `/openhands/workspace/neural_network.v`

## Step 2: Create a Self-Checking Testbench
- Develop a comprehensive testbench that verifies the neural network against the Python model.
- Ensure it automatically verifies correctness and prints the results.
- Save the output in a Markdown file with:
  - **Test title**
  - **Pass/Fail status**

Ensure the following points are addressed within the testbench:

### Basic Operations: (1 pts)
   - Test input loading and weight initialization.

### Python Validation: (1 pts)
   - Test against Python model outputs.

### Wishbone Protocol: (1 pts)
   - Test memory-mapped I/O operations.

### Control Flow: (1 pts)
   - Test start/ready signaling and computation flow.

### Edge Cases: (1 pts)
   - Test boundary conditions and special values.

### Parallel Processing: (1 pts)
   - Test concurrent neuron computations.

### Reset Behavior: (1 pts)
   - Test reset functionality and state clearing.

Place the implemented testbench into `/openhands/workspace/neural_network_tb.v`
Place the test report into `/openhands/workspace/report.md`

## Step 3: Debug and Fix Issues
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.  