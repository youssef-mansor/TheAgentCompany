# Boolean Logic Simplification and Verilog Implementation

## Step 1: Simplify the Boolean Logic
- Simplify the following Boolean logic equation using the provided K-map:
  
  **K-map**:
  ```
          ab
   cd   | 00 | 01 | 11 | 10 |
  ----------------------------
   00   |  0 |  1 |  1 |  0 |  
   01   |  1 |  1 |  0 |  0 |  
   11   |  1 |  0 |  0 |  1 |  
   10   |  0 |  1 |  1 |  1 |  
  ```
- Implement the minimized Boolean logic as a Verilog module with the following interface:
  - Inputs: `a`, `b`, `c`, `d`
  - Output: `f`
  
  Place the implemented module into `/openhands/workspace/logic_module.v`

---

## Step 2: Create a Self-Checking Testbench  
- Develop a comprehensive testbench for the module to verify its functionality.
- Ensure the testbench is self-checking and automatically verifies correctness.
- Save the output of the test results in a Markdown file with:
  - **Test title**
  - **Pass/Fail status**

Ensure the following points are addressed within the testbench:

### Exhaustive Testing: (1 pt)
    Verify all 16 possible input combinations (2^4) to ensure correctness.

### Correct Behavior: (1 pt)
    Check that the logic matches the original K-map truth table.

  Place the implemented testbench into `/openhands/workspace/logic_tb.v`
  Place the implemented report into `/openhands/workspace/report.md`

---

## Step 3: Debug and Fix Issues  
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.