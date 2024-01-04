import inspect
import math
import rdna3emu.isa.utils as utils
from rdna3emu.isa.registers import Registers as Re
from rdna3emu.isa.memory import Memory as Me
import numpy as np


class VectorOps:
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

    # VOP2 instructions
    # Copy data from one of two inputs based on the vector condition code and store the result into a vector register.
    # In VOP3 the VCC source may be a scalar GPR specified in S2.
    def v_cndmask_b32(self, reg_d, arg_0, arg_1, arg_2):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_u32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_u32)
        if isinstance(arg_2, str):
            arg_2_value = self.registers.vcc
        else:
            arg_2_value = self.registers.sgpr_u32(arg_2)
        reg_d_value = arg_0_value if arg_2_value else arg_1_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Dot product of packed FP16 values, accumulate with destination.
    def v_dot2acc_f32_f16(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.vgpr_f16(reg_v0)
        reg_v1_value = self.registers.vgpr_f32(reg_v1)
        reg_v0_value_low = utils.fp16_to_fp32(reg_v0_value & 0xFFFF)
        reg_v0_value_high = utils.fp16_to_fp32(reg_v0_value >> 16)
        reg_v1_value_low = utils.fp16_to_fp32(reg_v1_value & 0xFFFF)
        reg_v1_value_high = utils.fp16_to_fp32(reg_v1_value >> 16)
        reg_d_value = (reg_v0_value_low * reg_v1_value_low) + (
            reg_v0_value_high * reg_v1_value_high
        )
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Add two floating point inputs and store the result into a vector register.
    def v_add_f32(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.vgpr_f32(reg_v0)
        reg_v1_value = self.registers.vgpr_f32(reg_v1)
        reg_d_value = reg_v0_value + reg_v1_value
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Subtract the second floating point input from the first input and store the result into a vector register.
    def v_sub_f32(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f32)
        reg_d_value = arg_0_value - arg_1_value
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Subtract the first floating point input from the second input and store the result into a vector register.
    def v_subrev_f32(self, reg_d, reg_v0, reg_v1):
        self.v_sub_f32(reg_d, reg_v1, reg_v0)

    # Multiply two single-precision values and accumulate the result with the destination. Follows DX9 rules where 0.0 times anything produces 0.0 (this is not IEEE compliant).
    def v_fmac_dx9_zero_f32(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.vgpr_f32(reg_v0)
        reg_v1_value = self.registers.vgpr_f32(reg_v1)
        reg_d_value = self.registers.vgpr_f32(reg_d)
        if reg_v0_value == 0 or reg_v1_value == 0:
            reg_d_value = 0
        else:
            reg_d_value = reg_d_value + (reg_v0_value * reg_v1_value)
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Multiply two floating point inputs and store the result in a vector register. Follows DX9 rules where 0.0 times anything produces 0.0 (this differs from other APIs when the other input is infinity or NaN).
    def v_mul_dx9_zero_f32(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f32)
        if arg_0_value == 0 or arg_1_value == 0:
            reg_d_value = 0
        else:
            reg_d_value = arg_0_value * arg_1_value
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Multiply two floating point inputs and store the result into a vector register.
    def v_mul_f32(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f32)
        reg_d_value = arg_0_value * arg_1_value
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Multiply two signed 24 bit integer inputs and store the result as a signed 32 bit integer into a vector register.
    def v_mul_i32_i24(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.get_register(
            reg_v0, signed=True, size=24, reg_type="VGPR_INT"
        )
        reg_v1_value = self.registers.get_register(
            reg_v1, signed=True, size=24, reg_type="VGPR_INT"
        )
        reg_d_value = reg_v0_value * reg_v1_value
        self.registers.set_vgpr_i32(reg_d, reg_d_value)

    # Multiply two signed 24 bit integer inputs and store the high 32 bits of the result as a signed 32 bit integer into a vector register.
    def v_mul_hi_i32_i24(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.get_register(
            reg_v0, signed=True, size=24, reg_type="VGPR_INT"
        )
        reg_v1_value = self.registers.get_register(
            reg_v1, signed=True, size=24, reg_type="VGPR_INT"
        )
        reg_d_value = (reg_v0_value * reg_v1_value) >> 32
        self.registers.set_vgpr_i32(reg_d, reg_d_value)

    # Multiply two unsigned 24 bit integer inputs and store the result as a unsigned 32 bit integer into a vector register.
    def v_mul_u32_u24(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.get_register(
            reg_id=reg_v0, signed=False, size=24, reg_type="VGPR_INT"
        )
        reg_v1_value = self.registers.get_register(
            reg_id=reg_v1, signed=False, size=24, reg_type="VGPR_INT"
        )
        reg_d_value = reg_v0_value * reg_v1_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Multiply two unsigned 24 bit integer inputs and store the high 32 bits of the result as a unsigned 32 bit integer into a vector register.
    def v_mul_hi_u32_u24(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.get_register(
            reg_id=reg_v0, signed=False, size=24, reg_type="VGPR_INT"
        )
        reg_v1_value = self.registers.get_register(
            reg_id=reg_v1, signed=False, size=24, reg_type="VGPR_INT"
        )
        reg_d_value = (reg_v0_value * reg_v1_value) >> 32
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Select the minimum of two floating point inputs and store the result into a vector register
    def v_min_f32(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f32)
        reg_d_value = min(arg_0_value, arg_1_value)
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Select the maximum of two floating point inputs and store the result into a vector register
    def v_max_f32(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f32)
        reg_d_value = max(arg_0_value, arg_1_value)
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Select the minimum of two signed integers and store the selected value into a vector register.
    def v_min_i32(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_i32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_i32)
        reg_d_value = min(arg_0_value, arg_1_value)
        self.registers.set_vgpr_i32(reg_d, reg_d_value)

    # Select the maximum of two signed integers and store the selected value into a vector register.
    def v_max_i32(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.vgpr_i32(reg_v0)
        reg_v1_value = self.registers.vgpr_i32(reg_v1)
        reg_d_value = max(reg_v0_value, reg_v1_value)
        self.registers.set_vgpr_i32(reg_d, reg_d_value)

    # Select the minimum of two unsigned integers and store the selected value into a vector register.
    def v_min_u32(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_v1_value = self.registers.vgpr_u32(reg_v1)
        reg_d_value = min(reg_v0_value, reg_v1_value)
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Select the maximum of two unsigned integers and store the selected value into a vector register.
    def v_max_u32(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_v1_value = self.registers.vgpr_u32(reg_v1)
        reg_d_value = max(reg_v0_value, reg_v1_value)
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Given a shift count in the first vector input, calculate the logical shift left of the second vector input and store the result into a vector register.
    def v_lshlrev_b32(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_v1_value = self.registers.vgpr_u32(reg_v1)
        reg_d_value = reg_v1_value << reg_v0_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Given a shift count in the first vector input, calculate the logical shift right of the second vector input and store the result into a vector register
    def v_lshrrev_b32(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_v1_value = self.registers.vgpr_u32(reg_v1)
        reg_d_value = reg_v1_value >> reg_v0_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Given a shift count in the first vector input, calculate the arithmetic shift right (preserving sign bit) of the second vector input and store the result into a vector register.
    def v_ashrrev_i32(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.vgpr_i32(reg_v0)
        reg_v1_value = self.registers.vgpr_i32(reg_v1)
        reg_d_value = reg_v1_value >> reg_v0_value
        self.registers.set_vgpr_i32(reg_d, reg_d_value)

    # Calculate bitwise AND on two vector inputs and store the result into a vector register.
    def v_and_b32(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_u32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_u32)
        reg_d_value = arg_0_value & arg_1_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Calculate bitwise OR on two vector inputs and store the result into a vector register.
    def v_or_b32(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_u32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_u32)
        # Convert any floats to ints
        if isinstance(arg_0_value, float):
            arg_0_value = int(arg_0_value)
        if isinstance(arg_1_value, float):
            arg_1_value = int(arg_1_value)
        reg_d_value = arg_0_value | arg_1_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Calculate bitwise XOR on two vector inputs and store the result into a vector register.
    def v_xor_b32(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_v1_value = self.registers.vgpr_u32(reg_v1)
        reg_d_value = reg_v0_value ^ reg_v1_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Calculate bitwise XNOR on two vector inputs and store the result into a vector register.
    def v_xnor_b32(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_v1_value = self.registers.vgpr_u32(reg_v1)
        reg_d_value = ~(reg_v0_value ^ reg_v1_value)
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Add two unsigned inputs and a bit from a carry-in mask, store the result into a vector register and store the carry-out mask into a scalar register.
    # v_add_co_ci_u32_e32 v1, vcc_lo, s5, v1, vcc_lo
    # In VOP3 the VCC destination may be an arbitrary SGPR-pair, and the VCC source comes from the SGPR-pair at S2.u.
    def v_add_co_ci_u32(self, reg_d, arg_0, arg_1, arg_2, arg_3):
        arg_1_value = self.try_get_literal(arg_1, self.registers.sgpr_u32)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_u32)
        if isinstance(arg_3, str):
            arg_3_value = self.registers.vcc & 1
        else:
            arg_3_value = self.registers.sgpr_u32(arg_3) & 1

        reg_d_value = arg_1_value + arg_2_value + arg_3_value

        arg_0_value = reg_d_value > 0xFFFFFFFF

        if isinstance(arg_0, str):
            self.registers.vcc = arg_0_value
        else:
            self.registers.set_sgpr_u32(arg_0, arg_0_value)

        reg_d_value = reg_d_value & 0xFFFFFFFF
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Subtract the second unsigned input from the first input, subtract a bit from the carry-in mask, store the result into a vector register and store the carry-out mask to a scalar register
    def v_sub_co_ci_u32(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_v1_value = self.registers.vgpr_u32(reg_v1)
        reg_vcc_value = self.registers.vcc
        reg_d_value = reg_v0_value - reg_v1_value - reg_vcc_value
        reg_vcc_value = 1 if reg_d_value < 0 else 0
        self.registers.vcc = reg_vcc_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Subtract the first unsigned input from the second input, subtract a bit from the carry-in mask, store the result into a vector register and store the carry-out mask to a scalar register.
    def v_subrev_co_ci_u32(self, reg_d, reg_v0, reg_v1):
        self.v_sub_co_ci_u32(reg_d, reg_v1, reg_v0)

    # Add two unsigned inputs and store the result into a vector register. No carry-in or carry-out support.
    def v_add_nc_u32(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_u32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_u32)
        reg_d_value = arg_0_value + arg_1_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Subtract the second unsigned input from the first input and store the result into a vector register. No carry-in or carry-out support.
    def v_sub_nc_u32(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_v1_value = self.registers.vgpr_u32(reg_v1)
        reg_d_value = reg_v0_value - reg_v1_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Subtract the first unsigned input from the second input and store the result into a vector register. No carry-in or carry-out support.
    def v_subrev_nc_u32(self, reg_d, reg_v0, reg_v1):
        self.v_sub_nc_u32(reg_d, reg_v1, reg_v0)

    # Multiply two floating point inputs and accumulate the result into the destination register using fused multiplyadd.
    def v_fmac_f32(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f32)
        reg_d_value = self.registers.vgpr_f32(reg_d)
        reg_d_value = reg_d_value + (arg_0_value * arg_1_value)
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Multiply a single-precision float with a literal constant and add a second single-precision float using fused multiply-add.
    def v_fmamk_f32(self, reg_d, reg_v0, simm32, reg_v1):
        reg_v0_value = self.registers.vgpr_f32(reg_v0)
        reg_v1_value = self.registers.vgpr_f32(reg_v1)
        reg_d_value = reg_v1_value + (reg_v0_value * simm32)
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Multiply two single-precision floats and add a literal constant using fused multiply-add.
    def v_fmaak_f32(self, reg_d, reg_v0, reg_v1, simm32):
        reg_v0_value = self.registers.vgpr_f32(reg_v0)
        reg_v1_value = self.registers.vgpr_f32(reg_v1)
        reg_d_value = simm32 + (reg_v0_value * reg_v1_value)
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Convert two single-precision float inputs into a packed FP16 result with round toward zero semantics (ignore the current rounding mode), and store the result into a vector register.
    def v_cvt_pk_rtz_f16_f32(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f32)

        # Convert the first input.
        arg_0_value = utils.fp32_to_fp16(arg_0_value)

        # Convert the second input.
        arg_1_value = utils.fp32_to_fp16(arg_1_value)
        arg_1_value = arg_1_value << 16

        # Combine the two inputs.
        reg_d_value = arg_0_value | arg_1_value
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Add two floating point inputs and store the result into a vector register.
    def v_add_f16(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f16)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f16)
        arg_0_value = utils.fp16_to_fp32(arg_0_value)
        arg_1_value = utils.fp16_to_fp32(arg_1_value)
        reg_d_value = arg_0_value + arg_1_value
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Subtract the second floating point input from the first input and store the result into a vector register.
    def v_sub_f16(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f16)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f16)
        arg_0_value = utils.fp16_to_fp32(arg_0_value)
        arg_1_value = utils.fp16_to_fp32(arg_1_value)
        reg_d_value = arg_0_value - arg_1_value
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Subtract the first floating point input from the second input and store the result into a vector register.
    def v_subrev_f16(self, reg_d, reg_v0, reg_v1):
        self.v_sub_f16(reg_d, reg_v1, reg_v0)

    # Multiply two floating point inputs and store the result into a vector register.
    def v_mul_f16(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f16)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f16)
        arg_0_value = utils.fp16_to_fp32(arg_0_value)
        arg_1_value = utils.fp16_to_fp32(arg_1_value)
        reg_d_value = arg_0_value * arg_1_value
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Multiply two floating point inputs and accumulate the result into the destination register using fused multiplyadd.
    def v_fmac_f16(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f16)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f16)
        arg_0_value = utils.fp16_to_fp32(arg_0_value)
        arg_1_value = utils.fp16_to_fp32(arg_1_value)
        reg_d_value = utils.fp16_to_fp32(self.registers.vgpr_f16(reg_d))
        reg_d_value = reg_d_value + (arg_0_value * arg_1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Multiply a FP16 value with a literal constant and add a second FP16 value using fused multiply-add.
    def v_fmamk_f16(self, reg_d, reg_v0, reg_v1, simm32):
        reg_v0_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_v0))
        reg_v1_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_v1))
        reg_d_value = reg_v1_value + (reg_v0_value * simm32)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Multiply two FP16 values and add a literal constant using fused multiply-add.
    def v_fmaak_f16(self, reg_d, reg_v0, reg_v1, simm32):
        reg_v0_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_v0))
        reg_v1_value = utils.fp16_to_fp32(self.registers.vgpr_f32(reg_v1))
        reg_d_value = simm32 + (reg_v0_value * reg_v1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Select the maximum of two floating point inputs and store the result into a vector register.
    def v_max_f16(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f16)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f16)
        arg_0_value = utils.fp16_to_fp32(arg_0_value)
        arg_1_value = utils.fp16_to_fp32(arg_1_value)
        reg_d_value = max(arg_0_value, arg_1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Select the minimum of two floating point inputs and store the result into a vector register.
    def v_min_f16(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f16)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f16)
        arg_0_value = utils.fp16_to_fp32(arg_0_value)
        arg_1_value = utils.fp16_to_fp32(arg_1_value)
        reg_d_value = min(arg_0_value, arg_1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Multiply the first input, a floating point value, by an integral power of 2 specified in the second input, a signed integer value, and store the floating point result into a vector register. Compare with the ldexp() function in C.
    def v_ldexp_f16(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f16)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_i16)
        arg_0_value = utils.fp16_to_fp32(arg_0_value)
        arg_1_value = np.int32(arg_1_value)
        reg_d_value = arg_0_value * (2**arg_1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Multiply packed FP16 values and accumulate with destination.
    def v_pk_fmac_f16(self, reg_d, reg_v0, reg_v1):
        reg_v0_value = self.registers.vgpr_f32(reg_v0)
        reg_v1_value = self.registers.vgpr_f16(reg_v1)

        # Extract the first input.
        reg_v0_value_lo = utils.fp32_to_fp16(reg_v0_value & 0xFFFF)
        reg_v0_value_hi = utils.fp32_to_fp16(reg_v0_value >> 16)

        # Extract the second input.
        reg_v1_value_lo = utils.fp32_to_fp16(reg_v1_value & 0xFFFF)
        reg_v1_value_hi = utils.fp32_to_fp16(reg_v1_value >> 16)

        reg_d_value = self.registers.vgpr_f32(reg_d)

        # Extract the destination.
        reg_d_value_lo = utils.fp32_to_fp16(reg_d_value & 0xFFFF)
        reg_d_value_hi = utils.fp32_to_fp16(reg_d_value >> 16)

        # Accumulate the result.
        reg_d_value_lo = reg_d_value_lo + (reg_v0_value_lo * reg_v1_value_lo)
        reg_d_value_hi = reg_d_value_hi + (reg_v0_value_hi * reg_v1_value_hi)
        reg_d_value = utils.fp16_to_fp32(reg_d_value_lo) | (
            utils.fp16_to_fp32(reg_d_value_hi) << 16
        )
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # VOP1 instructions
    # Do nothing.
    def v_nop(self):
        pass  # raise Exception("OP... not implemented")

    # mov data from a vector input into a vector register.
    def v_mov_b32(self, reg_d, arg_0):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_u32)
        if isinstance(arg_0_value, float):
            self.registers.set_vgpr_f32(reg_d, arg_0_value)
        else:
            self.registers.set_vgpr_u32(reg_d, arg_0_value)

    # Read the scalar value in the lowest active lane of the input vector register and store it into a scalar register.
    def v_readfirstlane_b32(self, reg_d, reg_v0):
        # This would normally go through all the enabled lanes (exec masked) and find the first one. Or force lane 0 if all lanes are disabled.
        # Our emulator only has one lane, so we can just read the value from the lane.
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_d_value = reg_v0_value
        self.registers.set_sgpr_u32(reg_d, reg_d_value)

    # Convert from a double-precision float input to a signed 32-bit integer and store the result into a vector register.
    def v_cvt_i32_f64(self, reg_d, reg_s):
        s_value = self.registers.vgpr_f64(reg_s)
        d_value = int(s_value)
        self.registers.set_vgpr_i32(reg_d, d_value)

    # Convert from a signed 32-bit integer input to a double-precision float and store the result into a vector register.
    def v_cvt_f64_i32(self, reg_d, reg_s):
        s_value = self.registers.vgpr_i32(reg_s)
        d_value = float(s_value)
        self.registers.set_vgpr_f64(reg_d, d_value)

    # Convert from a signed 32-bit integer input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_i32(self, reg_d, reg_s):
        s_value = self.registers.vgpr_i32(reg_s)
        d_value = float(s_value)
        self.registers.set_vgpr_f32(reg_d, d_value)

    # Convert from an unsigned 32-bit integer input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_u32(self, reg_d, reg_s):
        s_value = self.registers.vgpr_u32(reg_s)
        d_value = float(s_value)
        self.registers.set_vgpr_f32(reg_d, d_value)

    # Convert from a single-precision float input to an unsigned 32-bit integer and store the result into a vector register.
    def v_cvt_u32_f32(self, reg_d, reg_s):
        s_value = self.registers.vgpr_f32(reg_s)
        d_value = int(s_value)
        self.registers.set_vgpr_u32(reg_d, d_value)

    # Convert from a single-precision float input to a signed 32-bit integer and store the result into a vector register.
    def v_cvt_i32_f32(self, reg_d, reg_s):
        s_value = self.registers.vgpr_f32(reg_s)
        d_value = int(s_value)
        self.registers.set_vgpr_i32(reg_d, d_value)

    # Convert from a single-precision float input to an FP16 float and store the result into a vector register.
    def v_cvt_f16_f32(self, reg_d, reg_s):
        s_value = self.registers.vgpr_f32(reg_s)
        d_value = s_value.astype(np.float16)
        self.registers.set_vgpr_f16(reg_d, d_value)

    # Convert from an FP16 float input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_f16(self, reg_d, reg_s):
        s_value = self.registers.vgpr_f16(reg_s)
        d_value = s_value.astype(np.float32)
        self.registers.set_vgpr_f32(reg_d, d_value)

    # Convert from a single-precision float input to a signed 32-bit integer using round-to-nearest-integer semantics (ignore the default rounding mode) and store the result into a vector register.
    def v_cvt_nearest_i32_f32(self, reg_d, reg_s):
        s_value = self.registers.vgpr_f32(reg_s)
        d_value = int(round(s_value))
        self.registers.set_vgpr_i32(reg_d, d_value)

    # Convert from a single-precision float input to a signed 32-bit integer using round-down semantics (ignore the default rounding mode) and store the result into a vector register.
    def v_cvt_floor_i32_f32(self, reg_d, reg_s):
        s_value = self.registers.vgpr_f32(reg_s)
        d_value = int(np.floor(s_value))
        self.registers.set_vgpr_i32(reg_d, d_value)

    # Convert from a signed 4-bit integer to a single-precision float using an offset table and store the result into a vector register.
    def v_cvt_off_f32_i4(self, reg_d, reg_s):
        pass  # raise Exception("OP... not implemented")

    # Convert from a double-precision float input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_f64(self, reg_d, reg_s):
        s_value = self.registers.vgpr_f64(reg_s)
        d_value = float(np.float32(s_value))
        self.registers.set_vgpr_f32(reg_d, d_value)

    # Convert from a single-precision float input to a double-precision float and store the result into a vector register.
    def v_cvt_f64_f32(self, reg_d, reg_s):
        s_value = self.registers.vgpr_f32(reg_s)
        d_value = float(np.float64(s_value))
        self.registers.set_vgpr_f64(reg_d, d_value)

    # Convert an unsigned byte in byte 0 of the input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_ubyte0(self, reg_d, reg_s):
        byte_value = self.registers.vgpr_u32(reg_s) & 0xFF  # Extract byte 0
        d_value = float(byte_value)
        self.registers.set_vgpr_f32(reg_d, d_value)

    # Convert an unsigned byte in byte 1 of the input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_ubyte1(self, reg_d, reg_s):
        byte_value = (self.registers.vgpr_u32(reg_s) >> 8) & 0xFF  # Extract byte 1
        d_value = float(byte_value)
        self.registers.set_vgpr_f32(reg_d, d_value)

    # Convert an unsigned byte in byte 2 of the input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_ubyte2(self, reg_d, reg_s):
        byte_value = (self.registers.vgpr_u32(reg_s) >> 16) & 0xFF  # Extract byte 2
        d_value = float(byte_value)
        self.registers.set_vgpr_f32(reg_d, d_value)

    # Convert an unsigned byte in byte 3 of the input to a single-precision float and store the result into a vector register.
    def v_cvt_f32_ubyte3(self, reg_d, reg_s):
        byte_value = (self.registers.vgpr_u32(reg_s) >> 24) & 0xFF  # Extract byte 3
        d_value = float(byte_value)
        self.registers.set_vgpr_f32(reg_d, d_value)

    # Convert from a double-precision float input to an unsigned 32-bit integer and store the result into a vector register.
    def v_cvt_u32_f64(self):
        pass  # raise Exception("OP... not implemented")

    # Convert from an unsigned 32-bit integer input to a double-precision float and store the result into a vector register.
    def v_cvt_f64_u32(self):
        pass  # raise Exception("OP... not implemented")

    # Compute the integer part of a double-precision float input with round-toward-zero semantics and store the result in floating point format into a vector register.
    def v_trunc_f64(self):
        pass  # raise Exception("OP... not implemented")

    # Round the double-precision float input up to next integer and store the result in floating point format into a vector register.
    def v_ceil_f64(self):
        pass  # raise Exception("OP... not implemented")

    # Round the double-precision float input to the nearest even integer and store the result in floating point format into a vector register.
    def v_rndne_f64(self):
        pass  # raise Exception("OP... not implemented")

    # Round the double-precision float input down to previous integer and store the result in floating point format into a vector register.
    def v_floor_f64(self):
        pass  # raise Exception("OP... not implemented")

    # Flush the VALU destination cache.
    def v_pipeflush(self):
        pass  # raise Exception("OP... not implemented")

    # mov data to a VGPR.
    def v_mov_b16(self):
        pass  # raise Exception("OP... not implemented")

    # Compute the fractional portion of a single-precision float input and store the result in floating point format into a vector register.
    def v_fract_f32(self):
        pass  # raise Exception("OP... not implemented")

    # Compute the integer part of a single-precision float input with round-toward-zero semantics and store the result in floating point format into a vector register.
    def v_trunc_f32(self):
        pass  # raise Exception("OP... not implemented")

    # Round the single-precision float input up to next integer and store the result in floating point format into a vector register.
    def v_ceil_f32(self):
        pass  # raise Exception("OP... not implemented")

    # Round the single-precision float input to the nearest even integer and store the result in floating point format into a vector register.
    def v_rndne_f32(self, reg_d, arg_0):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f32)
        d_value = round(arg_0_value)
        self.registers.set_vgpr_f32(reg_d, d_value)

    # Round the single-precision float input down to previous integer and store the result in floating point format into a vector register.
    def v_floor_f32(self):
        pass  # raise Exception("OP... not implemented")

    # Calculate 2 raised to the power of the single-precision float input and store the result into a vector register.
    def v_exp_f32(self):
        pass  # raise Exception("OP... not implemented")

    # Calculate the base 2 logarithm of the single-precision float input and store the result into a vector register.
    def v_log_f32(self, reg_d, arg_0):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f32)
        neg_zero = 0x80000000
        pos_zero = 0x00000000
        neg_inf = 0xFF800000
        pos_inf = 0x7F800000
        nan = 0xFFC00000
        if (arg_0_value == neg_zero) or (arg_0_value == pos_zero):
            # log(-0.0) = -INF
            # log(+0.0) = -INF
            reg_d_value = neg_inf
        elif (arg_0_value == neg_inf) or (arg_0_value < 0) or (arg_0_value == nan):
            # log(-INF) = NAN
            # log(-1) = NAN
            # log(NAN) = NAN
            reg_d_value = nan
        elif arg_0_value == pos_inf:
            # log(+INF) = +INF
            reg_d_value = pos_inf
        else:
            reg_d_value = math.log2(arg_0_value)

        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Calculate the reciprocal of the single-precision float input using IEEE rules and store the result into a vector register.
    def v_rcp_f32(self, reg_d, arg_0):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f32)
        d_value = 1 / arg_0_value
        self.registers.set_vgpr_f32(reg_d, d_value)

    # Calculate the reciprocal of the vector float input in a manner suitable for integer division and store the result into a vector register. This opcode is intended for use as part of an integer division macro.
    def v_rcp_iflag_f32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_rsq_f32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_rcp_f64(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_rsq_f64(self):
        pass  # raise Exception("OP... not implemented")

    # Calculate the square root of the single-precision float input using IEEE rules and store the result into a vector register.
    def v_sqrt_f32(self, reg_d, arg_0):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f32)
        d_value = math.sqrt(arg_0_value)
        self.registers.set_vgpr_f32(reg_d, d_value)

    #
    def v_sqrt_f64(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_sin_f32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cos_f32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_not_b32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_bfrev_b32(self):
        pass  # raise Exception("OP... not implemented")

    # Count the number of leading "0" bits before the first "1" in a vector input and store the result into a vector register. Store -1 if there are no "1" bits.
    def v_clz_i32_u32(self, reg_d, reg_s):
        s_value = self.registers.vgpr_u32(reg_s)
        d_value = -1
        for i in range(32):
            if s_value & (1 << (31 - i)):
                d_value = i
                break
        self.registers.set_vgpr_i32(reg_d, d_value)

    #
    def v_ctz_i32_b32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cls_i32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_frexp_exp_i32_f64(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_frexp_mant_f64(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_fract_f64(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_frexp_exp_i32_f32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_frexp_mant_f32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_movreld_b32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_movrels_b32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_movrelsd_b32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_movrelsd_2_b32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cvt_f16_u16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cvt_f16_i16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cvt_u16_f16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cvt_i16_f16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_rcp_f16(self):
        pass  # raise Exception("OP... not implemented")

    # Calculate the square root of the half-precision float input using IEEE rules and store the result into a vector register.
    def v_sqrt_f16(self, reg_d, arg_0):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f16)
        d_value = math.sqrt(arg_0_value)
        self.registers.set_vgpr_f16(reg_d, d_value)

    #
    def v_rsq_f16(self):
        pass  # raise Exception("OP... not implemented")

    # Calculate the base 2 logarithm of the half-precision float input and store the result into a vector register
    def v_log_f16(self, reg_d, arg_0):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f16)
        neg_zero = 0x8000
        pos_zero = 0x0000
        neg_inf = 0xFC00
        pos_inf = 0x7C00
        nan = 0xFE00
        if (arg_0_value == neg_zero) or (arg_0_value == pos_zero):
            # log(-0.0) = -INF
            # log(+0.0) = -INF
            reg_d_value = neg_inf
        elif (arg_0_value == neg_inf) or (arg_0_value < 0) or (arg_0_value == nan):
            # log(-INF) = NAN
            # log(-1) = NAN
            # log(NAN) = NAN
            reg_d_value = nan
        elif arg_0_value == pos_inf:
            # log(+INF) = +INF
            reg_d_value = pos_inf
        else:
            reg_d_value = math.log2(arg_0_value)

        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Calculate 2 raised to the power of the half-precision float input and store the result into a vector register.
    def v_exp_f16(self, reg_d, arg_0):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f16)
        d_value = 2**arg_0_value
        self.registers.set_vgpr_f16(reg_d, d_value)

    #
    def v_frexp_mant_f16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_frexp_exp_i16_f16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_floor_f16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_ceil_f16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_trunc_f16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_rndne_f16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_fract_f16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_sin_f16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cos_f16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_sat_pk_u8_i16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cvt_norm_i16_f16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cvt_norm_u16_f16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_swap_b32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_swap_b16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_permlane64_b32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_swaprel_b32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_not_b16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cvt_i32_i16(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cvt_u32_u16(self):
        pass  # raise Exception("OP... not implemented")

    # VOP3 instructions
    # IEEE numeric class function specified in S1.u, performed on S0.f.
    # The function reports true if the floating point value is any of the numeric types selected in S1.u according to the
    # following list:
    # S1.u[0] -- value is a signaling NAN.
    # S1.u[1] -- value is a quiet NAN.
    # S1.u[2] -- value is negative infinity.
    # S1.u[3] -- value is a negative normal value.
    # S1.u[4] -- value is a negative denormal value.
    # S1.u[5] -- value is negative zero.
    # S1.u[6] -- value is positive zero.
    # S1.u[7] -- value is a positive denormal value.
    # S1.u[8] -- value is a positive normal value.
    # S1.u[9] -- value is positive infinity.
    def v_cmp_class_f32(self, arg_0, arg_1, arg_2):
        arg_1_value = np.uint32(self.try_get_literal(arg_1, self.registers.vgpr_f32))
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_u32)
        result = 0

        nan = 0xFFC00000
        quite_nan = 0x7FC00000
        neg_inf = 0xFF800000
        pos_inf = 0x7F800000
        neg_zero = 0x80000000
        pos_zero = 0x00000000

        if arg_2_value & (0x1 << 0):
            # Signaling NAN
            result = arg_1_value == nan
        elif arg_2_value & (0x1 << 1):
            # Quiet NAN
            result = arg_1_value == quite_nan
        elif arg_2_value & (0x1 << 2):
            # Negative infinity
            result = arg_1_value == neg_inf
        elif arg_2_value & (0x1 << 3):
            # Negative normal value
            result = arg_1_value | 0x80000000
        elif arg_2_value & (0x1 << 4):
            # Negative denormal value
            result = arg_1_value | 0x80000000
        elif arg_2_value & (0x1 << 5):
            # Negative zero
            result = arg_1_value == neg_zero
        elif arg_2_value & (0x1 << 6):
            # Positive zero
            result = arg_1_value == pos_zero
        elif arg_2_value & (0x1 << 7):
            # Positive denormal value
            result = arg_1_value & 0x7FFFFFFF
        elif arg_2_value & (0x1 << 8):
            # Positive normal value
            result = arg_1_value & 0x7FFFFFFF
        elif arg_2_value & (0x1 << 9):
            # Positive infinity
            result = arg_1_value == pos_inf

        # Set vcc/dst
        if not isinstance(arg_0, str):
            self.registers.set_sgpr_u32(arg_0, result)
        else:
            if arg_0 == "vcc_lo":
                result = (result & 0xFFFF) | (self.registers.vcc & 0xFFFF0000)
            elif arg_0 == "vcc_hi":
                result = (result << 16) | (self.registers.vcc & 0xFFFF)
            else:
                raise Exception(
                    "Invalid argument to {}".format(
                        inspect.currentframe().f_code.co_name
                    )
                )

            self.registers.vcc = result

    # Bitfield extract. Extract unsigned bitfield from first operand using field offset in second operand and field size in third operand.
    # D0.u = ((S0.u >> S1.u[4 : 0].u) & 32'U((1 << S2.u[4 : 0].u) - 1))
    def v_bfe_u32(self, reg_d, arg_0, arg_1, arg_2):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_u32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_u32) & 0x1F
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_u32) & 0x1F
        d_value = (arg_0_value >> arg_1_value) & ((1 << arg_2_value) - 1)
        self.registers.set_vgpr_u32(reg_d, d_value)

    def unpack_f32(self, arg_0):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f32)
        arg_0_value_lo = np.float16(np.uint32(arg_0_value) & 0xFFFF)
        arg_0_value_hi = np.float16(np.uint32(arg_0_value) >> 16)
        return arg_0_value_lo, arg_0_value_hi

    def pack_f32(self, lo, hi):
        lo = np.uint32(lo)
        hi = np.uint32(hi)
        fused = lo | (hi << 16)
        return np.float32(fused)

    # v_fma_f32 could call with either a literal or a register. We need to handle both cases.
    # Fused single precision multiply add.
    def v_fma_f32(self, reg_d, reg_v0, arg_0, arg_1):
        # Unpack the input register
        reg_v0_value_lo, reg_v0_value_hi = self.unpack_f32(reg_v0)

        # Unpack the literal or register.
        imm_0_value_lo, imm_0_value_hi = self.unpack_f32(arg_0)
        imm_1_value_lo, imm_1_value_hi = self.unpack_f32(arg_1)

        # Perform the fused multiply add.
        reg_d_value_lo = reg_v0_value_lo * imm_0_value_lo + imm_1_value_lo
        reg_d_value_hi = reg_v0_value_hi * imm_0_value_hi + imm_1_value_hi

        # Pack the result.
        reg_d_value = self.pack_f32(reg_d_value_lo, reg_d_value_hi)
        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # Align a value to the specified bit position.
    # ! S0 carries the MSBs and S1 carries the LSBs of the value being aligned
    # D0.u = 32'U(({ S0.u, S1.u } >> S2.u[4 : 0].u) & 0xffffffffLL)
    def v_alignbit_b32(self, reg_d, arg_0, arg_1, arg_2):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_u32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_u32)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_u32) & 0x1F

        reg_d_value = ((arg_0_value << 32) | arg_1_value) >> arg_2_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Calculate the bitwise XOR of three vector inputs and store the result into a vector register.
    def v_xor3_b32(self, reg_d, arg_0, arg_1, arg_2):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_u32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_u32)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_u32)
        reg_d_value = arg_0_value ^ arg_1_value ^ arg_2_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Given a shift count in the second input, calculate the logical shift left of the first input, then add the third input to the intermediate result, then store the final result into a vector register.
    # D0.u = (S0.u << S1.u[4 : 0].u) + S2.u
    def v_lshl_add_u32(self, reg_d, arg_0, arg_1, arg_2):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_u32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_u32) & 0x1F
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_u32)

        reg_d_value = (arg_0_value << arg_1_value) + arg_2_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Add the first two integer inputs, then given a shift count in the third input, calculate the logical shift left of the intermediate result, then store the final result into a vector register.
    # D0.u = ((S0.u + S1.u) << S2.u[4 : 0].u)
    def v_add_lshl_u32(self, reg_d, arg_0, arg_1, arg_2):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_u32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_u32)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_u32) & 0x1F

        reg_d_value = (arg_0_value + arg_1_value) << arg_2_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Fused half precision multiply add.
    def v_fma_f16(self, reg_d, reg_v0, arg_0, arg_1):
        # Unpack the input register
        reg_v0_value_lo, reg_v0_value_hi = self.unpack_f32(reg_v0)

        # Unpack the literal or register.
        imm_0_value_lo, imm_0_value_hi = self.unpack_f32(arg_0)
        imm_1_value_lo, imm_1_value_hi = self.unpack_f32(arg_1)

        # Perform the fused multiply add.
        reg_d_value_lo = reg_v0_value_lo * imm_0_value_lo + imm_1_value_lo
        reg_d_value_hi = reg_v0_value_hi * imm_0_value_hi + imm_1_value_hi

        # Pack the result.
        reg_d_value = self.pack_f32(reg_d_value_lo, reg_d_value_hi)
        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Half precision division fixup.
    # S0 = Quotient, S1 = Denominator, S2 = Numerator.
    # Given a numerator, denominator, and quotient from a divide, this opcode detects and applies specific case
    # numerics, touching up the quotient if necessary. This opcode also generates invalid, denorm and divide by
    # zero exceptions caused by the division.
    # sign_out = (sign(S1.f16) ^ sign(S2.f16));
    # if isNAN(64'F(S2.f16)) then
    #     D0.f16 = 16'F(cvtToQuietNAN(64'F(S2.f16)))
    # elsif isNAN(64'F(S1.f16)) then
    #     D0.f16 = 16'F(cvtToQuietNAN(64'F(S1.f16)))
    # elsif ((64'F(S1.f16) == 0.0) && (64'F(S2.f16) == 0.0)) then
    #     // 0/0
    #     D0.f16 = 16'F(0xfe00)
    # elsif ((64'F(abs(S1.f16)) == +INF) && (64'F(abs(S2.f16)) == +INF)) then
    #     // inf/inf
    #     D0.f16 = 16'F(0xfe00)
    # elsif ((64'F(S1.f16) == 0.0) || (64'F(abs(S2.f16)) == +INF)) then
    #     // x/0, or inf/y
    #     D0.f16 = sign_out ? -INF.f16 : +INF.f16
    # elsif ((64'F(abs(S1.f16)) == +INF) || (64'F(S2.f16) == 0.0)) then
    #     // x/inf, 0/y
    #     D0.f16 = sign_out ? -16'0.0 : 16'0.0
    # else
    #     D0.f16 = sign_out ? -abs(S0.f16) : abs(S0.f16)
    # endif
    def v_div_fixup_f16(self, reg_d, arg_0, arg_1, arg_2):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f16)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f16)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_f16)

        nan = 0xFE00
        neg_inf = 0xFC00
        pos_inf = 0x7C00
        neg_zero = 0x8000
        pos_zero = 0x0000

        sign_out = (arg_1_value < 0) ^ (arg_2_value < 0)

        if arg_1_value == nan:
            # Nan / anything = Nan
            reg_d_value = np.float16(nan)
        elif arg_2_value == nan:
            # Anything / Nan = Nan
            reg_d_value = np.float16(nan)
        elif (arg_1_value == 0) and (arg_2_value == 0):
            # 0 / 0 = Nan
            reg_d_value = np.float16(nan)
        elif ((arg_1_value == pos_inf) or (arg_1_value == neg_inf)) and (
            (arg_2_value == pos_inf) or (arg_2_value == neg_inf)
        ):
            # (+/-)Inf / (+/-)Inf = Nan
            reg_d_value = np.float16(nan)
        elif (arg_1_value == 0) or (
            (arg_2_value == pos_inf) or (arg_2_value == neg_inf)
        ):
            # x / 0 = Inf
            # (+/-)Inf / y = Inf
            reg_d_value = np.float16(neg_inf) if sign_out else np.float16(pos_inf)
        elif ((arg_1_value == pos_inf) or (arg_1_value == neg_inf)) or (
            arg_2_value == 0
        ):
            # x / (+/-)Inf = 0
            # 0 / y = 0
            reg_d_value = np.float16(neg_zero) if sign_out else np.float16(pos_zero)
        else:
            reg_d_value = (
                np.float16(-abs(arg_0_value))
                if sign_out
                else np.float16(abs(arg_0_value))
            )

        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # Calculate bitwise AND on the first two vector inputs, then compute the bitwise OR of the intermediate result and the third vector input, then store the result into a vector register.
    # ISA does not imply this format of the arguments, but it is the only one used.
    def v_and_or_b32(self, reg_d, reg_v0, reg_s0, arg_0):
        reg_v0_value = self.registers.vgpr_u32(reg_v0)
        reg_s0_value = self.registers.sgpr_u32(reg_s0)
        reg_d_value = (reg_v0_value & reg_s0_value) | arg_0
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    # Calculate the bitwise OR of three vector inputs and store the result into a vector register.
    def v_or3_b32(self, reg_d, arg_0, arg_1, arg_2):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_u32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_u32)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_u32)
        reg_d_value = arg_0_value | arg_1_value | arg_2_value
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

    #
    def v_mbcnt_lo_u32_b32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_mul_lo_u32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_mul_hi_u32(self):
        pass  # raise Exception("OP... not implemented")

    # Given a shift count in the first vector input, calculate the logical shift left of the second vector input and store the result into a vector register
    def v_lshlrev_b16(self, reg_d, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_u16) & 0xF
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_u16)

        reg_d_value = arg_1_value << arg_0_value
        self.registers.set_vgpr_u16(reg_d, reg_d_value)

    # Given a shift count in the first vector input, calculate the logical shift left of the second vector input and store the result into a vector register.
    # D0.u64 = (S1.u64 << S0[5 : 0].u)
    # v_lshlrev_b64 v[0:1], 1, v[9:10]
    def v_lshlrev_b64(self, reg_d0, reg_d1, arg_0, arg_1, arg_2):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_u32) & 0x3F
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_u32)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_u32)

        # Combine the two 32-bit values into a single 64-bit value.
        input_value = int(arg_1_value) | (int(arg_2_value) << 32)
        reg_d_value = input_value << arg_0_value
        reg_d0_value = np.uint32(reg_d_value & 0xFFFFFFFF)
        reg_d1_value = np.uint32(reg_d_value >> 32) & 0xFFFFFFFF

        self.registers.set_vgpr_u32(reg_d0, reg_d0_value)
        self.registers.set_vgpr_u32(reg_d1, reg_d1_value)

    #
    def v_writelane_b32(self):
        pass  # raise Exception("OP... not implemented")

    # Fused-multiply-add of single-precision values with MIX encoding.
    # Size and location of S0, S1 and S2 controlled by OPSEL: 0=src[31:0], 1=src[31:0], 2=src[15:0], 3=src[31:16]. Also,
    # for FMA_MIX, the NEG_HI field acts instead as an absolute-value modifier.
    def v_fma_mix_f32(
        self, reg_d, arg_0, arg_1, arg_2, opsel_0=0, opsel_1=0, opsel_2=0
    ):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f32)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_f32)
        inputs = [arg_0_value, arg_1_value, arg_2_value]
        opsels = [opsel_0, opsel_1, opsel_2]
        for i in range(3):
            # Unpack the literal or register.
            imm_value_lo, imm_value_hi = self.unpack_f32(inputs[i])
            opsel_lo = opsels[i] & 0x1
            opsel_hi = (opsels[i] >> 1) & 0x1
            if not opsel_hi:
                # 00, 01: Use the packed value.
                inputs[i] = self.pack_f32(imm_value_lo, imm_value_hi)
            elif not opsel_lo:
                # 10: Use the lower half.
                inputs[i] = imm_value_lo
            else:
                # 11: Use the upper half.
                inputs[i] = imm_value_hi

        # Perform the fused multiply add.
        reg_d_value = inputs[0] * inputs[1] + inputs[2]

        self.registers.set_vgpr_f32(reg_d, reg_d_value)

    # VOP3P instructions
    # Fused-multiply-add of FP16 values with MIX encoding, result stored in low 16 bits of destination.
    # Size and location of S0, S1 and S2 controlled by OPSEL: 0=src[31:0], 1=src[31:0], 2=src[15:0], 3=src[31:16]. Also,
    # for FMA_MIX, the NEG_HI field acts instead as an absolute-value modifier.
    # declare in : 32'F[3];
    # declare S : 32'B[3];
    # for i in 0 : 2 do
    #   if !OPSEL_HI.u3[i] then
    #       in[i] = S[i].f
    #   elsif OPSEL.u3[i] then
    #       in[i] = f16_to_f32(S[i][31 : 16].f16)
    #   else
    #       in[i] = f16_to_f32(S[i][15 : 0].f16)
    #   endif
    # endfor;
    # D0[15 : 0].f16 = f32_to_f16(fma(in[0], in[1], in[2]))
    def v_fma_mixlo_f16(
        self, reg_d, arg_0, arg_1, arg_2, opsel_0=0, opsel_1=0, opsel_2=0
    ):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f32)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_f32)
        inputs = [arg_0_value, arg_1_value, arg_2_value]
        opsels = [opsel_0, opsel_1, opsel_2]
        for i in range(3):
            # Unpack the literal or register.
            imm_value_lo, imm_value_hi = self.unpack_f32(inputs[i])
            opsel_lo = opsels[i] & 0x1
            opsel_hi = (opsels[i] >> 1) & 0x1
            if not opsel_hi:
                # 00, 01: Use the packed value.
                inputs[i] = self.pack_f32(imm_value_lo, imm_value_hi)
            elif not opsel_lo:
                # 10: Use the lower half.
                inputs[i] = imm_value_lo
            else:
                # 11: Use the upper half.
                inputs[i] = imm_value_hi

        # Perform the fused multiply add.
        reg_d_value = inputs[0] * inputs[1] + inputs[2]
        # Convert to half precision.
        reg_d_value = utils.fp32_to_fp16(reg_d_value)

        self.registers.set_vgpr_f16(reg_d, reg_d_value)

    # VOP3SD instructions
    #
    def v_mad_u64_u32(self, vdst0, vdst1, sdst, src0, src1, src2, src3=0):
        # src0_val, src1_val, src2_val, src3_val = src0, src1, src2, src3
        # if src0 < 256:
        #   src0_val = self.registers.vgpr_u32(src0)
        # if src1 < 256:
        #   src1_val = self.register.vgpr_u32(src1)
        # if src2 < 256:

        # src1_val = src1
        pass  # raise Exception("OP... not implemented")

    # Add two unsigned inputs, store the result into a vector register and store the carry-out mask into a scalar register.
    # Example: v_add_co_u32 v0, vcc_lo, s4, v0
    # In the example vcc_lo will fail to parse and is interpreted as only storing the carry-out mask into vcc.
    def v_add_co_u32(self, reg_d, arg_0, arg_1, arg_2):
        arg_1_value = self.try_get_literal(arg_1, self.registers.sgpr_u32)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_u32)

        reg_d_value = arg_1_value + arg_2_value
        carry_out = 1 if reg_d_value > 0xFFFFFFFF else 0
        self.registers.set_vgpr_u32(reg_d, reg_d_value)

        # Set vcc
        if isinstance(arg_0, str):
            if arg_0 == "vcc_lo":
                self.registers.vcc = (self.registers.vcc & 0xFFFF0000) | carry_out
            elif arg_0 == "vcc_hi":
                self.registers.vcc = (self.registers.vcc & 0xFFFF) | (carry_out << 16)
            else:
                raise Exception(
                    "Invalid argument to {}".format(
                        inspect.currentframe().f_code.co_name
                    )
                )
        else:
            self.registers.set_sgpr_u32(arg_0, carry_out)

    #
    def v_sub_co_u32(self):
        pass  # raise Exception("OP... not implemented")

    # Return 1 iff A less than B.
    def v_cmp_lt_f32(self, arg_0, arg_1, arg_2):
        # The first argument is the destination register.
        # But this may parse as a string of "vcc" if the destination register is omitted.
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f32)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_f32)

        result = arg_1_value < arg_2_value

        if not isinstance(arg_0, str):
            self.registers.set_sgpr_u32(arg_0, result)
        else:
            if arg_0 == "vcc_lo":
                result = (result & 0xFFFF) | (self.registers.vcc & 0xFFFF0000)
            elif arg_0 == "vcc_hi":
                result = (result << 16) | (self.registers.vcc & 0xFFFF)
            else:
                raise Exception(
                    "Invalid argument to {}".format(
                        inspect.currentframe().f_code.co_name
                    )
                )

            self.registers.vcc = result

    # Return 1 iff A greater than B.
    # D0 = VCC in VOPC encoding.
    def v_cmp_gt_f32(self, arg_0, arg_1, arg_2):
        # The first argument is the destination register.
        # But this may parse as a string of "vcc" if the destination register is omitted.
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f32)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_f32)

        result = arg_1_value > arg_2_value

        if isinstance(arg_0, str):
            if arg_0 == "vcc_lo":
                result = (result & 0xFFFF) | (self.registers.vcc & 0xFFFF0000)
            elif arg_0 == "vcc_hi":
                result = (result << 16) | (self.registers.vcc & 0xFFFF)
            else:
                raise Exception(
                    "Invalid argument to {}".format(
                        inspect.currentframe().f_code.co_name
                    )
                )

            self.registers.vcc = result
        else:
            self.registers.set_sgpr_u32(arg_0, result)

    # Return 1 iff A greater than or equal to B.
    def v_cmp_ge_f32(self, arg_0, arg_1, arg_2):
        # The first argument is the destination register.
        # But this may parse as a string of "vcc" if the destination register is omitted.
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f32)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_f32)

        result = arg_1_value >= arg_2_value

        if not isinstance(arg_0, str):
            self.registers.set_sgpr_u32(arg_0, result)
        else:
            if "_lo" in arg_0:
                result = (result & 0xFFFF) | (self.registers.vcc & 0xFFFF0000)
            elif "_hi" in arg_0:
                result = (result << 16) | (self.registers.vcc & 0xFFFF)

            self.registers.vcc = result

    # Return 1 iff A less than B.
    def v_cmp_lt_u32(self, arg_0, arg_1, arg_2):
        # The first argument is the destination register.
        # But this may parse as a string of "vcc" if the destination register is omitted.
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_u32)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_u32)

        result = arg_1_value < arg_2_value

        if not isinstance(arg_0, str):
            self.registers.set_sgpr_u32(arg_0, result)
        else:
            if "_lo" in arg_0:
                result = (result & 0xFFFF) | (self.registers.vcc & 0xFFFF0000)
            elif "_hi" in arg_0:
                result = (result << 16) | (self.registers.vcc & 0xFFFF)

            self.registers.vcc = result

    # VOPC instructions
    # Return 1 iff A equal to B.
    # D0 = VCC in VOPC encoding.
    def v_cmp_eq_u32(self, arg_0, arg_1, arg_2):
        # The first argument is the destination register.
        # But this may parse as a string of "vcc" if the destination register is omitted.
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_u32)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_u32)

        result = arg_1_value == arg_2_value

        if not isinstance(arg_0, str):
            self.registers.set_sgpr_u32(arg_0, result)
        else:
            if "_lo" in arg_0:
                result = (result & 0xFFFF) | (self.registers.vcc & 0xFFFF0000)
            elif "_hi" in arg_0:
                result = (result << 16) | (self.registers.vcc & 0xFFFF)

            self.registers.vcc = result

    #
    def v_cmp_ne_u32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cmp_lt_u64(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cmp_eq_u64(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cmp_gt_u64(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cmp_ne_u64(self):
        pass  # raise Exception("OP... not implemented")

    # Return 1 iff A not greater than B.
    def v_cmpx_ngt_f32(self, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_f32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f32)

        self.registers.exec = arg_0_value <= arg_1_value

    # IEEE numeric class function specified in S1.u, performed on S0.f16.
    # The function reports true if the floating point value is any of the numeric types selected in S1.u according to the
    # following list:
    # S1.u[0] -- value is a signaling NAN.
    # S1.u[1] -- value is a quiet NAN.
    # S1.u[2] -- value is negative infinity.
    # S1.u[3] -- value is a negative normal value.
    # S1.u[4] -- value is a negative denormal value.
    # S1.u[5] -- value is negative zero.
    # S1.u[6] -- value is positive zero.
    # S1.u[7] -- value is a positive denormal value.
    # S1.u[8] -- value is a positive normal value.
    # S1.u[9] -- value is positive infinity.
    def v_cmp_class_f16(self, arg_0, arg_1, arg_2):
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_f16)
        arg_2_value = self.try_get_literal(arg_2, self.registers.vgpr_u32)
        result = 0

        nan = 0xFE00
        quite_nan = 0x7E00
        neg_inf = 0xFC00
        pos_inf = 0x7C00
        neg_zero = 0x8000
        pos_zero = 0x0000

        if arg_2_value & (0x1 << 0):
            # Signaling NAN
            result = arg_1_value == nan
        elif arg_2_value & (0x1 << 1):
            # Quiet NAN
            result = arg_1_value == quite_nan
        elif arg_2_value & (0x1 << 2):
            # Negative infinity
            result = arg_1_value == neg_inf
        elif arg_2_value & (0x1 << 3):
            # Negative normal value
            result = arg_1_value | 0x8000
        elif arg_2_value & (0x1 << 4):
            # Negative denormal value
            result = arg_1_value | 0x8000
        elif arg_2_value & (0x1 << 5):
            # Negative zero
            result = arg_1_value == neg_zero
        elif arg_2_value & (0x1 << 6):
            # Positive zero
            result = arg_1_value == pos_zero
        elif arg_2_value & (0x1 << 7):
            # Positive denormal value
            result = arg_1_value & 0x7FFF
        elif arg_2_value & (0x1 << 8):
            # Positive normal value
            result = arg_1_value & 0x7FFF
        elif arg_2_value & (0x1 << 9):
            # Positive infinity
            result = arg_1_value == pos_inf

        # Set vcc/dst
        if not isinstance(arg_0, str):
            self.registers.set_sgpr_u32(arg_0, result)
        else:
            if arg_0 == "vcc_lo":
                result = (result & 0xFFFF) | (self.registers.vcc & 0xFFFF0000)
            elif arg_0 == "vcc_hi":
                result = (result << 16) | (self.registers.vcc & 0xFFFF)
            else:
                raise Exception(
                    "Invalid argument to {}".format(
                        inspect.currentframe().f_code.co_name
                    )
                )

            self.registers.vcc = result

    # Return 1 iff A equal to B.
    # Write only EXEC. SDST must be set to EXEC_LO. Signal 'invalid' on sNAN's, and also on qNAN's if clamp is set.
    def v_cmpx_eq_u32(self, arg_0, arg_1):
        arg_0_value = self.try_get_literal(arg_0, self.registers.vgpr_u32)
        arg_1_value = self.try_get_literal(arg_1, self.registers.vgpr_u32)

        self.registers.exec = arg_0_value == arg_1_value

    #
    def v_cmpx_gt_u32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cmpx_ne_u32(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cmpx_ne_u64(self):
        pass  # raise Exception("OP... not implemented")

    #
    def v_cmp_eq_u16(self):
        pass  # raise Exception("OP... not implemented")
