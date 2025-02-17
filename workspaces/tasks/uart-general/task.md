# Verilog UART Implementation and Testing

## Step 0: Files creation
Create the following files
- `/workspace/report.md`
- `/workspace/uart.v`
- `/workspace/uart_tb.v`

## Step 1: Implement a UART Module
Design a UART module in Verilog with the following interface:
```verilog
module uart(
    input clk,              // Clock signal for the UART module
    input rst,              // Synchronous reset signal
    input rx,               // Serial data input line
    input transmit,         // Ctrl signal to initiate transmission
    input [7:0] tx_byte,    // Data byte to be transmitted
    output tx,              // Serial data output line
    output received,        // Flag indicating a byte has been successfully received
    output [7:0] rx_byte,   // Data byte that has been received
    output is_receiving,    // Low when idle
    output is_transmitting, // Low when idle
    output recv_error       // Error flag for packet reception issues
);
```

The UART should implement:
- Configurable baud rate generation
- Byte-by-byte transmission (1 start bit, 8 data bits, 1 stop bit)
- Asynchronous serial reception with error detection
- Status signaling for transmission and reception states
- Proper reset behavior for all states

Place the implemented UART into `/workspace/uart.v`

## Step 2: Create a Self-Checking Testbench
- Develop a comprehensive testbench for the UART module that covers all possible cases.
- Ensure it automatically verifies correctness and prints the results.
- Save the output in a Markdown file with:
  - **Test title**
  - **Pass/Fail status**

Ensure the following points are addressed within the testbench:

### Basic Operation: (1 pts)
   - Test reset behavior and idle state verification.

### Transmission: (1 pts)
   - Verify single and continuous byte transmission.

### Reception: (1 pts)
   - Test single byte reception and error conditions.

### Error Handling: (1 pts)
   - Validate framing error detection and recovery.

### Full Duplex: (1 pts)
   - Test simultaneous transmission and reception.

### Baud Rate: (1 pts)
   - Verify correct timing and baud rate generation.

### Stress Testing: (1 pts)
   - Test continuous operation with random data.

Place the implemented testbench into `/workspace/uart_tb.v`
Place the test report into `/workspace/report.md`

## Step 3: Debug and Fix Issues
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.
