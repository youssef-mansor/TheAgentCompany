build a pipelined single-precision floating point unit (FPU) in Verilog. it should support basic arithmetic: add, sub, mul, div. also needs to do int-to-float and float-to-int conversions. use IEEE 754 standard, so make sure rounding works (round to nearest, toward zero, toward +inf, toward -inf). rounding_mode is 2 bits. operation is 3 bits — 000 for add, 001 sub, 010 mul, 011 div, 100 int->float, 101 float->int.

you’ll also need to handle exceptions: overflow, underflow, div_by_zero, inexact, and invalid_operation. make it pipelined so it can handle new inputs every clock.

inputs: clk, rounding_mode, operation, operand_A, operand_B
outputs: out, and all the exception flags

then write a testbench that checks:

basic arithmetic with known values

NaN, Inf, and 0 handling

all rounding modes

exception cases (like divide by zero)

the conversions (int ↔ float)

use assertions and make sure you use $fatal if something goes wrong. Using $fatal in case of a verilog testbench is obligatory.

debug until everything works right.

make a run_test.sh script that only runs the testbench, and run it to make sure it works.