## Action Checkpoints - Total 3 pt (grade_checkpoint1)

### File creation multiplier.v: (1 pts)
   - A file is created for the multiplier module `multiplier.v`

### File creation multiplier_tb.v: (1 pts)
   - A testbench file is created for the multiplier module `multiplier_tb.v`

### File creation report.md: (1 pts)
   - A test file is created for the output of the testbench `report.md`

---

## Main Module Checkpoints - Total 4 pts (grade_checkpoint2)

### 1. Pipeline Latency (1 pts)
   - The product is correctly calculated after three clock cycles.

### 2. Reset Priority (1 pts)
   - If `reset` is active, the pipeline clears (outputs are invalid) regardless of inputs.

### 3. Valid Signal (1 pts)
   - The valid signal is asserted only when the pipeline result is ready.

### 4. Interface (1 pts)
   - The module header correctly defines the required ports:
   ```verilog
   input wire clk,          // Clock signal
   input wire reset,        // Reset signal
   input wire [3:0] a,      // 4-bit input a
   input wire [3:0] b,      // 4-bit input b
   output reg [7:0] product,// 8-bit product output
   output reg valid         // Valid signal
   ```

# File Content

## multiplier.v

---

## Testbench Comprehensiveness checkpoints - Total 7 pts (grade_checkpoint3)

Ensure the following points are addressed within the test bench:

### Initial Reset: (1 pts)
   - Verify that the pipeline produces invalid output (e.g., valid = 0) after reset.

### Correctness: (1 pts)
   - Test all possible input combinations of a and b (4-bit × 4-bit = 256 cases). Verify correct products.

### Pipeline Behavior: (1 pts)
   - Confirm that the product is delayed by exactly three clock cycles and that valid is correctly asserted at the output.

### Reset During Operation: (1 pts)
   - Assert reset during active operation and verify the pipeline clears.

### Randomized Test: (1 pts)
   - Randomize inputs and clock behavior to ensure the pipeline remains functional in all cases.

### Edge Cases: (1 pts)
   - Test edge cases, including a = 0, b = 0, a = 15, and b = 15.

### Clock Stability: (1 pts)
   - Validate that the multiplier only produces output on rising clock edges.

# File Content

## multiplier_tb.v

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md