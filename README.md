# LEGv8


## Simulator

- ARM LEGv8 Simulator
    - Harvard architecture
    - Takes in assembly source code
    - Takes in memory file
    - Step through program execution
    - Jump to pre-defined break points in code

### CLI

CLI for interacting with simulator.

```
$ ./LEGv8/sim.py -f assembly_code.asm -d data_mem.hex
```

### TUI

Optional TUI for interacting with simulator. Has a handful of components. 

- Code pane
    - Indicator of current line of code with surrounding code
- Register & flag pane
    - Shows the values of all of the registers and the flags
    - Select/copy/edit values
- Memory & stack pane
    - Scroll through the entire memory space
    - Select/copy/edit values
- Keybindings for controlling the simulator
    - S - Step to next line
    - N - Jump to next breakpoint
    - T - Toggle breakpoint
    - Q - Quit

### Library

The simulator can also be integrated into another Python program as a library.