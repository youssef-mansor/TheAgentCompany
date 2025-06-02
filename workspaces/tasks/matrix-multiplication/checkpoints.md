
---

## Main Module Checkpoints - Total 7 pts

The following exists:

1. Presence of Two NxN Matrix Inputs (1 pt)

   * The module defines two matrix inputs, each structured as NxN elements, with each element being a fixed-width scalar (e.g., 8 bits).

2. Output Matrix with Sufficient Bit Width (1 pt)

   * The output is defined as an NxN matrix, with each element having at least twice the bit width of the input elements to handle multiplication and accumulation.

3. Dot Product Computation Structure (1 pt)

   * The implementation includes logic that performs a dot product for each output matrix element by iterating over a shared dimension.

4. Use of Nested Loops or Generate Constructs (1 pt)

   * The matrix computation is expressed using nested `for` loops or `generate` blocks to iterate over rows and columns systematically.

5. Parameterization for Matrix Size and Bit Width (1 pt)

   * The design is parameterized to allow configuration of matrix dimension and element bit width.

6. Intermediate Accumulator for Partial Sums (1 pt)

   * For each output element, the module accumulates multiple partial products in a temporary register or wire before assigning the final value.

7. Combinational or Clocked Evaluation Block (1 pt)

   * The multiplication and accumulation logic is enclosed in a combinational (`always @(*)`) or sequential (`always @(posedge clk)`) block.

---

## Testbench Comprehensiveness checkpoints - Total 7 pts

The following exists:

1. Test with Identity Matrix (1 pt)

   * One input matrix is the identity matrix, and the other is arbitrary. Output should match the arbitrary matrix exactly.

2. Test with Zero Matrix (1 pt)

   * One or both input matrices contain all zeros. Output matrix should be all zeros.

3. Test with Constant Matrices (3 pt)

   * Both input matrices contain constant values. Output verifies correct sum of products.

4. Test with Maximum Values (1 pt)

   * Inputs contain the maximum representable values for the element bit-width to check for overflow handling or correct wider output.

---
