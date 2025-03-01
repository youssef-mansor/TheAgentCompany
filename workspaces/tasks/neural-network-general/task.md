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
    // Clock and reset
    clk,                  // Clock signal
    rst,                  // Reset signal
   
     interface
    [31:0] addr_in,       // Address input
    [31:0] data_in,       // Data input
    we,                   // Write enable
    [31:0] data_out,     // Data output
    ack_o,               // Acknowledge signal
    
    // Control interface
    start,                // Start computation
    ready                // Result ready


Requirements:
- IEEE-754 single precision floating point compliance
- Wishbone protocol for memory-mapped I/O
- Modular design with separate functional units
- Hardware parallelism for efficient computation
- ReLU activation function implementation
- Control signals for operation flow

## Step 2: Create a Self-Checking Testbench
- Develop a comprehensive testbench using cocotb that verifies the neural network against the Python model with asserstions that covers all possible cases.  
- If a case fails, the assertion should stop the testbench execution. 
- The test bench should run the neural network in python one time and the verilog code another time and make sure outputs are the same.

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

## Step 3: Debug and Fix Issues
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.  

## Step 4: `run_test.sh` File Creation
- Create a shel script `run_test.sh` that contains the command to only run the testbench.
- execute the `run_test.sh` to make sure it successfully runs the testbench.