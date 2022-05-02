class mem:
    """Memory class for the EccCPU ISA"""

    flags = {"z": 0, "n": 0, "c": 0, ">u": 0, "<u": 0, "=": 0, ">s": 0, "<s": 0}
    ram = []
    pc = 0
    regs = []

    RAM_MOD = 8
    ADDR_MOD = 4
    PC_MOD = 8
    REGS_NUM = 4
    REGS_MOD = 8

    # initialize the memory and registers
    def __init__(self, dmem=[], dmemNum=16):
        """Init the memory

        Args:
            dmem (list, optional): Initial ram. Defaults to [].
            dmemNum (int, optional): Length of zeroed ram when `dmem` is default. Defaults to 16.
        """
        if dmem == []:
            self.ram = [0 for _ in range(dmemNum)]
        else:
            self.ram = dmem
        self.regs = [0 for _ in range(self.REGS_NUM)]

        self.ram_orig = self.ram[:]
        self.regs_orig = self.regs[:]

    def ram_read(self, addr: int) -> int:
        """Read from ram

        Args:
            addr (int): Byte-address to read from

        Returns:
            int: Stored value
        """
        return self.ram[int(addr) % 2**self.ADDR_MOD] % 2**self.RAM_MOD

    def ram_write(self, value: int, addr: int):
        """Write to ram

        Args:
            value (int): Value to be stored
            addr (int): Byte-address to store at
        """
        # print(f"{addr=}, {value=}")
        self.ram[int(addr) % 2**self.ADDR_MOD] = int(value) % 2**self.RAM_MOD

    def regs_read(self, reg: str) -> int:
        """Read the value stored in a register

        Args:
            reg (str): Register string (e.g. `r9`, `1`)

        Returns:
            int: Value stored in register
        """
        if reg[0] == "r":
            reg = int(reg[1:])
        return self.regs[int(reg)] % 2**self.REGS_MOD

    def regs_write(self, reg: str, value: int):
        """Write a value to a register

        Args:
            reg (str): Register string (e.g. `r9`, `1`)
            value (int): Value to store
        """
        if reg[0] == "r":
            reg = int(reg[1:])
        self.regs[int(reg)] = int(value) % 2**self.REGS_MOD

    def print(self):
        """Prints the data in the registers and memory to stdout"""

        print("Flags:")
        print(self.pcfl2str())

        print(f"Registers:")
        print(self.reg2str())

        print(f"Memory: ")
        print(self.mem2str())

    def mem2str(self):
        """For GUI, returns a string of the values stored in memory

        Returns:
            str: Formatted memory values
        """
        out = []
        width = 4
        length = int(len(self.ram) / width)
        for i in range(length):
            i *= width
            memstr = ""
            for j in range(width - 1, -1, -1):
                memstr += f"{self.ram[i+j]:02x}".replace("0", "-")
                if (j) % 1 == 0:
                    memstr += " "
                if (j) % 2 == 0:
                    memstr += " "
            out.append(f" {i+width-1:1x}-{i:1x}: {memstr}")
        return "\n".join(out)

    def reg2str(self):
        """For GUI, returns a string of the values stored in registers

        Returns:
            str: Formatted register values
        """
        out = []
        regs = self.regs
        for i in range(2):
            i *= 2
            regstr = ""
            for j in range(2):
                regstr += f" r{i+j:1}: " + f"{regs[i+j]:02x}"[:8].replace("0", "-")
            out.append(regstr)
        return "\n".join(out)

    def pcfl2str(self):
        """For GUI, returns a string of the values stored in PC and flags

        Returns:
            str: Formatted PC and flag values
        """
        out = [f"PC: {self.pc}"]
        for k, v in self.flags.items():
            out.append(f"{k}: {v}")
        return ", ".join(out)

    def reset(self):
        """Resets the memory to initialized values"""
        self.ram = self.ram_orig[:]
        self.regs = self.regs_orig[:]
        self.pc = 0
        self.flags = {
            "z": 0,
            "n": 0,
            "c": 0,
            ">u": 0,
            "<u": 0,
            "=": 0,
            ">s": 0,
            "<s": 0,
        }
