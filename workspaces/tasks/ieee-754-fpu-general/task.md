# Verilog IEEE 754 Single-Precision FPU Implementation and Testing

## Step 0: Files creation
Create the following files
- `/workspace/report.md`
- `/workspace/fpu.v` 
- `/workspace/fpu_tb.v`

## Step 1: Implement an IEEE 754 Single-Precision FPU
Design a pipelined single-precision floating-point unit (FPU) in Verilog with the following interface:
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
- Full exception handling
- Pipelined architecture for high throughput

Place the implemented FPU into `/workspace/fpu.v`

## Step 2: Create a Self-Checking Testbench
- Develop a comprehensive testbench for the FPU that covers all operations and cases.
- Ensure it automatically verifies correctness and prints the results.
- Save the output in a Markdown file with:
  - **Test title**
  - **Pass/Fail status**

Ensure the following points are addressed within the testbench:

### Basic Operations: (1 pts)
   - Test all arithmetic operations with simple cases.

### Special Values: (1 pts)
   - Test NaN, Infinity, and Zero handling.

### Rounding Modes: (1 pts)
   - Test all four rounding modes with boundary cases.

### Exceptions: (1 pts)
   - Test all exception conditions and flag assertions.

### Conversions: (1 pts)
   - Test int-to-float and float-to-int conversions.

### Edge Cases: (1 pts)
   - Test denormalized numbers and boundary conditions.

### Pipeline: (1 pts)
   - Test pipeline throughput and hazard handling.

Place the implemented testbench into `/workspace/fpu_tb.v`
Place the test report into `/workspace/report.md`

## Step 3: Debug and Fix Issues
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.  