#!/usr/bin/env python

import os, sys
import time
import re
import argparse

from legv8 import mem    as legv8_mem
from legv8 import execr  as legv8_execr
from legv8 import decode as legv8_decode

class Simulator:
    # Turn on print debug statements
    debug = False

    # SymbolsSymSym
    sym = {}

    def __init__(self, mem, decode, execr, imem, dmem=[]):
        self.mem = mem.mem(dmem)
        if dmem != []: self.mem.dmem = dmem
        self.decode = decode.decode
        self.execr = execr.execr
        self.imem = imem
        self.imem_len = len(imem)
        self.imem_raw = imem[:]
        self.icount = 0

        sym = decode.findSymbols(imem)

        for line_i in range(len(imem)):
            self.imem[line_i] = decode.decode(line_i, imem[line_i], sym)

    def run(self):
        while self.mem.pc < self.imem_len:
            self.step()

            # Step through each line
            if self.debug:
                self.printMem(self.mem)
                input(': ')
        
        # Print the memory contents at the end of execution
        self.mem.print()

    def step(self):
        # Get the current instruction
        instr = self.imem[self.mem.pc]

        # Print the instruction
        if self.debug:
            print(f'{self.mem.pc:3d}: {self.imem_raw[self.mem.pc]}')

        # Execute the instruction
        self.execr(self.mem, instr)

        # increment PC at the end of the cycle
        self.mem.pc += 1 
        self.icount += 1


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--asm', help="Assembly file",
    required=True)
parser.add_argument('-d', '--mem', help="Data memory file")
parser.add_argument('--isa', default="legv8", help="ISA of assembly file")
parser.add_argument('--debug', action="store_true", default=False)
parser.add_argument('--perf', action="store_true", default=False)
parser.add_argument('--tui', action="store_true", default=False)

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
        execr = legv8_execr
    else:
        raise Exception(f'{args.isa} is not a valid ISA!')

    time_decode_start = time.time()
    cpu = Simulator(mem, decode, execr, imem, dmem)
    time_decode_end = time.time()

    if args.tui:
        pass
        print('TUI not implemented')
        exit(1)
    else:
        cpu.debug = args.debug
        time_exec_start = time.time()
        cpu.run()
        time_exec_end = time.time()

    if args.perf:
        print(f'Decode time: {time_decode_end - time_decode_start:f}s')
        print(f'Exec time:   {time_exec_end - time_exec_start:f}s')
        print(f'Instr count: {cpu.icount}')
        print(f'Instr/sec:   {int(cpu.icount/(time_exec_end - time_exec_start))}')
