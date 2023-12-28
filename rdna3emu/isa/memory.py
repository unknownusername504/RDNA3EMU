import numpy as np
import sys

# Add rdna3emu to path
# sys.path.append("../rdna3emu/")
from rdna3emu.isa.registers import Registers as Re


class Memory:
    def __init__(self, registers: Re, size=2**32):
        self.registers = registers
        self.size = size
        self.data = bytearray(size)
        self._data = np.zeros(size, dtype=np.uint8)
        # CAUSING SOME KIND OF OOM and crashes vscode
        # self._data[:] = self.data[:]
        # self._data = self._data.view(dtype=np.uint32)
        # self._data = self._data.reshape(size // 4)

        self.legal_sizes = [1, 2, 4, 8, 16, 32]

        # Track the memory accesses
        self.accesses = set()

    def dump_memory(self):
        print("==== Memory: ====")
        # Sort the accesses by address
        self.accesses = sorted(self.accesses)
        for access in self.accesses:
            # Read the current value given the address and size
            value = self.get_memory(access, 4)
            print(f"Address: {access:#x} Value: {value:#x}")

    def add_access(self, address, size):
        # Add the access to the set and if size > 4 add the next address
        self.accesses.add(address)
        while size > 4:
            address += 4
            self.accesses.add(address)
            size -= 4

    def flat_is_global(self, address):
        #  Addr[48] == 0
        return ((address >> 48) & 0x1) == 0

    def flat_is_private(self, address):
        #  Addr[48] == 1, Addr[47] == 0, Addr[46] == 0
        return (
            ((address >> 48) & 0x1) == 1
            and ((address >> 47) & 0x1) == 0
            and ((address >> 46) & 0x1) == 0
        )

    def flat_is_shared(self, address):
        #  Addr[48] == 1, Addr[47] == 0, Addr[46] == 1
        return (
            ((address >> 48) & 0x1) == 1
            and ((address >> 47) & 0x1) == 0
            and ((address >> 46) & 0x1) == 1
        )

    def flat_is_invalid(self, address):
        #  Addr[48] == 1, Addr[47] == 1
        return ((address >> 48) & 0x1) == 1 and ((address >> 47) & 0x1) == 1

    # Sanitize the address
    def sanitize_address(self, address, size):
        # Check that the address is a valid integer
        if not isinstance(address, int):
            raise Exception("Invalid memory access address type")
        # Check that the address is within the memory range
        if address < 0 or address > self.size:
            raise Exception(f"Invalid memory access address {address:#x} is invalid")
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
        self.add_access(address, size)

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
        return self.get_memory(address, size)

    def set_global_memory(self, address, size, value):
        self.set_memory(address, size, value)

    def get_local_memory(self, address, size):
        return self.get_memory(address, size)

    def set_local_memory(self, address, size, value):
        self.set_memory(address, size, value)

    # Multi dword access is handles currently as split dword accesses through the parsing phase

    # Untyped buffer load unsigned byte, zero extend in data register.
    def global_load_u8(self, reg_d, reg_v0, reg_s0, reg_s1, offset=0):
        reg_d_value = self.registers.vgpr_u32(reg_d)
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)

        address = reg_v0_value + reg_s0_value + reg_s1_value + offset

        reg_d_value = self.get_global_memory(address, 1)
        self.registers.set_vgpr_u8(reg_d, reg_d_value)

    # Untyped buffer load signed byte, sign extend in data register.
    def global_load_i8(self, reg_d, reg_v0, reg_s0, reg_s1, offset=0):
        reg_d_value = self.registers.vgpr_u32(reg_d)
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)

        address = reg_v0_value + reg_s0_value + reg_s1_value + offset

        reg_d_value = self.get_global_memory(address, 1)
        self.registers.set_vgpr_u8(reg_d, reg_d_value)

    # Untyped buffer load unsigned short, zero extend in data register.
    def global_load_u16(self, reg_d, reg_v0, reg_s0, reg_s1, offset=0):
        reg_d_value = self.registers.vgpr_u32(reg_d)
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)

        address = reg_v0_value + reg_s0_value + reg_s1_value + offset

        reg_d_value = self.get_global_memory(address, 2)
        self.registers.set_vgpr_u16(reg_d, reg_d_value)

    # Untyped buffer load signed short, sign extend in data register.
    def global_load_i16(self, reg_d, reg_v0, reg_s0, reg_s1, offset=0):
        reg_d_value = self.registers.vgpr_u32(reg_d)
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)

        address = reg_v0_value + reg_s0_value + reg_s1_value + offset

        reg_d_value = self.get_global_memory(address, 2)
        self.registers.set_vgpr_u16(reg_d, reg_d_value)

    # Load 32-bit data from a given memory location into a vector register.
    def global_load_b32(self, reg_d, reg_v0, reg_s0, reg_s1, offset=0):
        # Force the offset to be an integer for now since that is not handled in the parser correctly
        if not isinstance(offset, int):
            offset = int(offset)
            # Print a warning
            print("Warning: Offset is not an integer")
        reg_d_value = self.registers.vgpr_u32(reg_d)
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)

        address = reg_v0_value + reg_s0_value + reg_s1_value + offset

        reg_d_value = self.get_global_memory(address, 4)
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Untyped buffer store byte.
    def global_store_u8(self, reg_d, reg_v0, reg_s0, reg_s1, offset=0):
        reg_d_value = self.registers.vgpr_u8(reg_d)
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        address = reg_v0_value + reg_s0_value + reg_s1_value + offset

        self.set_global_memory(address, 1, reg_d_value)

    # Signed byte store.
    def global_store_i8(self, reg_d, reg_v0, reg_s0, reg_s1, offset=0):
        reg_d_value = self.registers.vgpr_i8(reg_d)
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        address = reg_v0_value + reg_s0_value + reg_s1_value + offset

        self.set_global_memory(address, 1, reg_d_value)

    # Untyped buffer store short.
    def global_store_u16(self, reg_d, reg_v0, reg_s0, reg_s1, offset=0):
        reg_d_value = self.registers.vgpr_u16(reg_d)
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        address = reg_v0_value + reg_s0_value + reg_s1_value + offset

        self.set_global_memory(address, 2, reg_d_value)

    # Signed short store.
    def global_store_i16(self, reg_d, reg_v0, reg_s0, reg_s1, offset=0):
        reg_d_value = self.registers.vgpr_i16(reg_d)
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        address = reg_v0_value + reg_s0_value + reg_s1_value + offset

        self.set_global_memory(address, 2, reg_d_value)

    # Store 32-bit data from a vector register into a given memory location.
    def global_store_b32(self, reg_d, reg_v0, reg_s0, reg_s1, offset=0):
        # Force the offset to be an integer for now since that is not handled in the parser correctly
        if not isinstance(offset, int):
            offset = int(offset)
            # Print a warning
            print("Warning: Offset is not an integer")
        reg_d_value = self.registers.vgpr_u32(reg_d)
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)

        address = reg_v0_value + reg_s0_value + reg_s1_value + offset

        self.set_global_memory(address, 4, reg_d_value)

    # Store 32-bit data from a vector register into a given memory location.
    def ds_load_b32(self, reg_d, reg_s0, offset=0):
        # Force the offset to be an integer for now since that is not handled in the parser correctly
        if not isinstance(offset, int):
            offset = int(offset)
            # Print a warning
            print("Warning: Offset is not an integer")
        reg_d_value = self.registers.vgpr_u32(reg_d)

        address = reg_d_value + offset

        reg_s0_value = self.get_local_memory(address, 4)
        self.registers.set_vgpr_u32(reg_s0, reg_s0_value)

    # this instruction takes a 32-bit value from the register reg_s0 and stores it in the local data share at the address specified by the value in the register reg_d.
    def ds_store_b32(self, reg_d, reg_s0, offset=0):
        # Force the offset to be an integer for now since that is not handled in the parser correctly
        if not isinstance(offset, int):
            offset = int(offset)
            # Print a warning
            print("Warning: Offset is not an integer")
        reg_d_value = self.registers.vgpr_u32(reg_d)
        reg_s0_value = self.registers.vgpr_u32(reg_s0)

        address = reg_d_value + offset

        self.set_local_memory(address, 4, reg_s0_value)
