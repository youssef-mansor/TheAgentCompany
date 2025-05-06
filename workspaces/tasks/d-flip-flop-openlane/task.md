Write a Verilog module for a D flip-flop.
Then, write a self-checking testbench that makes sure it behaves correctly: `q` should follow `d` on the rising edge of `clk`, and go to 0 when `reset` is asserted. Use `$fatal` in the testbench to fail fast if anything goes wrong in case  your testbech was designed in verilog and not cocotb.

After that, write a `run_test.sh` script that compiles and runs the testbench only — make sure it actually works.

Once everything passes, use OpenLane to harden the top module. Make sure the flow completes and generates a GDSII file. Try to keep PPA (power, performance, area) reasonable.