## Action Points (4 pts)  

- Check for the existence of `uart/.git` (1 pt)  
- Check for the existence of `verilog/rtl/user_project_wrapper.v` (1 pt)  
- Check for the existence of `verilog/dv/test_user_project_wrapper.py` (1 pt)  
- Check for the existence of `report.md`  (1 pt)

---

## Check for User Project Wrapper Module (4 pts)  

- Ensure that a Wishbone wrapper for the UART module is instantiated correctly within the `user_project_wrapper`.  
- If `USE_POWER_PINS` is defined, verify the presence of `.VPWR(vccd2)` and `.VGND(vssd2)` connections to ensure proper power and ground connections. (1 pt)  
- Verify that all Wishbone interface signals are correctly connected. (1 pt)  
- Ensure that the IO pads are properly connected. (1 pt)  
- Confirm that the interrupt request line is connected with `.irq(user_irq)`, ensuring the module can signal interrupts to the system. (1 pt)  

# File Content  

## user_project_wrapper.v  

---

## Check for User Project Wrapper Test (4 pts)  

Ensure the following points are addressed in the test: (1 pt)  

- **Data Transmission:** Iterate over a range of values, setting input signals and asserting control signals to simulate data transactions. (1 pt)  
- **Assertions:** Use assert statements to verify that the output matches the expected results. (1 pt)  
- **Logging:** Log messages to indicate the completion and success of the test. (1 pt)  

# File Content  

## test_user_project_wrapper.py  

---

## Functionality  

The test should return the count of passed test cases in the `report.md` file and the total number of cases in the following format:  

**Final Score: `<score - number of cases passed>/<total number of cases>`**  

# File Content  

## report.md  
