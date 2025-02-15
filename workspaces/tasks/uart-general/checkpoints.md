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
   - The code contains the following ports:
     - The code implements clock and reset inputs
     - The code implements RX and TX data lines as single-bit ports
     - The code implements transmission control signal (transmit) with proper edge detection
     - The code implements status signals (received, is_receiving, is_transmitting, recv_error) with correct timing
     - The code implements 8-bit data buses (tx_byte for transmission, rx_byte for reception)

### 2. Transmission Logic (1 pts)
   - The code implements the transmission protocol:
     - The code generates start bit (logic 0) for one bit period at transmission begin
     - The code transmits 8-bit data serially (LSB first) with correct bit timing
     - The code generates stop bit (logic 1) for one bit period at transmission end
     - The code controls timing using a bit counter and clock divider based on baud rate
     - The code maintains is_transmitting flag throughout the transmission sequence
     - The code handles back-to-back transmission requests properly

### 3. Reception Logic (1 pts)
   - The code implements the reception protocol:
     - The code detects start bit by sampling RX line at 16x baud rate
     - The code validates start bit by checking middle sample points
     - The code samples 8-bit data at the middle of each bit period (8 samples at 16x baud rate)
     - The code verifies stop bit is logic 1 at the expected time
     - The code sets error flags for:
       - Framing error (invalid stop bit)
       - Break condition (all bits including stop bit are 0)
       - Overrun error (new data received before previous read)
     - The code handles metastability on the RX input

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

### Basic Operation: (1 pts)
   - The testbench code tests:
     - The code verifies all outputs are in correct state after reset
     - The code verifies idle state has TX high and flags inactive
     - The code tests state transitions with timing verification

### Transmission Tests: (1 pts)
   - The testbench code tests:
     - The code transmits bytes with alternating bit patterns (0x55, 0xAA)
     - The code performs back-to-back transmissions with minimum gap
     - The code verifies each bit period matches baud rate with <2% error
     - The code checks is_transmitting flag timing matches exact transmission period

### Reception Tests: (1 pts)
   - The testbench code tests:
     - The code receives bytes with various bit patterns
     - The code handles minimum and maximum speed variations (±5% baud rate)
     - The code samples data with proper 16x oversampling
     - The code verifies received flag timing and duration

### Error Handling: (1 pts)
   - The testbench code tests:
     - The code detects frame errors with early and late stop bits
     - The code recovers within one bit time after error conditions
     - The code signals specific error types through status flags
     - The code handles noise on RX line (glitches shorter than 1/16 bit time)

### Full Duplex: (1 pts)
   - The testbench code tests:
     - The code performs transmission during active reception
     - The code maintains independent bit timing for TX and RX
     - The code preserves data integrity under maximum load
     - The code handles collisions on external loopback

### Baud Rate: (1 pts)
   - The testbench code tests:
     - The code operates with standard baud rates (9600, 19200, etc.)
     - The code maintains bit timing accuracy over full byte
     - The code synchronizes RX sampling with center of bits
     - The code handles clock ratios that aren't perfect multiples

### Stress Testing: (1 pts)
   - The testbench code tests:
     - The code handles continuous operation for >1000 bytes
     - The code processes pseudo-random data patterns
     - The code maintains stability with noisy inputs
     - The code operates correctly at temperature and voltage corners

# File Content

## uart_tb.v

---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md