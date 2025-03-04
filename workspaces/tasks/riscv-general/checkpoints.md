
---

## Main Module Checkpoints - Total 19 pts (grade_checkpoint2)

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
     - The code handles the load word instruction (LW) (1 pts)
     - The code handles the store word instruction SW (1 pts)
     - The code implements arithmetic/logic instructions (ADD, SUB, AND, OR) (1 pts)
     - The code implements shift instructions (SLL, SRL, SRA) (1 pts)
     - The code implements the branch instruction (BEQ) (1 pts)

### 4. Interface (4 pts)
   - The code implements the module with these ports:
     - The code defines clock, reset, and instruction memory interface signals properly (1 pts)
     - The code defines data memory interface signals properly (1 pts)
     - The code defines debug interface signals properly (1 pts)
     - The code maintains proper signal widths (32-bit for addresses and data) (1 pts)

---

## Testbench Comprehensiveness checkpoints - Total 14 pts (grade_checkpoint3)

### ALU Operations: (4 pts)
   - The testbench code tests arithmetic:
     - The code tests ADD/SUB with positive/negative numbers (1 pts)
     - The code tests logical operations (AND, OR, XOR) (1 pts)
     - The code tests shifts with different amounts (1 pts)
     - The code verifies results against expected values (1 pts)

### Memory Operations: (2 pts)
   - The testbench code tests memory access:
     - The code tests loads with sign extension (1 pts)
     - The code tests word stores (1 pts)

### Branch & Jump: (2 pts)
   - The testbench code tests control flow:
     - The code tests branch taken/not-taken paths (1 pts)
     - The code tests forward and backward jumps (1 pts)

### Control Flow: (3 pts)
   - The testbench code tests execution:
     - The code tests instruction pipeline flow (1 pts)
     - The code tests hazard detection and handling (1 pts)
     - The code tests pipeline stalls and flushes (1 pts)

### Register File: (3 pts)
   - The testbench code tests registers:
     - The code tests x0 remains zero (1 pts)
     - The code tests read-after-write hazards (1 pts)
     - The code tests forwarding paths (1 pts)
---
