write a 4-bit carry lookahead adder in verilog. it should use the usual generate/propagate signals for the lookahead logic. also needs to handle a carry-in and output a carry-out along with the 4-bit sum.

then make a testbench that checks it properly. test random inputs for A, B, and cin, and don’t forget edge cases like all zeros or all ones (e.g. 15). use assertions - make sure to use $fatal if something fails in case the testbench is a verilog testbench.

if the test doesn’t pass, fix the design or the testbench until everything’s working.

you must make a run_test.sh script that just runs the testbench. run it and make sure it works.