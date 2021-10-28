
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
        return self.regs[int(reg[1:])]
    
    def regs_write(self, reg, value):
        self.regs[int(reg[1:])] = value % 2**self.regsMod

    def print(self):
        regs = self.regs
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
        length = int(len(self.dmem)/width)
        for i in range(length):
            i *= width
            memstr = ""
            for j in range(width-1,-1,-1):
                memstr += f'{self.dmem[i+j]:02x}'.replace('0','-')
                if (j) % 4 == 0:
                    memstr += " "
                if (j) % 8 == 0:
                    memstr += " "
            print(f' {i+width-1:2x}-{i:2x}: {memstr}')