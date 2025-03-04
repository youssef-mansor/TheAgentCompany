first of all create /workspace/report.md file as it will be used later.

# Clone and Run UART Testbench  

Clone this repo: [https://github.com/jamieiles/uart](https://github.com/jamieiles/uart).  
Check the README for info. Run the testbench and print the results.  

# Integrate with Caravel  

Integrate the UART module into `caravel`'s `user_project_wrapper` by first making a wishbone wrapper for it.  
The `user_project_wrapper` is part of the openlane2 git repository.

# Create a Testbench  

Make a testbench for the `user_project_wrapper` by creating a Cocotb test runner inside the `verilog/dv` directory of the Caravel template. 
- **Do not run** the OpenLane flow.  

## Testbench Requirements  

- Iterate over a range of values, setting input signals and asserting control signals to simulate data transactions.  
- Use assert statements to verify that the output matches the expected results. If a case fails, the assertion should stop the testbench execution.  
- Log messages to indicate the completion and success of the test.  

# `run_test.sh` File Creation
- Create a shel script `run_test.sh` that contains the command to only run the testbench.
- execute the `run_test.sh` to make sure it successfully runs the testbench.