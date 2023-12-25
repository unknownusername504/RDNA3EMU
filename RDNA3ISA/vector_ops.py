import utils
from registers import Registers as Re
class VectorOps:
    def __init__(self, registers: Re):
        self.registers = registers
    def v_cndmask_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_type = self.get_register_type(reg_s0)
        reg_s1_type = self.get_register_type(reg_s1)
        reg_s0_value = self.registers.get_register(reg_s0, signed=False, size=32, reg_type=reg_s0_type)
        reg_s1_value = self.registers.get_register(reg_s1, signed=False, size=32, reg_type=reg_s1_type)
        reg_vcc_value = self.get_vcc_value()
        reg_d_value = reg_s0_value if reg_vcc_value == 1 else reg_s1_value
        reg_d_type = reg_s0_type if reg_s0_type == reg_s1_type else reg_s1_type
        self.registers.set_register(reg_d, reg_d_value, signed=False, size=32, reg_type=reg_d_type)

    
    # Dot product of packed FP16 values, accumulate with destination.
    def v_dot2acc_f32_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s0_value_low = utils.fp16_to_fp32(reg_s0_value & 0xFFFF)
        reg_s0_value_high = utils.fp16_to_fp32(reg_s0_value >> 16)
        reg_s1_value_low = utils.fp16_to_fp32(reg_s1_value & 0xFFFF)
        reg_s1_value_high = utils.fp16_to_fp32(reg_s1_value >> 16)
        reg_d_value = (reg_s0_value_low * reg_s1_value_low) + (reg_s0_value_high * reg_s1_value_high)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Add two floating point inputs and store the result into a vector register.
    def v_add_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = reg_s0_value + reg_s1_value
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Subtract the second floating point input from the first input and store the result into a vector register.
    def v_sub_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = reg_s0_value - reg_s1_value
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Subtract the first floating point input from the second input and store the result into a vector register.
    def v_subrev_f32(self, reg_d, reg_s0, reg_s1):
        self.v_sub_f32(reg_d, reg_s1, reg_s0)
    
    # Multiply two single-precision values and accumulate the result with the destination. Follows DX9 rules where 0.0 times anything produces 0.0 (this is not IEEE compliant).
    def v_fmac_dx9_zero_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = self.registers.get_register(reg_d, signed=None, size=32, reg_type="VGPR_FLOAT")
        if reg_s0_value == 0 or reg_s1_value == 0:
            reg_d_value = 0
        else:
            reg_d_value = reg_d_value + (reg_s0_value * reg_s1_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply two floating point inputs and store the result in a vector register. Follows DX9 rules where 0.0 times anything produces 0.0 (this differs from other APIs when the other input is infinity or NaN).
    def v_mul_dx9_zero_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        if reg_s0_value == 0 or reg_s1_value == 0:
            reg_d_value = 0
        else:
            reg_d_value = reg_s0_value * reg_s1_value
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply two floating point inputs and store the result into a vector register.
    def v_mul_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = reg_s0_value * reg_s1_value
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply two signed 24 bit integer inputs and store the result as a signed 32 bit integer into a vector register.
    def v_mul_i32_i24(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=True, size=24, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=True, size=24, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value * reg_s1_value
        self.registers.set_register(reg_d, reg_d_value, signed=True, size=32, reg_type="VGPR_INT")
    
    # Multiply two signed 24 bit integer inputs and store the high 32 bits of the result as a signed 32 bit integer into a vector register.
    def v_mul_hi_i32_i24(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=True, size=24, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=True, size=24, reg_type="VGPR_INT")
        reg_d_value = (reg_s0_value * reg_s1_value) >> 32
        self.registers.set_register(reg_d, reg_d_value, signed=True, size=32, reg_type="VGPR_INT")
    
    # Multiply two unsigned 24 bit integer inputs and store the result as a unsigned 32 bit integer into a vector register.
    def v_mul_u32_u24(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=False, size=24, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=False, size=24, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value * reg_s1_value
        self.registers.set_register(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Multiply two unsigned 24 bit integer inputs and store the high 32 bits of the result as a unsigned 32 bit integer into a vector register.
    def v_mul_hi_u32_u24(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=False, size=24, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=False, size=24, reg_type="VGPR_INT")
        reg_d_value = (reg_s0_value * reg_s1_value) >> 32
        self.registers.set_register(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Select the minimum of two floating point inputs and store the result into a vector register
    def v_min_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = min(reg_s0_value, reg_s1_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Select the maximum of two floating point inputs and store the result into a vector register
    def v_max_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = max(reg_s0_value, reg_s1_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")    
    
    # Select the minimum of two signed integers and store the selected value into a vector register.
    def v_min_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=True, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=True, size=32, reg_type="VGPR_INT")
        reg_d_value = min(reg_s0_value, reg_s1_value)
        self.registers.set_register(reg_d, reg_d_value, signed=True, size=32, reg_type="VGPR_INT")
    
    # Select the maximum of two signed integers and store the selected value into a vector register.
    def v_max_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=True, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=True, size=32, reg_type="VGPR_INT")
        reg_d_value = max(reg_s0_value, reg_s1_value)
        self.registers.set_register(reg_d, reg_d_value, signed=True, size=32, reg_type="VGPR_INT")
    
    # Select the minimum of two unsigned integers and store the selected value into a vector register.
    def v_min_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = min(reg_s0_value, reg_s1_value)
        self.registers.set_register(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Select the maximum of two unsigned integers and store the selected value into a vector register.
    def v_max_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = max(reg_s0_value, reg_s1_value)
        self.registers.set_register(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Given a shift count in the first vector input, calculate the logical shift left of the second vector input and store the result into a vector register.
    def v_lshlrev_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s1_value << reg_s0_value
        self.registers.set_register(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Given a shift count in the first vector input, calculate the logical shift right of the second vector input and store the result into a vector register
    def v_lshrrev_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s1_value >> reg_s0_value
        self.registers.set_register(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Given a shift count in the first vector input, calculate the arithmetic shift right (preserving sign bit) of the second vector input and store the result into a vector register.
    def v_ashrrev_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=True, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=True, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s1_value >> reg_s0_value
        self.registers.set_register(reg_d, reg_d_value, signed=True, size=32, reg_type="VGPR_INT")
    
    # Calculate bitwise AND on two vector inputs and store the result into a vector register.
    def v_and_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value & reg_s1_value
        self.registers.set_register(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Calculate bitwise OR on two vector inputs and store the result into a vector register.
    def v_or_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value | reg_s1_value
        self.registers.set_register(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Calculate bitwise XOR on two vector inputs and store the result into a vector register.
    def v_xor_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value ^ reg_s1_value
        self.registers.set_register(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Calculate bitwise XNOR on two vector inputs and store the result into a vector register.
    def v_xnor_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_INT")
        reg_d_value = ~(reg_s0_value ^ reg_s1_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_INT")
    
    # Add two unsigned inputs and a bit from a carry-in mask, store the result into a vector register and store the carry-out mask into a scalar register.
    def v_add_co_ci_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_vcc_value = self.get_vcc_value()
        reg_d_value = reg_s0_value + reg_s1_value + reg_vcc_value
        reg_vcc_value = 1 if reg_d_value > 0xFFFFFFFF else 0
        self.set_vcc_value(reg_vcc_value)
        self.registers.set_register(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Subtract the second unsigned input from the first input, subtract a bit from the carry-in mask, store the result into a vector register and store the carry-out mask to a scalar register
    def v_sub_co_ci_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_vcc_value = self.get_vcc_value()
        reg_d_value = reg_s0_value - reg_s1_value - reg_vcc_value
        reg_vcc_value = 1 if reg_d_value < 0 else 0
        self.set_vcc_value(reg_vcc_value)
        self.registers.set_register(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Subtract the first unsigned input from the second input, subtract a bit from the carry-in mask, store the result into a vector register and store the carry-out mask to a scalar register.
    def v_subrev_co_ci_u32(self, reg_d, reg_s0, reg_s1):
        self.v_sub_co_ci_u32(reg_d, reg_s1, reg_s0)
    
    # Add two unsigned inputs and store the result into a vector register. No carry-in or carry-out support.
    def v_add_nc_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value + reg_s1_value
        self.registers.set_register(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Subtract the second unsigned input from the first input and store the result into a vector register. No carry-in or carry-out support.
    def v_sub_nc_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value - reg_s1_value
        self.registers.set_register(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Subtract the first unsigned input from the second input and store the result into a vector register. No carry-in or carry-out support.
    def v_subrev_nc_u32(self, reg_d, reg_s0, reg_s1):
        self.v_sub_nc_u32(reg_d, reg_s1, reg_s0)
    
    # Multiply two floating point inputs and accumulate the result into the destination register using fused multiplyadd.
    def v_fmac_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = self.registers.get_register(reg_d, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = reg_d_value + (reg_s0_value * reg_s1_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply a single-precision float with a literal constant and add a second single-precision float using fused multiply-add.
    def v_fmamk_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_simm32_value = self.registers.get_register(self.reg_simm, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = reg_s1_value + (reg_s0_value * reg_simm32_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply two single-precision floats and add a literal constant using fused multiply-add.
    def v_fmaak_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_simm32_value = self.registers.get_register(self.reg_simm, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = reg_simm32_value + (reg_s0_value * reg_s1_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Convert two single-precision float inputs into a packed FP16 result with round toward zero semantics (ignore the current rounding mode), and store the result into a vector register.
    def v_cvt_pk_rtz_f16_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        
        # Convert the first input.
        reg_s0_value = utils.fp32_to_fp16(reg_s0_value)
        
        # Convert the second input.
        reg_s1_value = utils.fp32_to_fp16(reg_s1_value)
        reg_s1_value = reg_s1_value << 16
        
        # Combine the two inputs.
        reg_d_value = reg_s0_value | reg_s1_value
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Add two floating point inputs and store the result into a vector register.
    def v_add_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = reg_s0_value + reg_s1_value
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Subtract the second floating point input from the first input and store the result into a vector register.
    def v_sub_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = reg_s0_value - reg_s1_value
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Subtract the first floating point input from the second input and store the result into a vector register.
    def v_subrev_f16(self, reg_d, reg_s0, reg_s1):
        self.v_sub_f16(reg_d, reg_s1, reg_s0)
    
    # Multiply two floating point inputs and store the result into a vector register.
    def v_mul_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = reg_s0_value * reg_s1_value
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply two floating point inputs and accumulate the result into the destination register using fused multiplyadd.
    def v_fmac_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = utils.fp16_to_fp32(self.registers.get_register(reg_d, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = reg_d_value + (reg_s0_value * reg_s1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply a FP16 value with a literal constant and add a second FP16 value using fused multiply-add.
    def v_fmamk_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_simm32_value = utils.fp16_to_fp32(self.registers.get_register(self.reg_simm, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = reg_s1_value + (reg_s0_value * reg_simm32_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply two FP16 values and add a literal constant using fused multiply-add.
    def v_fmaak_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_simm32_value = utils.fp16_to_fp32(self.registers.get_register(self.reg_simm, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = reg_simm32_value + (reg_s0_value * reg_s1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Select the maximum of two floating point inputs and store the result into a vector register.
    def v_max_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = max(reg_s0_value, reg_s1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Select the minimum of two floating point inputs and store the result into a vector register.
    def v_min_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = min(reg_s0_value, reg_s1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    #Multiply the first input, a floating point value, by an integral power of 2 specified in the second input, a signed integer value, and store the floating point result into a vector register. Compare with the ldexp() function in C.
    def v_ldexp_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = self.registers.get_register(reg_s1, signed=True, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value * (2 ** reg_s1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")

    # Multiply packed FP16 values and accumulate with destination.
    def v_pk_fmac_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.registers.get_register(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.registers.get_register(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        
        # Extract the first input.
        reg_s0_value_lo = utils.fp32_to_fp16(reg_s0_value & 0xFFFF)
        reg_s0_value_hi = utils.fp32_to_fp16(reg_s0_value >> 16)
        
        # Extract the second input.
        reg_s1_value_lo = utils.fp32_to_fp16(reg_s1_value & 0xFFFF)
        reg_s1_value_hi = utils.fp32_to_fp16(reg_s1_value >> 16)
        
        reg_d_value = self.registers.get_register(reg_d, signed=None, size=32, reg_type="VGPR_FLOAT")
        
        # Extract the destination.
        reg_d_value_lo = utils.fp32_to_fp16(reg_d_value & 0xFFFF)
        reg_d_value_hi = utils.fp32_to_fp16(reg_d_value >> 16)
        
        # Accumulate the result.
        reg_d_value_lo = reg_d_value_lo + (reg_s0_value_lo * reg_s1_value_lo)
        reg_d_value_hi = reg_d_value_hi + (reg_s0_value_hi * reg_s1_value_hi)
        reg_d_value = utils.fp16_to_fp32(reg_d_value_lo) | (utils.fp16_to_fp32(reg_d_value_hi) << 16)
        self.registers.set_register(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")    

   