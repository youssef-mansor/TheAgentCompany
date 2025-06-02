
---

## Main Module Checkpoints - Total 20 pts

The following exists:

1. Clocked Sequential Control (3 pts)

   * Presence of a clock and reset input. (1 pt)
   * State machine driven by clock edges and reset conditions. (1 pt)
   * Round tracking logic that updates on clock edges (e.g., a round counter or phase control). (1 pt)

2. Modular Structure (2 pts)

   * Separate instantiations for core AES steps (SubBytes, ShiftRows, etc.). (1 pt)
   * Separation of datapath and control logic using modules or internal structuring. (1 pt)

3. Key Expansion Storage (2 pts)

   * Logic to compute or precompute multiple round keys. (1 pt)
   * Storage mechanism for all required round keys (e.g., an array or memory). (1 pt)

4. AES Round Operations (4 pts)

   * Inclusion of SubBytes transformation. (1 pt)
   * Inclusion of ShiftRows transformation. (1 pt)
   * Inclusion of MixColumns transformation. (1 pt)
   * Conditional omission of MixColumns in the final round. (1 pt)

5. Internal State Register (2 pts)

   * Register or equivalent for holding 128-bit internal state. (1 pt)
   * State updated sequentially between rounds. (1 pt)

6. Round Completion Detection (2 pts)

   * Logic to detect when the last round is reached. (1 pt)
   * Signal or condition that flags encryption completion. (1 pt)

7. Output Assignment (3 pts)

   * Output derived from internal AES state after final round. (1 pt)
   * Output held stable until next encryption session. (1 pt)
   * Output only assigned after encryption is completed. (1 pt)
---

## Testbench Comprehensiveness checkpoints - Total 8 pts


1. Known Correctness Vector(s) Used (4 pts)

   * At least one test case using a published AES-128 test vector (e.g., from NIST or FIPS-197). (1 pt)
   * The expected ciphertext is explicitly checked against the DUT output. (3 pt)

2. All-Zero Edge Case (1 pt)

   * A test case where both the key and plaintext are all zeros.

3. All-One Edge Case (1 pt)

   * A test case where the key and plaintext are all ones (0xFF).

4. Repeated Input Stability (1 pt)

   * A test case that encrypts the same input multiple times and checks for deterministic, repeatable output.

5. Final Round Verification (1 pt)

   * A test case where the output is checked to ensure that MixColumns is skipped in the final round.

---
