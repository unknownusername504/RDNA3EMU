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
            "VOP2": {
                "V_CNDMASK_B32": self.v_cndmask_b32,
                "V_DOT2ACC_F32_F16": self.v_dot2acc_f32_f16,
                "V_ADD_F32": self.v_add_f32,
                "V_SUB_F32": self.v_sub_f32,
                "V_SUBREV_F32": self.v_subrev_f32,
                "V_FMAC_DX9_ZERO_F32": self.v_fmac_dx9_zero_f32,
                "V_MUL_DX9_ZERO_F32": self.v_mul_dx9_zero_f32,
                "V_MUL_F32": self.v_mul_f32,
                "V_MUL_I32_I24": self.v_mul_i32_i24,
                "V_MUL_HI_I32_I24": self.v_mul_hi_i32_i24,
                "V_MUL_U32_U24": self.v_mul_u32_u24,
                "V_MUL_HI_U32_U24": self.v_mul_hi_u32_u24,
                "V_MIN_F32": self.v_min_f32,
                "V_MAX_F32": self.v_max_f32,
                "V_MIN_I32": self.v_min_i32,
                "V_MAX_I32": self.v_max_i32,
                "V_MIN_U32": self.v_min_u32,
                "V_MAX_U32": self.v_max_u32,
                "V_LSHLREV_B32": self.v_lshlrev_b32,
                "V_LSHRREV_B32": self.v_lshrrev_b32,
                "V_ASHRREV_I32": self.v_ashrrev_i32,
                "V_AND_B32": self.v_and_b32,
                "V_OR_B32": self.v_or_b32,
                "V_XOR_B32": self.v_xor_b32,
                "V_XNOR_B32": self.v_xnor_b32,
                "V_ADD_CO_CI_U32": self.v_add_co_ci_u32,
                "V_SUB_CO_CI_U32": self.v_sub_co_ci_u32,
                "V_SUBREV_CO_CI_U32": self.v_subrev_co_ci_u32,
                "V_ADD_NC_U32": self.v_add_nc_u32,
                "V_SUB_NC_U32": self.v_sub_nc_u32,
                "V_SUBREV_NC_U32": self.v_subrev_nc_u32,
                "V_FMAC_F32": self.v_fmac_f32,
                "V_FMAMK_F32": self.v_fmamk_f32,
                "V_FMAAK_F32": self.v_fmaak_f32,
                "V_CVT_PK_RTZ_F16_F32": self.v_cvt_pk_rtz_f16_f32,
                "V_ADD_F16": self.v_add_f16,
                "V_SUB_F16": self.v_sub_f16,
                "V_SUBREV_F16": self.v_subrev_f16,
                "V_MUL_F16": self.v_mul_f16,
                "V_FMAC_F16": self.v_fmac_f16,
                "V_FMAMK_F16": self.v_fmamk_f16,
                "V_FMAAK_F16": self.v_fmaak_f16,
                "V_MAX_F16": self.v_max_f16,
                "V_MIN_F16": self.v_min_f16,
                "V_LDEXP_F16": self.v_ldexp_f16,
                "V_PK_FMAC_F16": self.v_pk_fmac_f16,
            },
        }
        # Reg types
        self.reg_types = {
            "VGPR_INT": 0,
            "VGPR_FLOAT": 1,
            "SGPR": 2,
            "SPECIAL": 3,
        }
        # Register file adressable arrays, register size imposed by the ISA interface.
        # All registers below are unique to each wave except for TBA and TMA which are shared.
        # Even alignment required for 64-bit data/addr
        # Quad alignment required for >64-bit data/addr
        self.vector_registers = {
            # Vector sources and dests use a 8-bit encoding
            "VGPR": [0] * 256, # 0-255=VGPR
        }
        self.scalar_registers = {
            # Scalar sources and dests use a 7-bit encoding
            "SGPR": [0] * 106, # Scalar 0-105=SGPR
            "VCC": [0] * 2, # 106,107={VCC_LO,VCC_HI}
            "TTMP0-15": [0] * 16, # 108-123=TTMP0-15
            "NULL": [0] * 1, # 124=NULL
            "M0": [0] * 1, # 125=M0
            "EXEC": [0] * 2, # 126,127={EXEC_LO,EXEC_HI}
            "RESERVED_128-131": [0] * 4, # 128-131=RESERVED
        }
        # Status register bit fields.
        self.status_register = {
            "SCC": {"bit_pos": 0, "bit_width": 1},
            "SYS_PRIO": {"bit_pos": 1, "bit_width": 2},
            "USER_PRIO": {"bit_pos": 3, "bit_width": 2},
            "PRIV": {"bit_pos": 5, "bit_width": 1},
            "TRAP_EN": {"bit_pos": 6, "bit_width": 1},
            "RESERVED_7": {"bit_pos": 7, "bit_width": 1}, # Always 0.
            "EXPORT_RDY": {"bit_pos": 8, "bit_width": 1},
            "EXECZ": {"bit_pos": 9, "bit_width": 1},
            "VCCZ": {"bit_pos": 10, "bit_width": 1},
            "IN_WG": {"bit_pos": 11, "bit_width": 1},
            "IN_BARRIER": {"bit_pos": 12, "bit_width": 1},
            "HALT": {"bit_pos": 13, "bit_width": 1},
            "TRAP": {"bit_pos": 14, "bit_width": 1},
            "RESERVED_15": {"bit_pos": 15, "bit_width": 1}, # Always 0.
            "VALID": {"bit_pos": 16, "bit_width": 1},
            "RESERVED_17": {"bit_pos": 17, "bit_width": 1}, # Always 0.
            "SKIP_EXPORT": {"bit_pos": 18, "bit_width": 1},
            "PERF_EN": {"bit_pos": 19, "bit_width": 1},
            "CDBG_USER": {"bit_pos": 20, "bit_width": 1},
            "CDBG_SYS": {"bit_pos": 21, "bit_width": 1},
            "RESERVED_22": {"bit_pos": 22, "bit_width": 1}, # Always 0.
            "FATAL_HALT": {"bit_pos": 23, "bit_width": 1},
            "NO_VGPRS": {"bit_pos": 24, "bit_width": 1},
            "LDS_PARAM_RDY": {"bit_pos": 25, "bit_width": 1},
            "MUST_GS_ALLOC": {"bit_pos": 26, "bit_width": 1},
            "MUST_EXPORT": {"bit_pos": 27, "bit_width": 1},
            "IDLE": {"bit_pos": 28, "bit_width": 1},
            "SCRATCH_EN": {"bit_pos": 29, "bit_width": 1},
            "RESERVED_30-31": {"bit_pos": 30, "bit_width": 2}, # Always 0.
        }
        # Special registers file
        self.special_registers = {
            "SPECIAL": [0] * 32,
        }
        # Special named registers for wave state with special ids
        self.special_registers_meta = {
            "Reserved": {"reg_id": 0, "reg_fields": None},
            "MODE": {"reg_id": 1, "reg_fields": None},
            "STATUS": {"reg_id": 2, "reg_fields": self.status_register},
            "TRAPSTS": {"reg_id": 3, "reg_fields": None},
            "FLUSH_IB": {"reg_id": 14, "reg_fields": None},
            "SH_MEM_BASES": {"reg_id": 15, "reg_fields": None},
            "FLAT_SCRATCH_LO": {"reg_id": 20, "reg_fields": None},
            "FLAT_SCRATCH_HI": {"reg_id": 21, "reg_fields": None},
            "HW_ID1": {"reg_id": 23, "reg_fields": None},
            "HW_ID2": {"reg_id": 24, "reg_fields": None},
            "SHADER_CYCLES": {"reg_id": 29, "reg_fields": None},
        }
        # The following registers are special access registers that are not part of the register file.
        self.PC = 0 # Program counter for the wave. Initialized to 0. 64-bit.
        self.TMA = 0 # Trap Memory Address. 48-bit.
        self.TBA = 0 # Trap Base Address. 48-bit.
    
    # Add two unsigned inputs, store the result into a scalar register and store the carry-out bit into SCC.
    def s_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = reg_s0_value + reg_s1_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Subtract the second unsigned input from the first input, store the result into a scalar register and store the carry-out bit into SCC.
    def s_sub_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = reg_s0_value - reg_s1_value
        reg_scc_value = 1 if (reg_d_value < 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Add two signed inputs, store the result into a scalar register and store the carry-out bit into SCC.
    def s_add_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32, reg_type="SGPR")
        reg_d_value = reg_s0_value + reg_s1_value
        sign = 1 if (reg_d_value < 0) else 0
        reg_scc_value = 1 if (sign != (reg_s0_value < 0)) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32, reg_type="SGPR")
    
    # Subtract the second signed input from the first input, store the result into a scalar register and store the carryout bit into SCC.
    def s_sub_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32, reg_type="SGPR")
        reg_d_value = reg_s0_value - reg_s1_value
        sign = 1 if (reg_d_value < 0) else 0
        reg_scc_value = 1 if (sign != (reg_s0_value < 0)) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32, reg_type="SGPR")
    
    # Add two unsigned inputs and a carry-in bit, store the result into a scalar register and store the carry-out bit into SCC.
    def s_addc_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_scc_value = self.get_scc_value()
        reg_d_value = reg_s0_value + reg_s1_value + reg_scc_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Subtract the second unsigned input from the first input, subtract the carry-in bit, store the result into a scalar register and store the carry-out bit into SCC.
    def s_subb_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_scc_value = self.get_scc_value()
        reg_d_value = reg_s0_value - reg_s1_value - reg_scc_value
        reg_scc_value = 1 if (reg_d_value < 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Calculate the absolute value of difference between two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_absdiff_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32, reg_type="SGPR")
        reg_d_value = abs(reg_s0_value - reg_s1_value)
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32, reg_type="SGPR")
    
    # Given a shift count in the second scalar input, calculate the logical shift left of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_lshl_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = reg_s0_value << reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Given a shift count in the second scalar input, calculate the logical shift left of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_lshl_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64, reg_type="SGPR")
        reg_d_value = reg_s0_value << reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64, reg_type="SGPR")
    
    # Given a shift count in the second scalar input, calculate the logical shift right of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_lshr_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = reg_s0_value >> reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Given a shift count in the second scalar input, calculate the logical shift right of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_lshr_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64, reg_type="SGPR")
        reg_d_value = reg_s0_value >> reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64, reg_type="SGPR")

    # Given a shift count in the second scalar input, calculate the arithmetic shift right (preserving sign bit) of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_ashr_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = reg_s0_value >> reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32, reg_type="SGPR")

    # Given a shift count in the second scalar input, calculate the arithmetic shift right (preserving sign bit) of the first scalar input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_ashr_i64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=64, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64, reg_type="SGPR")
        reg_d_value = reg_s0_value >> reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=64, reg_type="SGPR")
    
    # Calculate the logical shift left of the first input by 1, then add the second input, store the result into a scalar register and set SCC iff the summation results in an unsigned overflow.
    def s_lshl1_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = (reg_s0_value << 1) + reg_s1_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Calculate the logical shift left of the first input by 2, then add the second input, store the result into a scalar register and set SCC iff the summation results in an unsigned overflow.
    def s_lshl2_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = (reg_s0_value << 2) + reg_s1_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Calculate the logical shift left of the first input by 3, then add the second input, store the result into a scalar register and set SCC iff the summation results in an unsigned overflow.
    def s_lshl3_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = (reg_s0_value << 3) + reg_s1_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Calculate the logical shift left of the first input by 4, then add the second input, store the result into a scalar register and set SCC iff the summation results in an unsigned overflow.
    def s_lshl4_add_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = (reg_s0_value << 4) + reg_s1_value
        reg_scc_value = 1 if (reg_d_value >= 2**32) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")

    # Select the minimum of two signed integers, store the selected value into a scalar register and set SCC iff the first value is selected.
    def s_min_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32, reg_type="SGPR")
        reg_d_value = min(reg_s0_value, reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == reg_s0_value) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32, reg_type="SGPR")
    
    # Select the minimum of two unsigned integers, store the selected value into a scalar register and set SCC iff the first value is selected.
    def s_min_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = min(reg_s0_value, reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == reg_s0_value) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")

    # Select the maximum of two signed integers, store the selected value into a scalar register and set SCC iff the first value is selected.
    def s_max_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32, reg_type="SGPR")
        reg_d_value = max(reg_s0_value, reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == reg_s0_value) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32, reg_type="SGPR")

    # Select the maximum of two unsigned integers, store the selected value into a scalar register and set SCC iff the first value is selected.
    def s_max_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = max(reg_s0_value, reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == reg_s0_value) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")

    # Calculate bitwise AND on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_and_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = reg_s0_value & reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")

    # Calculate bitwise AND on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_and_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64, reg_type="SGPR")
        reg_d_value = reg_s0_value & reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64, reg_type="SGPR")
    
    # Calculate bitwise OR on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_or_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = reg_s0_value | reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")

    # Calculate bitwise OR on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_or_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64, reg_type="SGPR")
        reg_d_value = reg_s0_value | reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64, reg_type="SGPR")

    # Calculate bitwise XOR on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_xor_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = reg_s0_value ^ reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Calculate bitwise XOR on two scalar inputs, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_xor_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64, reg_type="SGPR")
        reg_d_value = reg_s0_value ^ reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64, reg_type="SGPR")
    
    # Calculate bitwise NAND on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_nand_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = ~(reg_s0_value & reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Calculate bitwise NAND on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_nand_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64, reg_type="SGPR")
        reg_d_value = ~(reg_s0_value & reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64, reg_type="SGPR")
    
    # Calculate bitwise NOR on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_nor_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = ~(reg_s0_value | reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Calculate bitwise NOR on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_nor_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64, reg_type="SGPR")
        reg_d_value = ~(reg_s0_value | reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64, reg_type="SGPR")
    
    # Calculate bitwise XNOR on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_xnor_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = ~(reg_s0_value ^ reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Calculate bitwise XNOR on two scalar inputs, store the result into a scalar register and set SCC if the result is nonzero.
    def s_xnor_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64, reg_type="SGPR")
        reg_d_value = ~(reg_s0_value ^ reg_s1_value)
        reg_scc_value = 1 if (reg_d_value == 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64, reg_type="SGPR")
    
    # Calculate bitwise AND with the first input and the negation of the second input, store the result into a scalar register and set SCC if the result is nonzero.
    def s_and_not1_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = reg_s0_value & ~reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Calculate bitwise AND with the first input and the negation of the second input, store the result into a scalar register and set SCC if the result is nonzero.
    def s_and_not1_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64, reg_type="SGPR")
        reg_d_value = reg_s0_value & ~reg_s1_value
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64, reg_type="SGPR")
    
    # Calculate bitwise OR with the first input and the negation of the second input, store the result into a scalar register and set SCC if the result is nonzero.
    def s_or_not1_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32, reg_type="SGPR")
        reg_d_value = reg_s0_value | ~reg_s1_value
        reg_scc_value = 1 if (reg_d_value != -1) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Calculate bitwise OR with the first input and the negation of the second input, store the result into a scalar register and set SCC if the result is nonzero.
    def s_or_not1_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=64, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=64, reg_type="SGPR")
        reg_d_value = reg_s0_value | ~reg_s1_value
        reg_scc_value = 1 if (reg_d_value != -1) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64, reg_type="SGPR")

    # Extract an unsigned bitfield from the first input using field offset and size encoded in the second input, store the result into a scalar register and set SCC iff the result is nonzero
    def s_bfe_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        # Field offset is [4:0] of reg_s1
        field_offset = reg_s1_value & 0x1F
        # Field size is [22:16] of reg_s1
        field_size = (reg_s1_value >> 16) & 0x7F
        reg_d_value = (reg_s0_value >> field_offset) & ((1 << field_size) - 1)
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=field_size, reg_type="SGPR")
    
    # Extract a signed bitfield from the first input using field offset and size encoded in the second input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_bfe_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        # Field offset is [4:0] of reg_s1
        field_offset = reg_s1_value & 0x1F
        # Field size is [22:16] of reg_s1
        field_size = (reg_s1_value >> 16) & 0x7F
        reg_d_value = (reg_s0_value >> field_offset) & ((1 << field_size) - 1)
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=field_size, reg_type="SGPR")
    
    # Extract an unsigned bitfield from the first input using field offset and size encoded in the second input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_bfe_u64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64, reg_type="SGPR")
        # Field offset is [5:0] of reg_s1
        field_offset = reg_s1_value & 0x3F
        # Field size is [22:16] of reg_s1
        field_size = (reg_s1_value >> 16) & 0x7F
        reg_d_value = (reg_s0_value >> field_offset) & ((1 << field_size) - 1)
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=field_size, reg_type="SGPR")
    
    # Extract a signed bitfield from the first input using field offset and size encoded in the second input, store the result into a scalar register and set SCC iff the result is nonzero.
    def s_bfe_i64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=64, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64, reg_type="SGPR")
        # Field offset is [5:0] of reg_s1
        field_offset = reg_s1_value & 0x3F
        # Field size is [22:16] of reg_s1
        field_size = (reg_s1_value >> 16) & 0x7F
        reg_d_value = (reg_s0_value >> field_offset) & ((1 << field_size) - 1)
        reg_scc_value = 1 if (reg_d_value != 0) else 0
        self.set_scc_value(reg_scc_value)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=field_size, reg_type="SGPR")
    
    # Calculate a bitfield mask given a field offset and size and store the result in a scalar register.
    def s_bfm_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        # Field offset is [4:0] of reg_s1
        field_offset = reg_s1_value & 0x1F
        # Field size is [4:0] of reg_s0
        field_size = reg_s0_value & 0x1F
        reg_d_value = ((1 << field_size) - 1) << field_offset
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Calculate a bitfield mask given a field offset and size and store the result in a scalar register.
    def s_bfm_b64(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=64, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=64, reg_type="SGPR")
        # Field offset is [5:0] of reg_s1
        field_offset = reg_s1_value & 0x3F
        # Field size is [5:0] of reg_s0
        field_size = reg_s0_value & 0x3F
        reg_d_value = ((1 << field_size) - 1) << field_offset
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64, reg_type="SGPR")
    
    # Multiply two signed integers and store the result into a scalar register.
    def s_mul_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32, reg_type="SGPR")
        reg_d_value = reg_s0_value * reg_s1_value
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32, reg_type="SGPR")
    
    # Multiply two unsigned integers and store the high 32 bits of the result into a scalar register.
    def s_mul_hi_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = (reg_s0_value * reg_s1_value) >> 32
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Multiply two signed integers and store the high 32 bits of the result into a scalar register.
    def s_mul_hi_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32, reg_type="SGPR")
        reg_d_value = (reg_s0_value * reg_s1_value) >> 32
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32, reg_type="SGPR")
    
    # Select the first input if SCC is true otherwise select the second input, then store the selected input into a scalar register.
    def s_cselect_b32(self, reg_d, reg_s0, reg_s1):
        reg_scc_value = self.get_scc_value()
        reg_d_value = reg_s0 if reg_scc_value == 1 else reg_s1
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Select the first input if SCC is true otherwise select the second input, then store the selected input into a scalar register.
    def s_cselect_b64(self, reg_d, reg_s0, reg_s1):
        reg_scc_value = self.get_scc_value()
        reg_d_value = reg_s0 if reg_scc_value == 1 else reg_s1
        self.set_register_value(reg_d, reg_d_value, signed=False, size=64, reg_type="SGPR")
    
    # Pack two 16-bit scalar values into a scalar register.
    def s_pack_ll_b32_b16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=16, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=16, reg_type="SGPR")
        reg_d_value = (reg_s1_value << 16) | reg_s0_value
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Pack two 16-bit scalar values into a scalar register.
    def s_pack_lh_b32_b16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=16, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = (reg_s1_value & 0xFFFF0000)| reg_s0_value
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Pack two 16-bit scalar values into a scalar register.
    def s_pack_hh_b32_b16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="SGPR")
        reg_d_value = (reg_s1_value & 0xFFFF0000) | (reg_s0_value >> 16)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")
    
    # Pack two 16-bit scalar values into a scalar register.
    def s_pack_hl_b32_b16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=16, reg_type="SGPR")
        reg_d_value = (reg_s1_value << 16) | (reg_s0_value >> 16)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="SGPR")

    # SOP1
    # Move scalar input into a scalar register. (32-bit)
    def s_move_b32(self, reg_d, reg_s0):
        reg_s0_val = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        self.set_register_value(reg_d, reg_s0_val, signed=False, size=32, reg_type="SGPR")

    # Move scalar input into a scalar register. (64-bit)
    def s_move_b64(self, reg_d, reg_s0):
        reg_s0_val = self.get_register_value(reg_s0, signed=False, size=64, reg_type="SGPR")
        self.set_register_value(reg_d, reg_s0_val, signed=False, size=64, reg_type="SGPR")

    # Move scalar input into a scalar register iff SCC is nonzero.
    def c_move_b32(self, reg_d, reg_s0):
       if (self.get_scc_value() == 1):
        self.s_move_b32(reg_d, reg_s0)
    
    def c_move_b64(self, reg_d, reg_s0):
       if (self.get_scc_value() == 1):
        self.s_move_b64(reg_d, reg_s0)

    # Reverse the order of bits in a scalar input and store the result into a scalar register.
    def s_brev_b32(self, reg_d, reg_s0):
        reg_s0_val = self.get_register_value(reg_s0, signed=False, size=32, reg_type="SGPR")
        tmp = utils.rev_b32(reg_s0_val)
        self.set_register_value(reg_d, tmp, signed=False, size=32, reg_type="SGPR")

        
    def s_brev_b64(self, reg_d, reg_s0):
        reg_s0_val = self.get_register_value(reg_s0, signed=False, size=64, reg_type="SGPR")
        tmp = utils.rev_b64(reg_s0_val)
        self.set_register_value(reg_d, tmp, signed=False, size=64, reg_type="SGPR")

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
    
    # Copy data from one of two inputs based on the vector condition code and store the result into a vector register.
    def v_cndmask_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_type = self.get_register_type(reg_s0)
        reg_s1_type = self.get_register_type(reg_s1)
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type=reg_s0_type)
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type=reg_s1_type)
        reg_vcc_value = self.get_vcc_value()
        reg_d_value = reg_s0_value if reg_vcc_value == 1 else reg_s1_value
        reg_d_type = reg_s0_type if reg_s0_type == reg_s1_type else reg_s1_type
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type=reg_d_type)
    
    # Dot product of packed FP16 values, accumulate with destination.
    def v_dot2acc_f32_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s0_value_low = utils.fp16_to_fp32(reg_s0_value & 0xFFFF)
        reg_s0_value_high = utils.fp16_to_fp32(reg_s0_value >> 16)
        reg_s1_value_low = utils.fp16_to_fp32(reg_s1_value & 0xFFFF)
        reg_s1_value_high = utils.fp16_to_fp32(reg_s1_value >> 16)
        reg_d_value = (reg_s0_value_low * reg_s1_value_low) + (reg_s0_value_high * reg_s1_value_high)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Add two floating point inputs and store the result into a vector register.
    def v_add_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = reg_s0_value + reg_s1_value
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Subtract the second floating point input from the first input and store the result into a vector register.
    def v_sub_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = reg_s0_value - reg_s1_value
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Subtract the first floating point input from the second input and store the result into a vector register.
    def v_subrev_f32(self, reg_d, reg_s0, reg_s1):
        self.v_sub_f32(reg_d, reg_s1, reg_s0)
    
    # Multiply two single-precision values and accumulate the result with the destination. Follows DX9 rules where 0.0 times anything produces 0.0 (this is not IEEE compliant).
    def v_fmac_dx9_zero_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = self.get_register_value(reg_d, signed=None, size=32, reg_type="VGPR_FLOAT")
        if reg_s0_value == 0 or reg_s1_value == 0:
            reg_d_value = 0
        else:
            reg_d_value = reg_d_value + (reg_s0_value * reg_s1_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply two floating point inputs and store the result in a vector register. Follows DX9 rules where 0.0 times anything produces 0.0 (this differs from other APIs when the other input is infinity or NaN).
    def v_mul_dx9_zero_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        if reg_s0_value == 0 or reg_s1_value == 0:
            reg_d_value = 0
        else:
            reg_d_value = reg_s0_value * reg_s1_value
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply two floating point inputs and store the result into a vector register.
    def v_mul_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = reg_s0_value * reg_s1_value
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply two signed 24 bit integer inputs and store the result as a signed 32 bit integer into a vector register.
    def v_mul_i32_i24(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=24, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=24, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value * reg_s1_value
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32, reg_type="VGPR_INT")
    
    # Multiply two signed 24 bit integer inputs and store the high 32 bits of the result as a signed 32 bit integer into a vector register.
    def v_mul_hi_i32_i24(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=24, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=24, reg_type="VGPR_INT")
        reg_d_value = (reg_s0_value * reg_s1_value) >> 32
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32, reg_type="VGPR_INT")
    
    # Multiply two unsigned 24 bit integer inputs and store the result as a unsigned 32 bit integer into a vector register.
    def v_mul_u32_u24(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=24, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=24, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value * reg_s1_value
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Multiply two unsigned 24 bit integer inputs and store the high 32 bits of the result as a unsigned 32 bit integer into a vector register.
    def v_mul_hi_u32_u24(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=24, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=24, reg_type="VGPR_INT")
        reg_d_value = (reg_s0_value * reg_s1_value) >> 32
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Select the minimum of two floating point inputs and store the result into a vector register
    def v_min_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = min(reg_s0_value, reg_s1_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Select the maximum of two floating point inputs and store the result into a vector register
    def v_max_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = max(reg_s0_value, reg_s1_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")    
    
    # Select the minimum of two signed integers and store the selected value into a vector register.
    def v_min_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32, reg_type="VGPR_INT")
        reg_d_value = min(reg_s0_value, reg_s1_value)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32, reg_type="VGPR_INT")
    
    # Select the maximum of two signed integers and store the selected value into a vector register.
    def v_max_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32, reg_type="VGPR_INT")
        reg_d_value = max(reg_s0_value, reg_s1_value)
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32, reg_type="VGPR_INT")
    
    # Select the minimum of two unsigned integers and store the selected value into a vector register.
    def v_min_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = min(reg_s0_value, reg_s1_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Select the maximum of two unsigned integers and store the selected value into a vector register.
    def v_max_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = max(reg_s0_value, reg_s1_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Given a shift count in the first vector input, calculate the logical shift left of the second vector input and store the result into a vector register.
    def v_lshlrev_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s1_value << reg_s0_value
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Given a shift count in the first vector input, calculate the logical shift right of the second vector input and store the result into a vector register
    def v_lshrrev_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s1_value >> reg_s0_value
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Given a shift count in the first vector input, calculate the arithmetic shift right (preserving sign bit) of the second vector input and store the result into a vector register.
    def v_ashrrev_i32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=True, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s1_value >> reg_s0_value
        self.set_register_value(reg_d, reg_d_value, signed=True, size=32, reg_type="VGPR_INT")
    
    # Calculate bitwise AND on two vector inputs and store the result into a vector register.
    def v_and_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value & reg_s1_value
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Calculate bitwise OR on two vector inputs and store the result into a vector register.
    def v_or_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value | reg_s1_value
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Calculate bitwise XOR on two vector inputs and store the result into a vector register.
    def v_xor_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value ^ reg_s1_value
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Calculate bitwise XNOR on two vector inputs and store the result into a vector register.
    def v_xnor_b32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_INT")
        reg_d_value = ~(reg_s0_value ^ reg_s1_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_INT")
    
    # Add two unsigned inputs and a bit from a carry-in mask, store the result into a vector register and store the carry-out mask into a scalar register.
    def v_add_co_ci_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_vcc_value = self.get_vcc_value()
        reg_d_value = reg_s0_value + reg_s1_value + reg_vcc_value
        reg_vcc_value = 1 if reg_d_value > 0xFFFFFFFF else 0
        self.set_vcc_value(reg_vcc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Subtract the second unsigned input from the first input, subtract a bit from the carry-in mask, store the result into a vector register and store the carry-out mask to a scalar register
    def v_sub_co_ci_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_vcc_value = self.get_vcc_value()
        reg_d_value = reg_s0_value - reg_s1_value - reg_vcc_value
        reg_vcc_value = 1 if reg_d_value < 0 else 0
        self.set_vcc_value(reg_vcc_value)
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Subtract the first unsigned input from the second input, subtract a bit from the carry-in mask, store the result into a vector register and store the carry-out mask to a scalar register.
    def v_subrev_co_ci_u32(self, reg_d, reg_s0, reg_s1):
        self.v_sub_co_ci_u32(reg_d, reg_s1, reg_s0)
    
    # Add two unsigned inputs and store the result into a vector register. No carry-in or carry-out support.
    def v_add_nc_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value + reg_s1_value
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Subtract the second unsigned input from the first input and store the result into a vector register. No carry-in or carry-out support.
    def v_sub_nc_u32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=False, size=32, reg_type="VGPR_INT")
        reg_s1_value = self.get_register_value(reg_s1, signed=False, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value - reg_s1_value
        self.set_register_value(reg_d, reg_d_value, signed=False, size=32, reg_type="VGPR_INT")
    
    # Subtract the first unsigned input from the second input and store the result into a vector register. No carry-in or carry-out support.
    def v_subrev_nc_u32(self, reg_d, reg_s0, reg_s1):
        self.v_sub_nc_u32(reg_d, reg_s1, reg_s0)
    
    # Multiply two floating point inputs and accumulate the result into the destination register using fused multiplyadd.
    def v_fmac_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = self.get_register_value(reg_d, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = reg_d_value + (reg_s0_value * reg_s1_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply a single-precision float with a literal constant and add a second single-precision float using fused multiply-add.
    def v_fmamk_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_simm32_value = self.get_register_value(self.reg_simm, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = reg_s1_value + (reg_s0_value * reg_simm32_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply two single-precision floats and add a literal constant using fused multiply-add.
    def v_fmaak_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_simm32_value = self.get_register_value(self.reg_simm, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_d_value = reg_simm32_value + (reg_s0_value * reg_s1_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Convert two single-precision float inputs into a packed FP16 result with round toward zero semantics (ignore the current rounding mode), and store the result into a vector register.
    def v_cvt_pk_rtz_f16_f32(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        
        # Convert the first input.
        reg_s0_value = utils.fp32_to_fp16(reg_s0_value)
        
        # Convert the second input.
        reg_s1_value = utils.fp32_to_fp16(reg_s1_value)
        reg_s1_value = reg_s1_value << 16
        
        # Combine the two inputs.
        reg_d_value = reg_s0_value | reg_s1_value
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Add two floating point inputs and store the result into a vector register.
    def v_add_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = reg_s0_value + reg_s1_value
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Subtract the second floating point input from the first input and store the result into a vector register.
    def v_sub_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = reg_s0_value - reg_s1_value
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Subtract the first floating point input from the second input and store the result into a vector register.
    def v_subrev_f16(self, reg_d, reg_s0, reg_s1):
        self.v_sub_f16(reg_d, reg_s1, reg_s0)
    
    # Multiply two floating point inputs and store the result into a vector register.
    def v_mul_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = reg_s0_value * reg_s1_value
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply two floating point inputs and accumulate the result into the destination register using fused multiplyadd.
    def v_fmac_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = utils.fp16_to_fp32(self.get_register_value(reg_d, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = reg_d_value + (reg_s0_value * reg_s1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply a FP16 value with a literal constant and add a second FP16 value using fused multiply-add.
    def v_fmamk_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_simm32_value = utils.fp16_to_fp32(self.get_register_value(self.reg_simm, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = reg_s1_value + (reg_s0_value * reg_simm32_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Multiply two FP16 values and add a literal constant using fused multiply-add.
    def v_fmaak_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_simm32_value = utils.fp16_to_fp32(self.get_register_value(self.reg_simm, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = reg_simm32_value + (reg_s0_value * reg_s1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Select the maximum of two floating point inputs and store the result into a vector register.
    def v_max_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = max(reg_s0_value, reg_s1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    # Select the minimum of two floating point inputs and store the result into a vector register.
    def v_min_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = utils.fp16_to_fp32(self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_d_value = min(reg_s0_value, reg_s1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")
    
    #Multiply the first input, a floating point value, by an integral power of 2 specified in the second input, a signed integer value, and store the floating point result into a vector register. Compare with the ldexp() function in C.
    def v_ldexp_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = utils.fp16_to_fp32(self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT"))
        reg_s1_value = self.get_register_value(reg_s1, signed=True, size=32, reg_type="VGPR_INT")
        reg_d_value = reg_s0_value * (2 ** reg_s1_value)
        reg_d_value = utils.fp32_to_fp16(reg_d_value)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")

    # Multiply packed FP16 values and accumulate with destination.
    def v_pk_fmac_f16(self, reg_d, reg_s0, reg_s1):
        reg_s0_value = self.get_register_value(reg_s0, signed=None, size=32, reg_type="VGPR_FLOAT")
        reg_s1_value = self.get_register_value(reg_s1, signed=None, size=32, reg_type="VGPR_FLOAT")
        
        # Extract the first input.
        reg_s0_value_lo = utils.fp32_to_fp16(reg_s0_value & 0xFFFF)
        reg_s0_value_hi = utils.fp32_to_fp16(reg_s0_value >> 16)
        
        # Extract the second input.
        reg_s1_value_lo = utils.fp32_to_fp16(reg_s1_value & 0xFFFF)
        reg_s1_value_hi = utils.fp32_to_fp16(reg_s1_value >> 16)
        
        reg_d_value = self.get_register_value(reg_d, signed=None, size=32, reg_type="VGPR_FLOAT")
        
        # Extract the destination.
        reg_d_value_lo = utils.fp32_to_fp16(reg_d_value & 0xFFFF)
        reg_d_value_hi = utils.fp32_to_fp16(reg_d_value >> 16)
        
        # Accumulate the result.
        reg_d_value_lo = reg_d_value_lo + (reg_s0_value_lo * reg_s1_value_lo)
        reg_d_value_hi = reg_d_value_hi + (reg_s0_value_hi * reg_s1_value_hi)
        reg_d_value = utils.fp16_to_fp32(reg_d_value_lo) | (utils.fp16_to_fp32(reg_d_value_hi) << 16)
        self.set_register_value(reg_d, reg_d_value, signed=None, size=32, reg_type="VGPR_FLOAT")

    # Get the register value from the register ID.
    def get_register_value(self, reg_id, signed, size, reg_type):
        if reg_type == self.reg_types["VGPR_INT"] or reg_type == self.reg_types["VGPR_FLOAT"]:
            reg_file = self.vector_registers
        elif reg_type == self.reg_types["SGPR"]:
            reg_file = self.scalar_registers
        elif reg_type == self.reg_types["SPECIAL"]:
            reg_file = self.special_registers
        else:
            raise Exception("Register type not found.")
        reg_value = reg_file[reg_id]
        if reg_type == self.reg_types["VGPR_FLOAT"]:
            reg_value = float(reg_value)
        else:
            reg_value = int(reg_value)
            if signed:
                if reg_type == self.reg_types["VGPR_FLOAT"]:
                    raise Exception("Floats should not be deemed signed.")
                sign = reg_value >> (size - 1)
                if sign == 1:
                    reg_value = reg_value - 2**size
            reg_value = reg_value % 2**size
        return reg_value

    # Set the register value from the register ID.
    def set_register_value(self, reg_id, reg_value, signed, size, reg_type):
        if reg_type == self.reg_types["VGPR_INT"] or reg_type == self.reg_types["VGPR_FLOAT"]:
            reg_file = self.vector_registers
        elif reg_type == self.reg_types["SGPR"]:
            reg_file = self.scalar_registers
        elif reg_type == self.reg_types["SPECIAL"]:
            reg_file = self.special_registers
        else:
            raise Exception("Register type not found.")
        if reg_type == self.reg_types["VGPR_FLOAT"]:
            reg_value = float(reg_value)
        else:
            reg_value = int(reg_value)
            if signed:
                sign = reg_value >> (size - 1)
                if sign == 1:
                    reg_value = reg_value - 2**size
            reg_value = reg_value % 2**size
        reg_file[reg_id] = reg_value
    
    # Get the special register ID from the special register name.
    def get_special_register_meta(self, reg_name):
        special_register = self.special_registers_meta.get(reg_name)
        if special_register == None:
            raise Exception("Special register name not found.")
        return special_register
    
    # Function to get a bitfield by name from a special register.
    def get_special_register_meta_bitfield(self, reg_name, field_name):
        special_register = self.get_special_register_meta(reg_name)
        reg_id = special_register["reg_id"]
        reg_fields = special_register["reg_fields"]
        reg_value = self.get_register_value(reg_id, signed=False, size=32, reg_type=self.reg_types["SPECIAL"])
        field_bit_pos = reg_fields[field_name]["bit_pos"]
        field_bit_width = reg_fields[field_name]["bit_width"]
        field_mask = ((1 << field_bit_width) - 1) << field_bit_pos
        field_value = (reg_value & field_mask) >> field_bit_pos
        return field_value

    # Function to set a bitfield by name from a special register.
    def set_special_register_bitfield(self, reg_name, field_name, field_value):
        special_register = self.get_special_register_meta(reg_name)
        reg_id = special_register["reg_id"]
        reg_fields = special_register["reg_fields"]
        reg_value = self.get_register_value(reg_id, signed=False, size=32, reg_type=self.reg_types["SPECIAL"])
        field_bit_pos = reg_fields[field_name]["bit_pos"]
        field_bit_width = reg_fields[field_name]["bit_width"]
        field_mask = ((1 << field_bit_width) - 1) << field_bit_pos
        # Choice to tolerate bitfield overflow or not.
        field_value = (field_value << field_bit_pos) & field_mask
        reg_value = (reg_value & ~field_mask) | field_value
        self.set_register_value(reg_id, reg_value, signed=False, size=32, reg_type="SGPR")

    # Function to set the SCC value.
    def set_scc_value(self, scc_value):
        self.set_special_register_bitfield("STATUS", "SCC", scc_value)
    
    def get_scc_value(self):
        scc = self.get_special_register_meta_bitfield("STATUS", "SCC")
        return scc
    
    # Function to set the VCC value.
    def set_vcc_value(self, vcc_value):
        self.set_special_register_bitfield("STATUS", "VCC", vcc_value)
    
    def get_vcc_value(self):
        vcc = self.get_special_register_meta_bitfield("STATUS", "VCC")
        return vcc