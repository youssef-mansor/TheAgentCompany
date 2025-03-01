# Verilog 8-Bit Shifter Implementation and Testing

## Step 1: Implement an 8-Bit Shifter
Design an 8-bit shifter in Verilog with the following interface:
- clk  
- reset  
- shift_in  
- shift_out  
- direction  (when 1 shift left)
The module should be capable of performing both left and right shifts based on the value of the direction input.  

## Step 2: Create a Self-Checking Testbench  
- Develop a comprehensive testbench for the shifter module with asserstions that covers all possible cases.  
- If a case fails, the assertion should stop the testbench execution. 


Ensure the following points are addressed within the testbench:

### Left Shift: (1 pt)
    Verify that when `direction = 1`, the register contents shift left, and `shift_out` holds the correct value after the shift.

### Right Shift: (1 pt)
    Verify that when `direction = 0`, the register contents shift right, and `shift_out` holds the correct value after the shift.

### Boundary Tests: (1 pt)
    Verify that bits shifted out of the register are discarded, and verify that no unexpected data appears at the empty positions.

## Step 3: Debug and Fix Issues  
- If the module does not pass all test cases, revisit and refine the Verilog code.  
- Modify the design until all test cases pass successfully.

## Step 4: `run_test.sh` File Creation
- Create a shel script `run_test.sh` that contains the command to only run the testbench.
- execute the `run_test.sh` to make sure it successfully runs the testbench.