# Verilog UART Implementation and Testing

## Step 1: Implement a UART Module
Design a UART module in Verilog with the following interface:
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

The UART should implement:
- Configurable baud rate generation
- Byte-by-byte transmission (1 start bit, 8 data bits, 1 stop bit)
- Standard UART reception logic 
- Asynchronous serial reception with error detection
- Status signaling for transmission and reception states
- Proper reset behavior for all states

## Step 2: Create a Self-Checking Testbench
- Develop a comprehensive testbench for the UART module with asserstions that covers all possible cases.  
- If a case fails, the assertion should stop the testbench execution. 

Ensure the following points are addressed within the testbench:

A simple testbench should check the following key aspects to ensure UART functionality:  

### Reset Behavior
   - Assert `rst` and ensure outputs (`rx_byte`, `received`, `is_transmitting`, `is_receiving`, `recv_error`) initialize correctly.  
   
### Basic Transmission
   - Set `tx_byte` to a value (e.g., 8'hA5), assert `transmit`, and check that `tx` outputs the correct UART waveform (start bit, 8 data bits, stop bit).  
   - Ensure `is_transmitting` is high during transmission and goes low after completion.  

### Basic Reception
   - Manually drive a valid UART frame (start bit, 8-bit data, stop bit) on `rx`.  
   - Verify `rx_byte` holds the correct received value and `received` is asserted after the full frame is received.  
   - Ensure `is_receiving` is high during reception and goes low after completion.  

### Loopback Test 
   - Connect `tx` to `rx`, send a byte, and check if `rx_byte` matches `tx_byte` after transmission completes.  
   - Verify `received` is asserted and `recv_error` remains low.  

### Idle State Check
   - After reset and between transmissions, ensure `is_transmitting` and `is_receiving` remain low, indicating idle operation.  

### Framing Error Check
   - Send a UART frame with an incorrect stop bit (e.g., force `rx` low instead of high at the stop bit) and verify that `recv_error` is set.  

### Glitch/Noise Handling
   - Introduce a brief glitch on `rx` (e.g., a short pulse during an idle or data bit period) and ensure it does not falsely trigger `received` or corrupt data.  

### Overrun Error Check
   - Send a new byte before the previous one is read and check if the module properly flags an overrun condition (if applicable) or correctly handles back-to-back reception.  

## Step 3: Debug and Fix Issues
- If the module does not pass all test cases, revisit and refine the Verilog code.
- Modify the design until all test cases pass successfully.

## Step 4: `run_test.sh` File Creation
- Create a shel script `run_test.sh` that contains the command to only run the testbench.
- execute the `run_test.sh` to make sure it successfully runs the testbench.