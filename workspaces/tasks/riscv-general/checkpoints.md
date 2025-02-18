## Action Checkpoints - Total 3 pts (grade_checkpoint1)

### File creation riscv32i.v: (1 pts)
   - A file is created for the RISC-V processor module `riscv32i.v` (1 pts)

### File creation riscv32i_tb.v: (1 pts)
   - A testbench file is created for the RISC-V processor module `riscv32i_tb.v` (1 pts)

### File creation report.md: (1 pts)
   - A test file is created for the output of the testbench `report.md` (1 pts)

---

## Main Module Checkpoints - Total 20 pts (grade_checkpoint2)

### 1. Interface & Modularity (5 pts)
   - The code implements the following components:
     - The code has synchronous clock and active-high reset inputs (1 pts)
     - The code implements separate instruction and data memory interfaces (1 pts)
     - The code includes a debug interface to read register file contents (1 pts)
     - The code implements instruction fetch and decode stages (1 pts)
     - The code implements execute, memory and writeback stages (1 pts)

### 2. Control & Datapath (5 pts)
   - The code implements control and data flow:
     - The code decodes instructions to generate ALU control signals (1 pts)
     - The code generates memory operation control signals (1 pts)
     - The code manages register file write control (1 pts)
     - The code implements data forwarding paths (1 pts)
     - The code handles pipeline stalls and flushes (1 pts)

### 3. Instruction Support (5 pts)
   - The code implements RV32I instructions:
     - The code handles load instructions (LW, LH, LB) with sign extension (1 pts)
     - The code handles store instructions (SW, SH, SB) (1 pts)
     - The code implements arithmetic/logic instructions (ADD, SUB, AND, OR, XOR) (1 pts)
     - The code implements shift instructions (SLL, SRL, SRA) (1 pts)
     - The code implements branch and jump instructions (BEQ, BNE, JAL, JALR) (1 pts)

### 4. Interface (5 pts)
   - The code implements the module with these ports:
     - The code defines clock, reset, and instruction memory interface signals properly (1 pts)
     - The code defines data memory interface signals properly (1 pts)
     - The code defines debug interface signals properly (1 pts)
     - The code uses correct port directions for all signals (1 pts)
     - The code maintains proper signal widths (32-bit for addresses and data) (1 pts)

---

## Testbench Comprehensiveness checkpoints - Total 28 pts (grade_checkpoint3)

### ALU Operations: (4 pts)
   - The testbench code tests arithmetic:
     - The code tests ADD/SUB with positive/negative numbers (1 pts)
     - The code tests logical operations (AND, OR, XOR) (1 pts)
     - The code tests shifts with different amounts (1 pts)
     - The code verifies results against expected values (1 pts)

### Memory Operations: (4 pts)
   - The testbench code tests memory access:
     - The code tests word/half/byte loads with sign extension (1 pts)
     - The code tests word/half/byte stores (1 pts)
     - The code tests unaligned access handling (1 pts)
     - The code verifies data persistence in memory (1 pts)

### Branch & Jump: (4 pts)
   - The testbench code tests control flow:
     - The code tests branch taken/not-taken paths (1 pts)
     - The code tests forward and backward jumps (1 pts)
     - The code tests JAL/JALR return address saving (1 pts)
     - The code verifies branch prediction accuracy (1 pts)

### Control Flow: (4 pts)
   - The testbench code tests execution:
     - The code tests instruction pipeline flow (1 pts)
     - The code tests hazard detection and handling (1 pts)
     - The code tests pipeline stalls and flushes (1 pts)
     - The code verifies control signal timing (1 pts)

### Register File: (4 pts)
   - The testbench code tests registers:
     - The code tests x0 remains zero (1 pts)
     - The code tests read-after-write hazards (1 pts)
     - The code tests forwarding paths (1 pts)
     - The code verifies register file integrity (1 pts)

### Edge Cases: (4 pts)
   - The testbench code tests boundaries:
     - The code tests arithmetic overflow scenarios (1 pts)
     - The code tests memory access at boundaries (1 pts)
     - The code tests maximum branch ranges (1 pts)
     - The code tests instruction combinations causing hazards (1 pts)

### Stress Testing: (4 pts)
   - The testbench code tests reliability:
     - The code runs sequences of dependent instructions (1 pts)
     - The code tests all instruction types mixed (1 pts)
     - The code verifies long-running stability (1 pts)
     - The code tests recovery from pipeline hazards (1 pts)

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md