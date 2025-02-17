first of all create /openhands/workspace/report.md file as it will be used later.

# Clone and Run UART Testbench  

Clone this repo: [https://github.com/jamieiles/uart](https://github.com/jamieiles/uart).  
Check the README for info. Run the testbench and print the results.  

# Integrate with Caravel  

Integrate the UART module into `caravel`'s `user_project_wrapper` by first making a wishbone wrapper for it.  

# Create a Testbench  

Make a testbench for the `user_project_wrapper` by creating a Cocotb test runner inside the `verilog/dv` directory of the Caravel template.  
- **Test file name:** `test_user_project_wrapper.py`  
- **Do not run** the OpenLane flow.  

## Testbench Requirements  

- Iterate over a range of values, setting input signals and asserting control signals to simulate data transactions.  
- Use assert statements to verify that the output matches the expected results.  
- Log messages to indicate the completion and success of the test.  

## Generate Test Report  

Save the output in a Markdown report file containing:  
- **Test title**  
- **Pass/Fail status**  

Place the report into:  
`/openhands/workspace/report.md`  
