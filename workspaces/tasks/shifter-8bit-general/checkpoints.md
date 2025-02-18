## Action Checkpoints - Total 3 pts (grade_checkpoint1)

### File creation shifter.v: (1 pt)
    A file is created for the shifter module `shifter.v`.

### File creation shifter_tb.v: (1 pt)
    A testbench file is created for the shifter module `shifter_tb.v`.

### File creation report.md: (1 pt)
    A test file is created for the output of the testbench `report.md`.

---

## Main Module Checkpoints - Total 4 pts (grade_checkpoint2)

### 1. Shift Logic (1 pt)
    The module should shift the contents of the register either left or right on the rising edge of `clk`, depending on the value of `direction`:  
    - When `direction` is 1, shift left.  
    - When `direction` is 0, shift right.

### 2. Shift Register Width (1 pt)
    Implement the shifter for an 8-bit register. Ensure that bits shifted out of the register are discarded, and new bits are inserted at the appropriate end based on the direction of the shift.

### 3. Reset Priority (1 pt)
    If `reset` is active, the contents of the shift register should be reset to 0, regardless of the clock or direction.

### 4. Interface (1 pt)
    The module should define the ports appropriately as specified in the prompt:  
    ```verilog
    input wire clk;           // Clock signal  
    input wire reset;         // Reset signal  
    input wire [7:0] shift_in; // 8-bit input data for shifting  
    input wire direction;     // Direction of the shift: 1 for left, 0 for right  
    output reg [7:0] shift_out; // 8-bit output data after shifting  
    ```

# File Content

## shifter.v

---

## Testbench Comprehensiveness Checkpoints - Total 3 pts (grade_checkpoint3)

Ensure the following points are addressed within the testbench:


### Left Shift: (1 pt)
    Verify that when `direction = 1`, the register contents shift left, and `shift_out` holds the correct value after the shift.

### Right Shift: (1 pt)
    Verify that when `direction = 0`, the register contents shift right, and `shift_out` holds the correct value after the shift.

### Boundary Tests: (1 pt)
    Verify that bits shifted out of the register are discarded, and verify that no unexpected data appears at the empty positions.

# File Content

## shifter_tb.v

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)

Returns the count of passed test cases in the `report.md` file and the total number of cases in the file in the specific format: 

**Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md