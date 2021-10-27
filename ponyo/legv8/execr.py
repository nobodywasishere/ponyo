
def immu2int(immu):
    if immu[0] == "#":
        return int(immu[1:])
    elif immu[:2] == "0x":
        return int(immu[2:], 16)
    elif immu[0] == "b":
        return int(immu[1:], 2)
    else:
        return int(immu)

def execr(mem, instr):

    # | type | op     | a1   | a2   | a3   | a4    |
    # |------|--------|------|------|------|-------|
    # | R    | opcode | Rd   | Rn   | Rm   | shamt |
    # | I    | opcode | Rd   | Rn   | Imm  | -     |
    # | D    | opcode | Rt   | Rn   | op   | Addr  |
    # | B    | opcode | Addr | -    | -    | -     |
    # | CB   | opcode | Rt   | Addr | -    | -     |
    # | IW   | opcode | Rd   | Imm  | -    | -     |

    op = instr['op'].upper()
    a1 = instr['a1']
    a2 = instr['a2']
    a3 = instr['a3']
    a4 = instr['a4']
    result = None

    if   op == "" or op == "NOP" or op == "NOOP":
        pass

    elif op == "ADD":
        mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] + mem.regs[int(a3[1:])]
    elif op == "ADDI":
        mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] + immu2int(a3)
    elif op == "ADDS":
        result = mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] + mem.regs[int(a3[1:])]
    elif op == "ADDIS":
        result = mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] + immu2int(a3)

    elif op == "AND":
        mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] & mem.regs[int(a3[1:])]
    elif op == "ANDI":
        mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] & immu2int(a3)
    elif op == "ANDS":
        result = mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] & mem.regs[int(a3[1:])]
    elif op == "ANDIS":
        result = mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] & immu2int(a3)

    elif op == "B":
        mem.pc += immu2int(a1) - 1
    elif op[:2] == "B.":
        cond = op[2:]
        branch = False
        if   cond == "EQ" and mem.flags['Z'] == 1:
            branch = True
        elif cond == "NE" and mem.flags['Z'] == 0:
            branch = True
        elif cond == "LT" and mem.flags['N'] != mem.flags['V']:
            branch = True
        elif cond == "LE" and not (mem.flags['Z'] == 0 and mem.flags['N'] == mem.flags['V']):
            branch = True
        elif cond == "GT" and (mem.flags['Z'] == 0 and mem.flags['N'] == mem.flags['V']):
            branch = True
        elif cond == "GE" and mem.flags['N'] == mem.flags['V']:
            branch = True
        elif cond == "LO" and mem.flags['C'] == 0:
            branch = True
        elif cond == "LS" and not (mem.flags['Z'] == 0 and mem.flags['C'] == 1):
            branch = True
        elif cond == "HI" and (mem.flags['Z'] == 0 and mem.flags['C'] == 1):
            branch = True
        elif cond == "HS" and mem.flags['C'] == 1:
            branch = True
        if branch:
            mem.pc += immu2int(a1) - 1
    elif op == "BL":
        mem.regs[30] = mem.pc + 1
        mem.pc += immu2int(a1) - 1
    elif op == "BR":
        mem.pc = mem.regs[int(a1[1:])] - 1
    elif op == "CBNZ":
        if mem.regs[int(a1[1:])] != 0:
            mem.pc += immu2int(a2) - 1
    elif op == "CBZ":
        if mem.regs[int(a1[1:])] == 0:
            mem.pc += immu2int(a2) - 1
    
    elif op == "EOR":
        mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] ^ mem.regs[int(a3[1:])]
    elif op == "EORI":
        mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] ^ immu2int(a3)

    elif op == "LDUR":
        mem.regs[int(a1[1:])] = mem.dmem_read(mem.regs[int(a2[1:])], immu2int(a3), 8)
    elif op == "LDURB":
        mem.regs[int(a1[1:])] = mem.dmem_read(mem.regs[int(a2[1:])], immu2int(a3), 1)
    elif op == "LDURH":
        mem.regs[int(a1[1:])] = mem.dmem_read(mem.regs[int(a2[1:])], immu2int(a3), 2)
    # elif op == "LDURSW":
    #     pass
    # elif op == "LDXR":
    #     pass

    elif op == "LSL":
        mem.regs[int(a1[1:])] == mem.regs[int(a2[1:])] << immu2int(a3)
    elif op == "LSR":
        mem.regs[int(a1[1:])] == mem.regs[int(a2[1:])] >> immu2int(a3)

    # elif op == "MOVK":
    #     pass
    # elif op == "MOVZ":
    #     pass

    elif op == "ORR":
        mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] | mem.regs[int(a3[1:])]
    elif op == "ORRI":
        mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] | immu2int(a3)

    elif op == "STUR":
        mem.dmem_write(mem.regs[int(a1[1:])], mem.regs[int(a2[1:])], immu2int(a3), 8)
    elif op == "STURB":
        mem.dmem_write(mem.regs[int(a1[1:])], mem.regs[int(a2[1:])], immu2int(a3), 1)
    elif op == "STURH":
        mem.dmem_write(mem.regs[int(a1[1:])], mem.regs[int(a2[1:])], immu2int(a3), 2)
    # elif op == "STURSW":
    #     pass
    # elif op == "STXR":
    #     pass

    elif op == "SUB":
        mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] - mem.regs[int(a3[1:])]
    elif op == "SUBI":
        mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] - immu2int(a3)
    elif op == "SUBS":
        result = mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] - mem.regs[int(a3[1:])]
    elif op == "SUBIS":
        result = mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] - immu2int(a3)

    # elif op == "FADDS":
    #     pass
    # elif op == "FADDD":
    #     pass
    # elif op == "FCMPS":
    #     pass
    # elif op == "FCMPD":
    #     pass
    # elif op == "FDIVS":
    #     pass
    # elif op == "FDIVD":
    #     pass
    # elif op == "FMULS":
    #     pass
    # elif op == "FMULD":
    #     pass
    # elif op == "FSUBS":
    #     pass
    # elif op == "FSUBD":
    #     pass

    # elif op == "LDURS":
    #     pass
    # elif op == "LDURD":
    #     pass
    # elif op == "MUL":
    #     mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])] * mem.regs[int(a3[1:])]
    # elif op == "SDIV":
    #     pass
    # elif op == "SMULH":
    #     mem.regs[int(a1[1:])] = (mem.regs[int(a2[1:])] * mem.regs[int(a3[1:])]) >> mem.regsMod
    # elif op == "UDIV":
    #     pass
    # elif op == "UMULH":
    #     pass

    elif op == "CMP":
        result = mem.regs[int(a2[1:])] - mem.regs[int(a3[1:])]
    elif op == "CMPI":
        result = mem.regs[int(a2[1:])] - immu2int(a3)
    # elif op == "LDA":
    #     pass
    elif op == "MOV":
        mem.regs[int(a1[1:])] = mem.regs[int(a2[1:])]

    else:
        raise Exception(f"Instruction {op} is not supported (yet)")

    # Only true for instructions that set flags
    if result is not None:
        # Zero
        if result == 0:
            mem.flags['Z'] = 1
        else:
            mem.flags['Z'] = 0

        # Negative
        if (result % 2**mem.regsMod) >= 2**(mem.regsMod - 1):
            mem.flags['N'] = 1
        else:
            mem.flags['N'] = 0

        # Carry
        if result >= 2**mem.regsMod:
            mem.flags['C'] = 1
        else:
            mem.flags['C'] = 0

        # Overflow
        in1 = mem.regs[int(a2[1:])]
        if op[-2] == "I":
            in2 = immu2int(a3)
        else:
            in2 = mem.regs[int(a3[1:])]
        regsNeg = 2**(mem.regsMod - 1)
        if   op[:3] == "AND":
            if (in1 <  regsNeg and in2 <  regsNeg and result >= regsNeg) or \
               (in1 >= regsNeg and in2 >= regsNeg and result <  regsNeg):
                mem.flags['V'] = 1
            else:
                mem.flags['V'] = 0
        elif op[:3] == "ORR":
            if (in1 <  regsNeg and in2 >= regsNeg and result >= regsNeg) or \
               (in1 >= regsNeg and in2 <  regsNeg and result <  regsNeg):
                mem.flags['V'] = 1
            else:
                mem.flags['V'] = 0

    mem.clean()
    return mem
            
        