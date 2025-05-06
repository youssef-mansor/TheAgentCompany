Design a single-cycle RISC-V32I processor in Verilog. It should support basic instructions like `lw`, `sw`, `add`, `sub`, `and`, `or`, `beq`, `sll`, `srl`, and `sra`. Use separate modules for instruction fetch, decode/register file, ALU, control logic, branching, and memory. The top-level interface should include:

```verilog
input clk,
input reset,
output [31:0] instr_mem_addr,
input [31:0] instr_mem_data,
output [31:0] data_mem_addr,
output [31:0] data_mem_data_in,
input [31:0] data_mem_data_out,
output data_mem_we,
input [4:0] regfile_debug_read_addr,
output [31:0] regfile_debug_read_data
```

Write a self-checking testbench that exercises all the instruction types listed. You must use `$fatal` to immediately stop simulation if any test fails if you choose to test with verilog, if cocotb ofc you there is not `$fatal` macro. Test ALU ops, memory reads/writes, branching (taken and not taken), register file behavior (especially making sure x0 always reads as zero), and correct control signal generation.

If any test fails, fix the bugs in your Verilog code until everything passes.

Also you must write a `run_test.sh` script that builds and runs just the testbench. Run it and confirm everything works.