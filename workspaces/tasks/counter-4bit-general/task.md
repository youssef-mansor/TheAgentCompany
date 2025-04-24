Write a simple 4-bit counter. make sure it’s resettable and that it counts up correctly.

then write a testbench for it. it should test normal incrementing and also make sure it wraps back to 0 after hitting 15. use assertions so that if anything breaks it stops right away (MUST use $fatal for that in case of a verilog testbench).

debug any issues you find. if something’s off in your design or test, fix it until all tests pass.

you must make a shell script called run_test.sh that runs your testbench only. try running it to make sure it actually works.