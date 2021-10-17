
class mem:
    flags = {
        'N': 0, # negative
        'Z': 0, # zero
        'V': 0, # overflow
        'C': 0  # carry
    }
    dmem = []
    memMod = 8
    pc = 0
    pcMod = 32
    regs = []
    regsNum = 32
    regsMod = 32

    # initialize the memory and registers
    def __init__(self, dmem=[], regsNum=32):
        if dmem == []:
            self.dmem = [0 for _ in range(256)]
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
            self.dmem[i] = self.dmem[i] % 8