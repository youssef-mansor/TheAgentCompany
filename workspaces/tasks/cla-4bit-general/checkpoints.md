## Action Checkpoints - Total 3 pts (grade_checkpoint1)

### File creation cla.v: (1 pts)
   - A file is created for the CLA module `cla.v` (1 pts)

### File creation cla_tb.v: (1 pts)
   - A testbench file is created for the CLA module `cla_tb.v` (1 pts)

### File creation report.md: (1 pts)
   - A test file is created for the output of the testbench `report.md` (1 pts)

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

## Testbench Comprehensiveness checkpoints - Total (1 pt) (grade_checkpoint3)

- The testbench tests all possible 512 unique combinations for `A`, `B`, `cin` (1 pt)


---

## Functionality - Total (# of tests in report.md) pts (grade_checkpoint4)
    Returns the count of passed test cases in the report.md file and the total number of cases in the file. in the specific format of course **Final Score: <score - number of cases passed>/<total number of cases>**

# File Content

## report.md