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

    # Stack
    stack = []

    # Assembly
    asm = []

    # Flags
    flags = {
        'N': 0, # negative
        'Z': 0, # zero
        'V': 0, # overflow
        'C': 0  # carry
    }

    # Symbols
    sym = {}

    # Step through each line of assembly
    #   Decode instruction
    #   Execute instruction
    def run(self):
        self.clean()
        self.findSymbols()

        while self.pc < len(self.asm) - 1:
            line = self.asm[self.pc]
            if self.debug: 
                print(line)
            instr = self.decode(line)
            self.execute(instr)
            if '//$break' in line:
                self.printInfo()
                input(': ')
            self.pc += 1 # increment PC at the end of the cycle
        
        self.printInfo()
        # exit when program stops
        return

    # Removes blank lines and trailing spaces
    def clean(self):
        code_clean = []
        for line_i in range(len(self.asm)):
            if self.asm[line_i] != "":
                code_clean.append(self.asm[line_i].strip())
        self.asm = code_clean[:]

    # Search assembly for symbols and return a dict of
    #   their names and values
    def findSymbols(self):
        line_i = 0
        for line in self.asm:
            op = line.split(' ')[0]
            if op[-1] == ":":
                self.symbols[op[:-1]] = line_i
            line_i = line_i + 1

    # Initialize registers
    # Initialize data memory
    # Initialize flags
    def initialize(self):
        for i in range(32):
            self.reg.append(0)

        # initialize data memory to zero
        # unsure how data mem should be handled yet

    # Decode an instruction into its component parts
    def decode(self, assembly):
        instr = {
            'op': None,
            'arg1': None,
            'arg2': None,
            'arg3': None,
            'arg4': None
        }

        # | type | op     | arg1 | arg2 | arg3  | arg4 |
        # |------|--------|------|------|-------|------|
        # | R    | opcode | Rd   | Rn   | shamt | Rm   |
        # | I    | opcode | Rd   | Rn   | Imm   | -    |
        # | D    | opcode | Rt   | Rn   | op    | Addr |
        # | B    | opcode | Addr | -    | -     | -    |
        # | CB   | opcode | Rt   | Addr | -     | -    |
        # | IW   | opcode | Rd   | Imm  | -     | -    |

        # Regex decode instruction

        return instr

    # Execute an instruction given args
    def execute(self, instr):
        pass

    # Prints a pretty output of the current state
    #   of the processor simulation
    def printInfo(self):
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
