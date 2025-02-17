# Verilog 4-bit Carry Lookahead Adder Implementation and Testing

## Step 0: Files creation
Create the following files
- `/workspace/report.md`
- `/workspace/cla.v`
- `/workspace/cla_tb.v`

## Step 1: Implement a 4-bit Carry Lookahead Adder
Design a 4-bit CLA in Verilog with the following interface:
- `A` (4-bit input)
- `B` (4-bit input)
- `cin` (carry-in)
- `S` (4-bit sum output)
- `cout` (carry-out)

The CLA should:
- Calculate generate (G) and propagate (P) signals
- Use lookahead logic for carry calculation
- Implement efficient carry propagation
- Calculate sum using P and carry signals

Place the implemented CLA into `/workspace/cla.v`

## Step 2: Create a Self-Checking Testbench
- Develop a comprehensive testbench for the CLA module that covers all possible cases.
- Ensure it automatically verifies correctness and prints the results.
- Save the output in a Markdown file with:
  - **Test title**
  - **Pass/Fail status**

Ensure the following points are addressed within the testbench:

### Full Combinatorial Test: (1 pts)
   - Test all possible combinations of inputs (A, B, cin).

### Edge Cases: (1 pts)
   - Test boundary conditions (all zeros, all ones, etc.).

### Carry Propagation: (1 pts)
   - Verify correct carry propagation through all bits.

### Lookahead Logic: (1 pts)
   - Validate proper implementation of generate and propagate signals.

### Random Tests: (1 pts)
   - Perform randomized testing of inputs.

### Performance: (1 pts)
   - Verify carry lookahead behavior vs ripple carry.

### Error Cases: (1 pts)
   - Test overflow conditions and boundary scenarios.

Place the implemented testbench into `/workspace/cla_tb.v`
Place the test report into `/workspace/report.md`

## Step 3: Debug and Fix Issues
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.
