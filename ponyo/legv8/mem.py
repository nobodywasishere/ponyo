
class mem:
    flags = {
        'N': 0, # negative
        'Z': 0, # zero
        'V': 0, # overflow
        'C': 0  # carry
    }
    dmem = []
    memMod = 256
    pc = 0
    pcMod = 32
    regs = []
    regsNum = 32
    regsMod = 64

    # initialize the memory and registers
    def __init__(self, dmem=[], regsNum=32, dmemNum=256):
        if dmem == []:
            self.dmem = [0 for _ in range(dmemNum)]
        else:
            self.dmem = dmem
        self.regsNum = regsNum
        self.regs = [0 for _ in range(regsNum)]

    # run once a cycle to clean up register values
    def clean(self):
        for i in range(self.regsNum):
            self.regs[i] = self.regs[i] % 2**self.regsMod

        self.regs[31] = 0

        for i in range(len(self.dmem)):
            self.dmem[i] = self.dmem[i] % self.memMod

    def dmem_read(self, addr, offset, size):
        index = addr + offset
        value = 0
        for i in range(size):
            value += self.dmem[index+(i)] << 8*i
        return value
    
    def dmem_write(self, value, addr, offset, size):
        index = addr + offset
        for i in range(size):
            self.dmem[index+(i)] = (value >> 8*i) & (self.memMod - 1)

    def regs_read(self, reg):
        reg = reg.upper()
        if   reg == "SP":
            reg = "X28"
        elif reg == "FP":
            reg = "X29"
        elif reg == "LR":
            reg = "X30"
        elif reg == "XZR":
            reg = "X31"

        return self.regs[int(reg[1:])]
    
    def regs_write(reg, value):
        reg = reg.upper()
        if   reg == "SP":
            reg = "X28"
        elif reg == "FP":
            reg = "X29"
        elif reg == "LR":
            reg = "X30"
        elif reg == "XZR":
            reg = "X31"

        self.regs[int(reg[1:])] = value % self.regsMod

def printMem(mem):
    regs = mem.regs
    print(f'Registers:')
    for i in range(8):
        i *= 4
        regstr = ""
        for j in range(4):
            regstr += f' X{i+j:2}: ' + f'{regs[i+j]:016x}'[:8].replace('0','-') + \
                " " + f'{regs[i+j]:016x}'[8:].replace('0','-')
        print(regstr)

    print(f'Memory: ')
    width = 32
    length = int(len(mem.dmem)/width)
    for i in range(length):
        i *= width
        memstr = ""
        for j in range(width-1,-1,-1):
            memstr += f'{mem.dmem[i+j]:02x}'.replace('0','-')
            if (j) % 4 == 0:
                memstr += " "
            if (j) % 8 == 0:
                memstr += " "
        print(f' {i+width-1:2x}-{i:2x}: {memstr}')