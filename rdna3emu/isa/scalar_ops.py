import rdna3emu.isa.utils as utils
from rdna3emu.isa.registers import Registers as Re


class ScalarOps:
    def __init__(self, registers: Re):
        self.registers = registers

    # SOP2 instructions
    # Add two unsigned inputs, store the result into a scalar register and store the carry-out bit into SCC.
    def s_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = reg_s0_value + reg_s1_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Subtract the second unsigned input from the first input, store the result into a scalar register and store the carry-out bit into SCC.
    def s_sub_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = reg_s0_value - reg_s1_value
        reg_scc_value = 1 if (reg_d_value < 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Add two signed inputs, store the result into a scalar register and store the carry-out bit into SCC.
    def s_add_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_i32(reg_s0)
        reg_s1_value = self.registers.sgpr_i32(reg_s1)
        reg_d_value = reg_s0_value + reg_s1_value
        sign = 1 if (reg_d_value < 0) else 0
        reg_scc_value = 1 if (sign != (reg_s0_value < 0)) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_i32(reg_d, reg_d_value)

    # Subtract the second signed input from the first input, store the result into a scalar register and store the carryout bit into SCC.
    def s_sub_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_i32(reg_s0)
        reg_s1_value = self.registers.sgpr_i32(reg_s1)
        reg_d_value = reg_s0_value - reg_s1_value
        sign = 1 if (reg_d_value < 0) else 0
        reg_scc_value = 1 if (sign != (reg_s0_value < 0)) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_i32(reg_d, reg_d_value)

    # Add two unsigned inputs and a carry-in bit, store the result into a scalar register and store the carry-out bit into SCC.
    def s_addc_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_scc_value = self.registers._status.scc
        ()
        reg_d_value = reg_s0_value + reg_s1_value + reg_scc_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Subtract the second unsigned input from the first input, subtract the carry-in bit, store the result into a scalar register and store the carry-out bit into SCC.
    def s_subb_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_scc_value = self.registers._status.scc
        ()
        reg_d_value = reg_s0_value - reg_s1_value - reg_scc_value
        reg_scc_value = 1 if (reg_d_value < 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Calculate the absolute value of difference between two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_absdiff_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_i32(reg_s0)
        reg_s1_value = self.registers.sgpr_i32(reg_s1)
        reg_d_value = abs(reg_s0_value - reg_s1_value)
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_i32(reg_d, reg_d_value)

    # Given a shift count in the second scalar input, calculate the logical shift left of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_lshl_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = reg_s0_value << reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Given a shift count in the second scalar input, calculate the logical shift left of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_lshl_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u64(reg_s0)
        reg_s1_value = self.registers.sgpr_u64(reg_s1)
        reg_d_value = reg_s0_value << reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u64(reg_d, reg_d_value)

    # Given a shift count in the second scalar input, calculate the logical shift right of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_lshr_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = reg_s0_value >> reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Given a shift count in the second scalar input, calculate the logical shift right of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_lshr_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u64(reg_s0)
        reg_s1_value = self.registers.sgpr_u64(reg_s1)
        reg_d_value = reg_s0_value >> reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u64(reg_d, reg_d_value)

    # Given a shift count in the second scalar input, calculate the arithmetic shift right (preserving sign bit) of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_ashr_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_i32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = reg_s0_value >> reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_i32(reg_d, reg_d_value)

    # Given a shift count in the second scalar input, calculate the arithmetic shift right (preserving sign bit) of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_ashr_i64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_i64(reg_s0)
        reg_s1_value = self.registers.sgpr_u64(reg_s1)
        reg_d_value = reg_s0_value >> reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_i64(reg_d, reg_d_value)

    # Calculate the logical shift left of the first input by 1, then add the second input, store the result into a scalar register and set SCC iff the summation results in an unsigned overflow.
    def s_lshl1_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = (reg_s0_value << 1) + reg_s1_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Calculate the logical shift left of the first input by 2, then add the second input, store the result into a scalar register and set SCC iff the summation results in an unsigned overflow.
    def s_lshl2_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = (reg_s0_value << 2) + reg_s1_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Calculate the logical shift left of the first input by 3, then add the second input, store the result into a scalar register and set SCC iff the summation results in an unsigned overflow.
    def s_lshl3_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = (reg_s0_value << 3) + reg_s1_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Calculate the logical shift left of the first input by 4, then add the second input, store the result into a scalar register and set SCC iff the summation results in an unsigned overflow.
    def s_lshl4_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sg
        reg_s1_value = self.registers.get_register(
            reg_s1, signed=False, size=32, reg_type="SGPR"
        )
        reg_d_value = (reg_s0_value << 4) + reg_s1_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_register(
            reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR"
        )

    # Select the minimum of two signed integers, store the selected value into a scalar register and set SCC iff the first value is selected.
    def s_min_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_i32(reg_s0)
        reg_s1_value = self.registers.sgpr_i32(reg_s1)
        reg_d_value = min(reg_s0_value, reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == reg_s0_value) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_i32(reg_d, reg_d_value)

    # Select the minimum of two unsigned integers, store the selected value into a scalar register and set SCC iff the first value is selected.
    def s_min_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = min(reg_s0_value, reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == reg_s0_value) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.sgpr_i32(reg_d, reg_d_value)

    # Select the maximum of two signed integers, store the selected value into a scalar register and set SCC iff the first value is selected.
    def s_max_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_i32(reg_s0)
        reg_s1_value = self.registers.sgpr_i32(reg_s1)
        reg_d_value = max(reg_s0_value, reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == reg_s0_value) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.sgpr_i32(reg_d, reg_d_value)

    # Select the maximum of two unsigned integers, store the selected value into a scalar register and set SCC iff the first value is selected.
    def s_max_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = max(reg_s0_value, reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == reg_s0_value) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.sgpr_i32(reg_d, reg_d_value)

    # Calculate bitwise AND on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_and_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = reg_s0_value & reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.sgpr_i32(reg_d, reg_d_value)

    # Calculate bitwise AND on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_and_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u64(reg_s0)
        reg_s1_value = self.registers.sgpr_u64(reg_s1)
        reg_d_value = reg_s0_value & reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.sgpr_i64(reg_d, reg_d_value)

    # Calculate bitwise OR on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_or_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = reg_s0_value | reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.sgpr_i32(reg_d, reg_d_value)

    # Calculate bitwise OR on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_or_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u64(reg_s0)
        reg_s1_value = self.registers.sgpr_u64(reg_s1)
        reg_d_value = reg_s0_value | reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.sgpr_i64(reg_d, reg_d_value)

    # Calculate bitwise XOR on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_xor_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = reg_s0_value ^ reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.sgpr_i32(reg_d, reg_d_value)

    # Calculate bitwise XOR on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_xor_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u64(reg_s0)
        reg_s1_value = self.registers.sgpr_u64(reg_s1)
        reg_d_value = reg_s0_value ^ reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.sgpr_i64(reg_d, reg_d_value)

    # Calculate bitwise NAND on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_nand_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = ~(reg_s0_value & reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Calculate bitwise NAND on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_nand_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u64(reg_s0)
        reg_s1_value = self.registers.sgpr_u64(reg_s1)
        reg_d_value = ~(reg_s0_value & reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u64(reg_d, reg_d_value)

    # Calculate bitwise NOR on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_nor_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = ~(reg_s0_value | reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Calculate bitwise NOR on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_nor_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u64(reg_s0)
        reg_s1_value = self.registers.sgpr_u64(reg_s1)
        reg_d_value = ~(reg_s0_value | reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u64(reg_d, reg_d_value)

    # Calculate bitwise XNOR on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_xnor_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = ~(reg_s0_value ^ reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Calculate bitwise XNOR on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_xnor_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u64(reg_s0)
        reg_s1_value = self.registers.sgpr_u64(reg_s1)
        reg_d_value = ~(reg_s0_value ^ reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u64(reg_d, reg_d_value)

    # Calculate bitwise AND with the first input and the negation of the second input, store the result into a scalar register and set SCC if the result is nonzero.
    def s_and_not1_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = reg_s0_value & ~reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Calculate bitwise AND with the first input and the negation of the second input, store the result into a scalar register and set SCC if the result is nonzero.
    def s_and_not1_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u64(reg_s0)
        reg_s1_value = self.registers.sgpr_u64(reg_s1)
        reg_d_value = reg_s0_value & ~reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u64(reg_d, reg_d_value)

    # Calculate bitwise OR with the first input and the negation of the second input, store the result into a scalar register and set SCC if the result is nonzero.
    def s_or_not1_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = reg_s0_value | ~reg_s1_value
        reg_scc_value = 1 if (reg_d_value != -1) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Calculate bitwise OR with the first input and the negation of the second input, store the result into a scalar register and set SCC if the result is nonzero.
    def s_or_not1_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u64(reg_s0)
        reg_s1_value = self.registers.sgpr_u64(reg_s1)
        reg_d_value = reg_s0_value | ~reg_s1_value
        reg_scc_value = 1 if (reg_d_value != -1) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u64(reg_d, reg_d_value)

    # Extract an unsigned bitfield from the first input using field offset and size encoded in the second input, store the result into a scalar register and set SCC iff the result is nonzero
    def s_bfe_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        # Field offset is [4:0] of reg_s1
        field_offset = reg_s1_value & 0x1F
        # Field size is [22:16] of reg_s1
        field_size = (reg_s1_value >> 16) & 0x7F
        reg_d_value = (reg_s0_value >> field_offset) & ((1 << field_size) - 1)
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Extract a signed bitfield from the first input using field offset and size encoded in the second input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_bfe_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_i32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        # Field offset is [4:0] of reg_s1
        field_offset = reg_s1_value & 0x1F
        # Field size is [22:16] of reg_s1
        field_size = (reg_s1_value >> 16) & 0x7F
        reg_d_value = (reg_s0_value >> field_offset) & ((1 << field_size) - 1)
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_i32(reg_d, reg_d_value)

    # Extract an unsigned bitfield from the first input using field offset and size encoded in the second input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_bfe_u64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u64(reg_s0)
        reg_s1_value = self.registers.sgpr_u64(reg_s1)
        # Field offset is [5:0] of reg_s1
        field_offset = reg_s1_value & 0x3F
        # Field size is [22:16] of reg_s1
        field_size = (reg_s1_value >> 16) & 0x7F
        reg_d_value = (reg_s0_value >> field_offset) & ((1 << field_size) - 1)
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_sgpr_u64(reg_d, reg_d_value)

    # Extract a signed bitfield from the first input using field offset and size encoded in the second input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_bfe_i64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(
            reg_s0, signed=True, size=64, reg_type="SGPR"
        )
        reg_s1_value = self.registers.get_register(
            reg_s1, signed=False, size=64, reg_type="SGPR"
        )
        # Field offset is [5:0] of reg_s1
        field_offset = reg_s1_value & 0x3F
        # Field size is [22:16] of reg_s1
        field_size = (reg_s1_value >> 16) & 0x7F
        reg_d_value = (reg_s0_value >> field_offset) & ((1 << field_size) - 1)
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        self.registers.set_register(
            reg_d, reg_d_value, signed=True, size=field_size, reg_type="SGPR"
        )

    # Calculate a bitfield mask given a field offset and size and store the result in a scalar register.
    def s_bfm_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        # Field offset is [4:0] of reg_s1
        field_offset = reg_s1_value & 0x1F
        # Field size is [4:0] of reg_s0
        field_size = reg_s0_value & 0x1F
        reg_d_value = ((1 << field_size) - 1) << field_offset
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Calculate a bitfield mask given a field offset and size and store the result in a scalar register.
    def s_bfm_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.set_sgpr_u64(reg_s0)
        reg_s1_value = self.registers.set_sgpr_u64(reg_s1)
        # Field offset is [5:0] of reg_s1
        field_offset = reg_s1_value & 0x3F
        # Field size is [5:0] of reg_s0
        field_size = reg_s0_value & 0x3F
        reg_d_value = ((1 << field_size) - 1) << field_offset
        self.registers.set_sgpr_u64(reg_d, reg_d_value)

    # Multiply two signed integers and store the result into a scalar register.
    def s_mul_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_i32(reg_s0)
        reg_s1_value = self.registers.sgpr_i32(reg_s1)
        reg_d_value = reg_s0_value * reg_s1_value
        self.registers.set_sgpr_i32(reg_d, reg_d_value)

    # Multiply two unsigned integers and store the high 32 bits of the result into a scalar register.
    def s_mul_hi_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = (reg_s0_value * reg_s1_value) >> 32
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Multiply two signed integers and store the high 32 bits of the result into a scalar register.
    def s_mul_hi_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_i32(reg_s0)
        reg_s1_value = self.registers.sgpr_i32(reg_s1)
        reg_d_value = (reg_s0_value * reg_s1_value) >> 32
        self.registers.set_sgpr_i32(reg_d, reg_d_value)

    # Select the first input if SCC is true otherwise select the second input, then store the selected input into a scalar register.
    def s_cselect_b32(self, reg_d, reg_s0, reg_s1):
        reg_scc_value = self.registers._status.scc
        ()
        reg_d_value = reg_s0 if reg_scc_value == 1 else reg_s1
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Select the first input if SCC is true otherwise select the second input, then store the selected input into a scalar register.
    def s_cselect_b64(self, reg_d, reg_s0, reg_s1):
        reg_scc_value = self.registers._status.scc
        ()
        reg_d_value = reg_s0 if reg_scc_value == 1 else reg_s1
        self.registers.set_sgpr_u64(reg_d, reg_d_value)

    # Pack two 16-bit scalar values into a scalar register.
    def s_pack_ll_b32_b16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u16(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = (reg_s1_value << 16) | reg_s0_value
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Pack two 16-bit scalar values into a scalar register.
    def s_pack_lh_b32_b16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u16(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = (reg_s1_value & 0xFFFF0000) | reg_s0_value
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Pack two 16-bit scalar values into a scalar register.
    def s_pack_hh_b32_b16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u16(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = (reg_s1_value & 0xFFFF0000) | (reg_s0_value >> 16)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Pack two 16-bit scalar values into a scalar register.
    def s_pack_hl_b32_b16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u16(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_d_value = (reg_s1_value << 16) | (reg_s0_value >> 16)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    def s_move_b32(self, reg_d, reg_s0):
        reg_s0_val = self.registers.sgpr_u32(reg_s0)
        self.registers.set_sgpr_u32(reg_d, reg_s0_val)

    # Move scalar input into a scalar register. (64-bit)
    def s_move_b64(self, reg_d, reg_s0):
        reg_s0_val = self.registers.sgpr_u64(reg_s0)
        self.registers.set_sgpr_u64(reg_d, reg_s0_val)

    # Move scalar input into a scalar register iff SCC is nonzero.
    def c_move_b32(self, reg_d, reg_s0):
        if self.registers._status.scc() == 1:
            self.s_move_b32(reg_d, reg_s0)

    def c_move_b64(self, reg_d, reg_s0):
        if self.registers._status.scc() == 1:
            self.s_move_b64(reg_d, reg_s0)

    # Reverse the order of bits in a scalar input and store the result into a scalar register.
    def s_brev_b32(self, reg_d, reg_s0):
        reg_s0_val = self.registers.sgpr_u32(reg_s0)
        tmp = utils.rev_b32(reg_s0_val)
        self.registers.set_sgpr_u32(reg_d, tmp)

    # Reverse the order of bits in a scalar input and store the result into a scalar register.
    def s_brev_b64(self, reg_d, reg_s0):
        reg_s0_val = self.registers.sgpr_u64(reg_s0)
        tmp = utils.rev_b64(reg_s0_val)
        self.registers.set_sgpr_u64(reg_d, tmp)

    # Count the number of trailing "0" bits before the first "1" in a scalar input and store the result into a scalar
    # register. Store -1 if there are no "1" bits in the input.
    def s_ctz_i32_b32(self, reg_d, reg_s0):
        reg_s0_val = self.registers.sgpr_u32(reg_s0)
        tmp = utils.ctz(reg_s0_val, 32)
        self.registers.sgpr_i32(reg_d, tmp)

    def s_ctz_i32_b64(self, reg_d, reg_s0):
        reg_s0_val = self.registers.sgpr_u64(reg_s0)
        tmp = utils.ctz(reg_s0_val, 64)
        self.registers.sgpr_i32(reg_d, tmp)

    def s_clz_i32_u32(self, reg_d, reg_s0):
        reg_s0_val = self.registers.get_register(reg_s0, signed=False, size=32)
        tmp = utils.clz(reg_s0_val, 32)
        self.registers.set_register(reg_d, tmp, signed=True, size=32)

    def s_clz_i32_u64(self, reg_d, reg_s0):
        reg_s0_val = self.registers.sgpr_u64(reg_s0)
        tmp = utils.clz(reg_s0_val, 64)
        self.registers.set_sgpr_i32(reg_d, tmp)

    def s_cls_i32(self, reg_d, reg_s0):
        reg_s0_val = self.registers.get_register(reg_s0, signed=False, size=32)
        tmp = utils.cls(reg_s0_val, 32)
        self.registers.set_sgpr_i32(reg_d, tmp)

    def s_cls_i32_i64(self, reg_d, reg_s0):
        reg_s0_val = self.registers.sgpr_i64(reg_s0)
        tmp = utils.cls(reg_s0_val, 64)
        self.registers.set_sgpr_i32(reg_d, tmp)

    # Sign extend an 8-bit scalar value to 32-bits
    def s_sext_i32_i8(self, reg_d, reg_s0):
        reg_s0_val = self.registers.sgpr_i8(reg_s0)
        tmp = utils.sext_i32(reg_s0_val, 8)
        self.registers.set_sgpr_i32(reg_d, tmp)

    # Sign extend an 16-bit scalar value to 32-bits
    def s_sext_i32_i16(self, reg_d, reg_s0):
        reg_s0_val = self.registers.sgpr_i16(reg_s0)
        tmp = utils.sext_i32(reg_s0_val, 16)
        self.registers.set_sgpr_i32(reg_d, tmp)

    # Set bit to 0 at offset (reg_s0) in reg_d
    def s_bitset0_b32(self, reg_d, reg_s0):
        offset = self.registers.sgpr_u32(reg_s0)
        reg_d_val = self.registers.sgpr_u32(reg_d)
        tmp = utils.bitset0(reg_d_val, offset)
        self.registers.set_sgpr_u32(reg_d, tmp)

    def s_bitset0_b64(self, reg_d, reg_s0):
        offset = self.registers.sgpr_u64(reg_s0)
        reg_d_val = self.registers.sgpr_u64(reg_d)
        tmp = utils.bitset0(reg_d_val, offset)
        self.registers.set_sgpr_u64(reg_d, tmp)

    def s_bitset1_b32(self, reg_d, reg_s0):
        offset = self.registers.sgpr_u32(reg_s0)
        reg_d_val = self.registers.sgpr_u32(reg_d)
        tmp = utils.bitset1(reg_d_val, offset)
        self.registers.set_sgpr_u32(reg_d, tmp)

    def s_bitset1_b64(self, reg_d, reg_s0):
        offset = self.registers.sgpr_u64(reg_s0)
        reg_d_val = self.registers.sgpr_u64(reg_d)
        tmp = utils.bitset1(reg_d_val, offset)
        self.registers.set_sgpr_u64(reg_d, tmp)

    # Substitute each bit of a 32 bit scalar input with two instances of itself and store the result into a 64 bit scalar
    # register.
    def s_bitreplicate_b64_b32(self, reg_d, reg_s0):
        reg_s0_val = self.registers.sgpr_u32(reg_s0)
        tmp = utils.bitreplicate(reg_s0_val)
        self.registers.set_sgpr_u64(reg_d, tmp)

    # Compute the absolute value of a scalar input, store the result into a scalar register and set SCC iff the result is
    # nonzero.
    def s_abs_i32(self, reg_d, reg_s0):
        reg_s0_val = self.registers.sgpr_i32(reg_s0)
        tmp = abs(reg_s0_val)
        self.registers.set_sgpr_i32(reg_d, tmp)
        self.registers._status.set_scc(0 if tmp != 0 else 1)

    # count the number of bits set to 0 in a scalar input and store the result into a scalar register.
    def s_bcnt0_i32_b32(self, reg_d, reg_s0):
        value = self.registers.sgpr_u32(reg_s0)
        count_of_zero_bits = utils.count_zero_bits(value, 32)
        self.registers.set_sgpr_i32(reg_d, count_of_zero_bits)
        self.registers._status.set_scc(1 if count_of_zero_bits != 0 else 0)

    # count the number of bits set to 0 in a scalar input and store the result into a scalar register.
    def s_bcnt0_i32_b64(self, reg_d, reg_s0):
        value = self.registers.sgpr_u64(reg_s0)
        count_of_zero_bits = utils.count_zero_bits(value, 64)
        self.registers.set_sgpr_i32(reg_d, count_of_zero_bits)
        self.registers._status.set_scc(1 if count_of_zero_bits != 0 else 0)

    # count the number of bits set to 1 in a scalar input and store the result into a scalar register.
    def s_bcnt1_i32_b32(self, reg_d, reg_s0):
        value = self.registers.sgpr_u32(reg_s0)
        count_of_one_bits = utils.count_one_bits(value, 32)
        self.registers.set_sgpr_i32(reg_d, count_of_one_bits)
        self.registers._status.set_scc(1 if count_of_one_bits != 0 else 0)

    # count the number of bits set to 1 in a scalar input and store the result into a scalar register.
    def s_bcnt1_i32_b64(self, reg_d, reg_s0):
        value = self.registers.sgpr_u64(reg_s0)
        count_of_one_bits = utils.count_one_bits(value, 64)
        self.registers.set_sgpr_i32(reg_d, count_of_one_bits)
        self.registers._status.set_scc(1 if count_of_one_bits != 0 else 0)

    def s_quadmask_b32(self, reg_d, reg_s0):
        s0_val = self.registers.sgpr_u32(reg_s0)
        tmp = 0
        for i in range(32):
            if s0_val & (0xF << (i & ~0x3)):
                tmp |= 1 << i
        self.registers.set_sgpr_u32(reg_d, tmp)
        self.registers._status.set_scc(1 if tmp != 0 else 0)

    def s_quadmask_b64(self, reg_d, reg_s0):
        s0_val = self.registers.sgpr_u64(reg_s0)
        tmp = 0
        for i in range(64):
            if s0_val & (0xF << (i & ~0x3)):
                tmp |= 1 << i
        self.registers.set_sgpr_u64(reg_d, tmp)
        self.registers._status.set_scc(1 if tmp != 0 else 0)

    def s_wqm_b32(self, reg_d, reg_s0):
        s0_val = self.registers.sgpr_u32(reg_s0)
        tmp = 0
        for i in range(32):
            if s0_val & (0xF << (i & ~0x3)):
                tmp |= 1 << i
        self.registers.set_sgpr_u32(reg_d, tmp)
        self.registers._status.set_scc(1 if tmp != 0 else 0)

    def s_wqm_b64(self, reg_d, reg_s0):
        s0_val = self.registers.sgpr_u64(reg_s0)
        tmp = 0
        for i in range(64):
            if s0_val & (0xF << (i & ~0x3)):
                tmp |= 1 << i
        self.registers.set_sgpr_u64(reg_d, tmp)
        self.registers._status.set_scc(1 if tmp != 0 else 0)

    def s_not_b32(self, reg_d, reg_s0):
        s0_val = self.registers.sgpr_u32(reg_s0)
        result = ~s0_val & 0xFFFFFFFF
        self.registers.set_sgpr_u32(reg_d, result)
        self.registers._status.set_scc(1 if result != 0 else 0)

    def s_not_b64(self, reg_d, reg_s0):
        s0_val = self.registers.sgpr_u64(reg_s0)
        result = ~s0_val & 0xFFFFFFFFFFFFFFFF
        self.registers.set_sgpr_u64(reg_d, result)
        self.registers._status.set_scc(1 if result != 0 else 0)

    def s_and_saveexec_b32(self, reg_d, reg_s0):
        original_exec = self.registers.exec
        s0_val = self.registers.sgpr_u32(reg_s0)
        new_exec = (original_exec & 0xFFFFFFFF00000000) | (
            (original_exec & 0xFFFFFFFF) & s0_val
        )
        self.registers.exec = new_exec
        self.registers.set_sgpr_u32(reg_d, original_exec & 0xFFFFFFFF)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_and_saveexec_b64(self, reg_d, reg_s0):
        original_exec = self.registers.exec
        s0_val = self.registers.sgpr_u64(reg_s0)
        new_exec = original_exec & s0_val
        self.registers.exec = new_exec
        self.registers.set_sgpr_u64(reg_d, original_exec)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_or_saveexec_b32(self, reg_d, reg_s0):
        original_exec = self.registers.exec
        s0_val = self.registers.sgpr_u32(reg_s0)
        new_exec = (original_exec & 0xFFFFFFFF00000000) | (
            (original_exec & 0xFFFFFFFF) | s0_val
        )
        self.registers.exec = new_exec
        self.registers.set_sgpr_u32(reg_d, original_exec & 0xFFFFFFFF)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_or_saveexec_b64(self, reg_d, reg_s0):
        original_exec = self.registers.exec  #
        s0_val = self.registers.sgpr_u64(reg_s0)
        new_exec = original_exec | s0_val
        self.registers.exec = new_exec
        self.registers.set_sgpr_u64(reg_d, original_exec)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_xor_saveexec_b32(self, reg_d, reg_s0):
        original_exec = self.registers.exec
        s0_val = self.registers.sgpr_u32(reg_s0)
        new_exec = (original_exec & 0xFFFFFFFF00000000) | (
            (original_exec & 0xFFFFFFFF) ^ s0_val
        )
        self.registers.exec = new_exec
        self.registers.set_sgpr_u32(reg_d, original_exec & 0xFFFFFFFF)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_xor_saveexec_b64(self, reg_d, reg_s0):
        original_exec = self.registers.exec
        s0_val = self.registers.sgpr_u64(reg_s0)
        new_exec = original_exec ^ s0_val
        self.registers.exec = new_exec
        self.registers.set_sgpr_u64(reg_d, original_exec)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_nand_saveexec_b32(self, reg_d, reg_s0):
        original_exec = self.registers.exec
        s0_val = self.registers.sgpr_u32(reg_s0)
        new_exec = (original_exec & 0xFFFFFFFF00000000) | (
            ~(original_exec & 0xFFFFFFFF) & s0_val
        )
        self.registers.exec = new_exec
        self.registers.set_sgpr_u32(reg_d, original_exec & 0xFFFFFFFF)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_nand_saveexec_b64(self, reg_d, reg_s0):
        original_exec = self.registers.exec
        s0_val = self.registers.sgpr_u64(reg_s0)
        new_exec = ~(original_exec & s0_val)
        self.registers.exec = new_exec
        self.registers.set_sgpr_u64(reg_d, original_exec)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_nor_saveexec_b32(self, reg_d, reg_s0):
        original_exec = self.registers.exec
        s0_val = self.registers.sgpr_u32(reg_s0)
        new_exec = (original_exec & 0xFFFFFFFF00000000) | (
            ~(original_exec | s0_val) & 0xFFFFFFFF
        )
        self.registers.exec = new_exec
        self.registers.set_sgpr_u32(reg_d, original_exec & 0xFFFFFFFF)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_nor_saveexec_b64(self, reg_d, reg_s0):
        original_exec = self.registers.exec
        s0_val = self.registers.sgpr_u64(reg_s0)
        new_exec = ~(original_exec | s0_val)
        self.registers.exec = new_exec
        self.registers.set_sgpr_u64(reg_d, original_exec)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_xnor_saveexec_b32(self, reg_d, reg_s0):
        original_exec = self.registers.exec
        s0_val = self.registers.sgpr_u32(reg_s0)
        new_exec = (original_exec & 0xFFFFFFFF00000000) | (
            ~(original_exec ^ s0_val) & 0xFFFFFFFF
        )
        self.registers.exec = new_exec
        self.registers.set_sgpr_u32(reg_d, original_exec & 0xFFFFFFFF)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_xnor_saveexec_b64(self, reg_d, reg_s0):
        original_exec = self.registers.exec
        s0_val = self.registers.sgpr_u64(reg_s0)
        new_exec = ~(original_exec ^ s0_val)
        self.registers.exec = new_exec
        self.registers.set_sgpr_u64(reg_d, original_exec)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_and_not0_saveexec_b32(self, reg_d, reg_s0):
        original_exec = self.registers.exec
        s0_val = ~self.registers.sgpr_u32(reg_s0) & 0xFFFFFFFF
        new_exec = (original_exec & 0xFFFFFFFF00000000) | (
            (original_exec & 0xFFFFFFFF) & s0_val
        )
        self.registers.exec = new_exec
        self.registers.set_sgpr_u32(reg_d, original_exec & 0xFFFFFFFF)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_and_not0_saveexec_b64(self, reg_d, reg_s0):
        original_exec = self.registers.exec
        s0_val = ~self.registers.sgpr_u64(reg_s0)
        new_exec = original_exec & s0_val
        self.registers.exec = new_exec
        self.registers.set_sgpr_u64(reg_d, original_exec)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_or_not0_saveexec_b32(self, reg_d, reg_s0):
        original_exec = self.registers.exec
        s0_val = ~self.registers.sgpr_u32(reg_s0) & 0xFFFFFFFF
        new_exec = (original_exec & 0xFFFFFFFF00000000) | (
            (original_exec & 0xFFFFFFFF) | s0_val
        )
        self.registers.exec = new_exec
        self.registers.set_sgpr_u32(reg_d, original_exec & 0xFFFFFFFF)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_and_not1_saveexec_b32(self, reg_d, reg_s0):
        original_exec = ~self.registers.exec & 0xFFFFFFFF00000000
        s0_val = self.registers.sgpr_u32(reg_s0) & 0xFFFFFFFF
        new_exec = original_exec | (s0_val & 0xFFFFFFFF)
        self.registers.exec = new_exec
        self.registers.set_sgpr_u32(reg_d, ~original_exec & 0xFFFFFFFF)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_and_not1_saveexec_b64(self, reg_d, reg_s0):
        original_exec = ~self.registers.exec
        s0_val = self.registers.sgpr_u64(reg_s0)
        new_exec = original_exec & s0_val
        self.registers.exec = new_exec
        self.registers.set_sgpr_u64(reg_d, ~original_exec)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_or_not1_saveexec_b32(self, reg_d, reg_s0):
        original_exec = ~self.registers.exec & 0xFFFFFFFF00000000
        s0_val = self.registers.sgpr_u32(reg_s0) & 0xFFFFFFFF
        new_exec = original_exec | (s0_val | 0xFFFFFFFF)
        self.registers.exec = new_exec
        self.registers.set_sgpr_u32(reg_d, ~original_exec & 0xFFFFFFFF)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_or_not1_saveexec_b64(self, reg_d, reg_s0):
        original_exec = ~self.registers.exec
        s0_val = self.registers.sgpr_u64(reg_s0)
        new_exec = original_exec | s0_val
        self.registers.exec = new_exec
        self.registers.set_sgpr_u64(reg_d, ~original_exec)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_and_not0_wrexec_b32(self, reg_d, reg_s0):
        s0_val = ~self.registers.sgpr_u32(reg_s0) & 0xFFFFFFFF
        new_exec = (self.registers.exec & 0xFFFFFFFF00000000) | (
            (self.registers.exec & 0xFFFFFFFF) & s0_val
        )
        self.registers.exec = new_exec
        self.registers.set_sgpr_u32(reg_d, new_exec & 0xFFFFFFFF)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_and_not0_wrexec_b64(self, reg_d, reg_s0):
        s0_val = ~self.registers.sgpr_u64(reg_s0)
        new_exec = self.registers.exec & s0_val
        self.registers.exec = new_exec
        self.registers.set_sgpr_u64(reg_d, new_exec)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_and_not1_wrexec_b32(self, reg_d, reg_s0):
        s0_val = self.registers.sgpr_u32(reg_s0) & 0xFFFFFFFF
        new_exec = (~self.registers.exec & 0xFFFFFFFF00000000) | (s0_val & 0xFFFFFFFF)
        self.registers.exec = new_exec
        self.registers.set_sgpr_u32(reg_d, new_exec & 0xFFFFFFFF)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_and_not1_wrexec_b64(self, reg_d, reg_s0):
        s0_val = self.registers.sgpr_u64(reg_s0)
        new_exec = ~self.registers.exec & s0_val
        self.registers.exec = new_exec
        self.registers.set_sgpr_u64(reg_d, new_exec)
        self.registers._status.set_scc(1 if new_exec != 0 else 0)

    def s_movrels_b32(self, reg_d, reg_s0):
        addr = self.registers.sgpr_u32(reg_s0)
        addr += self.registers.m0 & 0xFFFFFFFF  # Adding least significant 32 bits of M0
        value = self.registers.sgpr_u32(addr % len(self.registers._sgpr))
        self.registers.set_sgpr_u32(reg_d, value)

    def s_movereld_b32(self, reg_d, reg_s0):
        addr = self.registers.sgpr_u32(reg_s0)
        addr += self.registers.m0 & 0xFFFFFFFF
        value = self.registers.sgpr_u32(addr % len(self.registers._sgpr))
        self.registers.set_sgpr_u32(reg_d, value)

    def s_movreld_b64(self, reg_d, reg_s0):
        addr = self.registers.sgpr_u64(reg_s0)
        addr += self.registers.m0 & 0xFFFFFFFF
        value = self.registers.sgpr_u64(addr % len(self.registers._sgpr))
        self.registers.set_sgpr_u64(reg_d, value)

    def s_moverelsd_2_b32(self, reg_d, reg_s0):
        addr = self.registers.sgpr_u32(reg_s0)
        addr += self.registers.m0 & 0xFFFFFFFF
        value1 = self.registers.sgpr_u32(addr % len(self.registers._sgpr))
        value2 = self.registers.sgpr_u32((addr + 1) % len(self.registers._sgpr))
        combined_value = (value2 << 16) | value1  # Combining values
        self.registers.set_sgpr_u32(reg_d, combined_value)

    def s_getpc_b64(self, reg_d):
        next_instruction_address = self.registers.pc + 4
        self.registers.set_sgpr_u64(reg_d, next_instruction_address)

    def s_setpc_b64(self, reg_s):
        new_pc_value = self.registers.sgpr_u64(reg_s)
        self.registers.pc = new_pc_value

    def s_swappc_b64(self, reg_d, reg_s):
        next_instruction_address = self.registers.pc + 4
        self.registers.set_sgpr_u64(reg_d, next_instruction_address)
        jump_addr = self.registers.sgpr_u64(reg_s)
        self.registers.pc = jump_addr

    def s_rfe_b64(self, reg_s):
        self.registers.status.set_priv(0)
        jump_addr = self.registers.sgpr_u64(reg_s)
        self.registers.pc = jump_addr

    def s_sendmsg_rtn_b32(self):
        # Implementation for S_SENDMSG_RTN_B32
        pass

    def s_sendmsg_rtn_b64(self):
        # Implementation for S_SENDMSG_RTN_B64
        pass

    # SOPP instructions
    def s_nop(self):
        pass

    def s_sleep(self):
        pass

    def s_delay_alu(self):
        pass

    def s_waitcnt(self):
        pass

    def s_trap(self):
        pass

    def s_branch(self):
        pass

    def s_cbranch_scc1(self):
        pass

    def s_cbranch_vccz(self):
        pass

    def s_cbranch_vccnz(self):
        pass

    def s_cbranch_execz(self):
        pass

    def s_cbranch_execnz(self):
        pass

    def s_clause(self):
        pass

    def s_endpgm(self):
        pass

    def s_sendmsg(self):
        pass

    # SOPC instructions
    def s_cmp_eq_u32(self):
        pass

    # SMEM instructions
    def s_load_b32(self):
        pass

    def s_load_b64(self):
        pass

    def s_load_b128(self):
        pass

    # SOPK instructions
    def s_waitcnt_vscnt(self):
        pass
