Design a Verilog module for NxN matrix multiplication. The module should take two NxN matrices as inputs, where each matrix element is an 8-bit value, and output the resulting NxN matrix with 16-bit values. Implement the multiplication as a dot product of corresponding rows and columns, ensuring proper handling of partial sums. Use a parameterized design so the matrix size $N$ can be easily adjusted.

Create a comprehensive testbench that initializes matrices with known values, performs the multiplication, and displays the result for verification. The testbench should include assertions or checks to ensure the output matches expected values for given test cases, confirming the correctness of the implementation.

Use assertions - make sure to use $fatal if something fails in case the testbench is a verilog testbench.

if the test doesn’t pass, fix the design or the testbench until everything’s working.

you must make a run_test.sh script that just runs the testbench. run it and make sure it works.