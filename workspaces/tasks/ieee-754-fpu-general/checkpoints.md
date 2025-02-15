## Action Checkpoints - Total 3 pt (grade_checkpoint1)

### File creation fpu.v: (1 pts)
   - A file is created for the FPU module `fpu.v`

### File creation fpu_tb.v: (1 pts)
   - A testbench file is created for the FPU module `fpu_tb.v`

### File creation report.md: (1 pts)
   - A test report file is created `report.md`

---

## Main Module Checkpoints - Total 4 pts (grade_checkpoint2)

### 1. Interface & Modularity (1 pts)
   - The module correctly implements all required ports:
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

### 2. Operations Support (1 pts)
   - The code includes operation decoding logic using the 3-bit operation input
   - The code implements the following operations:
     - Addition: The code extracts sign, exponent, and mantissa
     - Subtraction: The code performs two's complement or similar negation
     - Multiplication: The code multiplies mantissas and adds exponents
     - Division: The code divides mantissas and subtracts exponents
     - Int-to-Float: The code scans integer bits and normalizes the result
     - Float-to-Int: The code performs rounding and range checking

### 3. IEEE 754 Compliance (1 pts)
   - The code checks special values:
     - NaN: The code detects when exponent is all 1's and mantissa is non-zero
     - Infinity: The code detects when exponent is all 1's and mantissa is zero
     - Zero: The code detects when exponent and mantissa are zero
   - The code implements rounding based on rounding_mode input:
     - [1:0] == 2'b00: The code examines LSB for nearest even rounding
     - [1:0] == 2'b01: The code truncates for round toward zero
     - [1:0] == 2'b10: The code rounds up for +∞
     - [1:0] == 2'b11: The code rounds down for -∞
   - The code sets exception flags:
     - overflow: The code detects when result's exponent > 8'hFF
     - underflow: The code detects when result's exponent < 8'h00
     - div_by_zero: The code detects when divisor is zero
     - inexact: The code detects when bits are truncated/rounded
     - invalid_operation: The code detects NaN operations or invalid combinations

### 4. Pipeline Implementation (1 pts)
   - The code uses pipeline registers between stages
   - The code implements these pipeline stages:
     - Decode stage: The code uses registers for operation and operand unpacking
     - Execute stage: The code uses registers for computation
     - Result stage: The code uses registers for result packaging
   - The code implements pipeline control:
     - The code uses valid bits or similar control signals between stages
     - The code implements stall logic
   - The code maintains consistent latency:
     - The code uses same number of clock cycles for similar operations

---

## Testbench Comprehensiveness - Total 7 pts (grade_checkpoint3)

### Basic Operations: (1 pts)
   - The testbench code tests:
     - Addition: The code tests positive and negative number combinations
     - Subtraction: The code tests positive and negative number combinations
     - Multiplication: The code tests positive and negative number combinations
     - Division: The code tests positive and negative number combinations

### Special Values: (1 pts)
   - The testbench code tests:
     - NaN: The code tests operations with NaN inputs
     - Infinity: The code tests operations with infinity inputs
     - Zero: The code tests operations with zero inputs
     - Denormalized numbers: The code tests with subnormal values

### Rounding Modes: (1 pts)
   - The testbench code tests each rounding mode:
     - Round to nearest even: The code tests values requiring tie-breaking
     - Round toward zero: The code tests positive and negative values
     - Round toward +∞: The code tests positive and negative values
     - Round toward -∞: The code tests positive and negative values

### Exceptions: (1 pts)
   - The testbench code tests exception triggers:
     - Overflow: The code tests operations exceeding maximum float value
     - Underflow: The code tests operations below minimum normalized value
     - Division by zero: The code tests division with zero divisor
     - Invalid operations: The code tests undefined arithmetic operations

### Conversions: (1 pts)
   - The testbench code tests:
     - Int-to-float: The code tests positive, negative, and boundary values
     - Float-to-int: The code tests values requiring rounding
     - The code tests values requiring rounding in different modes
     - The code tests values outside integer range

### Edge Cases: (1 pts)
   - The testbench code tests:
     - Maximum float: The code tests operations near maximum value
     - Minimum float: The code tests operations near minimum value
     - The code tests values around powers of 2
     - The code tests values requiring normalization

### Pipeline: (1 pts)
   - The testbench code tests:
     - The code tests operation sequences
     - The code tests mixed operation types
     - The code tests data dependencies
     - The code tests pipeline throughput

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**



