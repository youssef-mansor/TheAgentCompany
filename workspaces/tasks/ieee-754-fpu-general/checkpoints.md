## Action Checkpoints - Total 3 pt (grade_checkpoint1)

### File creation fpu.v: (1 pts)
   - A file is created for the FPU module `fpu.v`

### File creation fpu_tb.v: (1 pts)
   - A testbench file is created for the FPU module `fpu_tb.v`

### File creation report.md: (1 pts)
   - A test report file is created `report.md`

---

## Main Module Checkpoints - Total 4 pts (grade_checkpoint2)

### 1. Interface & Modularity (1 pts)
   - The module correctly implements all required ports:
     ```verilog
      module fpu(
         input wire clk,                  // Clock signal for pipelining
         input wire [1:0] rounding_mode,  // Selects the rounding mode
         input wire [2:0] operation,      // Selects the FPU operation
         input wire [31:0] operand_A,     // First operand (single-precision)
         input wire [31:0] operand_B,     // Second operand (single-precision)
         output wire [31:0] out,          // Result of the operation
         output wire overflow,            // Overflow exception
         output wire underflow,           // Underflow exception
         output wire div_by_zero,         // Division by zero exception
         output wire inexact,             // Inexact result exception
         output wire invalid_operation    // Invalid operation exception
      );
      ```

### 2. Operations Support (1 pts)
   - Implements all required operations:
     - Addition/Subtraction
     - Multiplication
     - Division
     - Int-to-Float/Float-to-Int conversion
   - Proper operation selection and control

### 3. IEEE 754 Compliance (1 pts)
   - Correct handling of special values (NaN, Infinity, Zero)
   - Proper implementation of rounding modes
   - Accurate exception generation
   - Correct sign handling

### 4. Pipeline Implementation (1 pts)
   - Proper pipeline stages for each operation
   - Correct data forwarding and hazard handling
   - Pipeline control signals properly managed
   - Consistent latency for operations

---

## Testbench Comprehensiveness - Total 7 pts (grade_checkpoint3)

### Basic Operations: (1 pts)
   - Test addition/subtraction with various operands
   - Test multiplication with different values
   - Test division with valid inputs
   - Test format conversions

### Special Values: (1 pts)
   - Test NaN handling
   - Test Infinity operations
   - Test Zero handling
   - Test denormalized numbers

### Rounding Modes: (1 pts)
   - Test round to nearest even
   - Test round toward zero
   - Test round toward +∞
   - Test round toward -∞

### Exceptions: (1 pts)
   - Test overflow conditions
   - Test underflow conditions
   - Test division by zero
   - Test invalid operations

### Conversions: (1 pts)
   - Test int-to-float conversion
   - Test float-to-int conversion
   - Test boundary cases
   - Test rounding during conversion

### Edge Cases: (1 pts)
   - Test boundary conditions
   - Test extreme values
   - Test special number combinations
   - Test corner cases

### Pipeline: (1 pts)
   - Test pipeline throughput
   - Test hazard handling
   - Test operation sequences
   - Test pipeline stalls

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**



