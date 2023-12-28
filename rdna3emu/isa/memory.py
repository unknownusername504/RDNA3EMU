import numpy as np
import sys

# Add rdna3emu to path
sys.path.append("../rdna3emu/")
from rdna3emu.isa.registers import Registers as Re


class Memory:
    def __init__(self, registers: Re, size=2**32):
        self.registers = registers
        self.size = size
        self.data = bytearray(size)
        self._data = np.zeros(size, dtype=np.uint8)
        self._data[:] = self.data[:]
        self._data = self._data.view(dtype=np.uint32)
        self._data = self._data.reshape(size // 4)

        self.legal_sizes = [1, 2, 4, 8, 16, 32]

    def is_global(self, address):
        #  Addr[48] == 0
        return ((address >> 48) & 0x1) == 0

    def is_private(self, address):
        #  Addr[48] == 1, Addr[47] == 0, Addr[46] == 0
        return (
            ((address >> 48) & 0x1) == 1
            and ((address >> 47) & 0x1) == 0
            and ((address >> 46) & 0x1) == 0
        )

    def is_shared(self, address):
        #  Addr[48] == 1, Addr[47] == 0, Addr[46] == 1
        return (
            ((address >> 48) & 0x1) == 1
            and ((address >> 47) & 0x1) == 0
            and ((address >> 46) & 0x1) == 1
        )

    def is_invalid(self, address):
        #  Addr[48] == 1, Addr[47] == 1
        return ((address >> 48) & 0x1) == 1 and ((address >> 47) & 0x1) == 1

    # Sanitize the address
    def sanitize_address(self, address, size):
        # Check if the address is valid
        if self.is_invalid(address):
            raise Exception("Invalid memory access")
        if size == 1:
            return address
        elif size in self.legal_sizes:
            return address & 0xFFFFFFFC
        else:
            raise Exception("Invalid memory access size")

    # Write to the memory structure
    def set_memory(self, address, size, value):
        address = self.sanitize_address(address, size)
        if size == 1:
            self.data[address] = value
        elif size == 2:
            self.data[address] = value & 0xFF
            self.data[address + 1] = (value >> 8) & 0xFF
        elif size in self.legal_sizes:
            self._data[address // 4] = value
        else:
            raise Exception("Invalid memory access size")

    # Write to the memory structure
    def get_memory(self, address, size):
        address = self.sanitize_address(address, size)
        if size == 1:
            return self.data[address]
        elif size == 2:
            return self.data[address] | (self.data[address + 1] << 8)
        elif size in self.legal_sizes:
            return self._data[address // 4]
        else:
            raise Exception("Invalid memory access size")

    def get_global_memory(self, address, size):
        # Check if the address is global
        if not self.is_global(address):
            raise Exception("Invalid memory access")
        return self.get_memory(address, size)

    # Multi dword access is handles currently as split dword accesses through the parsing phase

    # Untyped buffer load unsigned byte, zero extend in data register.
    def global_load_u8(self, reg_d, reg_s0, reg_s1, offset=0):
        reg_s0_value = self.registers.sgpr_u32(reg_s0) + offset
        reg_s1_value = self.registers.vgpr_u32(reg_s1)

        address = reg_s0_value + reg_s1_value

        reg_d_value = self.get_global_memory(address, 1)
        self.registers.set_vgpr_u8(reg_d, reg_d_value)

    # Untyped buffer load signed byte, sign extend in data register.
    def global_load_i8(self, reg_d, reg_s0, reg_s1, offset=0):
        reg_s0_value = self.registers.sgpr_u32(reg_s0) + offset
        reg_s1_value = self.registers.vgpr_u32(reg_s1)

        address = reg_s0_value + reg_s1_value

        reg_d_value = self.get_global_memory(address, 1)
        self.registers.set_vgpr_i8(reg_d, reg_d_value)

    # Untyped buffer load unsigned short, zero extend in data register.
    def global_load_u16(self, reg_d, reg_s0, reg_s1, offset=0):
        reg_s0_value = self.registers.sgpr_u32(reg_s0) + offset
        reg_s1_value = self.registers.vgpr_u32(reg_s1)

        address = reg_s0_value + reg_s1_value

        reg_d_value = self.get_global_memory(address, 2)
        self.registers.set_vgpr_u16(reg_d, reg_d_value)

    # Untyped buffer load signed short, sign extend in data register.
    def global_load_i16(self, reg_d, reg_s0, reg_s1, offset=0):
        reg_s0_value = self.registers.sgpr_u32(reg_s0) + offset
        reg_s1_value = self.registers.vgpr_u32(reg_s1)

        address = reg_s0_value + reg_s1_value

        reg_d_value = self.get_global_memory(address, 2)
        self.registers.set_vgpr_i16(reg_d, reg_d_value)

    # Untyped buffer load dword.
    def global_load_b32(self, reg_d, reg_s0, reg_s1, offset=0):
        reg_s0_value = self.registers.sgpr_u32(reg_s0) + offset
        reg_s1_value = self.registers.vgpr_u32(reg_s1)

        address = reg_s0_value + reg_s1_value

        reg_d_value = self.get_global_memory(address, 4)
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Untyped buffer store byte.
    def global_store_b8(self, reg_d, reg_s0, reg_s1, offset=0):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.vgpr_u32(reg_s1) + offset

        address = reg_s0_value + reg_s1_value

        value = self.registers.vgpr_u8(reg_d)
        self.set_memory(address, 1, value)

    # Untyped buffer store short.
    def global_store_b16(self, reg_d, reg_s0, reg_s1, offset=0):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.vgpr_u32(reg_s1) + offset

        address = reg_s0_value + reg_s1_value

        value = self.registers.vgpr_u16(reg_d)
        self.set_memory(address, 2, value)

    # Untyped buffer store dword.
    def global_store_b32(self, reg_d, reg_s0, reg_s1, offset=0):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.vgpr_u32(reg_s1) + offset

        address = reg_s0_value + reg_s1_value

        value = self.registers.vgpr_u32(reg_d)
        self.set_memory(address, 4, value)
