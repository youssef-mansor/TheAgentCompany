# **Checkpoints for CLA Integration into `user_project_wrapper`**  

## **Application Checkpoints - Total 1 pts** (grade_checkpoint1)  

### **File Creation: `user_project_wrapper.v` (1 pts)**  
- The `user_project_wrapper.v` file created. 
- The **module header** of `user_project_wrapper` must match the one provided by the **OpenLane2 template** illustrated below:  

    ```verilog
        module user_project_wrapper #(
            parameter BITS = 32
        ) (
        `ifdef USE_POWER_PINS
            inout vdda1,	// User area 1 3.3V supply
            inout vdda2,	// User area 2 3.3V supply
            inout vssa1,	// User area 1 analog ground
            inout vssa2,	// User area 2 analog ground
            inout vccd1,	// User area 1 1.8V supply
            inout vccd2,	// User area 2 1.8v supply
            inout vssd1,	// User area 1 digital ground
            inout vssd2,	// User area 2 digital ground
        `endif

            // Wishbone Slave ports (WB MI A)
            input wb_clk_i,
            input wb_rst_i,
            input wbs_stb_i,
            input wbs_cyc_i,
            input wbs_we_i,
            input [3:0] wbs_sel_i,
            input [31:0] wbs_dat_i,
            input [31:0] wbs_adr_i,
            output wbs_ack_o,
            output [31:0] wbs_dat_o,

            // Logic Analyzer Signals
            input  [127:0] la_data_in,
            output [127:0] la_data_out,
            input  [127:0] la_oenb,

            // IOs
            input  [`MPRJ_IO_PADS-1:0] io_in,
            output [`MPRJ_IO_PADS-1:0] io_out,
            output [`MPRJ_IO_PADS-1:0] io_oeb,

            // Analog (direct connection to GPIO pad---use with caution)
            // Note that analog I/O is not available on the 7 lowest-numbered
            // GPIO pads, and so the analog_io indexing is offset from the
            // GPIO indexing by 7 (also upper 2 GPIOs do not have analog_io).
            inout [`MPRJ_IO_PADS-10:0] analog_io,

            // Independent clock (on independent integer divider)
            input   user_clock2,

            // User maskable interrupt signals
            output [2:0] user_irq
        );
    ```

---

## **Integration Checkpoints - Total 5 pts** (grade_checkpoint2)  

The **CLA module** is correctly instantiated within `user_project_wrapper`.  (1 pts)
**Input ports** of the CLA module are connected to `io_in`.  (1 pts)
**Output ports** of the CLA module are connected to `io_out`.  (1 pts)
The CLA module instance ports are assigned **non-overlapping** ranges of `io_in` and `io_out`.  (1 pts)
The assigned bit widths match the required specifications.  (1 pts)
GPIO directions are assigned using io_oeb signals (1 for input; 0 for output) (1 pts)
The GPIO range **[6:0]** is **avoided** and **not assigned** to any CLA connections.  (1 pts)