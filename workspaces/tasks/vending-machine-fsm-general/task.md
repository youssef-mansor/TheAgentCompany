make a vending machine FSM in verilog. it should let you pick one of 3 products (A, B, or C), and you can insert money in 5, 10, or 20 units. prices are: A is 5, B is 10, C is 15. if you put in more than needed, it should return the extra as change. if you cancel before finishing, it should give back all the money. if not enough money is inserted, it should wait for more.

the inputs are clk, reset, money, select_product (2-bit), and extra_cash (for more money after the first insert). outputs are prodA, prodB, prodC, and balance.

then write a testbench that checks:

all money types (5, 10, 20)

buying each product

change being returned correctly

full amount returned if canceled

needing more money if not enough is inserted

use assertions and make sure to use $fatal (this is a must) if anything fails in case of a verilog testbench.

fix any bugs in your design or testbench until all tests pass.

you must create a run_test.sh script that just runs your testbench. try running it and see that it works.