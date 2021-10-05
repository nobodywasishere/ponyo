#!/usr/bin/env python

import os, sys
import re
import argparse

class LEGv8_Sim:
    # Turn on print debug statements
    debug = False

    # Program counter (line of code in assembly)
    pc = 0

    # Registers
    reg = []

    # Data Memory
    mem_size = 0
    mem = []

    # Assembly
    asm = []

    # Flags
    flags = {
        'N': 0, # negative
        'Z': 0, # zero
        'V': 0, # overflow
        'C': 0  # carry
    }

    # SymbolsSymSym
    sym = {}

    # Step through each line of assembly
    #   Decode instruction
    #   Execute instruction
    def run(self):
        self.findSymbols()
        self.initialize()
        if self.debug:
            print(self.sym)
        while self.pc < len(self.asm):
            line = self.asm[self.pc]
            if self.debug: 
                print(f'{self.pc:3d}: {line}')
            instr = self.decode(line)
            self.execute(instr)
            if '//$break' in line:
                self.printInfo()
                input(': ')
            self.pc += 1 # increment PC at the end of the cycle
        
        self.printInfo()
        # exit when program stops
        return

    # Search assembly for symbols and return a dict of
    #   their names and values
    def findSymbols(self):
        line_i = 0
        for line in self.asm:
            op = line.strip().upper().split(' ')[0]
            if len(op) > 1 and op[-1] == ":":
                self.sym[op[:-1]] = line_i
            line_i = line_i + 1

    # Initialize registers
    # Initialize data memory
    # Initialize flags
    def initialize(self):
        for i in range(32 - len(self.reg)):
            self.reg.append(0)

        # initialize data memory to zero
        # unsure how data mem should be handled yet

    # Decode an instruction into its component parts
    def decode(self, assembly):
        # Assumes assembly is correctly formatted

        instr = {
            'op': None,
            'arg1': None,
            'arg2': None,
            'arg3': None,
            'arg4': None
        }

        # | type | op     | arg1 | arg2 | arg3 | arg4  |
        # |------|--------|------|------|------|-------|
        # | R    | opcode | Rd   | Rn   | Rm   | shamt |
        # | I    | opcode | Rd   | Rn   | Imm  | -     |
        # | D    | opcode | Rt   | Rn   | op   | Addr  |
        # | B    | opcode | Addr | -    | -    | -     |
        # | CB   | opcode | Rt   | Addr | -    | -     |
        # | IW   | opcode | Rd   | Imm  | -    | -     |

        # Force uppercase
        assembly = assembly.strip().upper()

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
            re.sub(match, str(self.sym[match[1:]]), assembly)

        # Split into list
        assembly = assembly.split(' ')

        if len(assembly) > 0: instr['op']   = assembly[0]
        if len(assembly) > 1: instr['arg1'] = assembly[1]
        if len(assembly) > 2: instr['arg2'] = assembly[2]
        if len(assembly) > 3: instr['arg3'] = assembly[3]
        if len(assembly) > 4: instr['arg4'] = assembly[4]

        return instr

    # Execute an instruction given args
    def execute(self, instr):
        if   instr['op'] == "ADD":
            Rd = int(instr['arg1'][1:])
            Rn = int(instr['arg2'][1:])
            Rm = int(instr['arg3'][1:])
            self.reg[Rd] = self.reg[Rn] + self.reg[Rm]
        elif instr['op'] == "ADDI":
            pass
        pass

    # Prints a pretty output of the current state
    #   of the processor simulation
    def printInfo(self):
        for i in range(len(self.reg)):
            print(f'Reg X{i}: {self.reg[i]}')
        pass



parser = argparse.ArgumentParser()
parser.add_argument('-f', '--asm', help="Assembly file",
    required=True)
parser.add_argument('-d', '--mem', help="Data memory file")
parser.add_argument('--debug', action="store_true", default=False)

if __name__=="__main__":

    args = parser.parse_args()

    cpu = LEGv8_Sim()
    cpu.debug = args.debug
    cpu.asm = open(args.asm).read().splitlines()

    if args.mem:
        mem = open(args.mem).read().splitlines()
        cpu_mem_size = len(mem)
        cpu.mem = mem

    cpu.run()

    pass
