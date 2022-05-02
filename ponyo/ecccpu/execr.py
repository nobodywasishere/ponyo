def immu2int(immu: str) -> int:
    """Converts an immediate value into an integer

    Args:
        immu (str): Immediate value (e.g. `#10`, `0x03`, `b00101`)

    Returns:
        int: Value stored in immediate
    """
    if immu[0] == "#":
        return int(immu[1:])
    elif immu[:2] == "0x":
        return int(immu[2:], 16)
    elif immu[0] == "b":
        return int(immu[1:], 2)
    else:
        return int(immu)


def execr(mem, instr: dict[str, str]):
    """Executes the instruction on the simulator state for the EccCPU ISA

    Args:
        mem (ecccpu.mem): ISA memory class
        instr (dict[str, str]): Decoded instruction

    Raises:
        Exception: If an unsupported instruction is executed
    """

    # | instr.        | operation                      | flag |
    # |:-------------:|:------------------------------:|:----:|
    # | `NOP`         | No operation                   |      |
    # | `AND RR SS`   | And S and R, store in R        |   x  |
    # | `OR  RR SS`   | Or S and R, store in R         |   x  |
    # | `ADD RR SS`   | Add R to S, store in R         |   x  |
    # | `SUB RR SS`   | Sub S from R, store in R       |   x  |
    # | `INC RR`      | Increment R                    |   x  |
    # | `DEC RR`      | Decrement R                    |   x  |
    # | `CMP RR SS`   | Compare R with S               |   x  |
    # | `LDD RR DD`   | Load from data D into R        |      |
    # | `LDR RR SS`   | Load from D based on S into R  |      |
    # | `STD RR DD`   | Store R in data D              |      |
    # | `STR RR SS`   | Store R in addr by 4 bits of S |      |
    # | `JMP RR`      | Jump to address in R           |      |
    # | `JMP RR CC`   | Jump to address in R if C      |      |
    # | `LDI RR VV`   | Load immediate V into R        |      |

    op = instr["op"]
    a1 = instr["a1"]
    a2 = instr["a2"]
    result = None

    if op == "" or op == "NOP" or op == "NOOP":
        pass
    elif op == "AND":
        mem.regs_write(a1, mem.regs_read(a1) & mem.regs_read(a2))
        result = mem.regs_read(a1) & mem.regs_read(a2)
    elif op == "OR":
        mem.regs_write(a1, mem.regs_read(a1) | mem.regs_read(a2))
        result = mem.regs_read(a1) | mem.regs_read(a2)
    elif op == "ADD":
        mem.regs_write(a1, mem.regs_read(a1) + mem.regs_read(a2))
        result = mem.regs_read(a1) + mem.regs_read(a2)
    elif op == "SUB":
        mem.regs_write(a1, mem.regs_read(a1) - mem.regs_read(a2))
        result = mem.regs_read(a1) - mem.regs_read(a2)
    elif op == "INC":
        mem.regs_write(a1, mem.regs_read(a1) + 1)
        result = mem.regs_read(a1) + 1
    elif op == "DEC":
        mem.regs_write(a1, mem.regs_read(a1) - 1)
        result = mem.regs_read(a1) - 1
    elif op == "CMP":
        result = (mem.regs_read(a1), mem.regs_read(a2))
    elif op == "LDD":
        mem.regs_write(a1, mem.ram_read(immu2int(a2)))
    elif op == "LDR":
        mem.regs_write(a1, mem.ram_read(mem.regs_read(a2)))
    elif op == "STD":
        mem.ram_write(mem.regs_read(a1), immu2int(a2))
    elif op == "STR":
        mem.ram_write(mem.regs_read(a1), mem.regs_read(a2))
    elif op == "JMP":
        if a2 is not None:
            # | CMP | CCCC | int |
            # |:---:|:----:|:---:|
            # | any         | `0000` |  0 |
            # | zero        | `0001` |  1 |
            # | negative    | `0010` |  2 |
            # | carry       | `0011` |  3 |
            # | >  (unsign) | `0100` |  4 |
            # | <  (unsign) | `0101` |  5 |
            # | >= (unsign) | `0110` |  6 |
            # | <= (unsign) | `0111` |  7 |
            # | =           | `1000` |  8 |
            # | >  (signed) | `1100` | 12 |
            # | <  (signed) | `1101` | 13 |
            # | >= (signed) | `1110` | 14 |
            # | <= (signed) | `1111` | 15 |
            c = immu2int(a2)
            if (
                (c == 0)
                or (c == 1 and mem.flags["z"])
                or (c == 2 and mem.flags["n"])
                or (c == 3 and mem.flags["c"])
                or (c == 4 and mem.flags[">u"])
                or (c == 5 and mem.flags["<u"])
                or (c == 6 and (mem.flags["="] or mem.flags[">u"]))
                or (c == 7 and (mem.flags["="] or mem.flags["<u"]))
                or (c == 8 and mem.flags["="])
                or (c == 12 and mem.flags[">s"])
                or (c == 13 and mem.flags["<s"])
                or (c == 14 and (mem.flags["="] or mem.flags[">s"]))
                or (c == 15 and (mem.flags["="] or mem.flags["<s"]))
            ):
                mem.pc = mem.regs_read(a1)
        else:
            mem.pc = mem.regs_read(a1)
    elif op == "LDI":
        mem.regs_write(a1, immu2int(a2))

    else:
        raise Exception(f"Instruction {op} is not supported (yet)")

    # Only true for instructions that set flags
    if result is not None:
        # Zero
        if result == 0:
            mem.flags["z"] = 1
            mem.flags["="] = 1
        else:
            mem.flags["z"] = 0
            mem.flags["="] = 0

        # Negative
        if (result % 2**mem.REGS_MOD) > 2 ** (mem.REGS_MOD - 1):
            mem.flags["n"] = 1
        else:
            mem.flags["n"] = 0

        # Carry
        if result >= 2**mem.REGS_MOD:
            mem.flags["c"] = 1
        else:
            mem.flags["c"] = 0

        # Unsigned
