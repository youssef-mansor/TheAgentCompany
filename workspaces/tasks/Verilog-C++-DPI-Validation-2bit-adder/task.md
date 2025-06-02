Please generate a 2-bit SystemVerilog adder module and a C++ testbench to validate it using Verilator. The SystemVerilog module should only contain synthesizable code (no DPI calls inside it).

The C++ testbench should drive all possible inputs (0 to 3) for both inputs, call eval() to simulate, and validate the output matches the expected sum in C++.

The validation function should print an error message if the output is incorrect, otherwise run silently.
