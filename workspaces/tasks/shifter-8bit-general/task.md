write an 8-bit shifter in verilog. it should shift left when direction is 1 and shift right when direction is 0. make sure it has clk, reset, shift_in and shift_out signals.

then write a testbench for it. check that shifting left and right actually works like it should. when shifting left, bits should move left and zeros should come in from the right. when shifting right, bits should move right and zeros should come in from the left. also check boundary cases — make sure bits that are shifted out are gone and nothing weird shows up.

use assertions to check the outputs and you have to make sure to use $fatal if something fails.

if it doesn’t work, debug the module or the testbench until everything passes.

also you must make a run_test.sh script that only runs your testbench. run it and make sure it works.