import re


def findSymbols(imem: list[str]) -> dict[str, str]:
    """Find the symbols in the instruction memory, e.g. `main:`

    Args:
        imem (list[str]): Instruction memory

    Returns:
        dict[str, int]: Dictionary of symbols corresponding with their line numbers
    """
    sym = {}
    for line_i, line in enumerate(imem):
        op = line.strip().split(" ")[0]
        if len(op) > 1 and op[-1] == ":":
            sym[op[:-1]] = line_i
    return sym


# Decode an instruction into its component parts
def decode(pc: int, assembly: str, sym: dict[str, int]) -> dict[str, str]:
    """Decodes each instruction into a simpler format, replacing symbols, register aliases, and removing comments for the EccCPU ISA

    Args:
        pc (int): Program counter
        assembly (str): Instruction to decode
        sym (dict[str, int]): Symbol dictionary

    Returns:
        dict[str, str]: Decoded instruction
    """
    # Assumes assembly is correctly formatted

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

    instr = {"op": None, "a1": None, "a2": None}

    # Remove trailing spaces
    assembly = assembly.strip()

    # Remove duplicate spaces and tabs
    # and comments
    assembly = re.sub(r"( +|\t+|//.*|;.*)", " ", assembly)

    # Remove symbol location
    re_symbol = r"^[a-zA-Z0-9_\-.]+:"
    assembly = re.sub(re_symbol, "", assembly).strip()

    # Remove unnecessary characters
    re_chars = r"(\[|\]|,)"
    assembly = re.sub(re_chars, " ", assembly).strip()

    # Remove duplicate spaces and tabs (again)
    assembly = re.sub(r"( +|\t+)", " ", assembly)

    # Split into list
    split_asm = assembly.split(" ")

    if len(split_asm) > 0:
        instr["op"] = split_asm[0].upper()
    if len(split_asm) > 1:
        instr["a1"] = split_asm[1]
    if len(split_asm) > 2:
        if split_asm[2] in sym:
            instr["a2"] = str(sym[split_asm[2]])
        else:
            instr["a2"] = split_asm[2]

    return instr
