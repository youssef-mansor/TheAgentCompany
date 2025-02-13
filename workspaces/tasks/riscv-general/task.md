# Verilog RISC-V32I Single-Cycle Implementation and Testing

## Step 1: Implement a RISC-V32I Single-Cycle Processor
Design a RISC-V32I processor in Verilog with the following interface:
```verilog
module riscv32i(
    input wire clk,                      // Clock signal
    input wire reset,                    // Reset signal
    output wire [31:0] instr_mem_addr,   // Instruction memory address
    input wire [31:0] instr_mem_data,    // Instruction memory data
    output wire [31:0] data_mem_addr,    // Data memory address
    output wire [31:0] data_mem_data_in, // Data memory write data
    input wire [31:0] data_mem_data_out, // Data memory read data
    output wire data_mem_we,             // Data memory write enable
    input wire [4:0] regfile_debug_read_addr,  // Debug register address
    output wire [31:0] regfile_debug_read_data // Debug register data
);
```

The processor should implement:
- Basic RISC-V32I instruction set (load-store, ALU, branches)
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

Place the implemented processor into `/openhands/workspace/riscv32i.v`

## Step 2: Create a Self-Checking Testbench
- Develop a comprehensive testbench for the processor that covers all instruction types.
- Ensure it automatically verifies correctness and prints the results.
- Save the output in a Markdown file with:
  - **Test title**
  - **Pass/Fail status**

Ensure the following points are addressed within the testbench:

### ALU Operations: (1 pts)
   - Test arithmetic, logical, and shift instructions.

### Memory Operations: (1 pts)
   - Test load/store instructions with different data sizes.

### Branch & Jump: (1 pts)
   - Test conditional branches and jump instructions.

### Control Flow: (1 pts)
   - Test instruction sequencing and control signal generation.

### Register File: (1 pts)
   - Test register read/write operations and x0 behavior.

### Edge Cases: (1 pts)
   - Test overflow, alignment, and boundary conditions.

### Stress Testing: (1 pts)
   - Test complex instruction sequences and corner cases.

Place the implemented testbench into `/openhands/workspace/riscv32i_tb.v`
Place the test report into `/openhands/workspace/report.md`

## Step 3: Debug and Fix Issues
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.
