
---

## Main Module Checkpoints - Total  15 pts (grade_checkpoint2)

### 1. Input/Output Interface (5 pts)
   - The code contains the following ports:
     - The code implements clock and reset inputs (1 pts)
     - The code implements RX and TX data lines as single-bit ports (1 pts)
     - The code implements transmission control signal (transmit) with proper edge detection (1 pts)
     - The code implements status signals (received, is_receiving, is_transmitting, recv_error) with correct timing (1 pts)
     - The code implements 8-bit data buses (tx_byte for transmission, rx_byte for reception) (1 pts)

### 2. Transmission Logic (4 pts)
   - The code implements the transmission protocol:
     - The code generates start bit (logic 0) for one bit period at transmission begin (1 pts)
     - The code transmits 8-bit data serially (LSB first) with correct bit timing (1 pts)
     - The code generates stop bit (logic 1) for one bit period at transmission end (1 pts)
     - The code controls timing using a bit counter and clock divider based on baud rate (1 pts)

### 3. Reception Logic (5 pts)
   - The code implements the reception protocol:
     - The code detects start bit by sampling RX line at 16x baud rate (1 pts)
     - The code validates start bit by checking middle sample points (1 pts)
     - The code samples 8-bit data at the middle of each bit period (1 pts)
     - The code verifies stop bit is logic 1 at the expected time (1 pts)
     - The code handles metastability on the RX input (1 pts)

---

## Testbench Comprehensiveness checkpoints - Total 8 pts (grade_checkpoint3)

### Reset Check (1 pt)
- Assert `rst`, verify all outputs initialize correctly.  
### Transmission (1 pt)
- Set `tx_byte`, assert `transmit`, check `tx` waveform, ensure `is_transmitting` toggles correctly.  
### Reception (1 pt)
- Drive a valid UART frame on `rx`, verify `rx_byte`, `received`, and `is_receiving` behavior.  
### Loopback (1 pt)
- Connect `tx` to `rx`, send a byte, verify correct reception with `rx_byte` and `received`.  
### Idle Check (1 pt)
- Ensure `is_transmitting` and `is_receiving` stay low when idle.  
### Framing Error (1 pt)
- Send a frame with an invalid stop bit, verify `recv_error` is set.  
### Glitch Handling (1 pt)
- Inject brief noise on `rx`, ensure no false reception or data corruption.  
### Overrun Check (1 pt)
- Send a new byte before reading the previous one, verify handling or error flag.  

---
