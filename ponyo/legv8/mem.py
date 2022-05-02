
class mem:
    """Memory class for the LEGv8 ISA
    """

    flags = {
        'N': 0, # negative
        'Z': 0, # zero
        'V': 0, # overflow
        'C': 0  # carry
    }
    dmem = []
    pc = 0
    regs = []

    # Constants
    MEM_MOD = 256
    PC_MOD = 32
    REGS_NUM = 32
    REGS_MOD = 64

    # initialize the memory and registers
    def __init__(self, dmem: list = [], dmem_num: int = 512):
        """Initialize the memory

        Args:
            dmem (list, optional): Initial data memory. Defaults to [].
            dmem_num (int, optional): Length of zeroed data memory when `dmem` is default. Defaults to 512.
        """
        if dmem == []:
            self.dmem = [0 for _ in range(dmem_num)]
        else:
            self.dmem = dmem

        self.regs = [0 for _ in range(self.REGS_NUM)]

        self.dmem_orig = self.dmem[:]
        self.regs_orig = self.regs[:]

    def dmem_read(self, addr: int, offset: int, size: int) -> int:
        """Read from data memory

        Args:
            addr (int): Address to start from
            offset (int): Offset from address
            size (int): Number of bytes to read

        Returns:
            int: Value stored in data memory
        """
        index = addr + offset
        value = 0
        for i in range(size):
            value += self.dmem[index+(i)] << 8*i
        return value
    
    def dmem_write(self, value: int, addr: int, offset: int, size: int):
        """Write to data memory

        Args:
            value (int): Value to be stored
            addr (int): Address to start from
            offset (int): Offset from address
            size (int): Number of bytes to write
        """
        index = addr + offset
        for i in range(size):
            self.dmem[index+(i)] = (value >> 8*i) & (self.MEM_MOD - 1)

    def regs_read(self, reg: str) -> int:
        """Read the value stored in a register

        Args:
            reg (str): Register string (e.g. `X9`, `X11`)

        Returns:
            int: Value stored in register
        """
        return self.regs[int(reg[1:])]
    
    def regs_write(self, reg: str, value: int):
        """Write a value to a register

        Args:
            reg (str): Register string (e.g. `X9`, `X11`)
            value (int): Value to store
        """
        self.regs[int(reg[1:])] = value % 2**self.REGS_MOD

    def print(self):
        """Prints the data in the registers and memory to stdout
        """
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
        print(self.mem2str())

    def mem2str(self) -> str:
        """For GUI, returns a string of the values stored in memory

        Returns:
            str: Formatted memory values
        """
        out = []
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
            out.append(f' {i+width-1:3x}-{i:3x}: {memstr}')
        return '\n'.join(out)

    def reg2str(self) -> str:
        """For GUI, returns a string of the values stored in registers

        Returns:
            str: Formatted register values
        """
        regs = self.regs
        out = []
        for i in range(32):
            regstr = f' X{i:2}: ' + f'{regs[i]:032x}'.replace('0','-')
            out.append(regstr)
        return '\n'.join(out)

    def pcfl2str(self) -> str:
        """For GUI, returns a string of the values stored in PC and flags

        Returns:
            str: Formatted PC and flag values
        """
        pc = self.pc
        flags = self.flags
        return f'PC: {pc}, Negative: {flags["N"]}, Zero: {flags["Z"]}, Overflow: {flags["V"]}, Carry: {flags["C"]}'

    def reset(self):
        """Resets the memory to initialized values
        """
        self.dmem = self.dmem_orig[:]
        self.regs = self.regs_orig[:]
        self.pc = 0
        self.flags = {
            'N': 0,  # negative
            'Z': 0,  # zero
            'V': 0,  # overflow
            'C': 0  # carry
        }