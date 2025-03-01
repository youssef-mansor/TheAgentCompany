# Verilog IEEE 754 Single-Precision FPU Implementation and Testing

## Step 1: Implement an IEEE 754 Single-Precision FPU
Design a pipelined single-precision floating-point unit (FPU) in Verilog with the following interface:
   clk,                   // Clock signal for pipelining
   [1:0] rounding_mode,   // Selects the rounding mode
   [2:0] operation,       // Selects the FPU operation
   [31:0] operand_A,      // First operand (single-precision)
   [31:0] operand_B,      // Second operand (single-precision)
   [31:0] out,            // Result of the operation
   overflow,              // Overflow exception
   underflow,             // Underflow exception
   div_by_zero,           // Division by zero exception
   inexact,               // Inexact result exception
   invalid_operation      // Invalid operation exception


The FPU must implement:
- Basic arithmetic operations (add, subtract, multiply, divide)
- Format conversions (int-to-float, float-to-int)
- IEEE 754 rounding modes:
  - Round to nearest even (00)
  - Round toward zero (01)
  - Round toward +∞ (10)
  - Round toward -∞ (11)
- Operation codes:
  - Addition (000)
  - Subtraction (001)
  - Multiplication (010)
  - Division (011)
  - Int-to-Float (100)
  - Float-to-Int (101)
- Exception handling
- Pipelined architecture for high throughput

## Step 2: Create a Self-Checking Testbench
- Develop a comprehensive testbench for the FPU that covers all operations with asserstions.
- If a case fails, the assertion should stop the testbench execution. 


Ensure the following points are addressed within the testbench:

### Basic Operations:
   - Test all arithmetic operations with simple cases.

### Special Values:
   - Test NaN, Infinity, and Zero handling.

### Rounding Modes:
   - Test all four rounding modes.

### Exceptions:
   - Test all exception conditions.

### Conversions:
   - Test int-to-float and float-to-int conversions.

## Step 3: Debug and Fix Issues
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.  

## Step 4: `run_test.sh` File Creation
- Create a shel script `run_test.sh` that contains the command to only run the testbench.
- execute the `run_test.sh` to make sure it successfully runs the testbench.