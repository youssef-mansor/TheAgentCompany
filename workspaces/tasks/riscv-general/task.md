# Verilog RISC-V32I Single-Cycle Implementation and Testing

## Step 1: Implement a RISC-V32I Single-Cycle Processor
Design a RISC-V32I processor in Verilog with the following interface:
    input clk,                      // Clock signal
    input reset,                    // Reset signal
    output [31:0] instr_mem_addr,   // Instruction memory address
    input [31:0] instr_mem_data,    // Instruction memory data
    output [31:0] data_mem_addr,    // Data memory address
    output [31:0] data_mem_data_in, // Data memory write data
    input [31:0] data_mem_data_out, // Data memory read data
    output data_mem_we,             // Data memory write enable
    input [4:0] regfile_debug_read_addr,  // Debug register address
    output [31:0] regfile_debug_read_data // Debug register data

The processor should implement:
- Only basic RISC-V32I instruction set (load-store, ALU, branches, shifting). Specifically (lw, sw, add, sub, and, or, beq, SLL, SRL, SRA)
- Modular design with separate functional units
- Single-cycle execution
- Proper control signal generation
- Memory and register file interfaces

Required modules:
1. Instruction Fetch Unit
2. Instruction Decode & Register File
3. ALU
4. Control Unit
5. Branch & Jump Logic
6. Data Memory Interface


## Step 2: Create a Self-Checking Testbench
- Develop a comprehensive testbench for the top module with asserstions that covers all possible cases.  
- If a case fails, the assertion should stop the testbench execution. 
- the test bench should cover all instruction types.

Ensure the following points are addressed within the testbench:

### ALU Operations:
   - Test arithmetic, logical, and shift instructions.

### Memory Operations:
   - Test load/store instructions with different data sizes.

### Branch & Jump:
   - Test conditional branches and jump instructions.

### Control Flow:
   - Test instruction sequencing and control signal generation.

### Register File:
   - Test register read/write operations and x0 behavior.

## Step 3: Debug and Fix Issues
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.

## Step 4: `run_test.sh` File Creation
- Create a shel script `run_test.sh` that contains the command to only run the testbench.
- execute the `run_test.sh` to make sure it successfully runs the testbench.