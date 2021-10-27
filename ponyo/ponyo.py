#!/usr/bin/env python

import os, sys
import re
import argparse

from legv8 import mem    as legv8_mem
from legv8 import exec   as legv8_exec
from legv8 import decode as legv8_decode

class Simulator:
    # Turn on print debug statements
    debug = False

    # SymbolsSymSym
    sym = {}

    def __init__(self, mem, decode, exec, imem, dmem=[]):
        self.mem = mem.mem(dmem)
        if dmem != []: self.mem.dmem = dmem
        self.printMem = mem.printMem
        self.decode = decode.decode
        self.exec = exec.exec
        self.imem = imem
        self.imem_raw = imem[:]

        sym = decode.findSymbols(imem)

        for line_i in range(len(imem)):
            self.imem[line_i] = decode.decode(line_i, imem[line_i], sym)

    def run(self):
        while self.mem.pc < len(self.imem):
            self.step()

            # Step through each line
            if self.debug:
                self.printMem(self.mem)
                input(': ')
        
        # Print the memory contents at the end of execution
        self.printMem(self.mem)

    def step(self):
        # Get the current instruction
        instr = self.imem[self.mem.pc]

        # Print the instruction
        if self.debug:
            print(f'{self.mem.pc:3d}: {self.imem_raw[self.mem.pc]}')

        # Execute the instruction
        self.exec(self.mem, instr)

        # increment PC at the end of the cycle
        self.mem.pc += 1 
        

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--asm', help="Assembly file",
    required=True)
parser.add_argument('-d', '--mem', help="Data memory file")
parser.add_argument('--isa', default="legv8", help="ISA of assembly file")
parser.add_argument('--debug', action="store_true", default=False)
parser.add_argument('--step', action="store_true", default=False)

if __name__=="__main__":

    args = parser.parse_args()

    imem = open(args.asm).read().splitlines()
    if args.mem:
        dmem = open(args.mem).read().splitlines()
    else:
        dmem = []

    if args.isa == "legv8":
        mem = legv8_mem
        decode = legv8_decode
        exec = legv8_exec
    else:
        raise Exception(f'{args.isa} is not a valid ISA!')

    cpu = Simulator(mem, decode, exec, imem, dmem)

    cpu.debug = args.debug

    cpu.run()
