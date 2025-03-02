
---

## Main Module Checkpoints - Total 12 pts (grade_checkpoint2)

### 1. Interface (1 pts)
   - The code implements the following interface:
   ```psuedo-verilog
   module fpu(
      clk,                  // Clock signal for pipelining
      [1:0] rounding_mode,  // Selects the rounding mode
      [2:0] operation,      // Selects the FPU operation
      [31:0] operand_A,     // First operand (single-precision)
      [31:0] operand_B,     // Second operand (single-precision)
      [31:0] out,          // Result of the operation
      overflow,            // Overflow exception
      underflow,           // Underflow exception
      div_by_zero,         // Division by zero exception
      inexact,             // Inexact result exception
      invalid_operation    // Invalid operation exception
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
