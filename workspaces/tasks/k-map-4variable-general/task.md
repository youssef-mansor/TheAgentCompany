# Boolean Logic Simplification and Verilog Implementation

## Step 0: Files creation
Create the following files
- `/workspace/report.md`
- `/workspace/logic_module.v` 
- `/workspace/logic_tb.v`

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
  
  Place the implemented module into `/workspace/logic_module.v`

---

## Step 2: Create a Self-Checking Testbench  
- Develop a comprehensive testbench for the module to verify its functionality.
- Ensure the testbench is self-checking and automatically verifies correctness.
- Save the output of the test results in a Markdown file with:
  - **Test title**
  - **Pass/Fail status**

Ensure the testbench prints each test's pass/fail status directly into `/workspace/report.md` using Verilog file operations, with one line per test indicating "pass" or "fail."

Ensure to Verify all 16 possible input combinations (2^4).

  Place the implemented testbench into `/workspace/logic_tb.v`

---

## Step 3: Debug and Fix Issues  
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.