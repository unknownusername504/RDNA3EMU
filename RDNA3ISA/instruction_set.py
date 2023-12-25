# This file defines the instruction set for RNDA3.
from scalar_ops import ScalarOps
from vector_ops import VectorOps
from registers import Registers


class InstructionSet:
    def __init__(self):
        self.registers = Registers()
        self.vector_ops = VectorOps(self.registers)
        self.scalar_ops = ScalarOps(self.registers)
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
        }
