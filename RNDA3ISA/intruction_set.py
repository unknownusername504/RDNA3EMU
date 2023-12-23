# This file defines the instruction set for RNDA3.

class InstructionSet():
    def __init__(self):
        self.instructions = {
            "SOP2": {
                "S_ADD_U32": self.s_add_u32, 
                "S_SUB_U32": self.s_sub_u32, 
                "S_ADD_I32": self.s_add_i32,
                "S_SUB_I32": self.s_sub_i32, 
                "S_ADDC_U32": self.s_addc_u32, 
                "S_SUBB_U32": self.s_subb_u32, 
                "S_ABSDIFF_I32": self.s_absdiff_i32, 
                "S_LSHL_B32": self.s_lshl_b32, 
                "S_LSHL_B64": self.s_lshl_b64, 
                "S_LSHR_B32": self.s_lshr_b32, 
            },
        }
        # Register file 8-bit adressable array, register size imposed by the ISA interface.
        self.registers = [0] * (2**8)
        # Special named registers.
        self.register_id = {
            "SCC": 0,
        }
    
    # Add two unsigned inputs, store the result into a scalar register and store the carry-out bit into SCC.
    def s_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        temp = reg_s0_value + reg_s1_value
        reg_scc_value = 1 if (temp >= 2**32) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        reg_d_value = temp % 2**32
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Subtract the second unsigned input from the first input, store the result into a scalar register and store the carry-out bit into SCC.
    def s_sub_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        temp = reg_s0_value - reg_s1_value
        reg_scc_value = 1 if (temp < 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        reg_d_value = temp % 2**32
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Add two signed inputs, store the result into a scalar register and store the carry-out bit into SCC.
    def s_add_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32)
        temp = reg_s0_value + reg_s1_value
        sign = 1 if (temp < 0) else 0
        reg_scc_value = 1 if (sign != (reg_s0_value < 0)) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        reg_d_value = temp % 2**32
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32)
    
    # Subtract the second signed input from the first input, store the result into a scalar register and store the carryout bit into SCC.
    def s_sub_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32)
        temp = reg_s0_value - reg_s1_value
        sign = 1 if (temp < 0) else 0
        reg_scc_value = 1 if (sign != (reg_s0_value < 0)) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        reg_d_value = temp % 2**32
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32)
    
    # Add two unsigned inputs and a carry-in bit, store the result into a scalar register and store the carry-out bit into SCC.
    def s_addc_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_scc = self.get_register_id("SCC")
        reg_scc_value = self.get_register_value(reg_scc, signed=False, size=1)
        temp = reg_s0_value + reg_s1_value + reg_scc_value
        reg_scc_value = 1 if (temp >= 2**32) else 0
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        reg_d_value = temp % 2**32
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Subtract the second unsigned input from the first input, subtract the carry-in bit, store the result into a scalar register and store the carry-out bit into SCC.
    def s_subb_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_scc = self.get_register_id("SCC")
        reg_scc_value = self.get_register_value(reg_scc, signed=False, size=1)
        temp = reg_s0_value - reg_s1_value - reg_scc_value
        reg_scc_value = 1 if (temp < 0) else 0
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        reg_d_value = temp % 2**32
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Calculate the absolute value of difference between two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_absdiff_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32)
        temp = abs(reg_s0_value - reg_s1_value)
        reg_scc_value = 1 if (temp != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        reg_d_value = temp % 2**32
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32)
    
    # Given a shift count in the second scalar input, calculate the logical shift left of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_lshl_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        temp = reg_s0_value << reg_s1_value
        reg_scc_value = 1 if (temp != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        reg_d_value = temp % 2**32
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Given a shift count in the second scalar input, calculate the logical shift left of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_lshl_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64)
        temp = reg_s0_value << reg_s1_value
        reg_scc_value = 1 if (temp != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        reg_d_value = temp % 2**64
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64)

    # Get the register ID from the register name.
    def get_register_id(self, reg_name):
        register_id = self.register_id.get(reg_name)
        if register_id == None:
            raise Exception("Register name not found.")
        return self.register_id[reg_name]
    
    # Get the register value from the register ID.
    def get_register_value(self, reg_id, signed, size):
        reg_value = self.registers[reg_id]
        if signed:
            sign = reg_value >> (size - 1)
            if sign == 1:
                reg_value = reg_value - 2**size
        return reg_value

    # Set the register value from the register ID.
    def set_register_value(self, reg_id, reg_value, signed, size):
        if signed:
            reg_value = reg_value % 2**size
        self.registers[reg_id] = reg_value