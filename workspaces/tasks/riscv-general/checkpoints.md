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
   - The code implements the following components:
     - The code has synchronous clock and active-high reset inputs
     - The code implements separate instruction and data memory interfaces with 32-bit addresses
     - The code includes a debug interface to read register file contents
     - The code organizes pipeline stages:
       - Instruction Fetch (PC, instruction memory interface)
       - Instruction Decode (register file, immediate generation)
       - Execute (ALU, branch computation)
       - Memory (data memory interface)
       - Writeback (register write control)

### 2. Control & Datapath (1 pts)
   - The code implements control and data flow:
     - The code decodes instructions to generate control signals:
       - ALU operation selection (ADD, SUB, AND, OR, etc.)
       - Memory operation control (read/write, byte/half/word)
       - Register file write enable and source selection
       - Branch and jump control
     - The code implements data hazard handling:
       - Data forwarding paths between pipeline stages
       - Pipeline stall logic when needed
       - Branch prediction or flush mechanism

### 3. Instruction Support (1 pts)
   - The code implements RV32I instructions:
     - Load/Store:
       - The code handles LW, LH, LB (with sign extension)
       - The code handles SW, SH, SB
       - The code handles memory alignment
     - Arithmetic/Logic:
       - The code implements ADD, SUB, AND, OR, XOR
       - The code implements SLL, SRL, SRA
       - The code handles immediate variants (ADDI, etc.)
     - Control Flow:
       - The code implements BEQ, BNE, BLT, BGE
       - The code implements JAL with return address
       - The code implements JALR for indirect jumps

### 4. Interface (1 pts)
   - The code implements the module with these ports:
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

---

## Testbench Comprehensiveness checkpoints - Total 7 pts (grade_checkpoint3)

### ALU Operations: (1 pts)
   - The testbench code tests arithmetic:
     - The code tests ADD/SUB with positive/negative numbers
     - The code tests logical operations (AND, OR, XOR)
     - The code tests shifts with different amounts
     - The code verifies results against expected values

### Memory Operations: (1 pts)
   - The testbench code tests memory access:
     - The code tests word/half/byte loads with sign extension
     - The code tests word/half/byte stores
     - The code tests unaligned access handling
     - The code verifies data persistence in memory

### Branch & Jump: (1 pts)
   - The testbench code tests control flow:
     - The code tests branch taken/not-taken paths
     - The code tests forward and backward jumps
     - The code tests JAL/JALR return address saving
     - The code verifies branch prediction accuracy

### Control Flow: (1 pts)
   - The testbench code tests execution:
     - The code tests instruction pipeline flow
     - The code tests hazard detection and handling
     - The code tests pipeline stalls and flushes
     - The code verifies control signal timing

### Register File: (1 pts)
   - The testbench code tests registers:
     - The code tests x0 remains zero
     - The code tests read-after-write hazards
     - The code tests forwarding paths
     - The code verifies register file integrity

### Edge Cases: (1 pts)
   - The testbench code tests boundaries:
     - The code tests arithmetic overflow scenarios
     - The code tests memory access at boundaries
     - The code tests maximum branch ranges
     - The code tests instruction combinations causing hazards

### Stress Testing: (1 pts)
   - The testbench code tests reliability:
     - The code runs sequences of dependent instructions
     - The code tests all instruction types mixed
     - The code verifies long-running stability
     - The code tests recovery from pipeline hazards

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md