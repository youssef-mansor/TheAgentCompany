# Verilog Four-Bit Pipelined Multiplier Implementation and Testing

## Step 1: Implement a Four-Bit Pipelined Multiplier
Design a 4-bit unsigned pipelined multiplier in Verilog with the following interface:
- `clk`
- `reset`
- `a` (4-bit input)
- `b` (4-bit input)
- `product` (8-bit output)
- `valid` (output)

The multiplier should have a three-cycle pipeline latency.
Place the implemented multiplier into `/openhands/workspace/multiplier.v`

## Step 2: Create a Self-Checking Testbench
- Develop a comprehensive testbench for the multiplier module that covers all possible cases.
- Ensure it automatically verifies correctness and prints the results.
- Save the output in a Markdown file with:
  - **Test title**
  - **Pass/Fail status**


Place the implemented testbench into `/openhands/workspace/multiplier_tb.v`
Place the test report into `/openhands/workspace/report.md` even if not all tests passed. make sure to print testbench results into report.md

Ensure the following points are addressed within the testbench:

### Pipeline Latency: (1 pts)
   - Verify that the product is correctly calculated after exactly three clock cycles.

### Input Combinations: (1 pts)
   - Test all possible input combinations (4-bit × 4-bit = 256 cases).

### Reset Behavior: (1 pts)
   - Verify that the pipeline clears and outputs are invalid when reset is asserted.

### Valid Signal: (1 pts)
   - Ensure valid signal is asserted only when pipeline result is ready.


## Step 3: Debug and Fix Issues
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.
