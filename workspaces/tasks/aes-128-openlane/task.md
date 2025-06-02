Implement a modular, iterative AES-128 encryption design in Verilog. The design should consist of separate modules for Key Expansion, SubBytes (with an S-box), ShiftRows, MixColumns, AddRoundKey, and a top-level AES controller with a round counter and FSM to manage the flow across 10 rounds. Use an iterative approach, processing one round per clock cycle.

Include a testbench that feeds in known plaintext-key pairs and verifies the output ciphertext against official AES-128 test vectors (e.g., from NIST/FIPS 197). Try to make the testbench comprehenvise in the manner that it has multiple testcases each with different significance. Ensure the testbench checks correctness across all rounds and reports pass/fail for each case.

use assertions - make sure to use $fatal if something fails in case the testbench is a verilog testbench.

if the test doesn’t pass, fix the design or the testbench until everything’s working.

you must make a run_test.sh script that just runs the testbench. run it and make sure it works.

Once everything passes, use OpenLane to harden the top module. Make sure the flow completes and generates a GDSII file. Try to keep PPA (power, performance, area) reasonable.