## Action Checkpoints - Total 3 pt (grade_checkpoint1)

### File creation uart.v: (1 pts)
   - A file is created for the UART module `uart.v`

### File creation uart_tb.v: (1 pts)
   - A testbench file is created for the UART module `uart_tb.v`

### File creation report.md: (1 pts)
   - A test file is created for the output of the testbench `report.md`

---

## Main Module Checkpoints - Total 4 pts (grade_checkpoint2)

### 1. Input/Output Interface (1 pts)
   - The module correctly implements all required ports:
     - Clock and reset signals
     - RX and TX data lines
     - Control signals (transmit)
     - Status signals (received, is_receiving, is_transmitting, recv_error)
     - Data buses (tx_byte, rx_byte)

### 2. Transmission Logic (1 pts)
   - Implements correct transmission protocol:
     - Start bit generation
     - 8-bit data transmission
     - Stop bit generation
     - Baud rate timing control

### 3. Reception Logic (1 pts)
   - Implements correct reception protocol:
     - Start bit detection
     - 8-bit data sampling
     - Stop bit verification
     - Error detection and handling

### 4. Interface (1 pts)
   - The module header correctly defines the required ports:
   ```verilog
   input wire clk,              // Clock signal for the UART module
   input wire rst,              // Synchronous reset signal
   input wire rx,               // Serial data input line
   input wire transmit,         // Ctrl signal to initiate transmission
   input wire [7:0] tx_byte,    // Data byte to be transmitted
   output reg tx,               // Serial data output line
   output reg received,         // Flag indicating a byte has been successfully received
   output reg [7:0] rx_byte,    // Data byte that has been received
   output reg is_receiving,     // Low when idle
   output reg is_transmitting,  // Low when idle
   output reg recv_error        // Error flag for packet reception issues
   ```

# File Content

## uart.v

---

## Testbench Comprehensiveness checkpoints - Total 7 pts (grade_checkpoint3)

Ensure the following points are addressed within the test bench:

### Basic Operation: (1 pts)
   - Test reset behavior and idle state verification.

### Transmission Tests: (1 pts)
   - Test single byte transmission
   - Test continuous transmission
   - Verify baud rate timing

### Reception Tests: (1 pts)
   - Test single byte reception
   - Test error conditions
   - Verify data sampling

### Error Handling: (1 pts)
   - Test framing error detection
   - Test error recovery
   - Verify error signaling

### Full Duplex: (1 pts)
   - Test simultaneous TX and RX
   - Verify independent operation
   - Test data integrity

### Baud Rate: (1 pts)
   - Test different baud rates
   - Verify timing accuracy
   - Test clock synchronization

### Stress Testing: (1 pts)
   - Test continuous operation
   - Test random data patterns
   - Verify system stability

# File Content

## uart_tb.v

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md