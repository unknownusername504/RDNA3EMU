from rdna3emu.isa.utils import *
from rdna3emu.isa.registers import Registers as Re
from rdna3emu.isa.memory import Memory as Me


class ScalarOps:
    def __init__(self, registers: Re, memory: Me):
        self.registers = registers
        self.memory = memory

    def try_get_literal(self, arg, get_reg_func):
        # Argument could be a register or a literal
        if isinstance(arg, int) or isinstance(arg, float):
            # Literal
            return arg
        else:
            # Register, let the caller handle the type
            return get_reg_func(arg)

    # PRG_CTRL instructions
    def s_code_end(self):
        pass  # raise Exception("OP... not implemented")

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
        reg_scc_value = self.registers._status.scc()
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
    def s_lshl_b64(self, reg_d_hi, reg_d_lo, reg_s_hi, reg_s_lo, imm):
        reg_s_lobits = format(self.registers.sgpr_u32(reg_s_lo), "032b")
        reg_s_hibits = format(self.registers.sgpr_u32(reg_s_hi), "032b")
        reg_s_val = int(reg_s_hibits + reg_s_lobits, 2)
        reg_d_value = reg_s_val << imm
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.registers._status.set_scc(reg_scc_value)
        val_bits = format(reg_d_value, "064b")
        val_lobits = int(val_bits[0:32], 2)
        val_hibits = int(val_bits[32:64], 2)
        self.registers.set_sgpr_u32(reg_d_lo, val_lobits)
        self.registers.set_sgpr_u32(reg_d_hi, val_hibits)

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

    def s_mov_b32(self, reg_d, arg_0):
        # TODO: DEAL WITH ARG WHEN EXEC_LO, EXEC_HI, VCC etc.
        arg_0_val = self.try_get_literal(arg_0, self.registers.sgpr_u32)
        self.registers.set_sgpr_u32(reg_d, arg_0_val)

    # mov scalar input into a scalar register. (64-bit)
    def s_mov_b64(self, reg_d, reg_s0):
        reg_s0_val = self.registers.sgpr_u64(reg_s0)
        self.registers.set_sgpr_u64(reg_d, reg_s0_val)

    # mov scalar input into a scalar register iff SCC is nonzero.
    def c_mov_b32(self, reg_d, reg_s0):
        if self.registers._status.scc() == 1:
            self.s_mov_b32(reg_d, reg_s0)

    def c_mov_b64(self, reg_d, reg_s0):
        if self.registers._status.scc() == 1:
            self.s_mov_b64(reg_d, reg_s0)

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

    # Calculate bitwise AND on the scalar input and the negation of the EXEC mask, store the calculated result into
    # the EXEC mask, set SCC iff the calculated result is nonzero and store the original value of the EXEC mask into
    # the scalar destination register.
    # The original EXEC mask is saved to the destination SGPRs before the bitwise operation is performed.
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

    def s_movreld_b32(self, reg_d, reg_s0):
        addr = self.registers.sgpr_u32(reg_s0)
        addr += self.registers.m0 & 0xFFFFFFFF
        value = self.registers.sgpr_u32(addr % len(self.registers._sgpr))
        self.registers.set_sgpr_u32(reg_d, value)

    def s_movreld_b64(self, reg_d, reg_s0):
        addr = self.registers.sgpr_u64(reg_s0)
        addr += self.registers.m0 & 0xFFFFFFFF
        value = self.registers.sgpr_u64(addr % len(self.registers._sgpr))
        self.registers.set_sgpr_u64(reg_d, value)

    def s_movrelsd_2_b32(self, reg_d, reg_s0):
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
        pass  # raise Exception("OP... not implemented")

    def s_sendmsg_rtn_b64(self):
        # Implementation for S_SENDMSG_RTN_B64
        pass  # raise Exception("OP... not implemented")

    # SOPP instructions
    def s_nop(self, simm16):
        wait_states = simm16 & 0xF
        for _ in range(wait_states):
            self.nop()  # Represents a single clock cycle delay
        self.registers.pc += 4

    def s_sleep(self):
        pass  # raise Exception("OP... not implemented")

    def s_delay_alu(self):
        pass  # raise Exception("OP... not implemented")

    # Do nothing funtion that should ignore any input and do nothing
    def s_waitcnt(self, simm16=0):
        simm16 = simm16 & 0xFFFF
        pass

    def s_trap(self):
        pass  # raise Exception("OP... not implemented")

    def s_branch(self, simm16):
        offset = simm16 * 4
        self.registers.pc += offset + 4

    def s_cbranch_scc1(self, simm16):
        if self.registers._status.scc == 1:
            offset = simm16 * 4
            self.registers.pc += offset
        self.registers.pc += 4

    def s_cbranch_vccz(self, simm16):
        if self.registers._status.vccz == 1:
            offset = simm16 * 4
            self.registers.pc += offset
        self.registers.pc += 4

    def s_cbranch_vccnz(self, simm16):
        if self.registers._status.vccz == 0:
            offset = simm16 * 4
            self.registers.pc += offset
        self.registers.pc += 4

    def s_cbranch_execz(self, simm16):
        if self.registers._status.execz == 1:
            offset = simm16 * 4
            self.registers.pc += offset
        self.registers.pc += 4

    def s_cbranch_execnz(self, simm16):
        if self.registers._status.execz == 0:
            offset = simm16 * 4
            self.registers.pc += offset
        self.registers.pc += 4

    """
    Begin a clause consisting of instructions matching the instruction after the s_clause. 
    The clause length is: (SIMM16[5:0] + 1), and clauses must be between 2 and 63 instructions. 
    SIMM16[5:0] must be 1-62, not 0 or 63. 
    The clause breaks after every N instructions, N = simm[11:8] (0 - 15; 0 = no breaks)
    We will just pass # raise Exception("OP... not implemented") the max code block to this function and let it handle the rest.
    """

    def s_clause(self, simm16, clause_code_block):
        clause_length = (simm16 & 0x3F) + 1
        # Check between 1 and 62
        if (clause_length == 0) or (clause_length == 63):
            raise Exception("Clause length must be between 1 and 62")

        # Check if clause length is greater than the number of instructions in the clause
        if clause_length > len(clause_code_block):
            raise Exception(
                "Clause length must be less than the number of instructions in the clause"
            )

        clause_break = (simm16 >> 8) & 0xF
        # Check between 0 and 15
        if clause_break > 15:
            raise Exception("Clause break must be between 0 and 15")

        # Check if clause break is greater than the number of instructions in the clause
        if clause_break > clause_length:
            raise Exception(
                "Clause break must be less than the number of instructions in the clause"
            )

        # Execute the clause
        for i in range(clause_length):
            # Call the code block function
            clause_function = clause_code_block[i][0]
            clause_args = clause_code_block[i][1]
            print(clause_function, clause_args)
            clause_function(*clause_args)

    def s_endpgm(self):
        pass  # raise Exception("OP... not implemented")

    def s_sendmsg(self):
        pass  # raise Exception("OP... not implemented")

    # SOPC instructions
    def s_cmp_eq_u32(self, reg_s0, reg_s1):
        s0_value = self.registers.sgpr_u32(reg_s0)
        s1_value = self.registers.sgpr_u32(reg_s1)
        self.registers._status.set_scc(1 if s0_value == s1_value else 0)

    # SMEM instructions
    # Load a 32-bit value from memory into a scalar register.
    # If the offset is specified as an SGPR, the SGPR contains an UNSIGNED BYTE offset (the 2 LSBs are ignored).
    # If the offset is specified as an immediate 21-bit constant, the constant is a SIGNED BYTE offset.
    def s_load_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.sgpr_u64(reg_s0)
        reg_s1_value = self.registers.sgpr_u64(reg_s1)
        reg_d_value = self.memory.get_memory(reg_s0_value + reg_s1_value, 4)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    def s_load_b32_imm(self, reg_d, reg_s0, imm):
        reg_s0_value = self.registers.sgpr_u64(reg_s0)
        reg_d_value = self.memory.get_memory(reg_s0_value + imm, 4)
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # TODO: Imm can be a scalar (ignore 2 LSBs in that case)
    def s_load_b64(self, reg_d_upper, reg_d_lower, reg_s_upper, reg_s_lower, imm=None):
        reg_s_lobits = format(self.registers.sgpr_u32(reg_s_lower), "032b")
        reg_s_hibits = format(self.registers.sgpr_u32(reg_s_upper), "032b")
        base_addr = reg_s_hibits + reg_s_lobits
        addr = int(base_addr, 2)
        if imm:
            addr += imm
        val = self.memory.get_memory(addr, 8)
        print(f"addr={addr} val@addr={val}")
        val_bits = format(val, "064b")
        val_lobits = int(val_bits[0:32], 2)
        val_hibits = int(val_bits[32:64], 2)
        self.registers.set_sgpr_u32(reg_d_lower, val_lobits)
        self.registers.set_sgpr_u32(reg_d_upper, val_hibits)

    def s_load_b64_imm(self, reg_d, reg_s0, imm):
        reg_s0_value = self.registers.sgpr_u64(reg_s0)
        reg_d_value = self.memory.get_memory(reg_s0_value + imm, 8)
        self.registers.set_sgpr_u64(reg_d, reg_d_value)

    # # Load a 128-bit value from memory into a scalar register.
    # def s_load_b128(self, reg_d, reg_s0, reg_s1):
    #     reg_s0_value = self.registers.sgpr_u64(reg_s0)
    #     reg_s1_value = self.registers.sgpr_u64(reg_s1)
    #     reg_d_value = self.memory.get_memory(reg_s0_value + reg_s1_value, 16)
    #     self.registers.set_sgpr_u128(reg_d, reg_d_value)

    def s_load_b128(
        self,
        reg_d2_upper,
        reg_d2_lower,
        reg_d1_upper,
        reg_d1_lower,
        reg_s_upper,
        reg_s_lower,
        imm=None,
    ):
        reg_s_lobits = format(self.registers.sgpr_u32(reg_s_lower), "032b")
        reg_s_hibits = format(self.registers.sgpr_u32(reg_s_upper), "032b")
        base_addr = reg_s_hibits + reg_s_lobits
        addr = int(base_addr, 2)
        if imm:
            addr += imm
        val = self.memory.get_memory(addr, 16)
        print(f"addr={addr} val@addr={val}")
        val_bits = format(val, "0128b")
        val_1lobits = int(val_bits[0:32], 2)
        val_1hibits = int(val_bits[32:64], 2)
        val_2lobits = int(val_bits[64:96], 2)
        val_2hibits = int(val_bits[96:128], 2)
        self.registers.set_sgpr_u32(reg_d1_lower, val_1lobits)
        self.registers.set_sgpr_u32(reg_d1_upper, val_1hibits)
        self.registers.set_sgpr_u32(reg_d2_lower, val_2lobits)
        self.registers.set_sgpr_u32(reg_d2_upper, val_2hibits)

    def s_load_b128_imm(self, reg_d, reg_s0, imm):
        reg_s0_value = self.registers.sgpr_u64(reg_s0)
        reg_d_value = self.memory.get_memory(reg_s0_value + imm, 16)
        self.registers.set_sgpr_u128(reg_d, reg_d_value)

    # SOPK instructions
    # Do nothing funtion that should ignore any input and do nothing
    def s_waitcnt_any(self, simm16=0):
        simm16 = simm16 & 0xFFFF
        pass

    # Sign extend a literal 16-bit constant and store the result into a scalar register.
    def s_movk_i32(self, reg_d, simm16):
        simm32 = utils.sext_i32(simm16, 16)
        self.registers.set_sgpr_i32(reg_d, simm32)
