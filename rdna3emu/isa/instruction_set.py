# This file defines the instruction set for RNDA3.
import sys

# Add rdna3emu to path
sys.path.append("../rdna3emu/")

from rdna3emu.isa.scalar_ops import ScalarOps
from rdna3emu.isa.vector_ops import VectorOps
from rdna3emu.isa.registers import Registers
from rdna3emu.isa.memory import Memory
from rdna3emu.isa.utils import populate_instruction_usage


class InstructionSet:
    def __init__(self):
        self.registers = Registers()
        self.memory = Memory(self.registers)
        self.vector_ops = VectorOps(self.registers, self.memory)
        self.scalar_ops = ScalarOps(self.registers, self.memory)
        self.instruction_type_map = {
            "SCALAR": ["SOP2", "SOP1", "SOPP", "SOPC", "SOPK", "SMEM"],
            "VECTOR": ["VOP2", "VOP1", "VOPC", "VOP3", "VOP3SD", "VOPD"],
            "MEMORY": ["FLAT", "GLOBAL", "SCRATCH", "LDS"],
        }
        self.instructions = {
            "SOP2": {
                "S_ADD_U32": self.scalar_ops.s_add_u32,  # 0
                "S_SUB_U32": self.scalar_ops.s_sub_u32,  # 1
                "S_ADD_I32": self.scalar_ops.s_add_i32,  # 2
                "S_SUB_I32": self.scalar_ops.s_sub_i32,  # 3
                "S_ADDC_U32": self.scalar_ops.s_addc_u32,  # 4
                "S_SUBB_U32": self.scalar_ops.s_subb_u32,  # 5
                "S_ABSDIFF_I32": self.scalar_ops.s_absdiff_i32,  # 6
                "S_LSHL_B32": self.scalar_ops.s_lshl_b32,  # 8
                "S_LSHL_B64": self.scalar_ops.s_lshl_b64,  # 9
                "S_LSHR_B32": self.scalar_ops.s_lshr_b32,  # 10
                "S_LSHR_B64": self.scalar_ops.s_lshr_b64,  # 11
                "S_ASHR_I32": self.scalar_ops.s_ashr_i32,  # 12
                "S_ASHR_I64": self.scalar_ops.s_ashr_i64,  # 13
                "S_LSHL1_ADD_U32": self.scalar_ops.s_lshl1_add_u32,  # 14
                "S_LSHL2_ADD_U32": self.scalar_ops.s_lshl2_add_u32,  # 15
                "S_LSHL3_ADD_U32": self.scalar_ops.s_lshl3_add_u32,  # 16
                "S_LSHL4_ADD_U32": self.scalar_ops.s_lshl4_add_u32,  # 17
                "S_MIN_I32": self.scalar_ops.s_min_i32,  # 18
                "S_MIN_U32": self.scalar_ops.s_min_u32,  # 19
                "S_MAX_I32": self.scalar_ops.s_max_i32,  # 20
                "S_MAX_U32": self.scalar_ops.s_max_u32,  # 21
                "S_AND_B32": self.scalar_ops.s_and_b32,  # 22
                "S_AND_B64": self.scalar_ops.s_and_b64,  # 23
                "S_OR_B32": self.scalar_ops.s_or_b32,  # 24
                "S_OR_B64": self.scalar_ops.s_or_b64,  # 25
                "S_XOR_B32": self.scalar_ops.s_xor_b32,  # 26
                "S_XOR_B64": self.scalar_ops.s_xor_b64,  # 27
                "S_NAND_B32": self.scalar_ops.s_nand_b32,  # 28
                "S_NAND_B64": self.scalar_ops.s_nand_b64,  # 29
                "S_NOR_B32": self.scalar_ops.s_nor_b32,  # 30
                "S_NOR_B64": self.scalar_ops.s_nor_b64,  # 31
                "S_XNOR_B32": self.scalar_ops.s_xnor_b32,  # 32
                "S_XNOR_B64": self.scalar_ops.s_xnor_b64,  # 33
                "S_AND_NOT1_B32": self.scalar_ops.s_and_not1_b32,  # 34
                "S_AND_NOT1_B64": self.scalar_ops.s_and_not1_b64,  # 35
                "S_OR_NOT1_B32": self.scalar_ops.s_or_not1_b32,  # 36
                "S_OR_NOT1_B64": self.scalar_ops.s_or_not1_b64,  # 37
                "S_BFE_U32": self.scalar_ops.s_bfe_u32,  # 38
                "S_BFE_I32": self.scalar_ops.s_bfe_i32,  # 39
                "S_BFE_U64": self.scalar_ops.s_bfe_u64,  # 40
                "S_BFE_I64": self.scalar_ops.s_bfe_i64,  # 41
                "S_BFM_B32": self.scalar_ops.s_bfm_b32,  # 42
                "S_BFM_B64": self.scalar_ops.s_bfm_b64,  # 43
                "S_MUL_I32": self.scalar_ops.s_mul_i32,  # 44
                "S_MUL_HI_U32": self.scalar_ops.s_mul_hi_u32,  # 45
                "S_MUL_HI_I32": self.scalar_ops.s_mul_hi_i32,  # 46
                "S_CSELECT_B32": self.scalar_ops.s_cselect_b32,  # 48
                "S_CSELECT_B64": self.scalar_ops.s_cselect_b64,  # 49
                "S_PACK_LL_B32_B16": self.scalar_ops.s_pack_ll_b32_b16,  # 50
                "S_PACK_LH_B32_B16": self.scalar_ops.s_pack_lh_b32_b16,  # 51
                "S_PACK_HH_B32_B16": self.scalar_ops.s_pack_hh_b32_b16,  # 52
                "S_PACK_HL_B32_B16": self.scalar_ops.s_pack_hl_b32_b16,  # 53
            },
            "SOP1": {
                "S_MOV_B32": self.scalar_ops.s_move_b32,
                "S_MOV_B64": self.scalar_ops.s_move_b64,
                "C_MOV_B32": self.scalar_ops.c_move_b32,
                "C_MOV_B64": self.scalar_ops.c_move_b64,
                "S_BREV_B32": self.scalar_ops.s_brev_b32,
                "S_BREV_B64": self.scalar_ops.s_brev_b64,
                "S_CTZ_I32_B32": self.scalar_ops.s_ctz_i32_b32,
                "S_CTZ_I32_B64": self.scalar_ops.s_ctz_i32_b64,
                "S_CLZ_I32_U32": self.scalar_ops.s_clz_i32_u32,
                "S_CLZ_I32_U64": self.scalar_ops.s_clz_i32_u64,
                "S_CLS_I32": self.scalar_ops.s_cls_i32,
                "S_CLS_I32_I64": self.scalar_ops.s_cls_i32_i64,
                "S_SEXT_I32_I8": self.scalar_ops.s_sext_i32_i8,
                "S_SEXT_I32_I16": self.scalar_ops.s_sext_i32_i16,
                "S_BITSET0_B32": self.scalar_ops.s_bitset0_b32,
                "S_BITSET0_B64": self.scalar_ops.s_bitset0_b64,
                "S_BITSET1_B32": self.scalar_ops.s_bitset1_b32,
                "S_BITSET1_B64": self.scalar_ops.s_bitset1_b64,
                "S_BITREPLICATE_B64_B32": self.scalar_ops.s_bitreplicate_b64_b32,
                "S_ABS_I32": self.scalar_ops.s_abs_i32,
                "S_BCNT0_I32_B32": self.scalar_ops.s_bcnt0_i32_b32,
                "S_BCNT0_I32_B64": self.scalar_ops.s_bcnt0_i32_b64,
                "S_BCNT1_I32_B32": self.scalar_ops.s_bcnt1_i32_b32,
                "S_BCNT1_I32_B64": self.scalar_ops.s_bcnt1_i32_b64,
                "S_QUADMASK_B32": self.scalar_ops.s_quadmask_b32,
                "S_QUADMASK_B64": self.scalar_ops.s_quadmask_b64,
                "S_WQM_B32": self.scalar_ops.s_wqm_b32,
                "S_WQM_B64": self.scalar_ops.s_wqm_b64,
                "S_NOT_B32": self.scalar_ops.s_not_b32,
                "S_NOT_B64": self.scalar_ops.s_not_b64,
                "S_AND_SAVEEXEC_B32": self.scalar_ops.s_and_saveexec_b32,
                "S_AND_SAVEEXEC_B64": self.scalar_ops.s_and_saveexec_b64,
                "S_OR_SAVEEXEC_B32": self.scalar_ops.s_or_saveexec_b32,
                "S_OR_SAVEEXEC_B64": self.scalar_ops.s_or_saveexec_b64,
                "S_XOR_SAVEEXEC_B32": self.scalar_ops.s_xor_saveexec_b32,
                "S_XOR_SAVEEXEC_B64": self.scalar_ops.s_xor_saveexec_b64,
                "S_NAND_SAVEEXEC_B32": self.scalar_ops.s_nand_saveexec_b32,
                "S_NAND_SAVEEXEC_B64": self.scalar_ops.s_nand_saveexec_b64,
                "S_NOR_SAVEEXEC_B32": self.scalar_ops.s_nor_saveexec_b32,
                "S_NOR_SAVEEXEC_B64": self.scalar_ops.s_nor_saveexec_b64,
                "S_XNOR_SAVEEXEC_B32": self.scalar_ops.s_xnor_saveexec_b32,
                "S_XNOR_SAVEEXEC_B64": self.scalar_ops.s_xnor_saveexec_b64,
                "S_AND_NOT0_SAVEEXEC_B32": self.scalar_ops.s_and_not0_saveexec_b32,
                "S_AND_NOT0_SAVEEXEC_B64": self.scalar_ops.s_and_not0_saveexec_b64,
                "S_OR_NOT0_SAVEEXEC_B32": self.scalar_ops.s_or_not0_saveexec_b32,
                "S_AND_NOT1_SAVEEXEC_B32": self.scalar_ops.s_and_not1_saveexec_b32,
                "S_AND_NOT1_SAVEEXEC_B64": self.scalar_ops.s_and_not1_saveexec_b64,
                "S_OR_NOT1_SAVEEXEC_B32": self.scalar_ops.s_or_not1_saveexec_b32,
                "S_OR_NOT1_SAVEEXEC_B64": self.scalar_ops.s_or_not1_saveexec_b64,
                "S_AND_NOT0_WREXEC_B32": self.scalar_ops.s_and_not0_wrexec_b32,
                "S_AND_NOT0_WREXEC_B64": self.scalar_ops.s_and_not0_wrexec_b64,
                "S_AND_NOT1_WREXEC_B32": self.scalar_ops.s_and_not1_wrexec_b32,
                "S_AND_NOT1_WREXEC_B64": self.scalar_ops.s_and_not1_wrexec_b64,
                "S_MOVRELS_B32": self.scalar_ops.s_movrels_b32,
                "S_MOVRELD_B32": self.scalar_ops.s_movereld_b32,
                "S_MOVRELD_B64": self.scalar_ops.s_movreld_b64,
                "S_MOVRELSD_2_B32": self.scalar_ops.s_moverelsd_2_b32,
                "S_GETPC_B64": self.scalar_ops.s_getpc_b64,
                "S_SETPC_B64": self.scalar_ops.s_setpc_b64,
                "S_SWAPPC_B64": self.scalar_ops.s_swappc_b64,
                "S_RFE_B64": self.scalar_ops.s_rfe_b64,
                "S_SENDMSG_RTN_B32": self.scalar_ops.s_sendmsg_rtn_b32,
                "S_SENDMSG_RTN_B64": self.scalar_ops.s_sendmsg_rtn_b64,
            },
            "VOP2": {
                "V_CNDMASK_B32": self.vector_ops.v_cndmask_b32,
                "V_DOT2ACC_F32_F16": self.vector_ops.v_dot2acc_f32_f16,
                "V_ADD_F32": self.vector_ops.v_add_f32,
                "V_SUB_F32": self.vector_ops.v_sub_f32,
                "V_SUBREV_F32": self.vector_ops.v_subrev_f32,
                "V_FMAC_DX9_ZERO_F32": self.vector_ops.v_fmac_dx9_zero_f32,
                "V_MUL_DX9_ZERO_F32": self.vector_ops.v_mul_dx9_zero_f32,
                "V_MUL_F32": self.vector_ops.v_mul_f32,
                "V_MUL_I32_I24": self.vector_ops.v_mul_i32_i24,
                "V_MUL_HI_I32_I24": self.vector_ops.v_mul_hi_i32_i24,
                "V_MUL_U32_U24": self.vector_ops.v_mul_u32_u24,
                "V_MUL_HI_U32_U24": self.vector_ops.v_mul_hi_u32_u24,
                "V_MIN_F32": self.vector_ops.v_min_f32,
                "V_MAX_F32": self.vector_ops.v_max_f32,
                "V_MIN_I32": self.vector_ops.v_min_i32,
                "V_MAX_I32": self.vector_ops.v_max_i32,
                "V_MIN_U32": self.vector_ops.v_min_u32,
                "V_MAX_U32": self.vector_ops.v_max_u32,
                "V_LSHLREV_B32": self.vector_ops.v_lshlrev_b32,
                "V_LSHRREV_B32": self.vector_ops.v_lshrrev_b32,
                "V_ASHRREV_I32": self.vector_ops.v_ashrrev_i32,
                "V_AND_B32": self.vector_ops.v_and_b32,
                "V_OR_B32": self.vector_ops.v_or_b32,
                "V_XOR_B32": self.vector_ops.v_xor_b32,
                "V_XNOR_B32": self.vector_ops.v_xnor_b32,
                "V_ADD_CO_CI_U32": self.vector_ops.v_add_co_ci_u32,
                "V_SUB_CO_CI_U32": self.vector_ops.v_sub_co_ci_u32,
                "V_SUBREV_CO_CI_U32": self.vector_ops.v_subrev_co_ci_u32,
                "V_ADD_NC_U32": self.vector_ops.v_add_nc_u32,
                "V_SUB_NC_U32": self.vector_ops.v_sub_nc_u32,
                "V_SUBREV_NC_U32": self.vector_ops.v_subrev_nc_u32,
                "V_FMAC_F32": self.vector_ops.v_fmac_f32,
                "V_FMAMK_F32": self.vector_ops.v_fmamk_f32,
                "V_FMAAK_F32": self.vector_ops.v_fmaak_f32,
                "V_CVT_PK_RTZ_F16_F32": self.vector_ops.v_cvt_pk_rtz_f16_f32,
                "V_ADD_F16": self.vector_ops.v_add_f16,
                "V_SUB_F16": self.vector_ops.v_sub_f16,
                "V_SUBREV_F16": self.vector_ops.v_subrev_f16,
                "V_MUL_F16": self.vector_ops.v_mul_f16,
                "V_FMAC_F16": self.vector_ops.v_fmac_f16,
                "V_FMAMK_F16": self.vector_ops.v_fmamk_f16,
                "V_FMAAK_F16": self.vector_ops.v_fmaak_f16,
                "V_MAX_F16": self.vector_ops.v_max_f16,
                "V_MIN_F16": self.vector_ops.v_min_f16,
                "V_LDEXP_F16": self.vector_ops.v_ldexp_f16,
                "V_PK_FMAC_F16": self.vector_ops.v_pk_fmac_f16,
            },
            "VOP1": {
                "V_NOP": self.vector_ops.v_nop,  # 0
                "V_MOV_B32": self.vector_ops.v_mov_b32,  # 1
                "V_READFIRSTLANE_B32": self.vector_ops.v_readfirstlane_b32,  # 2
                "V_CVT_I32_F64": self.vector_ops.v_cvt_i32_f64,  # 3
                "V_CVT_F64_I32": self.vector_ops.v_cvt_f64_i32,  # 4
                "V_CVT_F32_I32": self.vector_ops.v_cvt_f32_i32,  # 5
                "V_CVT_F32_U32": self.vector_ops.v_cvt_f32_u32,  # 6
                "V_CVT_U32_F32": self.vector_ops.v_cvt_u32_f32,  # 7
                "V_CVT_I32_F32": self.vector_ops.v_cvt_i32_f32,  # 8
                "V_CVT_F16_F32": self.vector_ops.v_cvt_f16_f32,  # 10
                "V_CVT_F32_F16": self.vector_ops.v_cvt_f32_f16,  # 11
                "V_CVT_NEAREST_I32_F32": self.vector_ops.v_cvt_nearest_i32_f32,  # 12
                "V_CVT_FLOOR_I32_F32": self.vector_ops.v_cvt_floor_i32_f32,  # 13
                "V_CVT_OFF_F32_I4": self.vector_ops.v_cvt_off_f32_i4,  # 14
                "V_CVT_F32_F64": self.vector_ops.v_cvt_f32_f64,  # 15
                "V_CVT_F64_F32": self.vector_ops.v_cvt_f64_f32,  # 16
                "V_CVT_F32_UBYTE0": self.vector_ops.v_cvt_f32_ubyte0,  # 17
                "V_CVT_F32_UBYTE1": self.vector_ops.v_cvt_f32_ubyte1,  # 18
                "V_CVT_F32_UBYTE2": self.vector_ops.v_cvt_f32_ubyte2,  # 19
                "V_CVT_F32_UBYTE3": self.vector_ops.v_cvt_f32_ubyte3,  # 20
                "V_CVT_U32_F64": self.vector_ops.v_cvt_u32_f64,  # 21
                "V_CVT_F64_U32": self.vector_ops.v_cvt_f64_u32,  # 22
                "V_TRUNC_F64": self.vector_ops.v_trunc_f64,  # 23
                "V_CEIL_F64": self.vector_ops.v_ceil_f64,  # 24
                "V_RNDNE_F64": self.vector_ops.v_rndne_f64,  # 25
                "V_FLOOR_F64": self.vector_ops.v_floor_f64,  # 26
                "V_PIPEFLUSH": self.vector_ops.v_pipeflush,  # 27
                "V_MOV_B16": self.vector_ops.v_mov_b16,  # 28
                "V_FRACT_F32": self.vector_ops.v_fract_f32,  # 32
                "V_TRUNC_F32": self.vector_ops.v_trunc_f32,  # 33
                "V_CEIL_F32": self.vector_ops.v_ceil_f32,  # 34
                "V_RNDNE_F32": self.vector_ops.v_rndne_f32,  # 35
                "V_FLOOR_F32": self.vector_ops.v_floor_f32,  # 36
                "V_EXP_F32": self.vector_ops.v_exp_f32,  # 37
                "V_LOG_F32": self.vector_ops.v_log_f32,  # 39
                "V_RCP_F32": self.vector_ops.v_rcp_f32,  # 42
                "V_RCP_IFLAG_F32": self.vector_ops.v_rcp_iflag_f32,  # 43
                "V_RSQ_F32": self.vector_ops.v_rsq_f32,  # 46
                "V_RCP_F64": self.vector_ops.v_rcp_f64,  # 47
                "V_RSQ_F64": self.vector_ops.v_rsq_f64,  # 49
                "V_SQRT_F32": self.vector_ops.v_sqrt_f32,  # 51
                "V_SQRT_F64": self.vector_ops.v_sqrt_f64,  # 52
                "V_SIN_F32": self.vector_ops.v_sin_f32,  # 53
                "V_COS_F32": self.vector_ops.v_cos_f32,  # 54
                "V_NOT_B32": self.vector_ops.v_not_b32,  # 55
                "V_BFREV_B32": self.vector_ops.v_bfrev_b32,  # 56
                "V_CLZ_I32_U32": self.vector_ops.v_clz_i32_u32,  # 57
                "V_CTZ_I32_B32": self.vector_ops.v_ctz_i32_b32,  # 58
                "V_CLS_I32": self.vector_ops.v_cls_i32,  # 59
                "V_FREXP_EXP_I32_F64": self.vector_ops.v_frexp_exp_i32_f64,  # 60
                "V_FREXP_MANT_F64": self.vector_ops.v_frexp_mant_f64,  # 61
                "V_FRACT_F64": self.vector_ops.v_fract_f64,  # 62
                "V_FREXP_EXP_I32_F32": self.vector_ops.v_frexp_exp_i32_f32,  # 63
                "V_FREXP_MANT_F32": self.vector_ops.v_frexp_mant_f32,  # 64
                "V_MOVRELD_B32": self.vector_ops.v_movreld_b32,  # 66
                "V_MOVRELS_B32": self.vector_ops.v_movrels_b32,  # 67
                "V_MOVRELSD_B32": self.vector_ops.v_movrelsd_b32,  # 68
                "V_MOVRELSD_2_B32": self.vector_ops.v_movrelsd_2_b32,  # 72
                "V_CVT_F16_U16": self.vector_ops.v_cvt_f16_u16,  # 80
                "V_CVT_F16_I16": self.vector_ops.v_cvt_f16_i16,  # 81
                "V_CVT_U16_F16": self.vector_ops.v_cvt_u16_f16,  # 82
                "V_CVT_I16_F16": self.vector_ops.v_cvt_i16_f16,  # 83
                "V_RCP_F16": self.vector_ops.v_rcp_f16,  # 84
                "V_SQRT_F16": self.vector_ops.v_sqrt_f16,  # 85
                "V_RSQ_F16": self.vector_ops.v_rsq_f16,  # 86
                "V_LOG_F16": self.vector_ops.v_log_f16,  # 87
                "V_EXP_F16": self.vector_ops.v_exp_f16,  # 88
                "V_FREXP_MANT_F16": self.vector_ops.v_frexp_mant_f16,  # 89
                "V_FREXP_EXP_I16_F16": self.vector_ops.v_frexp_exp_i16_f16,  # 90
                "V_FLOOR_F16": self.vector_ops.v_floor_f16,  # 91
                "V_CEIL_F16": self.vector_ops.v_ceil_f16,  # 92
                "V_TRUNC_F16": self.vector_ops.v_trunc_f16,  # 93
                "V_RNDNE_F16": self.vector_ops.v_rndne_f16,  # 94
                "V_FRACT_F16": self.vector_ops.v_fract_f16,  # 95
                "V_SIN_F16": self.vector_ops.v_sin_f16,  # 96
                "V_COS_F16": self.vector_ops.v_cos_f16,  # 97
                "V_SAT_PK_U8_I16": self.vector_ops.v_sat_pk_u8_i16,  # 98
                "V_CVT_NORM_I16_F16": self.vector_ops.v_cvt_norm_i16_f16,  # 99
                "V_CVT_NORM_U16_F16": self.vector_ops.v_cvt_norm_u16_f16,  # 100
                "V_SWAP_B32": self.vector_ops.v_swap_b32,  # 101
                "V_SWAP_B16": self.vector_ops.v_swap_b16,  # 102
                "V_PERMLANE64_B32": self.vector_ops.v_permlane64_b32,  # 103
                "V_SWAPREL_B32": self.vector_ops.v_swaprel_b32,  # 104
                "V_NOT_B16": self.vector_ops.v_not_b16,  # 105
                "V_CVT_I32_I16": self.vector_ops.v_cvt_i32_i16,  # 106
                "V_CVT_U32_U16": self.vector_ops.v_cvt_u32_u16,  # 107
            },
            "SOPP": {
                "S_NOP": self.scalar_ops.s_nop,  # 0
                "S_SLEEP": self.scalar_ops.s_sleep,  # 3
                "S_DELAY_ALU": self.scalar_ops.s_delay_alu,  # 7
                "S_WAITCNT": self.scalar_ops.s_waitcnt,  # 9
                "S_TRAP": self.scalar_ops.s_trap,  # 16
                "S_BRANCH": self.scalar_ops.s_branch,  # 32
                "S_CBRANCH_SCC1": self.scalar_ops.s_cbranch_scc1,  # 34
                "S_CBRANCH_VCCZ": self.scalar_ops.s_cbranch_vccz,  # 35
                "S_CBRANCH_VCCNZ": self.scalar_ops.s_cbranch_vccnz,  # 36
                "S_CBRANCH_EXECZ": self.scalar_ops.s_cbranch_execz,  # 37
                "S_CBRANCH_EXECNZ": self.scalar_ops.s_cbranch_execnz,  # 38
                "S_CLAUSE": self.scalar_ops.s_clause,  # 39
                "S_ENDPGM": self.scalar_ops.s_endpgm,  # 48
                "S_SENDMSG": self.scalar_ops.s_sendmsg,  # 54
            },
            "SOPC": {
                "S_CMP_EQ_U32": self.scalar_ops.s_cmp_eq_u32,  # 6
            },
            "SMEM": {
                "S_LOAD_B32": self.scalar_ops.s_load_b32,  # 0
                "S_LOAD_B64": self.scalar_ops.s_load_b64,  # 1
                "S_LOAD_B128": self.scalar_ops.s_load_b128,  # 2
            },
            "SOPK": {
                "S_WAITCNT_VSCNT": self.scalar_ops.s_waitcnt_vscnt,  # 24
            },
            "VOP3": {
                "V_LSHL_ADD_U32": self.vector_ops.v_lshl_add_u32,  # 582
                "V_AND_OR_B32": self.vector_ops.v_and_or_b32,  # 599
                "V_OR3_B32": self.vector_ops.v_or3_b32,  # 600
                "V_MBCNT_LO_U32_B32": self.vector_ops.v_mbcnt_lo_u32_b32,  # 799
                "V_MUL_LO_U32": self.vector_ops.v_mul_lo_u32,  # 812
                "V_MUL_HI_U32": self.vector_ops.v_mul_hi_u32,  # 813
                "V_LSHLREV_B16": self.vector_ops.v_lshlrev_b16,  # 824
                "V_LSHLREV_B64": self.vector_ops.v_lshlrev_b64,  # 828
                "V_WRITELANE_B32": self.vector_ops.v_writelane_b32,  # 865
            },
            "VOP3SD": {
                "V_MAD_U64_U32": self.vector_ops.v_mad_u64_u32,  # 766
                "V_ADD_CO_U32": self.vector_ops.v_add_co_u32,  # 768
                "V_SUB_CO_U32": self.vector_ops.v_sub_co_u32,  # 769
            },
            "VOPC": {
                "V_CMP_EQ_U32": self.vector_ops.v_cmp_eq_u32,  # 74
                "V_CMP_NE_U32": self.vector_ops.v_cmp_ne_u32,  # 75
                "V_CMP_LT_U64": self.vector_ops.v_cmp_lt_u64,  # 89
                "V_CMP_EQ_U64": self.vector_ops.v_cmp_eq_u64,  # 90
                "V_CMP_GT_U64": self.vector_ops.v_cmp_gt_u64,  # 92
                "V_CMP_NE_U64": self.vector_ops.v_cmp_ne_u64,  # 93
                "V_CMPX_EQ_U32": self.vector_ops.v_cmpx_eq_u32,  # 202
                "V_CMPX_GT_U32": self.vector_ops.v_cmpx_gt_u32,  # 204
                "V_CMPX_NE_U32": self.vector_ops.v_cmpx_ne_u32,  # 205
                "V_CMPX_NE_U64": self.vector_ops.v_cmpx_ne_u64,  # 221
                "V_CMP_EQ_U16": self.vector_ops.v_cmp_eq_u16,  # 224
            },
            "VOPD": {
                "V_DUAL_MOV_B32": self.vector_ops.v_dual_mov_b32,  # 8
                "V_DUAL_CNDMASK_B32": self.vector_ops.v_dual_cndmask_b32,  # 9
            },
            "FLAT": {},
            "GLOBAL": {
                "GLOBAL_LOAD_U8": self.memory.global_load_u8,
                "GLOBAL_LOAD_I8": self.memory.global_load_i8,
                "GLOBAL_LOAD_U16": self.memory.global_load_u16,
                "GLOBAL_LOAD_I16": self.memory.global_load_i16,
                "GLOBAL_LOAD_B32": self.memory.global_load_b32,
                "GLOBAL_STORE_B8": self.memory.global_store_b8,
                "GLOBAL_STORE_B16": self.memory.global_store_b16,
                "GLOBAL_STORE_B32": self.memory.global_store_b32,
            },
            "SCRATCH": {},
            "LDS": {},
        }

    def get_instruction_func(self, instruction_subtype, instruction):
        return self.instructions[instruction_subtype][instruction]

    def find_instruction_func(self, instruction, instruction_type):
        instruction_func = None
        for instruction_subtype in self.instruction_type_map[instruction_type]:
            if instruction in self.instructions[instruction_subtype]:
                instruction_func = self.get_instruction_func(
                    instruction_subtype, instruction
                )
        return instruction_func


if __name__ == "__main__":
    populate_instruction_usage(InstructionSet().instructions)
