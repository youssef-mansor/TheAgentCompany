## Action Checkpoints - Total 3 pts (grade_checkpoint1)

### File creation edge_detector.v: (1 pts)
   - A file is created for the edge detector module `edge_detector.v` (1 pts)

### File creation edge_detector_tb.v: (1 pts)
   - A testbench file is created for the edge detector module `edge_detector_tb.v` (1 pts)

### File creation report.md: (1 pts)
   - A test file is created for the output of the testbench `report.md` (1 pts)

---

## Main Module Checkpoints - Total 20 pts (grade_checkpoint2)

### 1. Edge Detection Logic (5 pts)
   - The code implements edge detection:
     - The code detects rising edges correctly (1 pts)
     - The code maintains one-cycle output duration (1 pts)
     - The code handles consecutive edges properly (1 pts)
     - The code synchronizes with clock properly (1 pts)
     - The code prevents false edge detection (1 pts)

### 2. Reset Logic (5 pts)
   - The code implements reset functionality:
     - The code resets output to zero when active (1 pts)
     - The code maintains reset priority over clock (1 pts)
     - The code handles asynchronous reset properly (1 pts)
     - The code maintains reset until deasserted (1 pts)
     - The code resumes operation after reset (1 pts)

### 3. Clock Behavior (5 pts)
   - The code implements clock-based operation:
     - The code samples input on clock edges (1 pts)
     - The code maintains proper output timing (1 pts)
     - The code prevents glitch propagation (1 pts)
     - The code handles clock-to-output delay (1 pts)
     - The code ensures proper signal synchronization (1 pts)

### 4. Interface (5 pts)
   - The code implements module ports:
     - The code defines clock input properly (1 pts)
     - The code defines reset input properly (1 pts)
     - The code defines signal_in input properly (1 pts)
     - The code defines signal_out output properly (1 pts)
     - The code uses correct port directions (1 pts)

---

## Testbench Comprehensiveness checkpoints - Total 28 pts (grade_checkpoint3)

### Basic Edge Detection: (4 pts)
   - The testbench code tests:
     - The code tests single rising edge detection (1 pts)
     - The code verifies one-cycle output duration (1 pts)
     - The code tests falling edge non-detection (1 pts)
     - The code checks output timing accuracy (1 pts)

### Multiple Edge Scenarios: (4 pts)
   - The testbench code tests:
     - The code tests consecutive rising edges (1 pts)
     - The code tests varying edge spacing (1 pts)
     - The code verifies proper edge count (1 pts)
     - The code checks edge timing accuracy (1 pts)

### Reset Behavior: (4 pts)
   - The testbench code tests:
     - The code tests reset during edge detection (1 pts)
     - The code verifies reset priority (1 pts)
     - The code tests reset release behavior (1 pts)
     - The code checks multiple reset scenarios (1 pts)

### Clock Interaction: (4 pts)
   - The testbench code tests:
     - The code tests clock-edge alignment (1 pts)
     - The code verifies setup/hold times (1 pts)
     - The code tests clock frequency effects (1 pts)
     - The code checks clock-to-output delay (1 pts)

### Signal Stability: (4 pts)
   - The testbench code tests:
     - The code tests stable high input (1 pts)
     - The code tests stable low input (1 pts)
     - The code verifies no false triggers (1 pts)
     - The code checks signal integrity (1 pts)

### Edge Cases: (4 pts)
   - The testbench code tests:
     - The code tests glitch rejection (1 pts)
     - The code verifies metastability handling (1 pts)
     - The code tests power-up behavior (1 pts)
     - The code checks corner cases (1 pts)

### Performance Metrics: (4 pts)
   - The testbench code tests:
     - The code tests detection latency (1 pts)
     - The code verifies minimum edge spacing (1 pts)
     - The code tests maximum frequency (1 pts)
     - The code checks resource utilization (1 pts)

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## edge_detector.v

---

## Testbench Comprehensiveness checkpoints - Total 3 pts (grade_checkpoint3)

Ensure the following points are addressed within the test bench 

### Edge Detection: (1 pts)
   - Verify that `signal_out` is `1` only when there is a rising edge on `signal_in`.

### Multiple Edges: (1 pts)
   - Apply multiple rising edges on `signal_in` and confirm that `signal_out` is asserted for one clock cycle for each rising edge.

### No False Positives: (1 pts)
   - Ensure that `signal_out` remains `0` when `signal_in` remains stable (high or low) between clock cycles.


# File Content

## edge_detector_tb.v

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md