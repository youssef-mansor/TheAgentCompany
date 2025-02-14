# Instantiate CLA Module into Caravel `user_project_wrapper`  

## Module Header  

Instantiate the following module header for the **CLA (Carry Lookahead Adder)** module:  

```verilog
module cla (

// Definition of the Power Pins
`ifdef USE_POWER_PINS
    inout vccd1, // User area 1 - 1.8V Supply  
    inout vssd1, // User area 1 - Digital ground  
`endif

// Input Pins
input [3:0] A,  
input [3:0] B,  
input cin,  

// Output Pins
output [3:0] S,  
output cout  

);
```

into the **Caravel `user_project_wrapper`**. Use **only** General Purpose I/O (GPIO) for connections.

Don't run the openlande flow or make any testing. I just need the file user_proj_wrapper.v