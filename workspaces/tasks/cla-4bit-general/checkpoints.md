
---

## Main Module Checkpoints - Total 6 pts (grade_checkpoint2)

The module implements the following interface: (1 pt)
- `A` (4-bit input)
- `B` (4-bit input)
- `cin` (carry-in)
- `S` (4-bit sum output)
- `cout` (carry-out)

The code uses four full adders (one for each bit in the input) or does the addition normally but for each input bit (1 pt)

The code calculates the four Generate (G) terms (1 pt)

The code calculates the four Propagate (P) terms (1 pt)

The code calculates the Carry terms based on G terms, P terms and previous carry (1 pt)

The code returns the final sum using `S` and `cout` ports. (1 pt)

---

## Testbench Comprehensiveness checkpoints - Total (2 pt) (grade_checkpoint3)

- The testbench tests random combinations for `A`, `B`, `cin` (1 pt)
- The testbench tests some edge cases like zero, 15, etc.


---
