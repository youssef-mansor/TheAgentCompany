---

## Main Module Checkpoints - Total 15 pts

### 1. Input/Output Interface (5 pts)
- The code contains the following ports:
  - The code implements clock and reset inputs (1 pt)
  - The code implements serial input and output data lines as single-bit ports (1 pt)
  - The code implements a control signal to initiate transmission with proper edge detection (1 pt)
  - The code implements status signals indicating reception, transmission, and error states, with correct timing (1 pt)
  - The code implements two 8-bit data buses for sending and receiving data (1 pt)

### 2. Transmission Logic (4 pts)
- The code implements the transmission protocol:
  - The code generates a start bit (logic 0) for one bit period at the beginning of transmission (1 pt)
  - The code transmits 8 bits of data serially (LSB first) with correct bit timing (1 pt)
  - The code generates a stop bit (logic 1) for one bit period at the end of transmission (1 pt)
  - The code controls timing using a bit counter and a clock divider based on baud rate (1 pt)

### 3. Reception Logic (5 pts)
- The code implements the reception protocol:
  - The code detects the start bit by sampling the serial input line at 16x baud rate (1 pt)
  - The code validates the start bit by checking at the middle sample points (1 pt)
  - The code samples 8 bits of data at the middle of each bit period (1 pt)
  - The code verifies the stop bit is logic 1 at the expected time (1 pt)
  - The code handles metastability on the serial input line (1 pt)

---

## Testbench Comprehensiveness Checkpoints - Total 8 pts

### Reset Check (1 pt)
- Apply reset and verify all outputs initialize correctly.  

### Transmission (1 pt)
- Load a data byte for transmission, trigger the transmission, check the output waveform, and ensure transmission status signal toggles correctly.  

### Reception (1 pt)
- Drive a valid UART frame on the input line, verify the received data byte and reception status signals.  

### Loopback (1 pt)
- Connect the transmit output to the receive input, send a byte, and verify correct reception and status behavior.  

### Idle Check (1 pt)
- Ensure transmission and reception status signals remain low when idle.  

### Framing Error (1 pt)
- Send a frame with an invalid stop bit and verify the error status signal is asserted.  

### Glitch Handling (1 pt)
- Inject a brief glitch on the input line and ensure no false reception or data corruption occurs.  

### Overrun Check (1 pt)
- Send a new byte before the previous one is processed and verify appropriate handling or error detection.  

---

