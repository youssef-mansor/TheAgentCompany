write a UART module in verilog. it should support sending and receiving bytes one at a time (with 1 start bit, 8 data bits, and 1 stop bit). also needs a configurable baud rate, error detection, and proper status flags for when it’s transmitting, receiving, done receiving, or having faced an error. make sure reset works properly too.

then write a testbench for it. you should test a bunch of stuff:

check reset behavior (outputs should go to the right initial states)

try basic transmission (send a byte like 8'hA5 and make sure the tx line sends the right bits)

try basic reception (manually drive a uart frame on rx and check if it receives it correctly)

do a loopback test (connect tx back to rx and make sure what you send you also receive)

check idle states (make sure is_transmitting and is_receiving are low when idle)

inject framing errors (like wrong stop bit) and make sure recv_error is set

throw in some random glitches on rx and make sure it doesn’t wrongly detect a byte

test overrun by sending bytes faster than they can be read if you can

use assertions and make sure $fatal is used whenever something goes wrong.

if the tests don’t pass, fix either the design or the testbench until everything works.

also create a run_test.sh script to run the testbench, and make sure it actually works.