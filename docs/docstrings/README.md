<!-- markdownlint-disable -->

# API Overview

## Modules

- [`ecccpu`](./ecccpu.md#module-ecccpu)
- [`ecccpu.decode`](./ecccpu.decode.md#module-ecccpudecode)
- [`ecccpu.execr`](./ecccpu.execr.md#module-ecccpuexecr)
- [`ecccpu.mem`](./ecccpu.mem.md#module-ecccpumem)
- [`gui`](./gui.md#module-gui)
- [`legv8`](./legv8.md#module-legv8)
- [`legv8.decode`](./legv8.decode.md#module-legv8decode)
- [`legv8.execr`](./legv8.execr.md#module-legv8execr)
- [`legv8.mem`](./legv8.mem.md#module-legv8mem)
- [`ponyo`](./ponyo.md#module-ponyo)

## Classes

- [`mem.mem`](./ecccpu.mem.md#class-mem): Memory class for the EccCPU ISA
- [`mem.mem`](./legv8.mem.md#class-mem): Memory class for the LEGv8 ISA
- [`ponyo.Simulator`](./ponyo.md#class-simulator): ISA Simulator

## Functions

- [`decode.decode`](./ecccpu.decode.md#function-decode): Decodes each instruction into a simpler format, replacing symbols, register aliases, and removing comments for the EccCPU ISA
- [`decode.findSymbols`](./ecccpu.decode.md#function-findsymbols): Find the symbols in the instruction memory, e.g. `main:`
- [`execr.execr`](./ecccpu.execr.md#function-execr): Executes the instruction on the simulator state for the EccCPU ISA
- [`execr.immu2int`](./ecccpu.execr.md#function-immu2int): Converts an immediate value into an integer
- [`gui.currCode`](./gui.md#function-currcode): String showing surrounding code to PC
- [`gui.gui`](./gui.md#function-gui): Runs an interactive GUI for the simulator using PySimpleGUIQt
- [`decode.decode`](./legv8.decode.md#function-decode): Decodes each instruction into a simpler format, replacing symbols, register aliases, and removing comments for the LEGv8 ISA
- [`decode.findSymbols`](./legv8.decode.md#function-findsymbols): Find the symbols in the instruction memory, e.g. `main:`
- [`execr.execr`](./legv8.execr.md#function-execr): Executes the instruction on the simulator state for the LEGv8 ISA
- [`execr.immu2int`](./legv8.execr.md#function-immu2int): Converts an immediate value into an integer


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
