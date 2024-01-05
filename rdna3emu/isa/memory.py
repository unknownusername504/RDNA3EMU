import numpy as np

from rdna3emu.isa.registers import Registers as Re


class Memory:
    def __init__(self, registers: Re, size=2**64):
        self.reset(registers, size)

    def reset(self, registers: Re, size=2**64):
        self.registers = registers
        self.size = size
        # Create the memory structure as a dictionary of 32-bit values
        self.data = {}

        self.legal_sizes = [1, 2, 4, 8, 16, 32]

        # Track the memory accesses
        self.accesses = set()

    def print_global_memory_location(self, address, size):
        if size == 8:
            value_hi = self.get_global_memory(address, 4)
            value_lo = self.get_global_memory(address + 4, 4)
            value = value_hi << 32 | value_lo
            print(f"Address: {address:#x} Value: {value:#x}")
        else:
            value = self.get_global_memory(address, size)
            print(f"Address: {address:#x} Value: {value:#x}")

    def dump_memory(self, non_zero=False):
        # Lambda function to output to file using the same format as the print statements
        # fprint = lambda x: print(x, file=open("memory.txt", "a"))
        print("==== Memory: ====")
        # Sort the accesses by address
        # Use local because it changes self.accesses to a list
        accesses = sorted(self.accesses)
        for access in accesses:
            # Read the current value given the address and size
            value = self.get_memory(access, 4)
            if non_zero and value == 0:
                continue
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
        if not isinstance(size, int):
            raise Exception("Invalid memory access size type")

        # Check that the address is within the memory range
        if address < 0 or address > self.size:
            raise Exception(f"Invalid memory access address {address:#x} is invalid")

        # Check that the size is valid
        if size not in self.legal_sizes:
            raise Exception("Invalid memory access size")

        # Align the address to the payload size
        return address & (~(size - 1))

    # Write to the memory structure
    def set_memory(self, address, size, value):
        address = self.sanitize_address(address, size)
        if size == 1:
            # Word aligned
            word_address = address // 4
            # Check if the word exists
            if word_address not in self.data:
                self.data[word_address] = 0
            byte_offset = address % 4
            word = self.data[word_address]
            # Clear the byte
            word &= ~(0xFF << (byte_offset * 8))
            # Set the byte
            word |= (value & 0xFF) << (byte_offset * 8)
            # Check if the word is zero and delete it if it is
            if word == 0:
                del self.data[word_address]
            else:
                self.data[word_address] = word
        elif size == 2:
            # Word aligned
            word_address = address // 4
            # Check if the word exists
            if word_address not in self.data:
                self.data[word_address] = 0
            byte_offset = address % 4
            word = self.data[word_address]
            # Clear the byte
            word &= ~(0xFFFF << (byte_offset * 8))
            # Set the byte
            word |= (value & 0xFFFF) << (byte_offset * 8)
            # Check if the word is zero and delete it if it is
            if word == 0:
                del self.data[word_address]
            else:
                self.data[word_address] = word
        else:
            # Split the value into words
            num_words = size // 4
            for i in range(num_words):
                word_address = (address // 4) + i
                word = (value >> (i * 32)) & 0xFFFFFFFF
                # Check if the word is zero and delete it if it is
                if word == 0:
                    if word_address in self.data:
                        del self.data[word_address]
                else:
                    self.data[word_address] = word

    # Write to the memory structure
    def get_memory(self, address, size):
        address = self.sanitize_address(address, size)
        if size == 1:
            # Word aligned
            word_address = address // 4
            # Check if the word exists
            if word_address not in self.data:
                return 0
            byte_offset = address % 4
            word = self.data[word_address]
            return (word >> (byte_offset * 8)) & 0xFF
        elif size == 2:
            # Word aligned
            word_address = address // 4
            # Check if the word exists
            if word_address not in self.data:
                return 0
            byte_offset = address % 4
            word = self.data[word_address]
            return (word >> (byte_offset * 8)) & 0xFFFF
        else:
            # Combine the words
            num_words = size // 4
            value = 0
            for i in range(num_words):
                word_address = (address // 4) + i
                # Check if the word exists
                if word_address not in self.data:
                    continue
                value |= self.data[word_address] << (i * 32)
            return value

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
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)

        address = reg_v0_value + reg_s0_value + reg_s1_value + offset

        reg_d_value = self.get_global_memory(address, 4)
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Global: use the SGPR to provide a base address and the VGPR provides a 32-bit byte offset.
    def global_load_b128(
        self, reg_d3, reg_d2, reg_d1, reg_d0, regv_offset, reg_s_hi, reg_s_lo, offset=0
    ):
        reg_s_lobits = format(self.registers.sgpr_u32(reg_s_lo), "032b")
        reg_s_hibits = format(self.registers.sgpr_u32(reg_s_hi), "032b")
        voffset = self.registers.vgpr_u32(regv_offset)
        addr = int(reg_s_hibits + reg_s_lobits, 2) + voffset + offset
        val = self.get_global_memory(addr, 16)
        val_bits = format(val, "0128b")
        val_1lobits = int(val_bits[0:32], 2)
        val_1hibits = int(val_bits[32:64], 2)
        val_2lobits = int(val_bits[64:96], 2)
        val_2hibits = int(val_bits[96:128], 2)
        self.registers.set_vgpr_u32(reg_d0, val_1lobits)
        self.registers.set_vgpr_u32(reg_d1, val_1hibits)
        self.registers.set_vgpr_u32(reg_d2, val_2lobits)
        self.registers.set_vgpr_u32(reg_d3, val_2hibits)

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
    # global_store_b32 v1, v0, s[0:1]
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

        address = (reg_s0_value << 32) | reg_s1_value
        address += reg_v0_value + offset

        self.set_global_memory(address, 4, reg_d_value)

    # global_store_b64 v[0:1], v[2:3], off
    def global_store_b64(self, reg_d0, reg_d1, reg_v0, reg_v1, offset=0):
        if not isinstance(offset, int):
            offset = int(offset)
            # Print a warning
            print("Warning: Offset is not an integer")
        reg_d0_value = self.registers.vgpr_u32(reg_d0)
        reg_d1_value = self.registers.vgpr_u32(reg_d1)
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_v1_value = self.registers.vgpr_u32(reg_v1)

        address = (reg_v0_value << 32) | reg_v1_value
        address += offset

        self.set_global_memory(address, 4, reg_d0_value)
        self.set_global_memory(address + 4, 4, reg_d1_value)

    def global_preload_b64(self, data, offset):
        # print("global_preload_b64", "\ndata:", data, "\noffset:", offset)
        if not isinstance(offset, int):
            offset = int(offset)
            # Print a warning
            print("Warning: Offset is not an integer")
        address = offset
        data_bits = format(data, "064b")
        data_0 = int(data_bits[0:32], 2)
        data_1 = int(data_bits[32:64], 2)
        self.set_global_memory(address, 4, data_0)
        self.set_global_memory(address + 4, 4, data_1)

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

    def ds_load_b128(self, reg_d3, reg_d2, reg_d1, reg_d0, reg_s0, offset=0):
        if not isinstance(offset, int):
            offset = int(offset)
            # Print a warning
            print("Warning: Offset is not an integer")
        reg_s_value = self.registers.vgpr_u32(reg_s0)
        addr = reg_s_value + offset

        val = self.get_local_memory(addr, 16)
        val_bits = format(val, "0128b")
        val_1lobits = int(val_bits[0:32], 2)
        val_1hibits = int(val_bits[32:64], 2)
        val_2lobits = int(val_bits[64:96], 2)
        val_2hibits = int(val_bits[96:128], 2)
        self.registers.set_sgpr_u32(reg_d0, val_1lobits)
        self.registers.set_sgpr_u32(reg_d1, val_1hibits)
        self.registers.set_sgpr_u32(reg_d2, val_2lobits)
        self.registers.set_sgpr_u32(reg_d3, val_2hibits)

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
        print(address)

        self.set_local_memory(address, 4, reg_s0_value)
