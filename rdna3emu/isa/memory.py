import numpy as np


class Memory:
    def __init__(self, size=2**32):
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
    def global_load_u8(self, address):
        return self.get_global_memory(address, 1)

    # Untyped buffer load signed byte, sign extend in data register.
    def global_load_i8(self, address):
        return np.int8(self.get_global_memory(address, 1))

    # Untyped buffer load unsigned short, zero extend in data register.
    def global_load_u16(self, address):
        return self.get_global_memory(address, 2)

    # Untyped buffer load signed short, sign extend in data register.
    def global_load_i16(self, address):
        return np.int16(self.get_global_memory(address, 2))

    # Untyped buffer load dword.
    def global_load_b32(self, address):
        return self.get_global_memory(address, 4)

    # Untyped buffer load 2 dwords
    def global_load_b64(self, address):
        return self.get_global_memory(address, 8)

    # Untyped buffer load 3 dwords
    def global_load_b128(self, address):
        return self.get_global_memory(address, 16)

    # Untyped buffer load 4 dwords
    def global_load_b256(self, address):
        return self.get_global_memory(address, 32)

    # Untyped buffer store byte.
    def global_store_b8(self, address, value: np.uint8):
        self.set_memory(address, 1, value)

    # Untyped buffer store short.
    def global_store_b16(self, address, value: np.uint16):
        self.set_memory(address, 2, value)

    # Untyped buffer store dword.
    def global_store_b32(self, address, value: np.uint32):
        self.set_memory(address, 4, value)

    # Untyped buffer store 2 dwords.
    # Values is an array of 2 dwords.
    def global_store_b64(self, address, values: np.ndarray):
        values = values.astype(np.uint64)
        # Sanity check the size of the array
        if len(values) != 2:
            raise Exception("Invalid array size")
        for i in range(len(values)):
            self.set_memory(address + i * 4, 4, values[i])

    # Untyped buffer store 3 dwords.
    def global_store_b128(self, address, values: np.ndarray):
        values = values.astype(np.uint64)
        # Sanity check the size of the array
        if len(values) != 3:
            raise Exception("Invalid array size")
        for i in range(len(values)):
            self.set_memory(address + i * 4, 4, values[i])

    # Untyped buffer store 4 dwords.
    def global_store_b256(self, address, values: np.ndarray):
        values = values.astype(np.uint64)
        # Sanity check the size of the array
        if len(values) != 4:
            raise Exception("Invalid array size")
        for i in range(len(values)):
            self.set_memory(address + i * 4, 4, values[i])
