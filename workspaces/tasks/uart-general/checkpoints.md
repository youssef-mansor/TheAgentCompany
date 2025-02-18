## Action Checkpoints - Total 3 pts (grade_checkpoint1)

### File creation uart.v: (1 pts)
   - A file is created for the UART module `uart.v` (1 pts)

### File creation uart_tb.v: (1 pts)
   - A testbench file is created for the UART module `uart_tb.v` (1 pts)

### File creation report.md: (1 pts)
   - A test file is created for the output of the testbench `report.md` (1 pts)

---

## Main Module Checkpoints - Total 20 pts (grade_checkpoint2)

### 1. Input/Output Interface (5 pts)
   - The code contains the following ports:
     - The code implements clock and reset inputs (1 pts)
     - The code implements RX and TX data lines as single-bit ports (1 pts)
     - The code implements transmission control signal (transmit) with proper edge detection (1 pts)
     - The code implements status signals (received, is_receiving, is_transmitting, recv_error) with correct timing (1 pts)
     - The code implements 8-bit data buses (tx_byte for transmission, rx_byte for reception) (1 pts)

### 2. Transmission Logic (5 pts)
   - The code implements the transmission protocol:
     - The code generates start bit (logic 0) for one bit period at transmission begin (1 pts)
     - The code transmits 8-bit data serially (LSB first) with correct bit timing (1 pts)
     - The code generates stop bit (logic 1) for one bit period at transmission end (1 pts)
     - The code controls timing using a bit counter and clock divider based on baud rate (1 pts)
     - The code handles back-to-back transmission requests properly (1 pts)

### 3. Reception Logic (5 pts)
   - The code implements the reception protocol:
     - The code detects start bit by sampling RX line at 16x baud rate (1 pts)
     - The code validates start bit by checking middle sample points (1 pts)
     - The code samples 8-bit data at the middle of each bit period (1 pts)
     - The code verifies stop bit is logic 1 at the expected time (1 pts)
     - The code handles metastability on the RX input (1 pts)

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

## Testbench Comprehensiveness checkpoints - Total 28 pts (grade_checkpoint3)

### Basic Operation: (4 pts)
   - The testbench code tests:
     - The code verifies all outputs are in correct state after reset (1 pts)
     - The code verifies idle state has TX high and flags inactive (1 pts)
     - The code tests state transitions with timing verification (1 pts)
     - The code verifies initial conditions (1 pts)

### Transmission Tests: (4 pts)
   - The testbench code tests:
     - The code transmits bytes with alternating bit patterns (0x55, 0xAA) (1 pts)
     - The code performs back-to-back transmissions with minimum gap (1 pts)
     - The code verifies each bit period matches baud rate (1 pts)
     - The code checks is_transmitting flag timing (1 pts)

### Reception Tests: (4 pts)
   - The testbench code tests:
     - The code receives bytes with various bit patterns (1 pts)
     - The code handles minimum and maximum speed variations (1 pts)
     - The code samples data with proper 16x oversampling (1 pts)
     - The code verifies received flag timing and duration (1 pts)

### Error Handling: (4 pts)
   - The testbench code tests:
     - The code detects frame errors with early and late stop bits (1 pts)
     - The code recovers within one bit time after error conditions (1 pts)
     - The code signals specific error types through status flags (1 pts)
     - The code handles noise on RX line (1 pts)

### Full Duplex: (4 pts)
   - The testbench code tests:
     - The code performs transmission during active reception (1 pts)
     - The code maintains independent bit timing for TX and RX (1 pts)
     - The code preserves data integrity under maximum load (1 pts)
     - The code handles collisions on external loopback (1 pts)

### Baud Rate: (4 pts)
   - The testbench code tests:
     - The code operates with standard baud rates (9600, 19200, etc.) (1 pts)
     - The code maintains bit timing accuracy over full byte (1 pts)
     - The code synchronizes RX sampling with center of bits (1 pts)
     - The code handles clock ratios that aren't perfect multiples (1 pts)

### Stress Testing: (4 pts)
   - The testbench code tests:
     - The code handles continuous operation for >1000 bytes (1 pts)
     - The code processes pseudo-random data patterns (1 pts)
     - The code maintains stability with noisy inputs (1 pts)
     - The code operates correctly at temperature and voltage corners (1 pts)

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md