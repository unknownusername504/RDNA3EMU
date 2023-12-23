# This file defines the instruction set for RNDA3.
import utils


class InstructionSet():
    def __init__(self):
        self.instructions = {
            "SOP2": {
                "S_ADD_U32": self.s_add_u32, # 0
                "S_SUB_U32": self.s_sub_u32, # 1
                "S_ADD_I32": self.s_add_i32, # 2
                "S_SUB_I32": self.s_sub_i32, # 3
                "S_ADDC_U32": self.s_addc_u32, # 4
                "S_SUBB_U32": self.s_subb_u32, # 5
                "S_ABSDIFF_I32": self.s_absdiff_i32, # 6
                "S_LSHL_B32": self.s_lshl_b32, # 8
                "S_LSHL_B64": self.s_lshl_b64, # 9
                "S_LSHR_B32": self.s_lshr_b32, # 10
                "S_LSHR_B64": self.s_lshr_b64, # 11
                "S_ASHR_I32": self.s_ashr_i32, # 12
                "S_ASHR_I64": self.s_ashr_i64, # 13
                "S_LSHL1_ADD_U32": self.s_lshl1_add_u32, # 14
                "S_LSHL2_ADD_U32": self.s_lshl2_add_u32, # 15
                "S_LSHL3_ADD_U32": self.s_lshl3_add_u32, # 16
                "S_LSHL4_ADD_U32": self.s_lshl4_add_u32, # 17
                "S_MIN_I32": self.s_min_i32, # 18
                "S_MIN_U32": self.s_min_u32, # 19
                "S_MAX_I32": self.s_max_i32, # 20
                "S_MAX_U32": self.s_max_u32, # 21
                "S_AND_B32": self.s_and_b32, # 22
                "S_AND_B64": self.s_and_b64, # 23
                "S_OR_B32": self.s_or_b32, # 24
                "S_OR_B64": self.s_or_b64, # 25
                "S_XOR_B32": self.s_xor_b32, # 26
                "S_XOR_B64": self.s_xor_b64, # 27
                "S_NAND_B32": self.s_nand_b32, # 28
                "S_NAND_B64": self.s_nand_b64, # 29
                "S_NOR_B32": self.s_nor_b32, # 30
                "S_NOR_B64": self.s_nor_b64, # 31
                "S_XNOR_B32": self.s_xnor_b32, # 32
                "S_XNOR_B64": self.s_xnor_b64, # 33
                "S_AND_NOT1_B32": self.s_and_not1_b32, # 34
                "S_AND_NOT1_B64": self.s_and_not1_b64, # 35
                "S_OR_NOT1_B32": self.s_or_not1_b32, # 36
                "S_OR_NOT1_B64": self.s_or_not1_b64, # 37
                "S_BFE_U32": self.s_bfe_u32, # 38
                "S_BFE_I32": self.s_bfe_i32, # 39
                "S_BFE_U64": self.s_bfe_u64, # 40
                "S_BFE_I64": self.s_bfe_i64, # 41
                "S_BFM_B32": self.s_bfm_b32, # 42
                "S_BFM_B64": self.s_bfm_b64, # 43
                "S_MUL_I32": self.s_mul_i32, # 44
                "S_MUL_HI_U32": self.s_mul_hi_u32, # 45
                "S_MUL_HI_I32": self.s_mul_hi_i32, # 46
                "S_CSELECT_B32": self.s_cselect_b32, # 48
                "S_CSELECT_B64": self.s_cselect_b64, # 49
                "S_PACK_LL_B32_B16": self.s_pack_ll_b32_b16, # 50
                "S_PACK_LH_B32_B16": self.s_pack_lh_b32_b16, # 51
                "S_PACK_HH_B32_B16": self.s_pack_hh_b32_b16, # 52
                "S_PACK_HL_B32_B16": self.s_pack_hl_b32_b16, # 53
            },
            "SOP1": {
                "S_MOV_B32": self.s_move_b32,
                "S_MOV_B64": self.s_move_b64,
                "C_MOV_B32": self.c_move_b32,
                "C_MOV_B64": self.c_move_b64,
                "S_BREV_B32": self.s_brev_b32,
                "S_BREV_B64": self.s_brev_b64,
                "S_CTZ_I32_B32": self.s_ctz_i32_b32, 
                "S_CTZ_I32_B64": self.s_ctz_i32_b64, 
                "S_CLZ_I32_U32": self.s_clz_i32_u32,
                "S_CLZ_I32_U64": self.s_clz_i32_u64,
                "S_CLS_I32": self.s_cls_i32,
                "S_CLS_I32_I64": self.s_cls_i32_i64,
                "S_SEXT_I32_I8": self.s_sext_i32_i8,
                "S_SEXT_I32_I16": self.s_sext_i32_i16,
                "S_BITSET0_B32": self.s_bitset0_b32,
                "S_BITSET0_B64": self.s_bitset0_b64,
                "S_BITSET1_B32": self.s_bitset1_b32,
                "S_BITSET1_B64": self.s_bitset1_b64,
                "S_BITREPLICATE_B64_B32": self.s_bitreplicate_b64_b32,
                "S_ABS_I32": self.s_abs_i32,
                "S_BCNT0_I32_B32": self.s_bcnt0_i32_b32,
                "S_BCNT0_I32_B64": self.s_bcnt0_i32_b64,
                "S_BCNT1_I32_B32": self.s_bcnt1_i32_b32,
                "S_BCNT1_I32_B64": self.s_bcnt1_i32_b64,
                "S_QUADMASK_B32": self.s_quadmask_b32,
                "S_QUADMASK_B64": self.s_quadmask_b64,
                "S_WQM_B32": self.s_wqm_b32,
                "S_WQM_B64": self.s_wqm_b64,
                "S_NOT_B32": self.s_not_b32,
                "S_NOT_B64": self.s_not_b64,
                "S_AND_SAVEEXEC_B32": self.s_and_saveexec_b32,
                "S_AND_SAVEEXEC_B64": self.s_and_saveexec_b64,
                "S_OR_SAVEEXEC_B32": self.s_or_saveexec_b32,
                "S_OR_SAVEEXEC_B64": self.s_or_saveexec_b64,
                "S_XOR_SAVEEXEC_B32": self.s_xor_saveexec_b32,
                "S_XOR_SAVEEXEC_B64": self.s_xor_saveexec_b64,
                "S_NAND_SAVEEXEC_B32": self.s_nand_saveexec_b32,
                "S_NAND_SAVEEXEC_B64": self.s_nand_saveexec_b64,
                "S_NOR_SAVEEXEC_B32": self.s_nor_saveexec_b32,
                "S_NOR_SAVEEXEC_B64": self.s_nor_saveexec_b64,
                "S_XNOR_SAVEEXEC_B32": self.s_xnor_saveexec_b32,
                "S_XNOR_SAVEEXEC_B64": self.s_xnor_saveexec_b64,
                "S_AND_NOT0_SAVEEXEC_B32": self.s_and_not0_saveexec_b32,
                "S_AND_NOT0_SAVEEXEC_B64": self.s_and_not0_saveexec_b64,
                "S_OR_NOT0_SAVEEXEC_B32": self.s_or_not0_saveexec_b32,
                "S_AND_NOT1_SAVEEXEC_B32": self.s_and_not1_saveexec_b32,
                "S_AND_NOT1_SAVEEXEC_B64": self.s_and_not1_saveexec_b64,
                "S_OR_NOT1_SAVEEXEC_B32": self.s_or_not1_saveexec_b32,
                "S_OR_NOT1_SAVEEXEC_B64": self.s_or_not1_saveexec_b64,
                "S_AND_NOT0_WREXEC_B32": self.s_and_not0_wrexec_b32,
                "S_AND_NOT0_WREXEC_B64": self.s_and_not0_wrexec_b64,
                "S_AND_NOT1_WREXEC_B32": self.s_and_not1_wrexec_b32,
                "S_AND_NOT1_WREXEC_B64": self.s_and_not1_wrexec_b64,
                "S_MOVRELS_B32": self.s_movrels_b32,
                "S_MOVRELD_B32": self.s_movereld_b32,
                "S_MOVRELD_B64": self.s_movreld_b64,
                "S_MOVRELSD_2_B32": self.s_moverelsd_2_b32,
                "S_GETPC_B64": self.s_getpc_b64,
                "S_SETPC_B64": self.s_setpc_b64,
                "S_SWAPPC_B64": self.s_swappc_b64,
                "S_RFE_B64": self.s_rfe_b64,
                "S_SENDMSG_RTN_B32": self.s_sendmsg_rtn_b32,
                "S_SENDMSG_RTN_B64": self.s_sendmsg_rtn_b64,
            },
        }
        # Register file 8-bit adressable array, register size imposed by the ISA interface.
        self.registers = [0] * (2**8)
        last_register_index = len(self.registers) - 1
        # Special named registers.
        self.register_id = {
            "SCC": last_register_index + 0,
        }
        # Extend the register file with the special named registers.
        for reg_name in self.register_id.keys():
            self.registers[self.register_id[reg_name]] = 0
    
    # Add two unsigned inputs, store the result into a scalar register and store the carry-out bit into SCC.
    def s_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = reg_s0_value + reg_s1_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Subtract the second unsigned input from the first input, store the result into a scalar register and store the carry-out bit into SCC.
    def s_sub_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = reg_s0_value - reg_s1_value
        reg_scc_value = 1 if (reg_d_value < 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Add two signed inputs, store the result into a scalar register and store the carry-out bit into SCC.
    def s_add_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32)
        reg_d_value = reg_s0_value + reg_s1_value
        sign = 1 if (reg_d_value < 0) else 0
        reg_scc_value = 1 if (sign != (reg_s0_value < 0)) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32)
    
    # Subtract the second signed input from the first input, store the result into a scalar register and store the carryout bit into SCC.
    def s_sub_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32)
        reg_d_value = reg_s0_value - reg_s1_value
        sign = 1 if (reg_d_value < 0) else 0
        reg_scc_value = 1 if (sign != (reg_s0_value < 0)) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32)
    
    # Add two unsigned inputs and a carry-in bit, store the result into a scalar register and store the carry-out bit into SCC.
    def s_addc_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_scc = self.get_register_id("SCC")
        reg_scc_value = self.get_register_value(reg_scc, signed=False, size=1)
        reg_d_value = reg_s0_value + reg_s1_value + reg_scc_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Subtract the second unsigned input from the first input, subtract the carry-in bit, store the result into a scalar register and store the carry-out bit into SCC.
    def s_subb_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_scc = self.get_register_id("SCC")
        reg_scc_value = self.get_register_value(reg_scc, signed=False, size=1)
        reg_d_value = reg_s0_value - reg_s1_value - reg_scc_value
        reg_scc_value = 1 if (reg_d_value < 0) else 0
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Calculate the absolute value of difference between two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_absdiff_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32)
        reg_d_value = abs(reg_s0_value - reg_s1_value)
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32)
    
    # Given a shift count in the second scalar input, calculate the logical shift left of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_lshl_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = reg_s0_value << reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Given a shift count in the second scalar input, calculate the logical shift left of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_lshl_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64)
        reg_d_value = reg_s0_value << reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64)
    
    # Given a shift count in the second scalar input, calculate the logical shift right of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_lshr_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = reg_s0_value >> reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Given a shift count in the second scalar input, calculate the logical shift right of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_lshr_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64)
        reg_d_value = reg_s0_value >> reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64)

    # Given a shift count in the second scalar input, calculate the arithmetic shift right (preserving sign bit) of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_ashr_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = reg_s0_value >> reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32)

    # Given a shift count in the second scalar input, calculate the arithmetic shift right (preserving sign bit) of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_ashr_i64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=64)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64)
        reg_d_value = reg_s0_value >> reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=64)
    
    # Calculate the logical shift left of the first input by 1, then add the second input, store the result into a scalar register and set SCC iff the summation results in an unsigned overflow.
    def s_lshl1_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = (reg_s0_value << 1) + reg_s1_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Calculate the logical shift left of the first input by 2, then add the second input, store the result into a scalar register and set SCC iff the summation results in an unsigned overflow.
    def s_lshl2_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = (reg_s0_value << 2) + reg_s1_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Calculate the logical shift left of the first input by 3, then add the second input, store the result into a scalar register and set SCC iff the summation results in an unsigned overflow.
    def s_lshl3_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = (reg_s0_value << 3) + reg_s1_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Calculate the logical shift left of the first input by 4, then add the second input, store the result into a scalar register and set SCC iff the summation results in an unsigned overflow.
    def s_lshl4_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = (reg_s0_value << 4) + reg_s1_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)

    # Select the minimum of two signed integers, store the selected value into a scalar register and set SCC iff the first value is selected.
    def s_min_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32)
        reg_d_value = min(reg_s0_value, reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == reg_s0_value) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32)
    
    # Select the minimum of two unsigned integers, store the selected value into a scalar register and set SCC iff the first value is selected.
    def s_min_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = min(reg_s0_value, reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == reg_s0_value) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)

    # Select the maximum of two signed integers, store the selected value into a scalar register and set SCC iff the first value is selected.
    def s_max_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32)
        reg_d_value = max(reg_s0_value, reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == reg_s0_value) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32)

    # Select the maximum of two unsigned integers, store the selected value into a scalar register and set SCC iff the first value is selected.
    def s_max_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = max(reg_s0_value, reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == reg_s0_value) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)

    # Calculate bitwise AND on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_and_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = reg_s0_value & reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)

    # Calculate bitwise AND on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_and_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64)
        reg_d_value = reg_s0_value & reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64)
    
    # Calculate bitwise OR on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_or_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = reg_s0_value | reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)

    # Calculate bitwise OR on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_or_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64)
        reg_d_value = reg_s0_value | reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64)

    # Calculate bitwise XOR on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_xor_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = reg_s0_value ^ reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Calculate bitwise XOR on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_xor_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64)
        reg_d_value = reg_s0_value ^ reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64)
    
    # Calculate bitwise NAND on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_nand_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = ~(reg_s0_value & reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Calculate bitwise NAND on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_nand_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64)
        reg_d_value = ~(reg_s0_value & reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64)
    
    # Calculate bitwise NOR on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_nor_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = ~(reg_s0_value | reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Calculate bitwise NOR on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_nor_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64)
        reg_d_value = ~(reg_s0_value | reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64)
    
    # Calculate bitwise XNOR on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_xnor_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = ~(reg_s0_value ^ reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Calculate bitwise XNOR on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_xnor_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64)
        reg_d_value = ~(reg_s0_value ^ reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64)
    
    # Calculate bitwise AND with the first input and the negation of the second input, store the result into a scalar register and set SCC if the result is nonzero.
    def s_and_not1_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = reg_s0_value & ~reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Calculate bitwise AND with the first input and the negation of the second input, store the result into a scalar register and set SCC if the result is nonzero.
    def s_and_not1_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64)
        reg_d_value = reg_s0_value & ~reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64)
    
    # Calculate bitwise OR with the first input and the negation of the second input, store the result into a scalar register and set SCC if the result is nonzero.
    def s_or_not1_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32)
        reg_d_value = reg_s0_value | ~reg_s1_value
        reg_scc_value = 1 if (reg_d_value != -1) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Calculate bitwise OR with the first input and the negation of the second input, store the result into a scalar register and set SCC if the result is nonzero.
    def s_or_not1_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=64)
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=64)
        reg_d_value = reg_s0_value | ~reg_s1_value
        reg_scc_value = 1 if (reg_d_value != -1) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64)

    # Extract an unsigned bitfield from the first input using field offset and size encoded in the second input, store the result into a scalar register and set SCC iff the result is nonzero
    def s_bfe_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        # Field offset is [4:0] of reg_s1
        field_offset = reg_s1_value & 0x1F
        # Field size is [22:16] of reg_s1
        field_size = (reg_s1_value >> 16) & 0x7F
        reg_d_value = (reg_s0_value >> field_offset) & ((1 << field_size) - 1)
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=field_size)
    
    # Extract a signed bitfield from the first input using field offset and size encoded in the second input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_bfe_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        # Field offset is [4:0] of reg_s1
        field_offset = reg_s1_value & 0x1F
        # Field size is [22:16] of reg_s1
        field_size = (reg_s1_value >> 16) & 0x7F
        reg_d_value = (reg_s0_value >> field_offset) & ((1 << field_size) - 1)
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=field_size)
    
    # Extract an unsigned bitfield from the first input using field offset and size encoded in the second input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_bfe_u64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64)
        # Field offset is [5:0] of reg_s1
        field_offset = reg_s1_value & 0x3F
        # Field size is [22:16] of reg_s1
        field_size = (reg_s1_value >> 16) & 0x7F
        reg_d_value = (reg_s0_value >> field_offset) & ((1 << field_size) - 1)
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=field_size)
    
    # Extract a signed bitfield from the first input using field offset and size encoded in the second input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_bfe_i64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=64)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64)
        # Field offset is [5:0] of reg_s1
        field_offset = reg_s1_value & 0x3F
        # Field size is [22:16] of reg_s1
        field_size = (reg_s1_value >> 16) & 0x7F
        reg_d_value = (reg_s0_value >> field_offset) & ((1 << field_size) - 1)
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        reg_scc = self.get_register_id("SCC")
        self.set_register_value(reg_scc, reg_scc_value, signed=False, size=1)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=field_size)
    
    # Calculate a bitfield mask given a field offset and size and store the result in a scalar register.
    def s_bfm_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        # Field offset is [4:0] of reg_s1
        field_offset = reg_s1_value & 0x1F
        # Field size is [4:0] of reg_s0
        field_size = reg_s0_value & 0x1F
        reg_d_value = ((1 << field_size) - 1) << field_offset
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Calculate a bitfield mask given a field offset and size and store the result in a scalar register.
    def s_bfm_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64)
        # Field offset is [5:0] of reg_s1
        field_offset = reg_s1_value & 0x3F
        # Field size is [5:0] of reg_s0
        field_size = reg_s0_value & 0x3F
        reg_d_value = ((1 << field_size) - 1) << field_offset
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64)
    
    # Multiply two signed integers and store the result into a scalar register.
    def s_mul_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32)
        reg_d_value = reg_s0_value * reg_s1_value
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32)
    
    # Multiply two unsigned integers and store the high 32 bits of the result into a scalar register.
    def s_mul_hi_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = (reg_s0_value * reg_s1_value) >> 32
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Multiply two signed integers and store the high 32 bits of the result into a scalar register.
    def s_mul_hi_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32)
        reg_d_value = (reg_s0_value * reg_s1_value) >> 32
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32)
    
    # Select the first input if SCC is true otherwise select the second input, then store the selected input into a scalar register.
    def s_cselect_b32(self, reg_d, reg_s0, reg_s1):
        reg_scc = self.get_register_id("SCC")
        reg_scc_value = self.get_register_value(reg_scc, signed=False, size=1)
        reg_d_value = reg_s0 if reg_scc_value == 1 else reg_s1
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Select the first input if SCC is true otherwise select the second input, then store the selected input into a scalar register.
    def s_cselect_b64(self, reg_d, reg_s0, reg_s1):
        reg_scc = self.get_register_id("SCC")
        reg_scc_value = self.get_register_value(reg_scc, signed=False, size=1)
        reg_d_value = reg_s0 if reg_scc_value == 1 else reg_s1
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64)
    
    # Pack two 16-bit scalar values into a scalar register.
    def s_pack_ll_b32_b16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=16)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=16)
        reg_d_value = (reg_s1_value << 16) | reg_s0_value
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Pack two 16-bit scalar values into a scalar register.
    def s_pack_lh_b32_b16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=16)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = (reg_s1_value & 0xFFFF0000)| reg_s0_value
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Pack two 16-bit scalar values into a scalar register.
    def s_pack_hh_b32_b16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32)
        reg_d_value = (reg_s1_value & 0xFFFF0000) | (reg_s0_value >> 16)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)
    
    # Pack two 16-bit scalar values into a scalar register.
    def s_pack_hl_b32_b16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=16)
        reg_d_value = (reg_s1_value << 16) | (reg_s0_value >> 16)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32)

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

    # Get all the op code names.
    def get_op_code_names(self):
        return self.instructions.keys()

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
        return reg_value % 2**size

    # Set the register value from the register ID.
    def set_register_value(self, reg_id, reg_value, signed, size):
        if signed:
            sign = reg_value >> (size - 1)
            if sign == 1:
                reg_value = reg_value - 2**size
        self.registers[reg_id] = reg_value % 2**size
    
    def get_scc_value(self):
        return self.get_register_value(
            self.get_register_id("SCC"), signed=False, size=1)
        