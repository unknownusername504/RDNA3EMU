import rdna3emu.isa.utils as utils
from rdna3emu.isa.registers import Registers as Re


class VectorOps:
    def __init__(self, registers: Re):
        self.registers = registers

    # VOP2 instructions
    # Copy data from one of two inputs based on the vector condition code and store the result into a vector register.
    def v_cndmask_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_type = self.get_register_type(reg_s0)
        reg_s1_type = self.get_register_type(reg_s1)
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_s1_value = self.registers.sgpr_u32(reg_s1)
        reg_vcc_value = self.get_vcc_value()
        reg_d_value = reg_s0_value if reg_vcc_value == 1 else reg_s1_value
        reg_d_type = reg_s0_type if reg_s0_type == reg_s1_type else reg_s1_type
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Dot product of packed FP16 values, accumulate with destination.
    def v_dot2acc_f32_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_f16(reg_s0)
        reg_s1_value = self.registers.vgpr_f32(reg_s1)
        reg_s0_value_low = utils.fp16_to_fp32(reg_s0_value & 0xFFFF)
        reg_s0_value_high = utils.fp16_to_fp32(reg_s0_value >> 16)
        reg_s1_value_low = utils.fp16_to_fp32(reg_s1_value & 0xFFFF)
        reg_s1_value_high = utils.fp16_to_fp32(reg_s1_value >> 16)
        reg_d_value = (reg_s0_value_low * reg_s1_value_low) + (
            reg_s0_value_high * reg_s1_value_high
        )
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Add two floating point inputs and store the result into a vector register.
    def v_add_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_f32(reg_s0)
        reg_s1_value = self.registers.vgpr_f32(reg_s1)
        reg_d_value = reg_s0_value + reg_s1_value
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Subtract the second floating point input from the first input and store the result into a vector register.
    def v_sub_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_f32(reg_s0)
        reg_s1_value = self.registers.vgpr_f32(reg_s1)
        reg_d_value = reg_s0_value - reg_s1_value
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Subtract the first floating point input from the second input and store the result into a vector register.
    def v_subrev_f32(self, reg_d, reg_s0, reg_s1):
        self.v_sub_f32(reg_d, reg_s1, reg_s0)

    # Multiply two single-precision values and accumulate the result with the destination. Follows DX9 rules where 0.0 times anything produces 0.0 (this is not IEEE compliant).
    def v_fmac_dx9_zero_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_f32(reg_s0)
        reg_s1_value = self.registers.vgpr_f32(reg_s1)
        reg_d_value = self.registers.vgpr_f32(reg_d)
        if reg_s0_value == 0 or reg_s1_value == 0:
            reg_d_value = 0
        else:
            reg_d_value = reg_d_value + (reg_s0_value * reg_s1_value)
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Multiply two floating point inputs and store the result in a vector register. Follows DX9 rules where 0.0 times anything produces 0.0 (this differs from other APIs when the other input is infinity or NaN).
    def v_mul_dx9_zero_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_f32(reg_s0)
        reg_s1_value = self.registers.vgpr_f32(reg_s1)
        if reg_s0_value == 0 or reg_s1_value == 0:
            reg_d_value = 0
        else:
            reg_d_value = reg_s0_value * reg_s1_value
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Multiply two floating point inputs and store the result into a vector register.
    def v_mul_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_f32(reg_s0)
        reg_s1_value = self.registers.vgpr_f32(reg_s1)
        reg_d_value = reg_s0_value * reg_s1_value
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Multiply two signed 24 bit integer inputs and store the result as a signed 32 bit integer into a vector register.
    def v_mul_i32_i24(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(
            reg_s0, signed=True, size=24, reg_type="VGPR_INT"
        )
        reg_s1_value = self.registers.get_register(
            reg_s1, signed=True, size=24, reg_type="VGPR_INT"
        )
        reg_d_value = reg_s0_value * reg_s1_value
        self.registers.set_vgpr_i32(reg_d, reg_d_value)

    # Multiply two signed 24 bit integer inputs and store the high 32 bits of the result as a signed 32 bit integer into a vector register.
    def v_mul_hi_i32_i24(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(
            reg_s0, signed=True, size=24, reg_type="VGPR_INT"
        )
        reg_s1_value = self.registers.get_register(
            reg_s1, signed=True, size=24, reg_type="VGPR_INT"
        )
        reg_d_value = (reg_s0_value * reg_s1_value) >> 32
        self.registers.set_register(
            reg_d, reg_d_value, signed=True, size=32, reg_type="VGPR_INT"
        )

    # Multiply two unsigned 24 bit integer inputs and store the result as a unsigned 32 bit integer into a vector register.
    def v_mul_u32_u24(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(
            reg_s0, signed=False, size=24, reg_type="VGPR_INT"
        )
        reg_s1_value = self.registers.get_register(
            reg_s1, signed=False, size=24, reg_type="VGPR_INT"
        )
        reg_d_value = reg_s0_value * reg_s1_value
        self.registers.set_register(
            reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT"
        )

    # Multiply two unsigned 24 bit integer inputs and store the high 32 bits of the result as a unsigned 32 bit integer into a vector register.
    def v_mul_hi_u32_u24(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(
            reg_s0, signed=False, size=24, reg_type="VGPR_INT"
        )
        reg_s1_value = self.registers.get_register(
            reg_s1, signed=False, size=24, reg_type="VGPR_INT"
        )
        reg_d_value = (reg_s0_value * reg_s1_value) >> 32
        self.registers.set_register(
            reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT"
        )

    # Select the minimum of two floating point inputs and store the result into a vector register
    def v_min_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_f32(reg_s0)
        reg_s1_value = self.registers.get_register(
            reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"
        )
        reg_d_value = min(reg_s0_value, reg_s1_value)
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Select the maximum of two floating point inputs and store the result into a vector register
    def v_max_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_f32(reg_s0)
        reg_s1_value = self.registers.vgpr_f32(reg_s1)
        reg_d_value = max(reg_s0_value, reg_s1_value)
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Select the minimum of two signed integers and store the selected value into a vector register.
    def v_min_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_i32(reg_s0)
        reg_s1_value = self.registers.vgpr_i32(reg_s1)
        reg_d_value = min(reg_s0_value, reg_s1_value)
        self.registers.set_vgpr_i32(reg_d, reg_d_value)

    # Select the maximum of two signed integers and store the selected value into a vector register.
    def v_max_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_i32(reg_s0)
        reg_s1_value = self.registers.vgpr_i32(reg_s1)
        reg_d_value = max(reg_s0_value, reg_s1_value)
        self.registers.set_vgpr_i32(reg_d, reg_d_value)

    # Select the minimum of two unsigned integers and store the selected value into a vector register.
    def v_min_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_u32(reg_s0)
        reg_s1_value = self.registers.vgpr_u32(reg_s1)
        reg_d_value = min(reg_s0_value, reg_s1_value)
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Select the maximum of two unsigned integers and store the selected value into a vector register.
    def v_max_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_u32(reg_s0)
        reg_s1_value = self.registers.vgpr_u32(reg_s1)
        reg_d_value = max(reg_s0_value, reg_s1_value)
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Given a shift count in the first vector input, calculate the logical shift left of the second vector input and store the result into a vector register.
    def v_lshlrev_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_u32(reg_s0)
        reg_s1_value = self.registers.vgpr_u32(reg_s1)
        reg_d_value = reg_s1_value << reg_s0_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Given a shift count in the first vector input, calculate the logical shift right of the second vector input and store the result into a vector register
    def v_lshrrev_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_u32(reg_s0)
        reg_s1_value = self.registers.vgpr_u32(reg_s1)
        reg_d_value = reg_s1_value >> reg_s0_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Given a shift count in the first vector input, calculate the arithmetic shift right (preserving sign bit) of the second vector input and store the result into a vector register.
    def v_ashrrev_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_i32(reg_s0)
        reg_s1_value = self.registers.vgpr_i32(reg_s1)
        reg_d_value = reg_s1_value >> reg_s0_value
        self.registers.set_vgpr_i32(reg_d, reg_d_value)

    # Calculate bitwise AND on two vector inputs and store the result into a vector register.
    def v_and_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_u32(reg_s0)
        reg_s1_value = self.registers.vgpr_u32(reg_s1)
        reg_d_value = reg_s0_value & reg_s1_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Calculate bitwise OR on two vector inputs and store the result into a vector register.
    def v_or_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_u32(reg_s0)
        reg_s1_value = self.registers.vgpr_u32(reg_s1)
        reg_d_value = reg_s0_value | reg_s1_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Calculate bitwise XOR on two vector inputs and store the result into a vector register.
    def v_xor_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_u32(reg_s0)
        reg_s1_value = self.registers.vgpr_u32(reg_s1)
        reg_d_value = reg_s0_value ^ reg_s1_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Calculate bitwise XNOR on two vector inputs and store the result into a vector register.
    def v_xnor_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_u32(reg_s0)
        reg_s1_value = self.registers.vgpr_u32(reg_s1)
        reg_d_value = ~(reg_s0_value ^ reg_s1_value)
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Add two unsigned inputs and a bit from a carry-in mask, store the result into a vector register and store the carry-out mask into a scalar register.
    def v_add_co_ci_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_u32(reg_s0)
        reg_s1_value = self.registers.vgpr_u32(reg_s1)
        reg_vcc_value = self.registers.vcc
        reg_d_value = reg_s0_value + reg_s1_value + reg_vcc_value
        reg_vcc_value = 1 if reg_d_value > 0xFFFFFFFF else 0
        self.registers.vcc(reg_vcc_value)
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Subtract the second unsigned input from the first input, subtract a bit from the carry-in mask, store the result into a vector register and store the carry-out mask to a scalar register
    def v_sub_co_ci_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_u32(reg_s0)
        reg_s1_value = self.registers.vgpr_u32(reg_s1)
        reg_vcc_value = self.registers.vcc
        reg_d_value = reg_s0_value - reg_s1_value - reg_vcc_value
        reg_vcc_value = 1 if reg_d_value < 0 else 0
        self.registers.vcc(reg_vcc_value)
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Subtract the first unsigned input from the second input, subtract a bit from the carry-in mask, store the result into a vector register and store the carry-out mask to a scalar register.
    def v_subrev_co_ci_u32(self, reg_d, reg_s0, reg_s1):
        self.v_sub_co_ci_u32(reg_d, reg_s1, reg_s0)

    # Add two unsigned inputs and store the result into a vector register. No carry-in or carry-out support.
    def v_add_nc_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_u32(reg_s0)
        reg_s1_value = self.registers.vgpr_u32(reg_s1)
        reg_d_value = reg_s0_value + reg_s1_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Subtract the second unsigned input from the first input and store the result into a vector register. No carry-in or carry-out support.
    def v_sub_nc_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_u32(reg_s0)
        reg_s1_value = self.registers.vgpr_u32(reg_s1)
        reg_d_value = reg_s0_value - reg_s1_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Subtract the first unsigned input from the second input and store the result into a vector register. No carry-in or carry-out support.
    def v_subrev_nc_u32(self, reg_d, reg_s0, reg_s1):
        self.v_sub_nc_u32(reg_d, reg_s1, reg_s0)

    # Multiply two floating point inputs and accumulate the result into the destination register using fused multiplyadd.
    def v_fmac_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_f32(reg_s0)
        reg_s1_value = self.registers.vgpr_f32(reg_s1)
        reg_d_value = self.registers.vgpr_f32(reg_d)
        reg_d_value = reg_d_value + (reg_s0_value * reg_s1_value)
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Multiply a single-precision float with a literal constant and add a second single-precision float using fused multiply-add.
    def v_fmamk_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_f32(reg_s0)
        reg_s1_value = self.registers.vgpr_f32(reg_s1)
        reg_simm32_value = self.registers.get_register(
            self.reg_simm, signed=None, size=32, reg_type="VGPR_FLOAT"
        )
        reg_d_value = reg_s1_value + (reg_s0_value * reg_simm32_value)
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Multiply two single-precision floats and add a literal constant using fused multiply-add.
    def v_fmaak_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_f32(reg_s0)
        reg_s1_value = self.registers.vgpr_f32(reg_s1)
        reg_simm32_value = self.registers.get_register(
            self.reg_simm, signed=None, size=32, reg_type="VGPR_FLOAT"
        )
        reg_d_value = reg_simm32_value + (reg_s0_value * reg_s1_value)
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Convert two single-precision float inputs into a packed FP16 result with round toward zero semantics (ignore the current rounding mode), and store the result into a vector register.
    def v_cvt_pk_rtz_f16_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_f32(reg_s0)
        reg_s1_value = self.registers.vgpr_f32(reg_s1)

        # Convert the first input.
        reg_s0_value = utils.fp32_to_fp16(reg_s0_value)

        # Convert the second input.
        reg_s1_value = utils.fp32_to_fp16(reg_s1_value)
        reg_s1_value = reg_s1_value << 16

        # Combine the two inputs.
        reg_d_value = reg_s0_value | reg_s1_value
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Add two floating point inputs and store the result into a vector register.
    def v_add_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.vgpr_f16(reg_s0))
        reg_s1_value = utils.fp16_to_fp32(self.registers.vgpr_f16(reg_s1))
        reg_d_value = reg_s0_value + reg_s1_value
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Subtract the second floating point input from the first input and store the result into a vector register.
    def v_sub_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_s0))
        reg_s1_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_s1))
        reg_d_value = reg_s0_value - reg_s1_value
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Subtract the first floating point input from the second input and store the result into a vector register.
    def v_subrev_f16(self, reg_d, reg_s0, reg_s1):
        self.v_sub_f16(reg_d, reg_s1, reg_s0)

    # Multiply two floating point inputs and store the result into a vector register.
    def v_mul_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_s0))
        reg_s1_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_s1))
        reg_d_value = reg_s0_value * reg_s1_value
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Multiply two floating point inputs and accumulate the result into the destination register using fused multiplyadd.
    def v_fmac_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_s0))
        reg_s1_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_s1))
        reg_d_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_d))
        reg_d_value = reg_d_value + (reg_s0_value * reg_s1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Multiply a FP16 value with a literal constant and add a second FP16 value using fused multiply-add.
    def v_fmamk_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_s0))
        reg_s1_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_s1))
        reg_simm32_value = utils.fp16_to_fp32(self.registers.vgpr_f32(self.reg_simm))
        reg_d_value = reg_s1_value + (reg_s0_value * reg_simm32_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Multiply two FP16 values and add a literal constant using fused multiply-add.
    def v_fmaak_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_s0))
        reg_s1_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_s1))
        reg_simm32_value = utils.fp16_to_fp32(self.registers.vgpr_f32(self.reg_simm))
        reg_d_value = reg_simm32_value + (reg_s0_value * reg_s1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Select the maximum of two floating point inputs and store the result into a vector register.
    def v_max_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_s0))
        reg_s1_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_s1))
        reg_d_value = max(reg_s0_value, reg_s1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Select the minimum of two floating point inputs and store the result into a vector register.
    def v_min_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_s0))
        reg_s1_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_s1))
        reg_d_value = min(reg_s0_value, reg_s1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Multiply the first input, a floating point value, by an integral power of 2 specified in the second input, a signed integer value, and store the floating point result into a vector register. Compare with the ldexp() function in C.
    def v_ldexp_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_s0))
        reg_s1_value = self.registers.get_register(
            reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"
        )
        reg_d_value = reg_s0_value * (2**reg_s1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Multiply packed FP16 values and accumulate with destination.
    def v_pk_fmac_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.vgpr_f32(reg_s0)
        reg_s1_value = self.registers.vgpr_f16(reg_s1)

        # Extract the first input.
        reg_s0_value_lo = utils.fp32_to_fp16(reg_s0_value & 0xFFFF)
        reg_s0_value_hi = utils.fp32_to_fp16(reg_s0_value >> 16)

        # Extract the second input.
        reg_s1_value_lo = utils.fp32_to_fp16(reg_s1_value & 0xFFFF)
        reg_s1_value_hi = utils.fp32_to_fp16(reg_s1_value >> 16)

        reg_d_value = self.registers.get_register(
            reg_d, signed=None, size=32, reg_type="VGPR_FLOAT"
        )

        # Extract the destination.
        reg_d_value_lo = utils.fp32_to_fp16(reg_d_value & 0xFFFF)
        reg_d_value_hi = utils.fp32_to_fp16(reg_d_value >> 16)

        # Accumulate the result.
        reg_d_value_lo = reg_d_value_lo + (reg_s0_value_lo * reg_s1_value_lo)
        reg_d_value_hi = reg_d_value_hi + (reg_s0_value_hi * reg_s1_value_hi)
        reg_d_value = utils.fp16_to_fp32(reg_d_value_lo) | (
            utils.fp16_to_fp32(reg_d_value_hi) << 16
        )
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # VOP1 instructions
    # Do nothing.
    def v_nop(self):
        pass

    # Move data from a vector input into a vector register.
    def v_mov_b32(self):
        pass

    # Read the scalar value in the lowest active lane of the input vector register and store it into a scalar register.
    def v_readfirstlane_b32(self, reg_d, reg_s0):
        # This would normally go through all the enabled lanes (exec masked) and find the first one. Or force lane 0 if all lanes are disabled.
        # Our emulator only has one lane, so we can just read the value from the lane.
        reg_s0_value = self.registers.vgpr_u32(reg_s0)
        reg_d_value = reg_s0_value
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Convert from a double-precision float input to a signed 32-bit integer and store the result into a vector register.
    def v_cvt_i32_f64(self):
        pass

    # Convert from a signed 32-bit integer input to a double-precision float and store the result into a vector register.
    def v_cvt_f64_i32(self):
        pass

    # Convert from a signed 32-bit integer input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_i32(self):
        pass

    # Convert from an unsigned 32-bit integer input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_u32(self):
        pass

    # Convert from a single-precision float input to an unsigned 32-bit integer and store the result into a vector register.
    def v_cvt_u32_f32(self):
        pass

    # Convert from a single-precision float input to a signed 32-bit integer and store the result into a vector register.
    def v_cvt_i32_f32(self):
        pass

    # Convert from a single-precision float input to an FP16 float and store the result into a vector register.
    def v_cvt_f16_f32(self):
        pass

    # Convert from an FP16 float input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_f16(self):
        pass

    # Convert from a single-precision float input to a signed 32-bit integer using round-to-nearest-integer semantics (ignore the default rounding mode) and store the result into a vector register.
    def v_cvt_nearest_i32_f32(self):
        pass

    # Convert from a single-precision float input to a signed 32-bit integer using round-down semantics (ignore the default rounding mode) and store the result into a vector register.
    def v_cvt_floor_i32_f32(self):
        pass

    # Convert from a signed 4-bit integer to a single-precision float using an offset table and store the result into a vector register.
    def v_cvt_off_f32_i4(self):
        pass

    # Convert from a double-precision float input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_f64(self):
        pass

    # Convert from a single-precision float input to a double-precision float and store the result into a vector register.
    def v_cvt_f64_f32(self):
        pass

    # Convert an unsigned byte in byte 0 of the input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_ubyte0(self):
        pass

    # Convert an unsigned byte in byte 1 of the input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_ubyte1(self):
        pass

    # Convert an unsigned byte in byte 2 of the input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_ubyte2(self):
        pass

    # Convert an unsigned byte in byte 3 of the input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_ubyte3(self):
        pass

    # Convert from a double-precision float input to an unsigned 32-bit integer and store the result into a vector register.
    def v_cvt_u32_f64(self):
        pass

    # Convert from an unsigned 32-bit integer input to a double-precision float and store the result into a vector register.
    def v_cvt_f64_u32(self):
        pass

    # Compute the integer part of a double-precision float input with round-toward-zero semantics and store the result in floating point format into a vector register.
    def v_trunc_f64(self):
        pass

    # Round the double-precision float input up to next integer and store the result in floating point format into a vector register.
    def v_ceil_f64(self):
        pass

    # Round the double-precision float input to the nearest even integer and store the result in floating point format into a vector register.
    def v_rndne_f64(self):
        pass

    # Round the double-precision float input down to previous integer and store the result in floating point format into a vector register.
    def v_floor_f64(self):
        pass

    # Flush the VALU destination cache.
    def v_pipeflush(self):
        pass

    # Move data to a VGPR.
    def v_mov_b16(self):
        pass

    # Compute the fractional portion of a single-precision float input and store the result in floating point format into a vector register.
    def v_fract_f32(self):
        pass

    # Compute the integer part of a single-precision float input with round-toward-zero semantics and store the result in floating point format into a vector register.
    def v_trunc_f32(self):
        pass

    # Round the single-precision float input up to next integer and store the result in floating point format into a vector register.
    def v_ceil_f32(self):
        pass

    # Round the single-precision float input to the nearest even integer and store the result in floating point format into a vector register.
    def v_rndne_f32(self):
        pass

    # Round the single-precision float input down to previous integer and store the result in floating point format into a vector register.
    def v_floor_f32(self):
        pass

    # Calculate 2 raised to the power of the single-precision float input and store the result into a vector register.
    def v_exp_f32(self):
        pass

    # Calculate the base 2 logarithm of the single-precision float input and store the result into a vector register.
    def v_log_f32(self):
        pass

    # Calculate the reciprocal of the single-precision float input using IEEE rules and store the result into a vector register.
    def v_rcp_f32(self):
        pass

    # Calculate the reciprocal of the vector float input in a manner suitable for integer division and store the result into a vector register. This opcode is intended for use as part of an integer division macro.
    def v_rcp_iflag_f32(self):
        pass

    #
    def v_rsq_f32(self):
        pass

    #
    def v_rcp_f64(self):
        pass

    #
    def v_rsq_f64(self):
        pass

    #
    def v_sqrt_f32(self):
        pass

    #
    def v_sqrt_f64(self):
        pass

    #
    def v_sin_f32(self):
        pass

    #
    def v_cos_f32(self):
        pass

    #
    def v_not_b32(self):
        pass

    #
    def v_bfrev_b32(self):
        pass

    #
    def v_clz_i32_u32(self):
        pass

    #
    def v_ctz_i32_b32(self):
        pass

    #
    def v_cls_i32(self):
        pass

    #
    def v_frexp_exp_i32_f64(self):
        pass

    #
    def v_frexp_mant_f64(self):
        pass

    #
    def v_fract_f64(self):
        pass

    #
    def v_frexp_exp_i32_f32(self):
        pass

    #
    def v_frexp_mant_f32(self):
        pass

    #
    def v_movreld_b32(self):
        pass

    #
    def v_movrels_b32(self):
        pass

    #
    def v_movrelsd_b32(self):
        pass

    #
    def v_movrelsd_2_b32(self):
        pass

    #
    def v_cvt_f16_u16(self):
        pass

    #
    def v_cvt_f16_i16(self):
        pass

    #
    def v_cvt_u16_f16(self):
        pass

    #
    def v_cvt_i16_f16(self):
        pass

    #
    def v_rcp_f16(self):
        pass

    #
    def v_sqrt_f16(self):
        pass

    #
    def v_rsq_f16(self):
        pass

    #
    def v_log_f16(self):
        pass

    #
    def v_exp_f16(self):
        pass

    #
    def v_frexp_mant_f16(self):
        pass

    #
    def v_frexp_exp_i16_f16(self):
        pass

    #
    def v_floor_f16(self):
        pass

    #
    def v_ceil_f16(self):
        pass

    #
    def v_trunc_f16(self):
        pass

    #
    def v_rndne_f16(self):
        pass

    #
    def v_fract_f16(self):
        pass

    #
    def v_sin_f16(self):
        pass

    #
    def v_cos_f16(self):
        pass

    #
    def v_sat_pk_u8_i16(self):
        pass

    #
    def v_cvt_norm_i16_f16(self):
        pass

    #
    def v_cvt_norm_u16_f16(self):
        pass

    #
    def v_swap_b32(self):
        pass

    #
    def v_swap_b16(self):
        pass

    #
    def v_permlane64_b32(self):
        pass

    #
    def v_swaprel_b32(self):
        pass

    #
    def v_not_b16(self):
        pass

    #
    def v_cvt_i32_i16(self):
        pass

    #
    def v_cvt_u32_u16(self):
        pass
