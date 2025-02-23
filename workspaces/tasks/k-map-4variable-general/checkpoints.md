## Action Checkpoints - Total 3 pts (grade_checkpoint1)

### File creation logic_module.v: (1 pt)
    Create a Verilog file (`logic_module.v` or `logic_module.sv`) for the minimized logic.

### File creation logic_tb.v: (1 pt)
    Develop a testbench file (`logic_tb.v` or `logic_tb.sv`) for the logic module.
    
### File creation report.md (1 pts)
    a test file is created for the output of the testbench report.md 

---

## Main Module Checkpoints - Total 3 pts (grade_checkpoint2)

### 1. Minimized Logic (1 pt)
    The derived equation from the K-map is correctly minimized (e.g., grouping and terms are correct).

### 2. Equation Implementation (1 pt)
    The Verilog module implements the exact minimized equation.

### 3. Interface (1 pt)
    The module correctly defines the following ports:  
    ```verilog
    input wire a,  // Input signal a  
    input wire b,  // Input signal b  
    input wire c,  // Input signal c  
    input wire d,  // Input signal d  
    output wire f  // Output signal f  
    ```

# File Content

## logic_module.v

---

## Testbench Checkpoints - Total 2 pts (grade_checkpoint3)

Ensure the following points are addressed within the testbench:

### Exhaustive Testing: (1 pt)
    Verify all 16 possible input combinations (2^4) to ensure correctness.


# File Content

## logic_tb.v

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)

Returns the count of passed test cases in the `report.md` file and the total number of cases in the file in the specific format:  
**Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md
