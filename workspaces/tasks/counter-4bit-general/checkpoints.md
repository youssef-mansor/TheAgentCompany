## Action Checkpoints - Total 3 pts (grade_checkpoint1)

### File creation counter.v: (1 pts)
    a file is created for counter module counter.v 
### File creation counter_tb.v: (1pts)
    a testbench file was created for the counter module counter_tb.v 

### File creation report.md (1 pts)
    a test file is created for the output of the testbench report.md 

---

## Main Module Checkpoints - Total 4 pts (grade_checkpoint2)

### 1. Increment Logic  (1 pts)
    Adds 1 to the count on each rising edge of `clk`. 

### 2. Width Constraint  (1 pts)
    Limits the counter to a range of 0 to 15 (4 bits).

### 3. Interface  (1 pts)
    The module header correctly defines the required ports:  
    ```verilog
    input wire clk;          // Clock signal  
    input wire reset;        // Reset signal  
    output reg [3:0] count;  // 4-bit count output  

# File Content

## counter.v

---

## Testbench Comprehensiveness checkpoints - Total 2 pts (grade_checkpoint3)

Ensure the following points are addressed within the test bench 

### Normal Increment: (1 pts)
     Allow the counter to increment and observe proper functionality at trigerring edge.
### Wrap-Around: (1 pts)
     Ensure the counter wraps back to 0 after reaching 15 (4-bit overflow).


# File Content

## counter_tb.v

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md



