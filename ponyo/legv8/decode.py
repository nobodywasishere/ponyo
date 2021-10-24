import re

# Decode an instruction into its component parts
def decode(pc, assembly, sym):
    # Assumes assembly is correctly formatted

    instr = {
        'op': None,
        'a1': None,
        'a2': None,
        'a3': None,
        'a4': None
    }

    # | type | op     | a1   | a2   | a3   | a4    |
    # |------|--------|------|------|------|-------|
    # | R    | opcode | Rd   | Rn   | Rm   | shamt |
    # | I    | opcode | Rd   | Rn   | Imm  | -     |
    # | D    | opcode | Rt   | Rn   | op   | Addr  |
    # | B    | opcode | Addr | -    | -    | -     |
    # | CB   | opcode | Rt   | Addr | -    | -     |
    # | IW   | opcode | Rd   | Imm  | -    | -     |

    # Force uppercase
    assembly = assembly.strip()

    # Remove duplicate spaces and tabs
    # and comments
    assembly = re.sub(r'( +|\t+|//.*)', ' ', assembly)

    # Remove symbol location
    re_symbol = r'^[a-zA-Z0-9_\-.]+:'
    assembly = re.sub(re_symbol, '', assembly).strip()

    # Remove unnecessary characters
    re_chars = r'(\[|\]|,)'
    assembly = re.sub(re_chars, '', assembly).strip()

    # Replace symbol value
    re_symbol = r'=[a-zA-Z0-9]+'
    matched_symbols = re.search(re_symbol, assembly)
    if matched_symbols:
        match = matched_symbols.group()
        assembly = assembly.replace(match, str(sym[match[1:]]-pc))

    assembly = assembly.replace('XZR', 'X31')

    # Remove duplicate spaces and tabs (again)
    assembly = re.sub(r'( +|\t+)', ' ', assembly)

    # Split into list
    assembly = assembly.split(' ')

    if len(assembly) > 0: instr['op'] = assembly[0]
    if len(assembly) > 1: instr['a1'] = assembly[1]
    if len(assembly) > 2: instr['a2'] = assembly[2]
    if len(assembly) > 3: instr['a3'] = assembly[3]
    if len(assembly) > 4: instr['a4'] = assembly[4]

    return instr