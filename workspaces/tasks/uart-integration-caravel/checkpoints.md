## Action Points (3 pts)  

- Check for the existence of `uart/.git` (1 pt)  
- Check for the existence of `verilog/rtl/user_project_wrapper.v` (1 pt)  

---

## Check for User Project Wrapper Module (4 pts)  
File Name: user_project_wrapper.v  

- Ensure that a Wishbone wrapper for the UART module is instantiated correctly within the `user_project_wrapper`.  
- If `USE_POWER_PINS` is defined, verify the presence of `.VPWR(vccd2)` and `.VGND(vssd2)` connections to ensure proper power and ground connections. (1 pt)  
- Verify that all Wishbone interface signals are correctly connected. (1 pt)  
- Ensure that the IO pads are properly connected. (1 pt)  
- Confirm that the interrupt request line is connected with `.irq(user_irq)`, ensuring the module can signal interrupts to the system. (1 pt)  


---

## Check for User Project Wrapper Test (3 pts)  

Ensure the following points are addressed in the test: (1 pt)  

- **Data Transmission:** Iterate over a range of values, setting input signals and asserting control signals to simulate data transactions. (1 pt)  
- **Assertions:** Use assert statements to verify that the output matches the expected results. (1 pt)  
- **Logging:** Log messages to indicate the completion and success of the test. (1 pt)  

---
