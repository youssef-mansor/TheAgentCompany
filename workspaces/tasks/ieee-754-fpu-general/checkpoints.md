## Action Checkpoints - Total 3 pts (grade_checkpoint1)

### File creation fpu.v: (1 pts)
   - A file is created for the FPU module `fpu.v` (1 pts)

### File creation fpu_tb.v: (1 pts)
   - A testbench file is created for the FPU module `fpu_tb.v` (1 pts)

### File creation report.md: (1 pts)
   - A test report file is created `report.md` (1 pts)

---

## Main Module Checkpoints - Total 12 pts (grade_checkpoint2)

### 1. Interface (1 pts)
   - The code implements the following interface:
   ```verilog
   module fpu(
      input wire clk,                  // Clock signal for pipelining
      input wire [1:0] rounding_mode,  // Selects the rounding mode
      input wire [2:0] operation,      // Selects the FPU operation
      input wire [31:0] operand_A,     // First operand (single-precision)
      input wire [31:0] operand_B,     // Second operand (single-precision)
      output wire [31:0] out,          // Result of the operation
      output wire overflow,            // Overflow exception
      output wire underflow,           // Underflow exception
      output wire div_by_zero,         // Division by zero exception
      output wire inexact,             // Inexact result exception
      output wire invalid_operation    // Invalid operation exception
   );
   ```

### 2. Operations Support (5 pts)
   - The code implements IEEE-754 operations:
     - The code implements addition/subtraction (1 pts)
     - The code implements multiplication (1 pts)
     - The code implements division (1 pts)
     - The code implements int-to-float conversion (1 pts)
     - The code implements float-to-int conversion (1 pts)

### 3. IEEE 754 Compliance (5 pts)
   - The code implements standard features:
     - The code handles special values (NaN, Infinity, Zero) (1 pts)
     - The code implements all four rounding modes (1 pts)
     - The code detects overflow and underflow (1 pts)
     - The code handles division by zero (1 pts)
     - The code detects invalid operations (1 pts)

### 4. Pipeline Implementation (1 pt)
   - The code implements pipelining. ( 1pt)
---

## Testbench Comprehensiveness checkpoints - Total 24 pts (grade_checkpoint3)

### Basic Operations: (4 pts)
   - The testbench code tests:
     - The code tests addition operations (1 pts)
     - The code tests subtraction operations (1 pts)
     - The code tests multiplication operations (1 pts)
     - The code tests division operations (1 pts)

### Special Values: (4 pts)
   - The testbench code tests:
     - The code tests NaN handling (1 pts)
     - The code tests infinity handling (1 pts)
     - The code tests zero handling (1 pts)
     - The code tests denormalized numbers (1 pts)

### Rounding Modes: (4 pts)
   - The testbench code tests:
     - The code tests round to nearest even (1 pts)
     - The code tests round toward zero (1 pts)
     - The code tests round toward +∞ (1 pts)
     - The code tests round toward -∞ (1 pts)

### Exceptions: (4 pts)
   - The testbench code tests:
     - The code tests overflow conditions (1 pts)
     - The code tests underflow conditions (1 pts)
     - The code tests division by zero (1 pts)
     - The code tests invalid operations (1 pts)

### Conversions: (4 pts)
   - The testbench code tests:
     - The code tests positive int-to-float conversion (1 pts)
     - The code tests negative int-to-float conversion (1 pts)
     - The code tests positive float-to-int conversion (1 pts)
     - The code tests negative float-to-int conversion (1 pts)

### Edge Cases: (4 pts)
   - The testbench code tests:
     - The code tests maximum float values (1 pts)
     - The code tests minimum float values (1 pts)
     - The code tests power of 2 boundaries (1 pts)
     - The code tests normalization cases (1 pts)

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**



