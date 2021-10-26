#!/usr/bin/env python

import os, sys
import re
import argparse

from legv8.mem    import mem, printMem
from legv8.exec   import exec
from legv8.decode import decode

class LEGv8_Sim:
    # Turn on print debug statements
    debug = False

    # SymbolsSymSym
    sym = {}

    def __init__(self, imem, dmem=[]):
        self.mem = mem(dmem)
        self.pmem = None
        self.imem = imem

    # Step through each line of assembly
    #   Decode instruction
    #   Execute instruction
    def run(self):
        self.findSymbols()
        if self.debug:
            print(self.sym)
        while self.mem.pc < len(self.imem):
            line = self.imem[self.mem.pc]
            if self.debug:
                print(f'{self.mem.pc:3d}: {line}')

            instr = decode(self.mem.pc, line, self.sym)
            self.mem = exec(self.mem, instr)

            if '//$step' in line and self.debug:
                self.step = True
            if '//$break' in line or self.step:
                printMem(self.mem)
                try:
                    input(': ')
                except:
                    exit()
    
            self.mem.pc += 1 # increment PC at the end of the cycle
        
        printMem(self.mem)
        # exit when program stops
        return

    # Search assembly for symbols and return a dict of
    #   their names and values
    def findSymbols(self):
        line_i = 0
        for line in self.imem:
            op = line.strip().split(' ')[0]
            if len(op) > 1 and op[-1] == ":":
                self.sym[op[:-1]] = line_i
            line_i = line_i + 1
        

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--asm', help="Assembly file",
    required=True)
parser.add_argument('-d', '--mem', help="Data memory file")
parser.add_argument('--debug', action="store_true", default=False)
parser.add_argument('--step', action="store_true", default=False)

if __name__=="__main__":

    args = parser.parse_args()

    imem = open(args.asm).read().splitlines()
    if args.mem:
        dmem = open(args.mem).read().splitlines()
    else:
        dmem = []
    cpu = LEGv8_Sim(imem, dmem)

    cpu.debug = args.debug
    cpu.step  = args.step

    cpu.run()
