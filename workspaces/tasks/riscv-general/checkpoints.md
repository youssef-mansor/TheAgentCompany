## Action Checkpoints - Total 3 pt (grade_checkpoint1)

### File creation riscv32i.v: (1 pts)
   - A file is created for the RISC-V processor module `riscv32i.v`

### File creation riscv32i_tb.v: (1 pts)
   - A testbench file is created for the RISC-V processor module `riscv32i_tb.v`

### File creation report.md: (1 pts)
   - A test file is created for the output of the testbench `report.md`

---

## Main Module Checkpoints - Total 4 pts (grade_checkpoint2)

### 1. Interface & Modularity (1 pts)
   - The module correctly implements all required ports and submodules:
     - Clock and reset signals
     - Memory interfaces (instruction and data)
     - Debug interface
     - Separate functional units (IF, ID, ALU, etc.)

### 2. Control & Datapath (1 pts)
   - Implements correct control and data flow:
     - Control signal generation
     - ALU operation selection
     - Memory access control
     - Register file control

### 3. Instruction Support (1 pts)
   - Implements required instruction types:
     - Load/Store instructions
     - ALU operations
     - Branch and jump instructions
     - Proper instruction decoding

### 4. Interface (1 pts)
   - The module header correctly defines the required ports:
   ```verilog
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
   ```

# File Content

## riscv32i.v

---

## Testbench Comprehensiveness checkpoints - Total 7 pts (grade_checkpoint3)

Ensure the following points are addressed within the test bench:

### ALU Operations: (1 pts)
   - Test arithmetic operations (ADD, SUB, etc.)
   - Test logical operations (AND, OR, XOR)
   - Test shift operations (SLL, SRL, SRA)

### Memory Operations: (1 pts)
   - Test load instructions (LW, LH, LB)
   - Test store instructions (SW, SH, SB)
   - Test memory alignment

### Branch & Jump: (1 pts)
   - Test conditional branches (BEQ, BNE, etc.)
   - Test unconditional jumps (JAL, JALR)
   - Test branch prediction

### Control Flow: (1 pts)
   - Test instruction sequencing
   - Test control signal generation
   - Test pipeline hazards

### Register File: (1 pts)
   - Test register read/write
   - Test x0 behavior
   - Test register forwarding

### Edge Cases: (1 pts)
   - Test overflow conditions
   - Test boundary conditions
   - Test error cases

### Stress Testing: (1 pts)
   - Test complex instruction sequences
   - Test random instruction patterns
   - Test system stability

# File Content

## riscv32i_tb.v

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md