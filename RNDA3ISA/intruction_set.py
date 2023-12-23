# This file defines the instruction set for RNDA3.
import utils

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
            "SOP1": {
                'S_MOV_B32': self.s_move_b32,
                'S_MOV_B64': self.s_move_b64,
                'C_MOV_B32': self.c_move_b32,
                'C_MOV_B64': self.c_move_b64,
                'S_BREV_B32': self.s_brev_b32,
                'S_BREV_B64': self.s_brev_b64,
                'S_CTZ_I32_B32': self.s_ctz_i32_b32, 
                'S_CTZ_I32_B64': self.s_ctz_i32_b64, 
                'S_CLZ_I32_U32': self.s_clz_i32_u32,
                'S_CLZ_I32_U64': self.s_clz_i32_u64,
                'S_CLS_I32': self.s_cls_i32,
                'S_CLS_I32_I64': self.s_cls_i32_i64,
                'S_SEXT_I32_I8': self.s_sext_i32_i8,
                'S_SEXT_I32_I16': self.s_sext_i32_i16,
                'S_BITSET0_B32': self.s_bitset0_b32,
                'S_BITSET0_B64': self.s_bitset0_b64,
                'S_BITSET1_B32': self.s_bitset1_b32,
                'S_BITSET1_B64': self.s_bitset1_b64,
                'S_BITREPLICATE_B64_B32': self.s_bitreplicate_b64_b32,
                'S_ABS_I32': self.s_abs_i32,
                'S_BCNT0_I32_B32': self.s_bcnt0_i32_b32,
                'S_BCNT0_I32_B64': self.s_bcnt0_i32_b64,
                'S_BCNT1_I32_B32': self.s_bcnt1_i32_b32,
                'S_BCNT1_I32_B64': self.s_bcnt1_i32_b64,
                'S_QUADMASK_B32': self.s_quadmask_b32,
                'S_QUADMASK_B64': self.s_quadmask_b64,
                'S_WQM_B32': self.s_wqm_b32,
                'S_WQM_B64': self.s_wqm_b64,
                'S_NOT_B32': self.s_not_b32,
                'S_NOT_B64': self.s_not_b64,
                'S_AND_SAVEEXEC_B32': self.s_and_saveexec_b32,
                'S_AND_SAVEEXEC_B64': self.s_and_saveexec_b64,
                'S_OR_SAVEEXEC_B32': self.s_or_saveexec_b32,
                'S_OR_SAVEEXEC_B64': self.s_or_saveexec_b64,
                'S_XOR_SAVEEXEC_B32': self.s_xor_saveexec_b32,
                'S_XOR_SAVEEXEC_B64': self.s_xor_saveexec_b64,
                'S_NAND_SAVEEXEC_B32': self.s_nand_saveexec_b32,
                'S_NAND_SAVEEXEC_B64': self.s_nand_saveexec_b64,
                'S_NOR_SAVEEXEC_B32': self.s_nor_saveexec_b32,
                'S_NOR_SAVEEXEC_B64': self.s_nor_saveexec_b64,
                'S_XNOR_SAVEEXEC_B32': self.s_xnor_saveexec_b32,
                'S_XNOR_SAVEEXEC_B64': self.s_xnor_saveexec_b64,
                'S_AND_NOT0_SAVEEXEC_B32': self.s_and_not0_saveexec_b32,
                'S_AND_NOT0_SAVEEXEC_B64': self.s_and_not0_saveexec_b64,
                'S_OR_NOT0_SAVEEXEC_B32': self.s_or_not0_saveexec_b32,
                'S_AND_NOT1_SAVEEXEC_B32': self.s_and_not1_saveexec_b32,
                'S_AND_NOT1_SAVEEXEC_B64': self.s_and_not1_saveexec_b64,
                'S_OR_NOT1_SAVEEXEC_B32': self.s_or_not1_saveexec_b32,
                'S_OR_NOT1_SAVEEXEC_B64': self.s_or_not1_saveexec_b64,
                'S_AND_NOT0_WREXEC_B32': self.s_and_not0_wrexec_b32,
                'S_AND_NOT0_WREXEC_B64': self.s_and_not0_wrexec_b64,
                'S_AND_NOT1_WREXEC_B32': self.s_and_not1_wrexec_b32,
                'S_AND_NOT1_WREXEC_B64': self.s_and_not1_wrexec_b64,
                'S_MOVRELS_B32': self.s_movrels_b32,
                'S_MOVRELD_B32': self.s_movereld_b32,
                'S_MOVRELD_B64': self.s_movreld_b64,
                'S_MOVRELSD_2_B32': self.s_moverelsd_2_b32,
                'S_GETPC_B64': self.s_getpc_b64,
                'S_SETPC_B64': self.s_setpc_b64,
                'S_SWAPPC_B64': self.s_swappc_b64,
                'S_RFE_B64': self.s_rfe_b64,
                'S_SENDMSG_RTN_B32': self.s_sendmsg_rtn_b32,
                'S_SENDMSG_RTN_B64': self.s_sendmsg_rtn_b64,
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

    # SOP1

    # Move scalar input into a scalar register. (32-bit)
    def s_move_b32(self, reg_d, reg_s0):
        reg_s0_val = self.get_register_value(reg_s0, signed=False, size=32)
        self.set_register_value(reg_d, reg_s0_val, signed=False, size=32)

    # Move scalar input into a scalar register. (64-bit)
    def s_move_b64(self, reg_d, reg_s0):
        reg_s0_val = self.get_register_value(reg_s0, signed=False, size=64)
        self.set_register_value(reg_d, reg_s0_val, signed=False, size=64)

    # Move scalar input into a scalar register iff SCC is nonzero.
    def c_move_b32(self, reg_d, reg_s0):
       if (self.get_scc_value() == 1):
        self.s_move_b32(reg_d, reg_s0)
    
    def c_move_b64(self, reg_d, reg_s0):
       if (self.get_scc_value() == 1):
        self.s_move_b64(reg_d, reg_s0)

    # Reverse the order of bits in a scalar input and store the result into a scalar register.
    def s_brev_b32(self, reg_d, reg_s0):
        reg_s0_val = self.get_register_value(reg_s0, signed=False, size=32)
        tmp = utils.rev_b32(reg_s0_val)
        self.set_register_value(reg_d, tmp, signed=False, size=32)

        
    def s_brev_b64(self, reg_d, reg_s0):
        reg_s0_val = self.get_register_value(reg_s0, signed=False, size=64)
        tmp = utils.rev_b64(reg_s0_val)
        self.set_register_value(reg_d, tmp, signed=False, size=64)

    def s_ctz_i32_b32(self):
        # Implementation for S_CTZ_I32_B32
        pass

    def s_ctz_i32_b64(self):
        # Implementation for S_CTZ_I32_B64
        pass

    def s_clz_i32_u32(self):
        # Implementation for S_CLZ_I32_U32
        pass

    def s_clz_i32_u64(self):
        # Implementation for S_CLZ_I32_U64
        pass

    def s_cls_i32(self):
        # Implementation for S_CLS_I32
        pass

    def s_cls_i32_i64(self):
        # Implementation for S_CLS_I32_I64
        pass

    def s_sext_i32_i8(self):
        # Implementation for S_SEXT_I32_I8
        pass

    def s_sext_i32_i16(self):
        # Implementation for S_SEXT_I32_I16
        pass

    def s_bitset0_b32(self):
        # Implementation for S_BITSET0_B32
        pass

    def s_bitset0_b64(self):
        # Implementation for S_BITSET0_B64
        pass

    def s_bitset1_b32(self):
        # Implementation for S_BITSET1_B32
        pass

    def s_bitset1_b64(self):
        # Implementation for S_BITSET1_B64
        pass

    def s_bitreplicate_b64_b32(self):
        # Implementation for S_BITREPLICATE_B64_B32
        pass

    def s_abs_i32(self):
        # Implementation for S_ABS_I32
        pass

    def s_bcnt0_i32_b32(self):
        # Implementation for S_BCNT0_I32_B32
        pass

    def s_bcnt0_i32_b64(self):
        # Implementation for S_BCNT0_I32_B64
        pass

    def s_bcnt1_i32_b32(self):
        # Implementation for S_BCNT1_I32_B32
        pass

    def s_bcnt1_i32_b64(self):
        # Implementation for S_BCNT1_I32_B64
        pass

    def s_quadmask_b32(self):
        # Implementation for S_QUADMASK_B32
        pass

    def s_quadmask_b64(self):
        # Implementation for S_QUADMASK_B64
        pass

    def s_wqm_b32(self):
        # Implementation for S_WQM_B32
        pass

    def s_wqm_b64(self):
        # Implementation for S_WQM_B64
        pass

    def s_not_b32(self):
        # Implementation for S_NOT_B32
        pass

    def s_not_b64(self):
        # Implementation for S_NOT_B64
        pass

    def s_and_saveexec_b32(self):
        # Implementation for S_AND_SAVEEXEC_B32
        pass

    def s_and_saveexec_b64(self):
        # Implementation for S_AND_SAVEEXEC_B64
        pass

    def s_or_saveexec_b32(self):
        # Implementation for S_OR_SAVEEXEC_B32
        pass

    def s_or_saveexec_b64(self):
        # Implementation for S_OR_SAVEEXEC_B64
        pass

    def s_xor_saveexec_b32(self):
        # Implementation for S_XOR_SAVEEXEC_B32
        pass

    def s_xor_saveexec_b64(self):
        # Implementation for S_XOR_SAVEEXEC_B64
        pass

    def s_nand_saveexec_b32(self):
        # Implementation for S_NAND_SAVEEXEC_B32
        pass

    def s_nand_saveexec_b64(self):
        # Implementation for S_NAND_SAVEEXEC_B64
        pass

    def s_nor_saveexec_b32(self):
        # Implementation for S_NOR_SAVEEXEC_B32
        pass

    def s_nor_saveexec_b64(self):
        # Implementation for S_NOR_SAVEEXEC_B64
        pass

    def s_xnor_saveexec_b32(self):
        # Implementation for S_XNOR_SAVEEXEC_B32
        pass

    def s_xnor_saveexec_b64(self):
        # Implementation for S_XNOR_SAVEEXEC_B64
        pass

    def s_and_not0_saveexec_b32(self):
        # Implementation for S_AND_NOT0_SAVEEXEC_B32
        pass

    def s_and_not0_saveexec_b64(self):
        # Implementation for S_AND_NOT0_SAVEEXEC_B64
        pass

    def s_or_not0_saveexec_b32(self):
        # Implementation for S_OR_NOT0_SAVEEXEC_B32
        pass

    def s_and_not1_saveexec_b32(self):
        # Implementation for S_AND_NOT1_SAVEEXEC_B32
        pass

    def s_and_not1_saveexec_b64(self):
        # Implementation for S_AND_NOT1_SAVEEXEC_B64
        pass

    def s_or_not1_saveexec_b32(self):
        # Implementation for S_OR_NOT1_SAVEEXEC_B32
        pass

    def s_or_not1_saveexec_b64(self):
        # Implementation for S_OR_NOT1_SAVEEXEC_B64
        pass

    def s_and_not0_wrexec_b32(self):
        # Implementation for S_AND_NOT0_WREXEC_B32
        pass

    def s_and_not0_wrexec_b64(self):
        # Implementation for S_AND_NOT0_WREXEC_B64
        pass

    def s_and_not1_wrexec_b32(self):
        # Implementation for S_AND_NOT1_WREXEC_B32
        pass

    def s_and_not1_wrexec_b64(self):
        # Implementation for S_AND_NOT1_WREXEC_B64
        pass

    def s_movrels_b32(self):
        # Implementation for S_MOVRELS_B32
        pass

    def s_movereld_b32(self):
        # Implementation for S_MOVRELD_B32
        pass

    def s_movreld_b64(self):
        # Implementation for S_MOVRELD_B64
        pass

    def s_moverelsd_2_b32(self):
        # Implementation for S_MOVRELSD_2_B32
        pass

    def s_getpc_b64(self):
        # Implementation for S_GETPC_B64
        pass

    def s_setpc_b64(self):
        # Implementation for S_SETPC_B64
        pass

    def s_swappc_b64(self):
        # Implementation for S_SWAPPC_B64
        pass

    def s_rfe_b64(self):
        # Implementation for S_RFE_B64
        pass

    def s_sendmsg_rtn_b32(self):
        # Implementation for S_SENDMSG_RTN_B32
        pass

    def s_sendmsg_rtn_b64(self):
        # Implementation for S_SENDMSG_RTN_B64
        pass
    # REGISTERS

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

    def get_scc_value(self):
        return self.get_register_value(
            self.get_register_id("SCC"), signed=False, size=1)
        