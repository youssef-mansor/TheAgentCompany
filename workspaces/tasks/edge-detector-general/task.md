write a rising-edge detector in verilog. it should have clk, reset, signal_in, and signal_out signals. signal_out should go high for one clock cycle whenever signal_in has a rising edge.

then make a testbench for it. test all the important stuff:

make sure signal_out is 1 only on a rising edge

if there are multiple rising edges, signal_out should pulse high for one clock cycle each time

make sure there’s no false positives when signal_in stays stable (either high or low)

use assertions to check everything and make sure to use $fatal (this is a must) if anything fails.

if something doesn’t work, fix the module or the testbench until it does.

also you must create a run_test.sh script that only runs your testbench. test it and make sure it works.

