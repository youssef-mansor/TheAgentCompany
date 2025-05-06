
build a synthesizable neural network in verilog that matches this tiny python model:

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

your verilog module should implement the same thing. make sure the interface includes:
- clock + reset
- wishbone-style memory-mapped I/O (32 bits):
   - addr_in, data_in, data_out, we, ack_o
- control signals:
   - start (kicks off computation)
   - ready (goes high when result is ready)

stuff it must support:
- single-precision floating point (IEEE-754)
- modular layout (break it up into clear units)
- ReLU instead of sigmoid (yeah, the python model uses sigmoid, but we're switching to ReLU in hardware)
- parallel hardware compute (for performance)
- clean control flow using start and ready


- Develop a comprehensive testbench using cocotb that verifies the neural network against the Python model with asserstions that covers all possible cases.  
- If a test case fails, the assertion should terminate the testbench execution. If you are using a Verilog testbench, you must use the **$fatal** macro.
- The test bench should run the neural network in python one time and the verilog code another time and make sure outputs are the same.

now write a cocotb testbench that checks everything:

* run the **same inputs** through the python model and your verilog module
* compare results — if they don’t match, assert and blow up with `$fatal`
* make sure the testbench covers:

  * input write + weight setup
  * correct results vs. python
  * proper wishbone read/write behavior
  * start/ready control logic
  * edge values, weird floats, etc.

debug until everything lines up with python.

last step: you must create a `run_test.sh` file that only runs your testbench. run it and make sure it works end-to-end.