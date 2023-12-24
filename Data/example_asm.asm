	.text
	.amdgcn_target "amdgcn-amd-amdhsa--gfx1100"
	.weak	__cxa_pure_virtual              ; -- Begin function __cxa_pure_virtual
	.p2align	2
	.type	__cxa_pure_virtual,@function
__cxa_pure_virtual:                     ; @__cxa_pure_virtual
; %bb.0:
	s_waitcnt vmcnt(0) expcnt(0) lgkmcnt(0)
	s_waitcnt_vscnt null, 0x0
	s_trap 2
.Lfunc_end0:
	.size	__cxa_pure_virtual, .Lfunc_end0-__cxa_pure_virtual
                                        ; -- End function
	.section	.AMDGPU.csdata
; Function info:
; codeLenInByte = 12
; NumSgprs: 0
; NumVgprs: 0
; ScratchSize: 1
; MemoryBound: 1
	.text
	.weak	__cxa_deleted_virtual           ; -- Begin function __cxa_deleted_virtual
	.p2align	2
	.type	__cxa_deleted_virtual,@function
__cxa_deleted_virtual:                  ; @__cxa_deleted_virtual
; %bb.0:
	s_waitcnt vmcnt(0) expcnt(0) lgkmcnt(0)
	s_waitcnt_vscnt null, 0x0
	s_trap 2
.Lfunc_end1:
	.size	__cxa_deleted_virtual, .Lfunc_end1-__cxa_deleted_virtual
                                        ; -- End function
	.section	.AMDGPU.csdata
; Function info:
; codeLenInByte = 12
; NumSgprs: 0
; NumVgprs: 0
; ScratchSize: 0
; MemoryBound: 0
	.text
	.hidden	__assert_fail                   ; -- Begin function __assert_fail
	.weak	__assert_fail
	.p2align	2
	.type	__assert_fail,@function
__assert_fail:                          ; @__assert_fail
; %bb.0:
	s_waitcnt vmcnt(0) expcnt(0) lgkmcnt(0)
	s_waitcnt_vscnt null, 0x0
	s_mov_b32 s20, s33
	s_mov_b32 s33, s32
	s_xor_saveexec_b32 s0, -1
	scratch_store_b32 off, v37, s33 offset:48 ; 4-byte Folded Spill
	s_mov_b32 exec_lo, s0
	v_writelane_b32 v37, s30, 0
	s_add_i32 s32, s32, 64
	v_writelane_b32 v37, s31, 1
	s_getpc_b64 s[0:1]
	s_add_u32 s0, s0, __const.__assert_fail.fmt@rel32@lo+20
	s_addc_u32 s1, s1, __const.__assert_fail.fmt@rel32@hi+28
	s_getpc_b64 s[2:3]
	s_add_u32 s2, s2, __const.__assert_fail.fmt@rel32@lo+4
	s_addc_u32 s3, s3, __const.__assert_fail.fmt@rel32@hi+12
	v_mbcnt_lo_u32_b32 v11, -1, 0
	s_clause 0x1
	s_load_b128 s[4:7], s[0:1], 0x0
	s_load_b128 s[12:15], s[2:3], 0x0
	s_load_b64 s[2:3], s[8:9], 0x50
	v_dual_mov_b32 v9, 0 :: v_dual_mov_b32 v8, v1
	v_dual_mov_b32 v7, v0 :: v_dual_mov_b32 v0, 0xa2e
	v_dual_mov_b32 v21, 0x73256020 :: v_dual_mov_b32 v16, v11
	v_mov_b32_e32 v22, 0x61662027
	v_mov_b32_e32 v23, 0x64656c69
	s_waitcnt lgkmcnt(0)
	v_dual_mov_b32 v15, s7 :: v_dual_mov_b32 v14, s6
	v_dual_mov_b32 v13, s5 :: v_dual_mov_b32 v12, s4
	v_dual_mov_b32 v20, s15 :: v_dual_mov_b32 v19, s14
	v_dual_mov_b32 v18, s13 :: v_dual_mov_b32 v17, s12
	s_clause 0x4
	scratch_store_b8 off, v9, s33 offset:46
	scratch_store_b16 off, v0, s33 offset:44
	scratch_store_b96 off, v[21:23], s33 offset:32
	scratch_store_b128 off, v[12:15], s33 offset:16
	scratch_store_b128 off, v[17:20], s33
	;;#ASMSTART
	;;#ASMEND
	v_readfirstlane_b32 s0, v16
	v_mov_b32_e32 v0, 0
	v_mov_b32_e32 v1, 0
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_cmp_eq_u32_e64 s0, s0, v16
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_6
; %bb.1:
	global_load_b64 v[14:15], v9, s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	s_clause 0x1
	global_load_b64 v[0:1], v9, s[2:3] offset:40
	global_load_b64 v[12:13], v9, s[2:3]
	s_mov_b32 s4, exec_lo
	s_waitcnt vmcnt(1)
	v_and_b32_e32 v1, v1, v15
	v_and_b32_e32 v0, v0, v14
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_mul_lo_u32 v1, v1, 24
	v_mul_hi_u32 v10, v0, 24
	v_mul_lo_u32 v0, v0, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_add_nc_u32_e32 v1, v10, v1
	s_waitcnt vmcnt(0)
	v_add_co_u32 v0, vcc_lo, v12, v0
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_ci_u32_e32 v1, vcc_lo, v13, v1, vcc_lo
	global_load_b64 v[12:13], v[0:1], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[0:1], v9, v[12:15], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmpx_ne_u64_e64 v[0:1], v[14:15]
	s_cbranch_execz .LBB3_5
; %bb.2:                                ; %.preheader90
	s_mov_b32 s5, 0
                                        ; implicit-def: $sgpr6
	.p2align	6
.LBB3_3:                                ; =>This Inner Loop Header: Depth=1
	s_sleep 1
	s_clause 0x1
	global_load_b64 v[12:13], v9, s[2:3] offset:40
	global_load_b64 v[17:18], v9, s[2:3]
	v_dual_mov_b32 v15, v1 :: v_dual_mov_b32 v14, v0
	s_waitcnt vmcnt(1)
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_and_b32_e32 v10, v12, v14
	s_waitcnt vmcnt(0)
	v_mad_u64_u32 v[0:1], null, v10, 24, v[17:18]
	v_and_b32_e32 v10, v13, v15
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_mad_u64_u32 v[12:13], null, v10, 24, v[1:2]
	v_mov_b32_e32 v1, v12
	global_load_b64 v[12:13], v[0:1], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[0:1], v9, v[12:15], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmp_eq_u64_e32 vcc_lo, v[0:1], v[14:15]
	s_or_b32 s5, vcc_lo, s5
	s_and_not1_b32 s6, s6, exec_lo
	s_and_b32 s7, vcc_lo, exec_lo
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 s6, s6, s7
	s_and_not1_b32 exec_lo, exec_lo, s5
	s_cbranch_execnz .LBB3_3
; %bb.4:                                ; %Flow684
	s_or_b32 exec_lo, exec_lo, s5
.LBB3_5:                                ; %Flow686
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s4
.LBB3_6:                                ; %Flow687
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s1
	v_mov_b32_e32 v17, 0
	v_readfirstlane_b32 s4, v0
	v_readfirstlane_b32 s5, v1
	s_mov_b64 s[6:7], exec
	s_clause 0x1
	global_load_b64 v[9:10], v17, s[2:3] offset:40
	global_load_b128 v[12:15], v17, s[2:3]
	s_waitcnt vmcnt(1)
	v_readfirstlane_b32 s10, v9
	v_readfirstlane_b32 s11, v10
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[10:11], s[4:5], s[10:11]
	s_mul_i32 s1, s11, 24
	s_mul_hi_u32 s12, s10, 24
	s_mul_i32 s13, s10, 24
	s_and_saveexec_b32 s14, s0
	s_cbranch_execz .LBB3_8
; %bb.7:
	s_add_i32 s15, s12, s1
	s_waitcnt vmcnt(0)
	v_add_co_u32 v0, vcc_lo, v12, s13
	v_add_co_ci_u32_e32 v1, vcc_lo, s15, v13, vcc_lo
	v_dual_mov_b32 v19, s7 :: v_dual_mov_b32 v18, s6
	v_dual_mov_b32 v20, 2 :: v_dual_mov_b32 v21, 1
	global_store_b128 v[0:1], v[18:21], off offset:8
.LBB3_8:
	s_or_b32 exec_lo, exec_lo, s14
	s_lshl_b64 s[6:7], s[10:11], 12
	v_lshlrev_b64 v[0:1], 6, v[16:17]
	s_waitcnt vmcnt(0)
	v_add_co_u32 v9, vcc_lo, v14, s6
	v_add_co_ci_u32_e32 v10, vcc_lo, s7, v15, vcc_lo
	s_mov_b32 s16, 0
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_u32 v0, vcc_lo, v9, v0
	s_mov_b32 s19, s16
	s_mov_b32 s17, s16
	s_mov_b32 s18, s16
	v_add_co_ci_u32_e32 v1, vcc_lo, v10, v1, vcc_lo
	v_dual_mov_b32 v16, 33 :: v_dual_mov_b32 v19, v17
	v_dual_mov_b32 v18, 1 :: v_dual_mov_b32 v23, s19
	v_dual_mov_b32 v22, s18 :: v_dual_mov_b32 v21, s17
	v_mov_b32_e32 v20, s16
	s_clause 0x3
	global_store_b128 v[0:1], v[16:19], off
	global_store_b128 v[0:1], v[20:23], off offset:16
	global_store_b128 v[0:1], v[20:23], off offset:32
	global_store_b128 v[0:1], v[20:23], off offset:48
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB3_16
; %bb.9:
	v_mov_b32_e32 v18, 0
	v_mov_b32_e32 v20, s5
	s_mov_b32 s7, exec_lo
	s_clause 0x1
	global_load_b64 v[21:22], v18, s[2:3] offset:32 glc
	global_load_b64 v[9:10], v18, s[2:3] offset:40
	v_mov_b32_e32 v19, s4
	s_waitcnt vmcnt(0)
	v_and_b32_e32 v9, s4, v9
	v_and_b32_e32 v10, s5, v10
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_mul_hi_u32 v14, v9, 24
	v_mul_lo_u32 v10, v10, 24
	v_mul_lo_u32 v9, v9, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_nc_u32_e32 v10, v14, v10
	v_add_co_u32 v9, vcc_lo, v12, v9
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_ci_u32_e32 v10, vcc_lo, v13, v10, vcc_lo
	global_store_b64 v[9:10], v[21:22], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[16:17], v18, v[19:22], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmpx_ne_u64_e64 v[16:17], v[21:22]
	s_cbranch_execz .LBB3_12
; %bb.10:                               ; %.preheader88
	s_mov_b32 s10, 0
.LBB3_11:                               ; =>This Inner Loop Header: Depth=1
	v_dual_mov_b32 v14, s4 :: v_dual_mov_b32 v15, s5
	s_sleep 1
	global_store_b64 v[9:10], v[16:17], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[14:15], v18, v[14:17], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[14:15], v[16:17]
	v_dual_mov_b32 v17, v15 :: v_dual_mov_b32 v16, v14
	s_or_b32 s10, vcc_lo, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_11
.LBB3_12:                               ; %Flow682
	s_or_b32 exec_lo, exec_lo, s7
	v_mov_b32_e32 v15, 0
	s_mov_b32 s10, exec_lo
	s_mov_b32 s7, exec_lo
	v_mbcnt_lo_u32_b32 v14, s10, 0
	global_load_b64 v[9:10], v15, s[2:3] offset:16
	v_cmpx_eq_u32_e32 0, v14
	s_cbranch_execz .LBB3_14
; %bb.13:
	s_bcnt1_i32_b32 s10, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	v_mov_b32_e32 v14, s10
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_add_u64 v[9:10], v[14:15], off offset:8
.LBB3_14:
	s_or_b32 exec_lo, exec_lo, s7
	s_waitcnt vmcnt(0)
	global_load_b64 v[14:15], v[9:10], off offset:16
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[14:15]
	s_cbranch_vccnz .LBB3_16
; %bb.15:
	global_load_b32 v9, v[9:10], off offset:24
	v_mov_b32_e32 v10, 0
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s7, v9
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_store_b64 v[14:15], v[9:10], off
	s_and_b32 m0, s7, 0xff
	s_sendmsg sendmsg(MSG_INTERRUPT)
.LBB3_16:                               ; %Flow683
	s_or_b32 exec_lo, exec_lo, s6
	s_add_i32 s12, s12, s1
	v_add_co_u32 v9, vcc_lo, v12, s13
	v_add_co_ci_u32_e32 v10, vcc_lo, s12, v13, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v9, vcc_lo, v9, 20
	v_add_co_ci_u32_e32 v10, vcc_lo, 0, v10, vcc_lo
	s_branch .LBB3_20
	.p2align	6
.LBB3_17:                               ;   in Loop: Header=BB3_20 Depth=1
	s_or_b32 exec_lo, exec_lo, s1
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_readfirstlane_b32 s1, v12
	s_cmp_eq_u32 s1, 0
	s_cbranch_scc1 .LBB3_19
; %bb.18:                               ;   in Loop: Header=BB3_20 Depth=1
	s_sleep 1
	s_cbranch_execnz .LBB3_20
	s_branch .LBB3_22
	.p2align	6
.LBB3_19:
	s_branch .LBB3_22
.LBB3_20:                               ; =>This Inner Loop Header: Depth=1
	v_mov_b32_e32 v12, 1
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_17
; %bb.21:                               ;   in Loop: Header=BB3_20 Depth=1
	global_load_b32 v12, v[9:10], off glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_and_b32_e32 v12, 1, v12
	s_branch .LBB3_17
.LBB3_22:
	global_load_b64 v[16:17], v[0:1], off
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_26
; %bb.23:
	v_mov_b32_e32 v9, 0
	s_clause 0x2
	global_load_b64 v[0:1], v9, s[2:3] offset:40
	global_load_b64 v[18:19], v9, s[2:3] offset:24 glc
	global_load_b64 v[14:15], v9, s[2:3]
	s_waitcnt vmcnt(2)
	v_add_co_u32 v10, vcc_lo, v0, 1
	v_add_co_ci_u32_e32 v20, vcc_lo, 0, v1, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v12, vcc_lo, v10, s4
	v_add_co_ci_u32_e32 v13, vcc_lo, s5, v20, vcc_lo
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[12:13]
	v_dual_cndmask_b32 v12, v12, v10 :: v_dual_cndmask_b32 v13, v13, v20
	v_and_b32_e32 v0, v12, v0
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_2) | instid1(VALU_DEP_1)
	v_mul_hi_u32 v10, v0, 24
	v_mul_lo_u32 v0, v0, 24
	s_waitcnt vmcnt(0)
	v_add_co_u32 v0, vcc_lo, v14, v0
	v_dual_mov_b32 v14, v18 :: v_dual_and_b32 v1, v13, v1
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_mul_lo_u32 v1, v1, 24
	v_add_nc_u32_e32 v1, v10, v1
	s_delay_alu instid0(VALU_DEP_1)
	v_add_co_ci_u32_e32 v1, vcc_lo, v15, v1, vcc_lo
	v_mov_b32_e32 v15, v19
	global_store_b64 v[0:1], v[18:19], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[14:15], v9, v[12:15], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_ne_u64_e32 vcc_lo, v[14:15], v[18:19]
	s_and_b32 exec_lo, exec_lo, vcc_lo
	s_cbranch_execz .LBB3_26
; %bb.24:                               ; %.preheader86
	s_mov_b32 s0, 0
.LBB3_25:                               ; =>This Inner Loop Header: Depth=1
	s_sleep 1
	global_store_b64 v[0:1], v[14:15], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[18:19], v9, v[12:15], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[18:19], v[14:15]
	v_dual_mov_b32 v14, v18 :: v_dual_mov_b32 v15, v19
	s_or_b32 s0, vcc_lo, s0
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s0
	s_cbranch_execnz .LBB3_25
.LBB3_26:
	s_or_b32 exec_lo, exec_lo, s1
	v_mov_b32_e32 v1, s33
	s_mov_b32 s0, 0
.LBB3_27:                               ; =>This Inner Loop Header: Depth=1
	scratch_load_u8 v9, v1, off
	v_add_nc_u32_e32 v0, 1, v1
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(SALU_CYCLE_1)
	v_mov_b32_e32 v1, v0
	s_waitcnt vmcnt(0)
	v_cmp_eq_u16_e32 vcc_lo, 0, v9
	s_or_b32 s0, vcc_lo, s0
	s_and_not1_b32 exec_lo, exec_lo, s0
	s_cbranch_execnz .LBB3_27
; %bb.28:
	s_or_b32 exec_lo, exec_lo, s0
	v_cmp_ne_u32_e64 s0, -1, s33
	s_delay_alu instid0(VALU_DEP_1)
	s_and_b32 vcc_lo, exec_lo, s0
	s_cbranch_vccz .LBB3_113
; %bb.29:
	v_cmp_ne_u32_e32 vcc_lo, -1, v0
	v_and_b32_e32 v12, -3, v16
	v_dual_mov_b32 v20, 2 :: v_dual_mov_b32 v21, 1
	s_mov_b32 s13, 0
	v_dual_cndmask_b32 v1, 0, v0 :: v_dual_mov_b32 v10, 0
	v_dual_mov_b32 v13, v17 :: v_dual_and_b32 v0, 2, v16
	s_mov_b32 s12, 0
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_subrev_nc_u32_e32 v34, s33, v1
	v_mov_b32_e32 v1, s33
	v_ashrrev_i32_e32 v35, 31, v34
	s_branch .LBB3_31
.LBB3_30:                               ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s1
	v_sub_co_u32 v34, vcc_lo, v34, v36
	v_sub_co_ci_u32_e32 v35, vcc_lo, v35, v38, vcc_lo
	v_add_nc_u32_e32 v1, v1, v36
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(SALU_CYCLE_1)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[34:35]
	s_or_b32 s12, vcc_lo, s12
	s_and_not1_b32 exec_lo, exec_lo, s12
	s_cbranch_execz .LBB3_114
.LBB3_31:                               ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB3_34 Depth 2
                                        ;     Child Loop BB3_42 Depth 2
                                        ;     Child Loop BB3_50 Depth 2
                                        ;     Child Loop BB3_58 Depth 2
                                        ;     Child Loop BB3_66 Depth 2
                                        ;     Child Loop BB3_74 Depth 2
                                        ;     Child Loop BB3_82 Depth 2
                                        ;     Child Loop BB3_90 Depth 2
                                        ;     Child Loop BB3_98 Depth 2
                                        ;     Child Loop BB3_107 Depth 2
                                        ;     Child Loop BB3_112 Depth 2
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_cmp_gt_u64_e32 vcc_lo, 56, v[34:35]
                                        ; implicit-def: $vgpr14_vgpr15
                                        ; implicit-def: $sgpr1
	s_mov_b32 s0, exec_lo
	v_cndmask_b32_e32 v38, 0, v35, vcc_lo
	v_cndmask_b32_e32 v36, 56, v34, vcc_lo
	v_cmpx_gt_u32_e32 8, v36
	s_xor_b32 s4, exec_lo, s0
	s_cbranch_execz .LBB3_37
; %bb.32:                               ;   in Loop: Header=BB3_31 Depth=1
	s_waitcnt vmcnt(0)
	v_mov_b32_e32 v14, 0
	v_mov_b32_e32 v15, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s5, exec_lo
	v_cmpx_ne_u32_e32 0, v36
	s_cbranch_execz .LBB3_36
; %bb.33:                               ; %.preheader83
                                        ;   in Loop: Header=BB3_31 Depth=1
	v_mov_b32_e32 v14, 0
	v_mov_b32_e32 v15, 0
	s_mov_b32 s6, 0
	s_mov_b32 s7, 0
	.p2align	6
.LBB3_34:                               ;   Parent Loop BB3_31 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1) | instskip(SKIP_1) | instid1(SALU_CYCLE_1)
	v_add_nc_u32_e32 v9, s7, v1
	s_add_i32 s7, s7, 1
	v_cmp_eq_u32_e32 vcc_lo, s7, v36
	scratch_load_u8 v9, v9, off
	s_waitcnt vmcnt(0)
	v_dual_mov_b32 v19, s13 :: v_dual_and_b32 v18, 0xffff, v9
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[18:19], s0, v[18:19]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s6, vcc_lo, s6
	v_or_b32_e32 v15, v19, v15
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v14, v18, v14
	s_and_not1_b32 exec_lo, exec_lo, s6
	s_cbranch_execnz .LBB3_34
; %bb.35:                               ; %Flow648
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
.LBB3_36:                               ; %Flow650
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s5
	s_mov_b32 s1, 0
.LBB3_37:                               ; %Flow652
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_saveexec_b32 s0, s4
	v_dual_mov_b32 v18, s1 :: v_dual_mov_b32 v9, v1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_39
; %bb.38:                               ;   in Loop: Header=BB3_31 Depth=1
	v_dual_mov_b32 v26, v10 :: v_dual_add_nc_u32 v9, 1, v1
	s_waitcnt vmcnt(0)
	v_add_nc_u32_e32 v14, 2, v1
	v_add_nc_u32_e32 v15, 3, v1
	v_add_nc_u32_e32 v19, 4, v1
	s_clause 0x3
	scratch_load_u8 v9, v9, off
	scratch_load_u8 v14, v14, off
	scratch_load_u8 v18, v15, off
	scratch_load_u8 v22, v1, off
	v_add_nc_u32_e32 v15, 5, v1
	v_add_nc_u32_e32 v23, 7, v1
	s_clause 0x1
	scratch_load_u8 v24, v15, off
	scratch_load_u8 v25, v19, off
	v_add_nc_u32_e32 v15, 6, v1
	scratch_load_u8 v23, v23, off
	v_mov_b32_e32 v19, s13
	scratch_load_d16_hi_u8 v26, v15, off
	v_mov_b32_e32 v15, s13
	s_waitcnt vmcnt(7)
	v_lshlrev_b16 v9, 8, v9
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v14, 0xffff, v14
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v18, 0xffff, v18
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v9, v9, v22
	v_lshlrev_b64 v[14:15], 16, v[14:15]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[18:19], 24, v[18:19]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v22, 8, v24
	v_and_b32_e32 v9, 0xffff, v9
	v_or3_b32 v15, 0, v15, v19
	s_delay_alu instid0(VALU_DEP_2)
	v_or3_b32 v9, v9, v14, v18
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v14, 24, v23
	v_add_nc_u32_e32 v18, -8, v36
	v_or3_b32 v15, v15, v25, v22
	v_or3_b32 v9, v9, 0, 0
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or3_b32 v15, v15, v26, v14
	v_or3_b32 v14, v9, 0, 0
	v_add_nc_u32_e32 v9, 8, v1
.LBB3_39:                               ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $vgpr22_vgpr23
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v18
	s_xor_b32 s4, exec_lo, s0
	s_cbranch_execz .LBB3_45
; %bb.40:                               ;   in Loop: Header=BB3_31 Depth=1
	v_mov_b32_e32 v22, 0
	v_mov_b32_e32 v23, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s5, exec_lo
	v_cmpx_ne_u32_e32 0, v18
	s_cbranch_execz .LBB3_44
; %bb.41:                               ; %.preheader81
                                        ;   in Loop: Header=BB3_31 Depth=1
	v_mov_b32_e32 v22, 0
	v_mov_b32_e32 v23, 0
	s_mov_b32 s6, 0
	s_mov_b32 s7, 0
	.p2align	6
.LBB3_42:                               ;   Parent Loop BB3_31 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1) | instskip(SKIP_1) | instid1(SALU_CYCLE_1)
	v_add_nc_u32_e32 v19, s7, v9
	s_add_i32 s7, s7, 1
	v_cmp_eq_u32_e32 vcc_lo, s7, v18
	scratch_load_u8 v19, v19, off
	s_waitcnt vmcnt(0)
	v_dual_mov_b32 v25, s13 :: v_dual_and_b32 v24, 0xffff, v19
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[24:25], s0, v[24:25]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s6, vcc_lo, s6
	v_or_b32_e32 v23, v25, v23
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v22, v24, v22
	s_and_not1_b32 exec_lo, exec_lo, s6
	s_cbranch_execnz .LBB3_42
; %bb.43:                               ; %Flow643
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
.LBB3_44:                               ; %Flow645
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s5
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr18
.LBB3_45:                               ; %Flow647
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_saveexec_b32 s0, s4
	v_mov_b32_e32 v19, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_47
; %bb.46:                               ;   in Loop: Header=BB3_31 Depth=1
	v_dual_mov_b32 v30, v10 :: v_dual_add_nc_u32 v19, 1, v9
	v_add_nc_u32_e32 v22, 2, v9
	v_add_nc_u32_e32 v23, 3, v9
	v_add_nc_u32_e32 v25, 4, v9
	s_clause 0x3
	scratch_load_u8 v19, v19, off
	scratch_load_u8 v22, v22, off
	scratch_load_u8 v24, v23, off
	scratch_load_u8 v26, v9, off
	v_add_nc_u32_e32 v23, 5, v9
	v_add_nc_u32_e32 v27, 7, v9
	s_clause 0x1
	scratch_load_u8 v28, v23, off
	scratch_load_u8 v29, v25, off
	v_add_nc_u32_e32 v23, 6, v9
	scratch_load_u8 v27, v27, off
	v_mov_b32_e32 v25, s13
	v_add_nc_u32_e32 v9, 8, v9
	scratch_load_d16_hi_u8 v30, v23, off
	v_mov_b32_e32 v23, s13
	s_waitcnt vmcnt(7)
	v_lshlrev_b16 v19, 8, v19
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v22, 0xffff, v22
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v24, 0xffff, v24
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v19, v19, v26
	v_lshlrev_b64 v[22:23], 16, v[22:23]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[24:25], 24, v[24:25]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v26, 8, v28
	v_and_b32_e32 v19, 0xffff, v19
	v_or3_b32 v23, 0, v23, v25
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v19, v19, v22, v24
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v22, 24, v27
	v_or3_b32 v23, v23, v29, v26
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v24, v19, 0, 0
	v_add_nc_u32_e32 v19, -8, v18
	s_waitcnt vmcnt(0)
	v_or3_b32 v23, v23, v30, v22
	s_delay_alu instid0(VALU_DEP_3)
	v_or3_b32 v22, v24, 0, 0
.LBB3_47:                               ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v19
	s_xor_b32 s4, exec_lo, s0
	s_cbranch_execz .LBB3_53
; %bb.48:                               ;   in Loop: Header=BB3_31 Depth=1
	v_mov_b32_e32 v24, 0
	v_mov_b32_e32 v25, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s5, exec_lo
	v_cmpx_ne_u32_e32 0, v19
	s_cbranch_execz .LBB3_52
; %bb.49:                               ; %.preheader79
                                        ;   in Loop: Header=BB3_31 Depth=1
	v_mov_b32_e32 v24, 0
	v_mov_b32_e32 v25, 0
	s_mov_b32 s6, 0
	s_mov_b32 s7, 0
	.p2align	6
.LBB3_50:                               ;   Parent Loop BB3_31 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1) | instskip(SKIP_1) | instid1(SALU_CYCLE_1)
	v_dual_mov_b32 v27, s13 :: v_dual_add_nc_u32 v18, s7, v9
	s_add_i32 s7, s7, 1
	v_cmp_eq_u32_e32 vcc_lo, s7, v19
	scratch_load_u8 v18, v18, off
	s_waitcnt vmcnt(0)
	v_and_b32_e32 v26, 0xffff, v18
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[26:27], s0, v[26:27]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s6, vcc_lo, s6
	v_or_b32_e32 v25, v27, v25
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v24, v26, v24
	s_and_not1_b32 exec_lo, exec_lo, s6
	s_cbranch_execnz .LBB3_50
; %bb.51:                               ; %Flow638
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
.LBB3_52:                               ; %Flow640
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s5
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr19
.LBB3_53:                               ; %Flow642
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_saveexec_b32 s0, s4
	v_mov_b32_e32 v18, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_55
; %bb.54:                               ;   in Loop: Header=BB3_31 Depth=1
	v_add_nc_u32_e32 v18, 1, v9
	v_add_nc_u32_e32 v24, 2, v9
	v_dual_mov_b32 v32, v10 :: v_dual_add_nc_u32 v25, 3, v9
	v_add_nc_u32_e32 v27, 4, v9
	s_clause 0x3
	scratch_load_u8 v18, v18, off
	scratch_load_u8 v24, v24, off
	scratch_load_u8 v26, v25, off
	scratch_load_u8 v28, v9, off
	v_add_nc_u32_e32 v25, 5, v9
	v_add_nc_u32_e32 v29, 7, v9
	s_clause 0x1
	scratch_load_u8 v30, v25, off
	scratch_load_u8 v31, v27, off
	v_add_nc_u32_e32 v25, 6, v9
	scratch_load_u8 v29, v29, off
	v_mov_b32_e32 v27, s13
	v_add_nc_u32_e32 v9, 8, v9
	scratch_load_d16_hi_u8 v32, v25, off
	v_mov_b32_e32 v25, s13
	s_waitcnt vmcnt(7)
	v_lshlrev_b16 v18, 8, v18
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v24, 0xffff, v24
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v26, 0xffff, v26
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v18, v18, v28
	v_lshlrev_b64 v[24:25], 16, v[24:25]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[26:27], 24, v[26:27]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v28, 8, v30
	v_and_b32_e32 v18, 0xffff, v18
	v_or3_b32 v25, 0, v25, v27
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v18, v18, v24, v26
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v24, 24, v29
	v_or3_b32 v25, v25, v31, v28
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v26, v18, 0, 0
	v_add_nc_u32_e32 v18, -8, v19
	s_waitcnt vmcnt(0)
	v_or3_b32 v25, v25, v32, v24
	s_delay_alu instid0(VALU_DEP_3)
	v_or3_b32 v24, v26, 0, 0
.LBB3_55:                               ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $vgpr26_vgpr27
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v18
	s_xor_b32 s4, exec_lo, s0
	s_cbranch_execz .LBB3_61
; %bb.56:                               ;   in Loop: Header=BB3_31 Depth=1
	v_mov_b32_e32 v26, 0
	v_mov_b32_e32 v27, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s5, exec_lo
	v_cmpx_ne_u32_e32 0, v18
	s_cbranch_execz .LBB3_60
; %bb.57:                               ; %.preheader77
                                        ;   in Loop: Header=BB3_31 Depth=1
	v_mov_b32_e32 v26, 0
	v_mov_b32_e32 v27, 0
	s_mov_b32 s6, 0
	s_mov_b32 s7, 0
	.p2align	6
.LBB3_58:                               ;   Parent Loop BB3_31 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1) | instskip(SKIP_1) | instid1(SALU_CYCLE_1)
	v_add_nc_u32_e32 v19, s7, v9
	s_add_i32 s7, s7, 1
	v_cmp_eq_u32_e32 vcc_lo, s7, v18
	scratch_load_u8 v19, v19, off
	s_waitcnt vmcnt(0)
	v_dual_mov_b32 v29, s13 :: v_dual_and_b32 v28, 0xffff, v19
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[28:29], s0, v[28:29]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s6, vcc_lo, s6
	v_or_b32_e32 v27, v29, v27
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v26, v28, v26
	s_and_not1_b32 exec_lo, exec_lo, s6
	s_cbranch_execnz .LBB3_58
; %bb.59:                               ; %Flow633
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
.LBB3_60:                               ; %Flow635
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s5
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr18
.LBB3_61:                               ; %Flow637
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_saveexec_b32 s0, s4
	v_mov_b32_e32 v19, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_63
; %bb.62:                               ;   in Loop: Header=BB3_31 Depth=1
	v_add_nc_u32_e32 v19, 1, v9
	v_dual_mov_b32 v39, v10 :: v_dual_add_nc_u32 v26, 2, v9
	v_add_nc_u32_e32 v27, 3, v9
	v_add_nc_u32_e32 v29, 4, v9
	s_clause 0x3
	scratch_load_u8 v19, v19, off
	scratch_load_u8 v26, v26, off
	scratch_load_u8 v28, v27, off
	scratch_load_u8 v30, v9, off
	v_add_nc_u32_e32 v27, 5, v9
	v_add_nc_u32_e32 v31, 7, v9
	s_clause 0x1
	scratch_load_u8 v32, v27, off
	scratch_load_u8 v33, v29, off
	v_add_nc_u32_e32 v27, 6, v9
	scratch_load_u8 v31, v31, off
	v_mov_b32_e32 v29, s13
	v_add_nc_u32_e32 v9, 8, v9
	scratch_load_d16_hi_u8 v39, v27, off
	v_mov_b32_e32 v27, s13
	s_waitcnt vmcnt(7)
	v_lshlrev_b16 v19, 8, v19
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v26, 0xffff, v26
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v28, 0xffff, v28
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v19, v19, v30
	v_lshlrev_b64 v[26:27], 16, v[26:27]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[28:29], 24, v[28:29]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v30, 8, v32
	v_and_b32_e32 v19, 0xffff, v19
	v_or3_b32 v27, 0, v27, v29
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v19, v19, v26, v28
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v26, 24, v31
	v_or3_b32 v27, v27, v33, v30
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v28, v19, 0, 0
	v_add_nc_u32_e32 v19, -8, v18
	s_waitcnt vmcnt(0)
	v_or3_b32 v27, v27, v39, v26
	s_delay_alu instid0(VALU_DEP_3)
	v_or3_b32 v26, v28, 0, 0
.LBB3_63:                               ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v19
	s_xor_b32 s4, exec_lo, s0
	s_cbranch_execz .LBB3_69
; %bb.64:                               ;   in Loop: Header=BB3_31 Depth=1
	v_mov_b32_e32 v28, 0
	v_mov_b32_e32 v29, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s5, exec_lo
	v_cmpx_ne_u32_e32 0, v19
	s_cbranch_execz .LBB3_68
; %bb.65:                               ; %.preheader75
                                        ;   in Loop: Header=BB3_31 Depth=1
	v_mov_b32_e32 v28, 0
	v_mov_b32_e32 v29, 0
	s_mov_b32 s6, 0
	s_mov_b32 s7, 0
	.p2align	6
.LBB3_66:                               ;   Parent Loop BB3_31 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1) | instskip(SKIP_1) | instid1(SALU_CYCLE_1)
	v_dual_mov_b32 v31, s13 :: v_dual_add_nc_u32 v18, s7, v9
	s_add_i32 s7, s7, 1
	v_cmp_eq_u32_e32 vcc_lo, s7, v19
	scratch_load_u8 v18, v18, off
	s_waitcnt vmcnt(0)
	v_and_b32_e32 v30, 0xffff, v18
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[30:31], s0, v[30:31]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s6, vcc_lo, s6
	v_or_b32_e32 v29, v31, v29
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v28, v30, v28
	s_and_not1_b32 exec_lo, exec_lo, s6
	s_cbranch_execnz .LBB3_66
; %bb.67:                               ; %Flow628
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
.LBB3_68:                               ; %Flow630
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s5
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr19
.LBB3_69:                               ; %Flow632
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_saveexec_b32 s0, s4
	v_mov_b32_e32 v18, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_71
; %bb.70:                               ;   in Loop: Header=BB3_31 Depth=1
	v_dual_mov_b32 v49, v10 :: v_dual_add_nc_u32 v18, 1, v9
	v_add_nc_u32_e32 v28, 2, v9
	v_add_nc_u32_e32 v29, 3, v9
	v_add_nc_u32_e32 v31, 4, v9
	s_clause 0x3
	scratch_load_u8 v18, v18, off
	scratch_load_u8 v28, v28, off
	scratch_load_u8 v30, v29, off
	scratch_load_u8 v32, v9, off
	v_add_nc_u32_e32 v29, 5, v9
	v_add_nc_u32_e32 v33, 7, v9
	s_clause 0x1
	scratch_load_u8 v39, v29, off
	scratch_load_u8 v48, v31, off
	v_add_nc_u32_e32 v29, 6, v9
	scratch_load_u8 v33, v33, off
	v_mov_b32_e32 v31, s13
	v_add_nc_u32_e32 v9, 8, v9
	scratch_load_d16_hi_u8 v49, v29, off
	v_mov_b32_e32 v29, s13
	s_waitcnt vmcnt(7)
	v_lshlrev_b16 v18, 8, v18
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v28, 0xffff, v28
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v30, 0xffff, v30
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v18, v18, v32
	v_lshlrev_b64 v[28:29], 16, v[28:29]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[30:31], 24, v[30:31]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v32, 8, v39
	v_and_b32_e32 v18, 0xffff, v18
	v_or3_b32 v29, 0, v29, v31
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v18, v18, v28, v30
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v28, 24, v33
	v_or3_b32 v29, v29, v48, v32
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v30, v18, 0, 0
	v_add_nc_u32_e32 v18, -8, v19
	s_waitcnt vmcnt(0)
	v_or3_b32 v29, v29, v49, v28
	s_delay_alu instid0(VALU_DEP_3)
	v_or3_b32 v28, v30, 0, 0
.LBB3_71:                               ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $vgpr30_vgpr31
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v18
	s_xor_b32 s4, exec_lo, s0
	s_cbranch_execz .LBB3_77
; %bb.72:                               ;   in Loop: Header=BB3_31 Depth=1
	v_mov_b32_e32 v30, 0
	v_mov_b32_e32 v31, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s5, exec_lo
	v_cmpx_ne_u32_e32 0, v18
	s_cbranch_execz .LBB3_76
; %bb.73:                               ; %.preheader73
                                        ;   in Loop: Header=BB3_31 Depth=1
	v_mov_b32_e32 v30, 0
	v_mov_b32_e32 v31, 0
	s_mov_b32 s6, 0
	s_mov_b32 s7, 0
	.p2align	6
.LBB3_74:                               ;   Parent Loop BB3_31 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1) | instskip(SKIP_1) | instid1(SALU_CYCLE_1)
	v_add_nc_u32_e32 v19, s7, v9
	s_add_i32 s7, s7, 1
	v_cmp_eq_u32_e32 vcc_lo, s7, v18
	scratch_load_u8 v19, v19, off
	s_waitcnt vmcnt(0)
	v_dual_mov_b32 v33, s13 :: v_dual_and_b32 v32, 0xffff, v19
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[32:33], s0, v[32:33]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s6, vcc_lo, s6
	v_or_b32_e32 v31, v33, v31
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v30, v32, v30
	s_and_not1_b32 exec_lo, exec_lo, s6
	s_cbranch_execnz .LBB3_74
; %bb.75:                               ; %Flow623
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
.LBB3_76:                               ; %Flow625
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s5
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr18
.LBB3_77:                               ; %Flow627
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_saveexec_b32 s0, s4
	v_mov_b32_e32 v19, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_79
; %bb.78:                               ;   in Loop: Header=BB3_31 Depth=1
	v_add_nc_u32_e32 v19, 1, v9
	v_dual_mov_b32 v51, v10 :: v_dual_add_nc_u32 v30, 2, v9
	v_add_nc_u32_e32 v31, 3, v9
	v_add_nc_u32_e32 v33, 4, v9
	s_clause 0x3
	scratch_load_u8 v19, v19, off
	scratch_load_u8 v30, v30, off
	scratch_load_u8 v32, v31, off
	scratch_load_u8 v39, v9, off
	v_add_nc_u32_e32 v31, 5, v9
	v_add_nc_u32_e32 v48, 7, v9
	s_clause 0x1
	scratch_load_u8 v49, v31, off
	scratch_load_u8 v50, v33, off
	v_add_nc_u32_e32 v31, 6, v9
	scratch_load_u8 v48, v48, off
	v_mov_b32_e32 v33, s13
	v_add_nc_u32_e32 v9, 8, v9
	scratch_load_d16_hi_u8 v51, v31, off
	v_mov_b32_e32 v31, s13
	s_waitcnt vmcnt(7)
	v_lshlrev_b16 v19, 8, v19
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v30, 0xffff, v30
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v32, 0xffff, v32
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v19, v19, v39
	v_lshlrev_b64 v[30:31], 16, v[30:31]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[32:33], 24, v[32:33]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v39, 8, v49
	v_and_b32_e32 v19, 0xffff, v19
	v_or3_b32 v31, 0, v31, v33
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v19, v19, v30, v32
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v30, 24, v48
	v_or3_b32 v31, v31, v50, v39
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v32, v19, 0, 0
	v_add_nc_u32_e32 v19, -8, v18
	s_waitcnt vmcnt(0)
	v_or3_b32 v31, v31, v51, v30
	s_delay_alu instid0(VALU_DEP_3)
	v_or3_b32 v30, v32, 0, 0
.LBB3_79:                               ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v19
	s_xor_b32 s4, exec_lo, s0
	s_cbranch_execz .LBB3_85
; %bb.80:                               ;   in Loop: Header=BB3_31 Depth=1
	v_mov_b32_e32 v32, 0
	v_mov_b32_e32 v33, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s5, exec_lo
	v_cmpx_ne_u32_e32 0, v19
	s_cbranch_execz .LBB3_84
; %bb.81:                               ; %.preheader71
                                        ;   in Loop: Header=BB3_31 Depth=1
	v_mov_b32_e32 v32, 0
	v_mov_b32_e32 v33, 0
	s_mov_b32 s6, 0
	.p2align	6
.LBB3_82:                               ;   Parent Loop BB3_31 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	scratch_load_u8 v18, v9, off
	v_mov_b32_e32 v49, s13
	v_add_nc_u32_e32 v19, -1, v19
	v_add_nc_u32_e32 v9, 1, v9
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_1)
	v_cmp_eq_u32_e32 vcc_lo, 0, v19
	s_waitcnt vmcnt(0)
	v_and_b32_e32 v48, 0xffff, v18
	v_lshlrev_b64 v[48:49], s0, v[48:49]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s6, vcc_lo, s6
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or_b32_e32 v33, v49, v33
	v_or_b32_e32 v32, v48, v32
	s_and_not1_b32 exec_lo, exec_lo, s6
	s_cbranch_execnz .LBB3_82
; %bb.83:                               ; %Flow618
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
.LBB3_84:                               ; %Flow620
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s5
                                        ; implicit-def: $vgpr9
.LBB3_85:                               ; %Flow622
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_and_not1_saveexec_b32 s0, s4
	s_cbranch_execz .LBB3_87
; %bb.86:                               ;   in Loop: Header=BB3_31 Depth=1
	v_dual_mov_b32 v51, v10 :: v_dual_add_nc_u32 v18, 1, v9
	v_add_nc_u32_e32 v19, 2, v9
	v_add_nc_u32_e32 v32, 3, v9
	v_add_nc_u32_e32 v33, 4, v9
	s_clause 0x3
	scratch_load_u8 v18, v18, off
	scratch_load_u8 v39, v19, off
	scratch_load_u8 v32, v32, off
	scratch_load_u8 v48, v9, off
	v_add_nc_u32_e32 v19, 5, v9
	scratch_load_u8 v50, v33, off
	v_mov_b32_e32 v33, s13
	scratch_load_u8 v49, v19, off
	v_add_nc_u32_e32 v19, 7, v9
	v_add_nc_u32_e32 v9, 6, v9
	s_clause 0x1
	scratch_load_u8 v52, v19, off
	scratch_load_d16_hi_u8 v51, v9, off
	v_mov_b32_e32 v19, s13
	s_waitcnt vmcnt(7)
	v_lshlrev_b16 v9, 8, v18
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v18, 0xffff, v39
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v32, 0xffff, v32
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v9, v9, v48
	v_lshlrev_b64 v[18:19], 16, v[18:19]
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[32:33], 24, v[32:33]
	v_and_b32_e32 v9, 0xffff, v9
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v19, 0, v19, v33
	s_waitcnt vmcnt(2)
	v_lshlrev_b32_e32 v33, 8, v49
	v_or3_b32 v9, v9, v18, v32
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v18, v19, v50, v33
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v19, 24, v52
	v_or3_b32 v9, v9, 0, 0
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or3_b32 v33, v18, v51, v19
	v_or3_b32 v32, v9, 0, 0
.LBB3_87:                               ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
	v_dual_mov_b32 v9, v11 :: v_dual_mov_b32 v18, 0
	;;#ASMSTART
	;;#ASMEND
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_readfirstlane_b32 s0, v9
	v_mov_b32_e32 v19, 0
	v_cmp_eq_u32_e64 s0, s0, v9
	s_delay_alu instid0(VALU_DEP_1)
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_93
; %bb.88:                               ;   in Loop: Header=BB3_31 Depth=1
	global_load_b64 v[50:51], v10, s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	s_clause 0x1
	global_load_b64 v[18:19], v10, s[2:3] offset:40
	global_load_b64 v[48:49], v10, s[2:3]
	s_mov_b32 s4, exec_lo
	s_waitcnt vmcnt(1)
	v_and_b32_e32 v19, v19, v51
	v_and_b32_e32 v18, v18, v50
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_mul_lo_u32 v19, v19, 24
	v_mul_hi_u32 v39, v18, 24
	v_mul_lo_u32 v18, v18, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_add_nc_u32_e32 v19, v39, v19
	s_waitcnt vmcnt(0)
	v_add_co_u32 v18, vcc_lo, v48, v18
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_ci_u32_e32 v19, vcc_lo, v49, v19, vcc_lo
	global_load_b64 v[48:49], v[18:19], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[18:19], v10, v[48:51], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmpx_ne_u64_e64 v[18:19], v[50:51]
	s_cbranch_execz .LBB3_92
; %bb.89:                               ; %.preheader69
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_mov_b32 s5, 0
                                        ; implicit-def: $sgpr6
	.p2align	6
.LBB3_90:                               ;   Parent Loop BB3_31 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_sleep 1
	s_clause 0x1
	global_load_b64 v[48:49], v10, s[2:3] offset:40
	global_load_b64 v[52:53], v10, s[2:3]
	v_dual_mov_b32 v51, v19 :: v_dual_mov_b32 v50, v18
	s_waitcnt vmcnt(1)
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_and_b32_e32 v39, v48, v50
	s_waitcnt vmcnt(0)
	v_mad_u64_u32 v[18:19], null, v39, 24, v[52:53]
	v_and_b32_e32 v39, v49, v51
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_mad_u64_u32 v[48:49], null, v39, 24, v[19:20]
	v_mov_b32_e32 v19, v48
	global_load_b64 v[48:49], v[18:19], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[18:19], v10, v[48:51], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmp_eq_u64_e32 vcc_lo, v[18:19], v[50:51]
	s_or_b32 s5, vcc_lo, s5
	s_and_not1_b32 s6, s6, exec_lo
	s_and_b32 s7, vcc_lo, exec_lo
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 s6, s6, s7
	s_and_not1_b32 exec_lo, exec_lo, s5
	s_cbranch_execnz .LBB3_90
; %bb.91:                               ; %Flow614
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s5
.LBB3_92:                               ; %Flow616
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s4
.LBB3_93:                               ; %Flow617
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s1
	s_clause 0x1
	global_load_b64 v[52:53], v10, s[2:3] offset:40
	global_load_b128 v[48:51], v10, s[2:3]
	v_readfirstlane_b32 s4, v18
	v_readfirstlane_b32 s5, v19
	s_mov_b64 s[10:11], exec
	s_waitcnt vmcnt(1)
	v_readfirstlane_b32 s6, v52
	v_readfirstlane_b32 s7, v53
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[6:7], s[4:5], s[6:7]
	s_mul_i32 s1, s7, 24
	s_mul_hi_u32 s14, s6, 24
	s_mul_i32 s15, s6, 24
	s_and_saveexec_b32 s16, s0
	s_cbranch_execz .LBB3_95
; %bb.94:                               ;   in Loop: Header=BB3_31 Depth=1
	s_add_i32 s17, s14, s1
	s_waitcnt vmcnt(0)
	v_add_co_u32 v52, vcc_lo, v48, s15
	v_add_co_ci_u32_e32 v53, vcc_lo, s17, v49, vcc_lo
	v_dual_mov_b32 v19, s11 :: v_dual_mov_b32 v18, s10
	global_store_b128 v[52:53], v[18:21], off offset:8
.LBB3_95:                               ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s16
	v_cmp_lt_u64_e32 vcc_lo, 56, v[34:35]
	v_or_b32_e32 v18, 0, v13
	v_or_b32_e32 v19, v12, v0
	v_lshl_add_u32 v39, v36, 2, 28
	s_lshl_b64 s[6:7], s[6:7], 12
	s_delay_alu instid0(VALU_DEP_2)
	v_dual_cndmask_b32 v13, v18, v13 :: v_dual_cndmask_b32 v12, v19, v12
	v_lshlrev_b64 v[18:19], 6, v[9:10]
	s_waitcnt vmcnt(0)
	v_add_co_u32 v9, vcc_lo, v50, s6
	v_and_b32_e32 v39, 0x1e0, v39
	v_add_co_ci_u32_e32 v50, vcc_lo, s7, v51, vcc_lo
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_add_co_u32 v18, vcc_lo, v9, v18
	v_and_or_b32 v12, 0xffffff1f, v12, v39
	s_delay_alu instid0(VALU_DEP_3)
	v_add_co_ci_u32_e32 v19, vcc_lo, v50, v19, vcc_lo
	s_clause 0x3
	global_store_b128 v[18:19], v[12:15], off
	global_store_b128 v[18:19], v[22:25], off offset:16
	global_store_b128 v[18:19], v[26:29], off offset:32
	global_store_b128 v[18:19], v[30:33], off offset:48
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB3_103
; %bb.96:                               ;   in Loop: Header=BB3_31 Depth=1
	s_clause 0x1
	global_load_b64 v[26:27], v10, s[2:3] offset:32 glc
	global_load_b64 v[12:13], v10, s[2:3] offset:40
	v_dual_mov_b32 v24, s4 :: v_dual_mov_b32 v25, s5
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s10, v12
	v_readfirstlane_b32 s11, v13
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[10:11], s[10:11], s[4:5]
	s_mul_i32 s7, s11, 24
	s_mul_hi_u32 s11, s10, 24
	s_mul_i32 s10, s10, 24
	s_add_i32 s11, s11, s7
	v_add_co_u32 v22, vcc_lo, v48, s10
	v_add_co_ci_u32_e32 v23, vcc_lo, s11, v49, vcc_lo
	s_mov_b32 s7, exec_lo
	global_store_b64 v[22:23], v[26:27], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[14:15], v10, v[24:27], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmpx_ne_u64_e64 v[14:15], v[26:27]
	s_cbranch_execz .LBB3_99
; %bb.97:                               ; %.preheader67
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_mov_b32 s10, 0
.LBB3_98:                               ;   Parent Loop BB3_31 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	v_dual_mov_b32 v12, s4 :: v_dual_mov_b32 v13, s5
	s_sleep 1
	global_store_b64 v[22:23], v[14:15], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[12:13], v10, v[12:15], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[12:13], v[14:15]
	v_dual_mov_b32 v15, v13 :: v_dual_mov_b32 v14, v12
	s_or_b32 s10, vcc_lo, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_98
.LBB3_99:                               ; %Flow612
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s7
	global_load_b64 v[12:13], v10, s[2:3] offset:16
	s_mov_b32 s10, exec_lo
	s_mov_b32 s7, exec_lo
	v_mbcnt_lo_u32_b32 v9, s10, 0
	s_delay_alu instid0(VALU_DEP_1)
	v_cmpx_eq_u32_e32 0, v9
	s_cbranch_execz .LBB3_101
; %bb.100:                              ;   in Loop: Header=BB3_31 Depth=1
	s_bcnt1_i32_b32 s10, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	v_mov_b32_e32 v9, s10
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_add_u64 v[12:13], v[9:10], off offset:8
.LBB3_101:                              ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s7
	s_waitcnt vmcnt(0)
	global_load_b64 v[14:15], v[12:13], off offset:16
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[14:15]
	s_cbranch_vccnz .LBB3_103
; %bb.102:                              ;   in Loop: Header=BB3_31 Depth=1
	global_load_b32 v9, v[12:13], off offset:24
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s7, v9
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_store_b64 v[14:15], v[9:10], off
	s_and_b32 m0, s7, 0xff
	s_sendmsg sendmsg(MSG_INTERRUPT)
.LBB3_103:                              ; %Flow613
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
	s_add_i32 s14, s14, s1
	v_add_co_u32 v9, vcc_lo, v48, s15
	v_add_co_ci_u32_e32 v13, vcc_lo, s14, v49, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v12, vcc_lo, v9, 20
	v_add_co_ci_u32_e32 v13, vcc_lo, 0, v13, vcc_lo
	s_branch .LBB3_107
	.p2align	6
.LBB3_104:                              ;   in Loop: Header=BB3_107 Depth=2
	s_or_b32 exec_lo, exec_lo, s1
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_readfirstlane_b32 s1, v9
	s_cmp_eq_u32 s1, 0
	s_cbranch_scc1 .LBB3_106
; %bb.105:                              ;   in Loop: Header=BB3_107 Depth=2
	s_sleep 1
	s_cbranch_execnz .LBB3_107
	s_branch .LBB3_109
	.p2align	6
.LBB3_106:                              ;   in Loop: Header=BB3_31 Depth=1
	s_branch .LBB3_109
.LBB3_107:                              ;   Parent Loop BB3_31 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	v_mov_b32_e32 v9, 1
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_104
; %bb.108:                              ;   in Loop: Header=BB3_107 Depth=2
	global_load_b32 v9, v[12:13], off glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_and_b32_e32 v9, 1, v9
	s_branch .LBB3_104
.LBB3_109:                              ;   in Loop: Header=BB3_31 Depth=1
	global_load_b128 v[12:15], v[18:19], off
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_30
; %bb.110:                              ;   in Loop: Header=BB3_31 Depth=1
	s_clause 0x2
	global_load_b64 v[14:15], v10, s[2:3] offset:40
	global_load_b64 v[18:19], v10, s[2:3] offset:24 glc
	global_load_b64 v[24:25], v10, s[2:3]
	s_waitcnt vmcnt(2)
	v_add_co_u32 v9, vcc_lo, v14, 1
	v_add_co_ci_u32_e32 v26, vcc_lo, 0, v15, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v22, vcc_lo, v9, s4
	v_add_co_ci_u32_e32 v23, vcc_lo, s5, v26, vcc_lo
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[22:23]
	v_dual_cndmask_b32 v23, v23, v26 :: v_dual_cndmask_b32 v22, v22, v9
	v_and_b32_e32 v9, v23, v15
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_and_b32_e32 v14, v22, v14
	v_mul_hi_u32 v15, v14, 24
	v_mul_lo_u32 v14, v14, 24
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_2) | instid1(VALU_DEP_1)
	v_add_co_u32 v14, vcc_lo, v24, v14
	v_mov_b32_e32 v24, v18
	v_mul_lo_u32 v9, v9, 24
	v_add_nc_u32_e32 v9, v15, v9
	s_delay_alu instid0(VALU_DEP_1)
	v_add_co_ci_u32_e32 v15, vcc_lo, v25, v9, vcc_lo
	v_mov_b32_e32 v25, v19
	global_store_b64 v[14:15], v[18:19], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[24:25], v10, v[22:25], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_ne_u64_e32 vcc_lo, v[24:25], v[18:19]
	s_and_b32 exec_lo, exec_lo, vcc_lo
	s_cbranch_execz .LBB3_30
; %bb.111:                              ; %.preheader65
                                        ;   in Loop: Header=BB3_31 Depth=1
	s_mov_b32 s0, 0
.LBB3_112:                              ;   Parent Loop BB3_31 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_sleep 1
	global_store_b64 v[14:15], v[24:25], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[18:19], v10, v[22:25], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[18:19], v[24:25]
	v_dual_mov_b32 v25, v19 :: v_dual_mov_b32 v24, v18
	s_or_b32 s0, vcc_lo, s0
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s0
	s_cbranch_execnz .LBB3_112
	s_branch .LBB3_30
.LBB3_113:
                                        ; implicit-def: $vgpr12_vgpr13
	s_cbranch_execnz .LBB3_115
	s_branch .LBB3_142
.LBB3_114:                              ; %Flow653
	s_or_b32 exec_lo, exec_lo, s12
	s_branch .LBB3_142
.LBB3_115:
	v_mov_b32_e32 v18, v11
	v_mov_b32_e32 v0, 0
	v_mov_b32_e32 v1, 0
	;;#ASMSTART
	;;#ASMEND
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_readfirstlane_b32 s0, v18
	v_cmp_eq_u32_e64 s0, s0, v18
	s_delay_alu instid0(VALU_DEP_1)
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_121
; %bb.116:
	v_mov_b32_e32 v9, 0
	s_mov_b32 s4, exec_lo
	global_load_b64 v[14:15], v9, s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	s_clause 0x1
	global_load_b64 v[0:1], v9, s[2:3] offset:40
	global_load_b64 v[12:13], v9, s[2:3]
	s_waitcnt vmcnt(1)
	v_and_b32_e32 v0, v0, v14
	v_and_b32_e32 v1, v1, v15
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_mul_hi_u32 v10, v0, 24
	v_mul_lo_u32 v1, v1, 24
	v_mul_lo_u32 v0, v0, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_add_nc_u32_e32 v1, v10, v1
	s_waitcnt vmcnt(0)
	v_add_co_u32 v0, vcc_lo, v12, v0
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_ci_u32_e32 v1, vcc_lo, v13, v1, vcc_lo
	global_load_b64 v[12:13], v[0:1], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[0:1], v9, v[12:15], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmpx_ne_u64_e64 v[0:1], v[14:15]
	s_cbranch_execz .LBB3_120
; %bb.117:                              ; %.preheader63
	s_mov_b32 s5, 0
                                        ; implicit-def: $sgpr6
	.p2align	6
.LBB3_118:                              ; =>This Inner Loop Header: Depth=1
	s_sleep 1
	s_clause 0x1
	global_load_b64 v[12:13], v9, s[2:3] offset:40
	global_load_b64 v[19:20], v9, s[2:3]
	v_dual_mov_b32 v15, v1 :: v_dual_mov_b32 v14, v0
	s_waitcnt vmcnt(1)
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_and_b32_e32 v10, v12, v14
	s_waitcnt vmcnt(0)
	v_mad_u64_u32 v[0:1], null, v10, 24, v[19:20]
	v_and_b32_e32 v10, v13, v15
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_mad_u64_u32 v[12:13], null, v10, 24, v[1:2]
	v_mov_b32_e32 v1, v12
	global_load_b64 v[12:13], v[0:1], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[0:1], v9, v[12:15], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmp_eq_u64_e32 vcc_lo, v[0:1], v[14:15]
	s_or_b32 s5, vcc_lo, s5
	s_and_not1_b32 s6, s6, exec_lo
	s_and_b32 s7, vcc_lo, exec_lo
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 s6, s6, s7
	s_and_not1_b32 exec_lo, exec_lo, s5
	s_cbranch_execnz .LBB3_118
; %bb.119:                              ; %Flow666
	s_or_b32 exec_lo, exec_lo, s5
.LBB3_120:                              ; %Flow668
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s4
.LBB3_121:                              ; %Flow669
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s1
	v_mov_b32_e32 v19, 0
	v_readfirstlane_b32 s4, v0
	v_readfirstlane_b32 s5, v1
	s_mov_b64 s[6:7], exec
	s_clause 0x1
	global_load_b64 v[9:10], v19, s[2:3] offset:40
	global_load_b128 v[12:15], v19, s[2:3]
	s_waitcnt vmcnt(1)
	v_readfirstlane_b32 s10, v9
	v_readfirstlane_b32 s11, v10
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[10:11], s[4:5], s[10:11]
	s_mul_i32 s1, s11, 24
	s_mul_hi_u32 s12, s10, 24
	s_mul_i32 s13, s10, 24
	s_and_saveexec_b32 s14, s0
	s_cbranch_execz .LBB3_123
; %bb.122:
	s_add_i32 s15, s12, s1
	s_waitcnt vmcnt(0)
	v_add_co_u32 v0, vcc_lo, v12, s13
	v_add_co_ci_u32_e32 v1, vcc_lo, s15, v13, vcc_lo
	v_dual_mov_b32 v21, s7 :: v_dual_mov_b32 v20, s6
	v_dual_mov_b32 v22, 2 :: v_dual_mov_b32 v23, 1
	global_store_b128 v[0:1], v[20:23], off offset:8
.LBB3_123:
	s_or_b32 exec_lo, exec_lo, s14
	s_lshl_b64 s[6:7], s[10:11], 12
	v_lshlrev_b64 v[0:1], 6, v[18:19]
	s_waitcnt vmcnt(0)
	v_add_co_u32 v9, vcc_lo, v14, s6
	v_add_co_ci_u32_e32 v10, vcc_lo, s7, v15, vcc_lo
	s_mov_b32 s16, 0
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_u32 v0, vcc_lo, v9, v0
	s_mov_b32 s19, s16
	s_mov_b32 s17, s16
	s_mov_b32 s18, s16
	v_and_or_b32 v16, 0xffffff1f, v16, 32
	v_add_co_ci_u32_e32 v1, vcc_lo, v10, v1, vcc_lo
	v_dual_mov_b32 v18, v19 :: v_dual_mov_b32 v23, s19
	v_dual_mov_b32 v22, s18 :: v_dual_mov_b32 v21, s17
	v_mov_b32_e32 v20, s16
	s_clause 0x3
	global_store_b128 v[0:1], v[16:19], off
	global_store_b128 v[0:1], v[20:23], off offset:16
	global_store_b128 v[0:1], v[20:23], off offset:32
	global_store_b128 v[0:1], v[20:23], off offset:48
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB3_131
; %bb.124:
	v_dual_mov_b32 v18, 0 :: v_dual_mov_b32 v19, s4
	v_mov_b32_e32 v20, s5
	s_clause 0x1
	global_load_b64 v[21:22], v18, s[2:3] offset:32 glc
	global_load_b64 v[9:10], v18, s[2:3] offset:40
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s10, v9
	v_readfirstlane_b32 s11, v10
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[10:11], s[10:11], s[4:5]
	s_mul_i32 s7, s11, 24
	s_mul_hi_u32 s11, s10, 24
	s_mul_i32 s10, s10, 24
	s_add_i32 s11, s11, s7
	v_add_co_u32 v9, vcc_lo, v12, s10
	v_add_co_ci_u32_e32 v10, vcc_lo, s11, v13, vcc_lo
	s_mov_b32 s7, exec_lo
	global_store_b64 v[9:10], v[21:22], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[16:17], v18, v[19:22], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmpx_ne_u64_e64 v[16:17], v[21:22]
	s_cbranch_execz .LBB3_127
; %bb.125:                              ; %.preheader61
	s_mov_b32 s10, 0
.LBB3_126:                              ; =>This Inner Loop Header: Depth=1
	v_dual_mov_b32 v14, s4 :: v_dual_mov_b32 v15, s5
	s_sleep 1
	global_store_b64 v[9:10], v[16:17], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[14:15], v18, v[14:17], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[14:15], v[16:17]
	v_dual_mov_b32 v17, v15 :: v_dual_mov_b32 v16, v14
	s_or_b32 s10, vcc_lo, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_126
.LBB3_127:                              ; %Flow664
	s_or_b32 exec_lo, exec_lo, s7
	v_mov_b32_e32 v15, 0
	s_mov_b32 s10, exec_lo
	s_mov_b32 s7, exec_lo
	v_mbcnt_lo_u32_b32 v14, s10, 0
	global_load_b64 v[9:10], v15, s[2:3] offset:16
	v_cmpx_eq_u32_e32 0, v14
	s_cbranch_execz .LBB3_129
; %bb.128:
	s_bcnt1_i32_b32 s10, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	v_mov_b32_e32 v14, s10
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_add_u64 v[9:10], v[14:15], off offset:8
.LBB3_129:
	s_or_b32 exec_lo, exec_lo, s7
	s_waitcnt vmcnt(0)
	global_load_b64 v[14:15], v[9:10], off offset:16
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[14:15]
	s_cbranch_vccnz .LBB3_131
; %bb.130:
	global_load_b32 v9, v[9:10], off offset:24
	v_mov_b32_e32 v10, 0
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s7, v9
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_store_b64 v[14:15], v[9:10], off
	s_and_b32 m0, s7, 0xff
	s_sendmsg sendmsg(MSG_INTERRUPT)
.LBB3_131:                              ; %Flow665
	s_or_b32 exec_lo, exec_lo, s6
	s_add_i32 s12, s12, s1
	v_add_co_u32 v9, vcc_lo, v12, s13
	v_add_co_ci_u32_e32 v10, vcc_lo, s12, v13, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v9, vcc_lo, v9, 20
	v_add_co_ci_u32_e32 v10, vcc_lo, 0, v10, vcc_lo
	s_branch .LBB3_135
	.p2align	6
.LBB3_132:                              ;   in Loop: Header=BB3_135 Depth=1
	s_or_b32 exec_lo, exec_lo, s1
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_readfirstlane_b32 s1, v12
	s_cmp_eq_u32 s1, 0
	s_cbranch_scc1 .LBB3_134
; %bb.133:                              ;   in Loop: Header=BB3_135 Depth=1
	s_sleep 1
	s_cbranch_execnz .LBB3_135
	s_branch .LBB3_137
	.p2align	6
.LBB3_134:
	s_branch .LBB3_137
.LBB3_135:                              ; =>This Inner Loop Header: Depth=1
	v_mov_b32_e32 v12, 1
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_132
; %bb.136:                              ;   in Loop: Header=BB3_135 Depth=1
	global_load_b32 v12, v[9:10], off glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_and_b32_e32 v12, 1, v12
	s_branch .LBB3_132
.LBB3_137:
	global_load_b64 v[12:13], v[0:1], off
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_141
; %bb.138:
	v_mov_b32_e32 v9, 0
	s_clause 0x2
	global_load_b64 v[0:1], v9, s[2:3] offset:40
	global_load_b64 v[18:19], v9, s[2:3] offset:24 glc
	global_load_b64 v[16:17], v9, s[2:3]
	s_waitcnt vmcnt(2)
	v_add_co_u32 v10, vcc_lo, v0, 1
	v_add_co_ci_u32_e32 v20, vcc_lo, 0, v1, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v14, vcc_lo, v10, s4
	v_add_co_ci_u32_e32 v15, vcc_lo, s5, v20, vcc_lo
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[14:15]
	v_dual_cndmask_b32 v14, v14, v10 :: v_dual_cndmask_b32 v15, v15, v20
	v_and_b32_e32 v0, v14, v0
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_2) | instid1(VALU_DEP_1)
	v_mul_hi_u32 v10, v0, 24
	v_mul_lo_u32 v0, v0, 24
	s_waitcnt vmcnt(0)
	v_add_co_u32 v0, vcc_lo, v16, v0
	v_dual_mov_b32 v16, v18 :: v_dual_and_b32 v1, v15, v1
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_mul_lo_u32 v1, v1, 24
	v_add_nc_u32_e32 v1, v10, v1
	s_delay_alu instid0(VALU_DEP_1)
	v_add_co_ci_u32_e32 v1, vcc_lo, v17, v1, vcc_lo
	v_mov_b32_e32 v17, v19
	global_store_b64 v[0:1], v[18:19], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[16:17], v9, v[14:17], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_ne_u64_e32 vcc_lo, v[16:17], v[18:19]
	s_and_b32 exec_lo, exec_lo, vcc_lo
	s_cbranch_execz .LBB3_141
; %bb.139:                              ; %.preheader59
	s_mov_b32 s0, 0
.LBB3_140:                              ; =>This Inner Loop Header: Depth=1
	s_sleep 1
	global_store_b64 v[0:1], v[16:17], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[18:19], v9, v[14:17], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[18:19], v[16:17]
	v_dual_mov_b32 v16, v18 :: v_dual_mov_b32 v17, v19
	s_or_b32 s0, vcc_lo, s0
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s0
	s_cbranch_execnz .LBB3_140
.LBB3_141:                              ; %Flow657
	s_or_b32 exec_lo, exec_lo, s1
.LBB3_142:
	v_dual_mov_b32 v0, v2 :: v_dual_mov_b32 v1, v3
	s_mov_b64 s[0:1], 0
	s_mov_b32 s4, 0
.LBB3_143:                              ; =>This Inner Loop Header: Depth=1
	flat_load_u8 v9, v[0:1]
	v_add_co_u32 v0, vcc_lo, v0, 1
	v_add_co_ci_u32_e32 v1, vcc_lo, 0, v1, vcc_lo
	s_add_u32 s0, s0, 0
	s_addc_u32 s1, s1, 1
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_cmp_eq_u16_e32 vcc_lo, 0, v9
	v_dual_mov_b32 v10, s1 :: v_dual_mov_b32 v9, s0
	s_or_b32 s4, vcc_lo, s4
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s4
	s_cbranch_execnz .LBB3_143
; %bb.144:
	s_or_b32 exec_lo, exec_lo, s4
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_ne_u64_e32 0, v[2:3]
	s_xor_b32 s12, exec_lo, s0
	s_cbranch_execz .LBB3_230
; %bb.145:
	v_ashrrev_i32_e32 v1, 31, v10
	v_dual_mov_b32 v0, v10 :: v_dual_and_b32 v9, 2, v12
	v_dual_mov_b32 v35, 0 :: v_dual_and_b32 v12, -3, v12
	v_dual_mov_b32 v16, 2 :: v_dual_mov_b32 v17, 1
	s_mov_b32 s14, 0
	s_mov_b32 s13, 0
	s_branch .LBB3_147
.LBB3_146:                              ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s1
	v_sub_co_u32 v0, vcc_lo, v0, v38
	v_sub_co_ci_u32_e32 v1, vcc_lo, v1, v39, vcc_lo
	v_add_co_u32 v2, s0, v2, v38
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_add_co_ci_u32_e64 v3, s0, v3, v39, s0
	v_cmp_eq_u64_e32 vcc_lo, 0, v[0:1]
	s_or_b32 s13, vcc_lo, s13
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s13
	s_cbranch_execz .LBB3_229
.LBB3_147:                              ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB3_150 Depth 2
                                        ;     Child Loop BB3_158 Depth 2
                                        ;     Child Loop BB3_166 Depth 2
                                        ;     Child Loop BB3_174 Depth 2
                                        ;     Child Loop BB3_182 Depth 2
                                        ;     Child Loop BB3_190 Depth 2
                                        ;     Child Loop BB3_198 Depth 2
                                        ;     Child Loop BB3_206 Depth 2
                                        ;     Child Loop BB3_214 Depth 2
                                        ;     Child Loop BB3_223 Depth 2
                                        ;     Child Loop BB3_228 Depth 2
	v_cmp_gt_u64_e32 vcc_lo, 56, v[0:1]
                                        ; implicit-def: $vgpr20_vgpr21
                                        ; implicit-def: $sgpr4
	s_mov_b32 s0, exec_lo
	v_dual_cndmask_b32 v39, 0, v1 :: v_dual_cndmask_b32 v38, 56, v0
	s_delay_alu instid0(VALU_DEP_1)
	v_cmpx_gt_u32_e32 8, v38
	s_xor_b32 s1, exec_lo, s0
	s_cbranch_execz .LBB3_153
; %bb.148:                              ;   in Loop: Header=BB3_147 Depth=1
	v_mov_b32_e32 v20, 0
	v_mov_b32_e32 v21, 0
	s_mov_b64 s[4:5], 0
	s_mov_b32 s6, exec_lo
	v_cmpx_ne_u32_e32 0, v38
	s_cbranch_execz .LBB3_152
; %bb.149:                              ; %.preheader56
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_waitcnt vmcnt(0)
	v_lshlrev_b64 v[14:15], 3, v[38:39]
	v_dual_mov_b32 v20, 0 :: v_dual_mov_b32 v19, v3
	v_dual_mov_b32 v21, 0 :: v_dual_mov_b32 v18, v2
	s_mov_b32 s7, 0
	.p2align	6
.LBB3_150:                              ;   Parent Loop BB3_147 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	flat_load_u8 v10, v[18:19]
	v_mov_b32_e32 v23, s14
	v_add_co_u32 v18, vcc_lo, v18, 1
	v_add_co_ci_u32_e32 v19, vcc_lo, 0, v19, vcc_lo
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_and_b32_e32 v22, 0xffff, v10
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_2)
	v_lshlrev_b64 v[22:23], s4, v[22:23]
	s_add_u32 s4, s4, 8
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e64 s0, s4, v14
	v_or_b32_e32 v21, v23, v21
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_or_b32_e32 v20, v22, v20
	s_or_b32 s7, s0, s7
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s7
	s_cbranch_execnz .LBB3_150
; %bb.151:                              ; %Flow578
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s7
.LBB3_152:                              ; %Flow580
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s6
	s_mov_b32 s4, 0
.LBB3_153:                              ; %Flow582
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_saveexec_b32 s0, s1
	s_waitcnt vmcnt(0)
	v_dual_mov_b32 v10, s4 :: v_dual_mov_b32 v15, v3
	v_mov_b32_e32 v14, v2
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_155
; %bb.154:                              ;   in Loop: Header=BB3_147 Depth=1
	s_clause 0x6
	flat_load_u8 v10, v[2:3] offset:1
	flat_load_u8 v14, v[2:3] offset:2
	flat_load_u8 v18, v[2:3] offset:3
	flat_load_u8 v20, v[2:3]
	flat_load_u8 v21, v[2:3] offset:5
	flat_load_u8 v22, v[2:3] offset:4
	flat_load_u8 v23, v[2:3] offset:7
	v_dual_mov_b32 v24, v35 :: v_dual_mov_b32 v15, s14
	v_mov_b32_e32 v19, s14
	flat_load_d16_hi_u8 v24, v[2:3] offset:6
	s_waitcnt vmcnt(7) lgkmcnt(0)
	v_lshlrev_b16 v10, 8, v10
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v14, 0xffff, v14
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v18, 0xffff, v18
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v10, v10, v20
	v_lshlrev_b64 v[14:15], 16, v[14:15]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[18:19], 24, v[18:19]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v20, 8, v21
	v_and_b32_e32 v10, 0xffff, v10
	v_or3_b32 v15, 0, v15, v19
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v10, v10, v14, v18
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v14, 24, v23
	v_or3_b32 v15, v15, v22, v20
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v18, v10, 0, 0
	v_add_nc_u32_e32 v10, -8, v38
	s_waitcnt vmcnt(0)
	v_or3_b32 v21, v15, v24, v14
	v_add_co_u32 v14, vcc_lo, v2, 8
	v_or3_b32 v20, v18, 0, 0
	v_add_co_ci_u32_e32 v15, vcc_lo, 0, v3, vcc_lo
.LBB3_155:                              ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $vgpr22_vgpr23
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v10
	s_xor_b32 s6, exec_lo, s0
	s_cbranch_execz .LBB3_161
; %bb.156:                              ;   in Loop: Header=BB3_147 Depth=1
	v_mov_b32_e32 v22, 0
	v_mov_b32_e32 v23, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s7, exec_lo
	v_cmpx_ne_u32_e32 0, v10
	s_cbranch_execz .LBB3_160
; %bb.157:                              ; %.preheader54
                                        ;   in Loop: Header=BB3_147 Depth=1
	v_mov_b32_e32 v22, 0
	v_mov_b32_e32 v23, 0
	s_mov_b32 s10, 0
	s_mov_b64 s[4:5], 0
	.p2align	6
.LBB3_158:                              ;   Parent Loop BB3_147 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_add_co_u32 v18, vcc_lo, v14, s4
	v_add_co_ci_u32_e32 v19, vcc_lo, s5, v15, vcc_lo
	s_add_u32 s4, s4, 1
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e32 vcc_lo, s4, v10
	flat_load_u8 v18, v[18:19]
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_dual_mov_b32 v19, s14 :: v_dual_and_b32 v18, 0xffff, v18
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[18:19], s0, v[18:19]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s10, vcc_lo, s10
	v_or_b32_e32 v23, v19, v23
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v22, v18, v22
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_158
; %bb.159:                              ; %Flow573
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s10
.LBB3_160:                              ; %Flow575
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s7
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr10
.LBB3_161:                              ; %Flow577
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_saveexec_b32 s0, s6
	v_mov_b32_e32 v18, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_163
; %bb.162:                              ;   in Loop: Header=BB3_147 Depth=1
	s_clause 0x6
	flat_load_u8 v18, v[14:15] offset:1
	flat_load_u8 v22, v[14:15] offset:2
	flat_load_u8 v24, v[14:15] offset:3
	flat_load_u8 v25, v[14:15]
	flat_load_u8 v26, v[14:15] offset:5
	flat_load_u8 v27, v[14:15] offset:4
	flat_load_u8 v28, v[14:15] offset:7
	v_mov_b32_e32 v29, v35
	v_mov_b32_e32 v19, s14
	s_waitcnt vmcnt(6) lgkmcnt(0)
	v_lshlrev_b16 v30, 8, v18
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v18, 0xffff, v22
	s_waitcnt vmcnt(4)
	v_and_b32_e32 v22, 0xffff, v24
	flat_load_d16_hi_u8 v29, v[14:15] offset:6
	v_add_co_u32 v14, vcc_lo, v14, 8
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v24, v30, v25
	v_mov_b32_e32 v23, s14
	v_lshlrev_b64 v[18:19], 16, v[18:19]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v25, 8, v26
	v_add_co_ci_u32_e32 v15, vcc_lo, 0, v15, vcc_lo
	v_and_b32_e32 v24, 0xffff, v24
	v_lshlrev_b64 v[22:23], 24, v[22:23]
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or3_b32 v19, 0, v19, v23
	v_or3_b32 v18, v24, v18, v22
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v22, 24, v28
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_or3_b32 v19, v19, v27, v25
	v_or3_b32 v24, v18, 0, 0
	v_add_nc_u32_e32 v18, -8, v10
	s_waitcnt vmcnt(0) lgkmcnt(0)
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_or3_b32 v23, v19, v29, v22
	v_or3_b32 v22, v24, 0, 0
.LBB3_163:                              ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v18
	s_xor_b32 s6, exec_lo, s0
	s_cbranch_execz .LBB3_169
; %bb.164:                              ;   in Loop: Header=BB3_147 Depth=1
	v_mov_b32_e32 v24, 0
	v_mov_b32_e32 v25, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s7, exec_lo
	v_cmpx_ne_u32_e32 0, v18
	s_cbranch_execz .LBB3_168
; %bb.165:                              ; %.preheader52
                                        ;   in Loop: Header=BB3_147 Depth=1
	v_mov_b32_e32 v24, 0
	v_mov_b32_e32 v25, 0
	s_mov_b32 s10, 0
	s_mov_b64 s[4:5], 0
	.p2align	6
.LBB3_166:                              ;   Parent Loop BB3_147 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_add_co_u32 v26, vcc_lo, v14, s4
	v_add_co_ci_u32_e32 v27, vcc_lo, s5, v15, vcc_lo
	s_add_u32 s4, s4, 1
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e32 vcc_lo, s4, v18
	flat_load_u8 v10, v[26:27]
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_dual_mov_b32 v27, s14 :: v_dual_and_b32 v26, 0xffff, v10
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[26:27], s0, v[26:27]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s10, vcc_lo, s10
	v_or_b32_e32 v25, v27, v25
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v24, v26, v24
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_166
; %bb.167:                              ; %Flow568
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s10
.LBB3_168:                              ; %Flow570
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s7
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr18
.LBB3_169:                              ; %Flow572
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_saveexec_b32 s0, s6
	v_mov_b32_e32 v10, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_171
; %bb.170:                              ;   in Loop: Header=BB3_147 Depth=1
	s_clause 0x6
	flat_load_u8 v10, v[14:15] offset:1
	flat_load_u8 v19, v[14:15] offset:2
	flat_load_u8 v26, v[14:15] offset:3
	flat_load_u8 v28, v[14:15]
	flat_load_u8 v29, v[14:15] offset:5
	flat_load_u8 v30, v[14:15] offset:4
	flat_load_u8 v31, v[14:15] offset:7
	v_dual_mov_b32 v32, v35 :: v_dual_mov_b32 v25, s14
	v_mov_b32_e32 v27, s14
	flat_load_d16_hi_u8 v32, v[14:15] offset:6
	v_add_co_u32 v14, vcc_lo, v14, 8
	v_add_co_ci_u32_e32 v15, vcc_lo, 0, v15, vcc_lo
	s_waitcnt vmcnt(7) lgkmcnt(0)
	v_lshlrev_b16 v10, 8, v10
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v24, 0xffff, v19
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v26, 0xffff, v26
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v19, 8, v29
	v_or_b32_e32 v10, v10, v28
	v_lshlrev_b64 v[24:25], 16, v[24:25]
	v_lshlrev_b64 v[26:27], 24, v[26:27]
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_and_b32_e32 v10, 0xffff, v10
	v_or3_b32 v25, 0, v25, v27
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v10, v10, v24, v26
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v24, 24, v31
	v_or3_b32 v19, v25, v30, v19
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v26, v10, 0, 0
	v_add_nc_u32_e32 v10, -8, v18
	s_waitcnt vmcnt(0)
	v_or3_b32 v25, v19, v32, v24
	s_delay_alu instid0(VALU_DEP_3)
	v_or3_b32 v24, v26, 0, 0
.LBB3_171:                              ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $vgpr26_vgpr27
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v10
	s_xor_b32 s6, exec_lo, s0
	s_cbranch_execz .LBB3_177
; %bb.172:                              ;   in Loop: Header=BB3_147 Depth=1
	v_mov_b32_e32 v26, 0
	v_mov_b32_e32 v27, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s7, exec_lo
	v_cmpx_ne_u32_e32 0, v10
	s_cbranch_execz .LBB3_176
; %bb.173:                              ; %.preheader50
                                        ;   in Loop: Header=BB3_147 Depth=1
	v_mov_b32_e32 v26, 0
	v_mov_b32_e32 v27, 0
	s_mov_b32 s10, 0
	s_mov_b64 s[4:5], 0
	.p2align	6
.LBB3_174:                              ;   Parent Loop BB3_147 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_add_co_u32 v18, vcc_lo, v14, s4
	v_add_co_ci_u32_e32 v19, vcc_lo, s5, v15, vcc_lo
	s_add_u32 s4, s4, 1
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e32 vcc_lo, s4, v10
	flat_load_u8 v18, v[18:19]
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_dual_mov_b32 v19, s14 :: v_dual_and_b32 v18, 0xffff, v18
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[18:19], s0, v[18:19]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s10, vcc_lo, s10
	v_or_b32_e32 v27, v19, v27
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v26, v18, v26
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_174
; %bb.175:                              ; %Flow563
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s10
.LBB3_176:                              ; %Flow565
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s7
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr10
.LBB3_177:                              ; %Flow567
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_saveexec_b32 s0, s6
	v_mov_b32_e32 v18, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_179
; %bb.178:                              ;   in Loop: Header=BB3_147 Depth=1
	s_clause 0x6
	flat_load_u8 v18, v[14:15] offset:1
	flat_load_u8 v26, v[14:15] offset:2
	flat_load_u8 v28, v[14:15] offset:3
	flat_load_u8 v29, v[14:15]
	flat_load_u8 v30, v[14:15] offset:5
	flat_load_u8 v31, v[14:15] offset:4
	flat_load_u8 v32, v[14:15] offset:7
	v_mov_b32_e32 v33, v35
	v_mov_b32_e32 v19, s14
	s_waitcnt vmcnt(6) lgkmcnt(0)
	v_lshlrev_b16 v34, 8, v18
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v18, 0xffff, v26
	s_waitcnt vmcnt(4)
	v_and_b32_e32 v26, 0xffff, v28
	flat_load_d16_hi_u8 v33, v[14:15] offset:6
	v_add_co_u32 v14, vcc_lo, v14, 8
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v28, v34, v29
	v_mov_b32_e32 v27, s14
	v_lshlrev_b64 v[18:19], 16, v[18:19]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v29, 8, v30
	v_add_co_ci_u32_e32 v15, vcc_lo, 0, v15, vcc_lo
	v_and_b32_e32 v28, 0xffff, v28
	v_lshlrev_b64 v[26:27], 24, v[26:27]
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or3_b32 v19, 0, v19, v27
	v_or3_b32 v18, v28, v18, v26
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v26, 24, v32
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_or3_b32 v19, v19, v31, v29
	v_or3_b32 v28, v18, 0, 0
	v_add_nc_u32_e32 v18, -8, v10
	s_waitcnt vmcnt(0) lgkmcnt(0)
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_or3_b32 v27, v19, v33, v26
	v_or3_b32 v26, v28, 0, 0
.LBB3_179:                              ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v18
	s_xor_b32 s6, exec_lo, s0
	s_cbranch_execz .LBB3_185
; %bb.180:                              ;   in Loop: Header=BB3_147 Depth=1
	v_mov_b32_e32 v28, 0
	v_mov_b32_e32 v29, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s7, exec_lo
	v_cmpx_ne_u32_e32 0, v18
	s_cbranch_execz .LBB3_184
; %bb.181:                              ; %.preheader48
                                        ;   in Loop: Header=BB3_147 Depth=1
	v_mov_b32_e32 v28, 0
	v_mov_b32_e32 v29, 0
	s_mov_b32 s10, 0
	s_mov_b64 s[4:5], 0
	.p2align	6
.LBB3_182:                              ;   Parent Loop BB3_147 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_add_co_u32 v30, vcc_lo, v14, s4
	v_add_co_ci_u32_e32 v31, vcc_lo, s5, v15, vcc_lo
	s_add_u32 s4, s4, 1
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e32 vcc_lo, s4, v18
	flat_load_u8 v10, v[30:31]
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_dual_mov_b32 v31, s14 :: v_dual_and_b32 v30, 0xffff, v10
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[30:31], s0, v[30:31]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s10, vcc_lo, s10
	v_or_b32_e32 v29, v31, v29
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v28, v30, v28
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_182
; %bb.183:                              ; %Flow558
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s10
.LBB3_184:                              ; %Flow560
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s7
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr18
.LBB3_185:                              ; %Flow562
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_saveexec_b32 s0, s6
	v_mov_b32_e32 v10, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_187
; %bb.186:                              ;   in Loop: Header=BB3_147 Depth=1
	s_clause 0x6
	flat_load_u8 v10, v[14:15] offset:1
	flat_load_u8 v19, v[14:15] offset:2
	flat_load_u8 v30, v[14:15] offset:3
	flat_load_u8 v32, v[14:15]
	flat_load_u8 v33, v[14:15] offset:5
	flat_load_u8 v34, v[14:15] offset:4
	flat_load_u8 v36, v[14:15] offset:7
	v_dual_mov_b32 v48, v35 :: v_dual_mov_b32 v29, s14
	v_mov_b32_e32 v31, s14
	flat_load_d16_hi_u8 v48, v[14:15] offset:6
	v_add_co_u32 v14, vcc_lo, v14, 8
	v_add_co_ci_u32_e32 v15, vcc_lo, 0, v15, vcc_lo
	s_waitcnt vmcnt(7) lgkmcnt(0)
	v_lshlrev_b16 v10, 8, v10
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v28, 0xffff, v19
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v30, 0xffff, v30
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v19, 8, v33
	v_or_b32_e32 v10, v10, v32
	v_lshlrev_b64 v[28:29], 16, v[28:29]
	v_lshlrev_b64 v[30:31], 24, v[30:31]
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_and_b32_e32 v10, 0xffff, v10
	v_or3_b32 v29, 0, v29, v31
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v10, v10, v28, v30
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v28, 24, v36
	v_or3_b32 v19, v29, v34, v19
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v30, v10, 0, 0
	v_add_nc_u32_e32 v10, -8, v18
	s_waitcnt vmcnt(0)
	v_or3_b32 v29, v19, v48, v28
	s_delay_alu instid0(VALU_DEP_3)
	v_or3_b32 v28, v30, 0, 0
.LBB3_187:                              ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $vgpr30_vgpr31
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v10
	s_xor_b32 s6, exec_lo, s0
	s_cbranch_execz .LBB3_193
; %bb.188:                              ;   in Loop: Header=BB3_147 Depth=1
	v_mov_b32_e32 v30, 0
	v_mov_b32_e32 v31, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s7, exec_lo
	v_cmpx_ne_u32_e32 0, v10
	s_cbranch_execz .LBB3_192
; %bb.189:                              ; %.preheader46
                                        ;   in Loop: Header=BB3_147 Depth=1
	v_mov_b32_e32 v30, 0
	v_mov_b32_e32 v31, 0
	s_mov_b32 s10, 0
	s_mov_b64 s[4:5], 0
	.p2align	6
.LBB3_190:                              ;   Parent Loop BB3_147 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_add_co_u32 v18, vcc_lo, v14, s4
	v_add_co_ci_u32_e32 v19, vcc_lo, s5, v15, vcc_lo
	s_add_u32 s4, s4, 1
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e32 vcc_lo, s4, v10
	flat_load_u8 v18, v[18:19]
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_dual_mov_b32 v19, s14 :: v_dual_and_b32 v18, 0xffff, v18
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[18:19], s0, v[18:19]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s10, vcc_lo, s10
	v_or_b32_e32 v31, v19, v31
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v30, v18, v30
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_190
; %bb.191:                              ; %Flow553
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s10
.LBB3_192:                              ; %Flow555
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s7
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr10
.LBB3_193:                              ; %Flow557
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_saveexec_b32 s0, s6
	v_mov_b32_e32 v18, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_195
; %bb.194:                              ;   in Loop: Header=BB3_147 Depth=1
	s_clause 0x6
	flat_load_u8 v18, v[14:15] offset:1
	flat_load_u8 v30, v[14:15] offset:2
	flat_load_u8 v32, v[14:15] offset:3
	flat_load_u8 v33, v[14:15]
	flat_load_u8 v34, v[14:15] offset:5
	flat_load_u8 v36, v[14:15] offset:4
	flat_load_u8 v48, v[14:15] offset:7
	v_mov_b32_e32 v49, v35
	v_mov_b32_e32 v19, s14
	s_waitcnt vmcnt(6) lgkmcnt(0)
	v_lshlrev_b16 v50, 8, v18
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v18, 0xffff, v30
	s_waitcnt vmcnt(4)
	v_and_b32_e32 v30, 0xffff, v32
	flat_load_d16_hi_u8 v49, v[14:15] offset:6
	v_add_co_u32 v14, vcc_lo, v14, 8
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v32, v50, v33
	v_mov_b32_e32 v31, s14
	v_lshlrev_b64 v[18:19], 16, v[18:19]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v33, 8, v34
	v_add_co_ci_u32_e32 v15, vcc_lo, 0, v15, vcc_lo
	v_and_b32_e32 v32, 0xffff, v32
	v_lshlrev_b64 v[30:31], 24, v[30:31]
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or3_b32 v19, 0, v19, v31
	v_or3_b32 v18, v32, v18, v30
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v30, 24, v48
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_or3_b32 v19, v19, v36, v33
	v_or3_b32 v32, v18, 0, 0
	v_add_nc_u32_e32 v18, -8, v10
	s_waitcnt vmcnt(0) lgkmcnt(0)
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_or3_b32 v31, v19, v49, v30
	v_or3_b32 v30, v32, 0, 0
.LBB3_195:                              ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v18
	s_xor_b32 s4, exec_lo, s0
	s_cbranch_execz .LBB3_201
; %bb.196:                              ;   in Loop: Header=BB3_147 Depth=1
	v_mov_b32_e32 v32, 0
	v_mov_b32_e32 v33, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s5, exec_lo
	v_cmpx_ne_u32_e32 0, v18
	s_cbranch_execz .LBB3_200
; %bb.197:                              ; %.preheader44
                                        ;   in Loop: Header=BB3_147 Depth=1
	v_mov_b32_e32 v32, 0
	v_mov_b32_e32 v33, 0
	s_mov_b32 s6, 0
	.p2align	6
.LBB3_198:                              ;   Parent Loop BB3_147 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	flat_load_u8 v10, v[14:15]
	v_dual_mov_b32 v49, s14 :: v_dual_add_nc_u32 v18, -1, v18
	v_add_co_u32 v14, vcc_lo, v14, 1
	v_add_co_ci_u32_e32 v15, vcc_lo, 0, v15, vcc_lo
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_2) | instid1(VALU_DEP_1)
	v_cmp_eq_u32_e32 vcc_lo, 0, v18
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_and_b32_e32 v48, 0xffff, v10
	v_lshlrev_b64 v[48:49], s0, v[48:49]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s6, vcc_lo, s6
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or_b32_e32 v33, v49, v33
	v_or_b32_e32 v32, v48, v32
	s_and_not1_b32 exec_lo, exec_lo, s6
	s_cbranch_execnz .LBB3_198
; %bb.199:                              ; %Flow548
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
.LBB3_200:                              ; %Flow550
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s5
                                        ; implicit-def: $vgpr14_vgpr15
.LBB3_201:                              ; %Flow552
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_and_not1_saveexec_b32 s0, s4
	s_cbranch_execz .LBB3_203
; %bb.202:                              ;   in Loop: Header=BB3_147 Depth=1
	s_clause 0x5
	flat_load_u8 v10, v[14:15] offset:1
	flat_load_u8 v18, v[14:15] offset:2
	flat_load_u8 v32, v[14:15] offset:3
	flat_load_u8 v33, v[14:15]
	flat_load_u8 v34, v[14:15] offset:5
	flat_load_u8 v36, v[14:15] offset:4
	v_dual_mov_b32 v48, v35 :: v_dual_mov_b32 v19, s14
	s_clause 0x1
	flat_load_u8 v49, v[14:15] offset:7
	flat_load_d16_hi_u8 v48, v[14:15] offset:6
	v_mov_b32_e32 v15, s14
	s_waitcnt vmcnt(7) lgkmcnt(0)
	v_lshlrev_b16 v10, 8, v10
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v14, 0xffff, v18
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v18, 0xffff, v32
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v10, v10, v33
	v_lshlrev_b64 v[14:15], 16, v[14:15]
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[18:19], 24, v[18:19]
	v_and_b32_e32 v10, 0xffff, v10
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v15, 0, v15, v19
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v19, 8, v34
	v_or3_b32 v10, v10, v14, v18
	s_waitcnt vmcnt(2)
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_4) | instid1(VALU_DEP_2)
	v_or3_b32 v14, v15, v36, v19
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v15, 24, v49
	v_or3_b32 v10, v10, 0, 0
	s_waitcnt vmcnt(0)
	v_or3_b32 v33, v14, v48, v15
	s_delay_alu instid0(VALU_DEP_2)
	v_or3_b32 v32, v10, 0, 0
.LBB3_203:                              ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
	v_mov_b32_e32 v34, v11
	v_mov_b32_e32 v14, 0
	v_mov_b32_e32 v15, 0
	;;#ASMSTART
	;;#ASMEND
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_readfirstlane_b32 s0, v34
	v_cmp_eq_u32_e64 s0, s0, v34
	s_delay_alu instid0(VALU_DEP_1)
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_209
; %bb.204:                              ;   in Loop: Header=BB3_147 Depth=1
	global_load_b64 v[50:51], v35, s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	s_clause 0x1
	global_load_b64 v[14:15], v35, s[2:3] offset:40
	global_load_b64 v[18:19], v35, s[2:3]
	s_mov_b32 s4, exec_lo
	s_waitcnt vmcnt(1)
	v_and_b32_e32 v10, v15, v51
	v_and_b32_e32 v14, v14, v50
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_mul_lo_u32 v10, v10, 24
	v_mul_hi_u32 v15, v14, 24
	v_mul_lo_u32 v14, v14, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_add_nc_u32_e32 v10, v15, v10
	s_waitcnt vmcnt(0)
	v_add_co_u32 v14, vcc_lo, v18, v14
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_ci_u32_e32 v15, vcc_lo, v19, v10, vcc_lo
	global_load_b64 v[48:49], v[14:15], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[14:15], v35, v[48:51], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmpx_ne_u64_e64 v[14:15], v[50:51]
	s_cbranch_execz .LBB3_208
; %bb.205:                              ; %.preheader42
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_mov_b32 s5, 0
                                        ; implicit-def: $sgpr6
	.p2align	6
.LBB3_206:                              ;   Parent Loop BB3_147 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_sleep 1
	s_clause 0x1
	global_load_b64 v[18:19], v35, s[2:3] offset:40
	global_load_b64 v[48:49], v35, s[2:3]
	v_dual_mov_b32 v51, v15 :: v_dual_mov_b32 v50, v14
	s_waitcnt vmcnt(1)
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_and_b32_e32 v10, v18, v50
	v_and_b32_e32 v36, v19, v51
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_mad_u64_u32 v[14:15], null, v10, 24, v[48:49]
	v_mov_b32_e32 v10, v15
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_mad_u64_u32 v[18:19], null, v36, 24, v[10:11]
	v_mov_b32_e32 v15, v18
	global_load_b64 v[48:49], v[14:15], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[14:15], v35, v[48:51], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmp_eq_u64_e32 vcc_lo, v[14:15], v[50:51]
	s_or_b32 s5, vcc_lo, s5
	s_and_not1_b32 s6, s6, exec_lo
	s_and_b32 s7, vcc_lo, exec_lo
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 s6, s6, s7
	s_and_not1_b32 exec_lo, exec_lo, s5
	s_cbranch_execnz .LBB3_206
; %bb.207:                              ; %Flow544
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s5
.LBB3_208:                              ; %Flow546
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s4
.LBB3_209:                              ; %Flow547
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s1
	s_clause 0x1
	global_load_b64 v[18:19], v35, s[2:3] offset:40
	global_load_b128 v[48:51], v35, s[2:3]
	v_readfirstlane_b32 s4, v14
	v_readfirstlane_b32 s5, v15
	s_mov_b64 s[10:11], exec
	s_waitcnt vmcnt(1)
	v_readfirstlane_b32 s6, v18
	v_readfirstlane_b32 s7, v19
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[6:7], s[4:5], s[6:7]
	s_mul_i32 s1, s7, 24
	s_mul_hi_u32 s15, s6, 24
	s_mul_i32 s16, s6, 24
	s_and_saveexec_b32 s17, s0
	s_cbranch_execz .LBB3_211
; %bb.210:                              ;   in Loop: Header=BB3_147 Depth=1
	s_add_i32 s18, s15, s1
	s_waitcnt vmcnt(0)
	v_add_co_u32 v18, vcc_lo, v48, s16
	v_add_co_ci_u32_e32 v19, vcc_lo, s18, v49, vcc_lo
	v_dual_mov_b32 v15, s11 :: v_dual_mov_b32 v14, s10
	global_store_b128 v[18:19], v[14:17], off offset:8
.LBB3_211:                              ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s17
	v_cmp_lt_u64_e32 vcc_lo, 56, v[0:1]
	v_or_b32_e32 v10, 0, v13
	v_or_b32_e32 v14, v12, v9
	v_lshl_add_u32 v15, v38, 2, 28
	s_lshl_b64 s[6:7], s[6:7], 12
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_cndmask_b32_e32 v19, v10, v13, vcc_lo
	v_cndmask_b32_e32 v10, v14, v12, vcc_lo
	s_delay_alu instid0(VALU_DEP_3)
	v_and_b32_e32 v14, 0x1e0, v15
	v_lshlrev_b64 v[12:13], 6, v[34:35]
	s_waitcnt vmcnt(0)
	v_add_co_u32 v15, vcc_lo, v50, s6
	v_add_co_ci_u32_e32 v34, vcc_lo, s7, v51, vcc_lo
	v_and_or_b32 v18, 0xffffff1f, v10, v14
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_add_co_u32 v50, vcc_lo, v15, v12
	v_add_co_ci_u32_e32 v51, vcc_lo, v34, v13, vcc_lo
	s_clause 0x3
	global_store_b128 v[50:51], v[18:21], off
	global_store_b128 v[50:51], v[22:25], off offset:16
	global_store_b128 v[50:51], v[26:29], off offset:32
	global_store_b128 v[50:51], v[30:33], off offset:48
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB3_219
; %bb.212:                              ;   in Loop: Header=BB3_147 Depth=1
	s_clause 0x1
	global_load_b64 v[22:23], v35, s[2:3] offset:32 glc
	global_load_b64 v[12:13], v35, s[2:3] offset:40
	v_dual_mov_b32 v20, s4 :: v_dual_mov_b32 v21, s5
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s10, v12
	v_readfirstlane_b32 s11, v13
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[10:11], s[10:11], s[4:5]
	s_mul_i32 s7, s11, 24
	s_mul_hi_u32 s11, s10, 24
	s_mul_i32 s10, s10, 24
	s_add_i32 s11, s11, s7
	v_add_co_u32 v18, vcc_lo, v48, s10
	v_add_co_ci_u32_e32 v19, vcc_lo, s11, v49, vcc_lo
	s_mov_b32 s7, exec_lo
	global_store_b64 v[18:19], v[22:23], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[14:15], v35, v[20:23], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmpx_ne_u64_e64 v[14:15], v[22:23]
	s_cbranch_execz .LBB3_215
; %bb.213:                              ; %.preheader40
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_mov_b32 s10, 0
.LBB3_214:                              ;   Parent Loop BB3_147 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	v_dual_mov_b32 v12, s4 :: v_dual_mov_b32 v13, s5
	s_sleep 1
	global_store_b64 v[18:19], v[14:15], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[12:13], v35, v[12:15], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[12:13], v[14:15]
	v_dual_mov_b32 v15, v13 :: v_dual_mov_b32 v14, v12
	s_or_b32 s10, vcc_lo, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_214
.LBB3_215:                              ; %Flow542
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s7
	global_load_b64 v[12:13], v35, s[2:3] offset:16
	s_mov_b32 s10, exec_lo
	s_mov_b32 s7, exec_lo
	v_mbcnt_lo_u32_b32 v10, s10, 0
	s_delay_alu instid0(VALU_DEP_1)
	v_cmpx_eq_u32_e32 0, v10
	s_cbranch_execz .LBB3_217
; %bb.216:                              ;   in Loop: Header=BB3_147 Depth=1
	s_bcnt1_i32_b32 s10, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	v_mov_b32_e32 v34, s10
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_add_u64 v[12:13], v[34:35], off offset:8
.LBB3_217:                              ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s7
	s_waitcnt vmcnt(0)
	global_load_b64 v[14:15], v[12:13], off offset:16
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[14:15]
	s_cbranch_vccnz .LBB3_219
; %bb.218:                              ;   in Loop: Header=BB3_147 Depth=1
	global_load_b32 v34, v[12:13], off offset:24
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s7, v34
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_store_b64 v[14:15], v[34:35], off
	s_and_b32 m0, s7, 0xff
	s_sendmsg sendmsg(MSG_INTERRUPT)
.LBB3_219:                              ; %Flow543
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
	s_add_i32 s15, s15, s1
	v_add_co_u32 v10, vcc_lo, v48, s16
	v_add_co_ci_u32_e32 v13, vcc_lo, s15, v49, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v12, vcc_lo, v10, 20
	v_add_co_ci_u32_e32 v13, vcc_lo, 0, v13, vcc_lo
	s_branch .LBB3_223
	.p2align	6
.LBB3_220:                              ;   in Loop: Header=BB3_223 Depth=2
	s_or_b32 exec_lo, exec_lo, s1
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_readfirstlane_b32 s1, v10
	s_cmp_eq_u32 s1, 0
	s_cbranch_scc1 .LBB3_222
; %bb.221:                              ;   in Loop: Header=BB3_223 Depth=2
	s_sleep 1
	s_cbranch_execnz .LBB3_223
	s_branch .LBB3_225
	.p2align	6
.LBB3_222:                              ;   in Loop: Header=BB3_147 Depth=1
	s_branch .LBB3_225
.LBB3_223:                              ;   Parent Loop BB3_147 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	v_mov_b32_e32 v10, 1
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_220
; %bb.224:                              ;   in Loop: Header=BB3_223 Depth=2
	global_load_b32 v10, v[12:13], off glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_and_b32_e32 v10, 1, v10
	s_branch .LBB3_220
.LBB3_225:                              ;   in Loop: Header=BB3_147 Depth=1
	global_load_b128 v[12:15], v[50:51], off
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_146
; %bb.226:                              ;   in Loop: Header=BB3_147 Depth=1
	s_clause 0x2
	global_load_b64 v[14:15], v35, s[2:3] offset:40
	global_load_b64 v[22:23], v35, s[2:3] offset:24 glc
	global_load_b64 v[20:21], v35, s[2:3]
	s_waitcnt vmcnt(2)
	v_add_co_u32 v10, vcc_lo, v14, 1
	v_add_co_ci_u32_e32 v24, vcc_lo, 0, v15, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v18, vcc_lo, v10, s4
	v_add_co_ci_u32_e32 v19, vcc_lo, s5, v24, vcc_lo
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[18:19]
	v_dual_cndmask_b32 v19, v19, v24 :: v_dual_cndmask_b32 v18, v18, v10
	v_and_b32_e32 v10, v19, v15
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_and_b32_e32 v14, v18, v14
	v_mul_lo_u32 v10, v10, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_mul_hi_u32 v15, v14, 24
	v_mul_lo_u32 v14, v14, 24
	v_add_nc_u32_e32 v10, v15, v10
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_3)
	v_add_co_u32 v14, vcc_lo, v20, v14
	v_mov_b32_e32 v20, v22
	v_add_co_ci_u32_e32 v15, vcc_lo, v21, v10, vcc_lo
	v_mov_b32_e32 v21, v23
	global_store_b64 v[14:15], v[22:23], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[20:21], v35, v[18:21], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_ne_u64_e32 vcc_lo, v[20:21], v[22:23]
	s_and_b32 exec_lo, exec_lo, vcc_lo
	s_cbranch_execz .LBB3_146
; %bb.227:                              ; %.preheader38
                                        ;   in Loop: Header=BB3_147 Depth=1
	s_mov_b32 s0, 0
.LBB3_228:                              ;   Parent Loop BB3_147 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_sleep 1
	global_store_b64 v[14:15], v[20:21], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[22:23], v35, v[18:21], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[22:23], v[20:21]
	v_dual_mov_b32 v20, v22 :: v_dual_mov_b32 v21, v23
	s_or_b32 s0, vcc_lo, s0
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s0
	s_cbranch_execnz .LBB3_228
	s_branch .LBB3_146
.LBB3_229:                              ; %Flow583
	s_or_b32 exec_lo, exec_lo, s13
.LBB3_230:                              ; %Flow601
	s_and_not1_saveexec_b32 s1, s12
	s_cbranch_execz .LBB3_258
; %bb.231:
	s_waitcnt vmcnt(0)
	v_dual_mov_b32 v14, v11 :: v_dual_mov_b32 v9, 0
	;;#ASMSTART
	;;#ASMEND
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_readfirstlane_b32 s0, v14
	v_mov_b32_e32 v10, 0
	v_cmp_eq_u32_e64 s0, s0, v14
	s_delay_alu instid0(VALU_DEP_1)
	s_and_saveexec_b32 s4, s0
	s_cbranch_execz .LBB3_237
; %bb.232:
	v_mov_b32_e32 v0, 0
	s_mov_b32 s5, exec_lo
	global_load_b64 v[17:18], v0, s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	s_clause 0x1
	global_load_b64 v[1:2], v0, s[2:3] offset:40
	global_load_b64 v[9:10], v0, s[2:3]
	s_waitcnt vmcnt(1)
	v_and_b32_e32 v1, v1, v17
	v_and_b32_e32 v2, v2, v18
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_mul_hi_u32 v3, v1, 24
	v_mul_lo_u32 v2, v2, 24
	v_mul_lo_u32 v1, v1, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_add_nc_u32_e32 v2, v3, v2
	s_waitcnt vmcnt(0)
	v_add_co_u32 v1, vcc_lo, v9, v1
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_ci_u32_e32 v2, vcc_lo, v10, v2, vcc_lo
	global_load_b64 v[15:16], v[1:2], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[9:10], v0, v[15:18], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmpx_ne_u64_e64 v[9:10], v[17:18]
	s_cbranch_execz .LBB3_236
; %bb.233:                              ; %.preheader36
	s_mov_b32 s6, 0
                                        ; implicit-def: $sgpr7
	.p2align	6
.LBB3_234:                              ; =>This Inner Loop Header: Depth=1
	s_sleep 1
	s_clause 0x1
	global_load_b64 v[1:2], v0, s[2:3] offset:40
	global_load_b64 v[15:16], v0, s[2:3]
	v_dual_mov_b32 v18, v10 :: v_dual_mov_b32 v17, v9
	s_waitcnt vmcnt(1)
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_and_b32_e32 v1, v1, v17
	s_waitcnt vmcnt(0)
	v_mad_u64_u32 v[9:10], null, v1, 24, v[15:16]
	v_and_b32_e32 v15, v2, v18
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_mov_b32_e32 v1, v10
	v_mad_u64_u32 v[2:3], null, v15, 24, v[1:2]
	s_delay_alu instid0(VALU_DEP_1)
	v_mov_b32_e32 v10, v2
	global_load_b64 v[15:16], v[9:10], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[9:10], v0, v[15:18], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmp_eq_u64_e32 vcc_lo, v[9:10], v[17:18]
	s_or_b32 s6, vcc_lo, s6
	s_and_not1_b32 s7, s7, exec_lo
	s_and_b32 s10, vcc_lo, exec_lo
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 s7, s7, s10
	s_and_not1_b32 exec_lo, exec_lo, s6
	s_cbranch_execnz .LBB3_234
; %bb.235:                              ; %Flow596
	s_or_b32 exec_lo, exec_lo, s6
.LBB3_236:                              ; %Flow598
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s5
.LBB3_237:                              ; %Flow599
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s4
	v_mov_b32_e32 v15, 0
	v_readfirstlane_b32 s4, v9
	v_readfirstlane_b32 s5, v10
	s_mov_b64 s[6:7], exec
	s_clause 0x1
	global_load_b64 v[16:17], v15, s[2:3] offset:40
	global_load_b128 v[0:3], v15, s[2:3]
	s_waitcnt vmcnt(1)
	v_readfirstlane_b32 s10, v16
	v_readfirstlane_b32 s11, v17
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[10:11], s[4:5], s[10:11]
	s_mul_i32 s12, s11, 24
	s_mul_hi_u32 s13, s10, 24
	s_mul_i32 s14, s10, 24
	s_and_saveexec_b32 s15, s0
	s_cbranch_execz .LBB3_239
; %bb.238:
	s_add_i32 s16, s13, s12
	s_waitcnt vmcnt(0)
	v_add_co_u32 v9, vcc_lo, v0, s14
	v_add_co_ci_u32_e32 v10, vcc_lo, s16, v1, vcc_lo
	v_dual_mov_b32 v17, s7 :: v_dual_mov_b32 v16, s6
	v_dual_mov_b32 v18, 2 :: v_dual_mov_b32 v19, 1
	global_store_b128 v[9:10], v[16:19], off offset:8
.LBB3_239:
	s_or_b32 exec_lo, exec_lo, s15
	s_lshl_b64 s[6:7], s[10:11], 12
	v_lshlrev_b64 v[9:10], 6, v[14:15]
	s_waitcnt vmcnt(0)
	v_add_co_u32 v2, vcc_lo, v2, s6
	v_add_co_ci_u32_e32 v3, vcc_lo, s7, v3, vcc_lo
	s_mov_b32 s16, 0
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_u32 v2, vcc_lo, v2, v9
	s_mov_b32 s17, s16
	s_mov_b32 s18, s16
	s_mov_b32 s19, s16
	v_and_or_b32 v12, 0xffffff1f, v12, 32
	v_add_co_ci_u32_e32 v3, vcc_lo, v3, v10, vcc_lo
	v_mov_b32_e32 v14, v15
	v_dual_mov_b32 v16, s16 :: v_dual_mov_b32 v19, s19
	v_dual_mov_b32 v17, s17 :: v_dual_mov_b32 v18, s18
	s_clause 0x3
	global_store_b128 v[2:3], v[12:15], off
	global_store_b128 v[2:3], v[16:19], off offset:16
	global_store_b128 v[2:3], v[16:19], off offset:32
	global_store_b128 v[2:3], v[16:19], off offset:48
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB3_247
; %bb.240:
	v_dual_mov_b32 v16, 0 :: v_dual_mov_b32 v17, s4
	v_mov_b32_e32 v18, s5
	s_clause 0x1
	global_load_b64 v[19:20], v16, s[2:3] offset:32 glc
	global_load_b64 v[9:10], v16, s[2:3] offset:40
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s10, v9
	v_readfirstlane_b32 s11, v10
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[10:11], s[10:11], s[4:5]
	s_mul_i32 s7, s11, 24
	s_mul_hi_u32 s11, s10, 24
	s_mul_i32 s10, s10, 24
	s_add_i32 s11, s11, s7
	v_add_co_u32 v9, vcc_lo, v0, s10
	v_add_co_ci_u32_e32 v10, vcc_lo, s11, v1, vcc_lo
	s_mov_b32 s7, exec_lo
	global_store_b64 v[9:10], v[19:20], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[14:15], v16, v[17:20], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmpx_ne_u64_e64 v[14:15], v[19:20]
	s_cbranch_execz .LBB3_243
; %bb.241:                              ; %.preheader34
	s_mov_b32 s10, 0
.LBB3_242:                              ; =>This Inner Loop Header: Depth=1
	v_dual_mov_b32 v12, s4 :: v_dual_mov_b32 v13, s5
	s_sleep 1
	global_store_b64 v[9:10], v[14:15], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[12:13], v16, v[12:15], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[12:13], v[14:15]
	v_dual_mov_b32 v15, v13 :: v_dual_mov_b32 v14, v12
	s_or_b32 s10, vcc_lo, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_242
.LBB3_243:                              ; %Flow594
	s_or_b32 exec_lo, exec_lo, s7
	v_mov_b32_e32 v13, 0
	s_mov_b32 s10, exec_lo
	s_mov_b32 s7, exec_lo
	v_mbcnt_lo_u32_b32 v12, s10, 0
	global_load_b64 v[9:10], v13, s[2:3] offset:16
	v_cmpx_eq_u32_e32 0, v12
	s_cbranch_execz .LBB3_245
; %bb.244:
	s_bcnt1_i32_b32 s10, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	v_mov_b32_e32 v12, s10
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_add_u64 v[9:10], v[12:13], off offset:8
.LBB3_245:
	s_or_b32 exec_lo, exec_lo, s7
	s_waitcnt vmcnt(0)
	global_load_b64 v[12:13], v[9:10], off offset:16
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[12:13]
	s_cbranch_vccnz .LBB3_247
; %bb.246:
	global_load_b32 v9, v[9:10], off offset:24
	v_mov_b32_e32 v10, 0
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s7, v9
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_store_b64 v[12:13], v[9:10], off
	s_and_b32 m0, s7, 0xff
	s_sendmsg sendmsg(MSG_INTERRUPT)
.LBB3_247:                              ; %Flow595
	s_or_b32 exec_lo, exec_lo, s6
	s_add_i32 s13, s13, s12
	v_add_co_u32 v0, vcc_lo, v0, s14
	v_add_co_ci_u32_e32 v1, vcc_lo, s13, v1, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v0, vcc_lo, v0, 20
	v_add_co_ci_u32_e32 v1, vcc_lo, 0, v1, vcc_lo
	s_branch .LBB3_251
	.p2align	6
.LBB3_248:                              ;   in Loop: Header=BB3_251 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_readfirstlane_b32 s6, v9
	s_cmp_eq_u32 s6, 0
	s_cbranch_scc1 .LBB3_250
; %bb.249:                              ;   in Loop: Header=BB3_251 Depth=1
	s_sleep 1
	s_cbranch_execnz .LBB3_251
	s_branch .LBB3_253
	.p2align	6
.LBB3_250:
	s_branch .LBB3_253
.LBB3_251:                              ; =>This Inner Loop Header: Depth=1
	v_mov_b32_e32 v9, 1
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB3_248
; %bb.252:                              ;   in Loop: Header=BB3_251 Depth=1
	global_load_b32 v9, v[0:1], off glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_and_b32_e32 v9, 1, v9
	s_branch .LBB3_248
.LBB3_253:
	global_load_b64 v[12:13], v[2:3], off
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB3_257
; %bb.254:
	v_mov_b32_e32 v14, 0
	s_clause 0x2
	global_load_b64 v[2:3], v14, s[2:3] offset:40
	global_load_b64 v[15:16], v14, s[2:3] offset:24 glc
	global_load_b64 v[9:10], v14, s[2:3]
	s_waitcnt vmcnt(2)
	v_add_co_u32 v17, vcc_lo, v2, 1
	v_add_co_ci_u32_e32 v18, vcc_lo, 0, v3, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v0, vcc_lo, v17, s4
	v_add_co_ci_u32_e32 v1, vcc_lo, s5, v18, vcc_lo
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[0:1]
	v_dual_cndmask_b32 v1, v1, v18 :: v_dual_cndmask_b32 v0, v0, v17
	v_and_b32_e32 v3, v1, v3
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_and_b32_e32 v2, v0, v2
	v_mul_lo_u32 v3, v3, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_mul_hi_u32 v17, v2, 24
	v_mul_lo_u32 v2, v2, 24
	v_add_nc_u32_e32 v3, v17, v3
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_3)
	v_add_co_u32 v9, vcc_lo, v9, v2
	v_mov_b32_e32 v2, v15
	v_add_co_ci_u32_e32 v10, vcc_lo, v10, v3, vcc_lo
	v_mov_b32_e32 v3, v16
	global_store_b64 v[9:10], v[15:16], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[2:3], v14, v[0:3], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_ne_u64_e32 vcc_lo, v[2:3], v[15:16]
	s_and_b32 exec_lo, exec_lo, vcc_lo
	s_cbranch_execz .LBB3_257
; %bb.255:                              ; %.preheader32
	s_mov_b32 s0, 0
.LBB3_256:                              ; =>This Inner Loop Header: Depth=1
	s_sleep 1
	global_store_b64 v[9:10], v[2:3], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[15:16], v14, v[0:3], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[15:16], v[2:3]
	v_dual_mov_b32 v2, v15 :: v_dual_mov_b32 v3, v16
	s_or_b32 s0, vcc_lo, s0
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s0
	s_cbranch_execnz .LBB3_256
.LBB3_257:                              ; %Flow587
	s_or_b32 exec_lo, exec_lo, s6
.LBB3_258:                              ; %Flow602
	s_delay_alu instid0(SALU_CYCLE_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	s_or_b32 exec_lo, exec_lo, s1
	s_waitcnt vmcnt(0)
	v_dual_mov_b32 v9, v11 :: v_dual_mov_b32 v14, 0
	;;#ASMSTART
	;;#ASMEND
	v_readfirstlane_b32 s0, v9
	v_mov_b32_e32 v15, 0
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_cmp_eq_u32_e64 s0, s0, v9
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_264
; %bb.259:
	v_mov_b32_e32 v0, 0
	s_mov_b32 s4, exec_lo
	global_load_b64 v[16:17], v0, s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	s_clause 0x1
	global_load_b64 v[1:2], v0, s[2:3] offset:40
	global_load_b64 v[14:15], v0, s[2:3]
	s_waitcnt vmcnt(1)
	v_and_b32_e32 v1, v1, v16
	v_and_b32_e32 v2, v2, v17
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_mul_hi_u32 v3, v1, 24
	v_mul_lo_u32 v2, v2, 24
	v_mul_lo_u32 v1, v1, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_add_nc_u32_e32 v2, v3, v2
	s_waitcnt vmcnt(0)
	v_add_co_u32 v1, vcc_lo, v14, v1
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_ci_u32_e32 v2, vcc_lo, v15, v2, vcc_lo
	global_load_b64 v[14:15], v[1:2], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[14:15], v0, v[14:17], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmpx_ne_u64_e64 v[14:15], v[16:17]
	s_cbranch_execz .LBB3_263
; %bb.260:                              ; %.preheader30
	s_mov_b32 s5, 0
                                        ; implicit-def: $sgpr6
	.p2align	6
.LBB3_261:                              ; =>This Inner Loop Header: Depth=1
	s_sleep 1
	s_clause 0x1
	global_load_b64 v[1:2], v0, s[2:3] offset:40
	global_load_b64 v[18:19], v0, s[2:3]
	v_dual_mov_b32 v17, v15 :: v_dual_mov_b32 v16, v14
	s_waitcnt vmcnt(1)
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_and_b32_e32 v1, v1, v16
	s_waitcnt vmcnt(0)
	v_mad_u64_u32 v[14:15], null, v1, 24, v[18:19]
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_dual_mov_b32 v1, v15 :: v_dual_and_b32 v10, v2, v17
	v_mad_u64_u32 v[2:3], null, v10, 24, v[1:2]
	s_delay_alu instid0(VALU_DEP_1)
	v_mov_b32_e32 v15, v2
	global_load_b64 v[14:15], v[14:15], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[14:15], v0, v[14:17], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmp_eq_u64_e32 vcc_lo, v[14:15], v[16:17]
	s_or_b32 s5, vcc_lo, s5
	s_and_not1_b32 s6, s6, exec_lo
	s_and_b32 s7, vcc_lo, exec_lo
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 s6, s6, s7
	s_and_not1_b32 exec_lo, exec_lo, s5
	s_cbranch_execnz .LBB3_261
; %bb.262:                              ; %Flow529
	s_or_b32 exec_lo, exec_lo, s5
.LBB3_263:                              ; %Flow531
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s4
.LBB3_264:                              ; %Flow532
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s1
	v_mov_b32_e32 v10, 0
	v_readfirstlane_b32 s4, v14
	v_readfirstlane_b32 s5, v15
	s_mov_b64 s[6:7], exec
	s_clause 0x1
	global_load_b64 v[16:17], v10, s[2:3] offset:40
	global_load_b128 v[0:3], v10, s[2:3]
	s_waitcnt vmcnt(1)
	v_readfirstlane_b32 s10, v16
	v_readfirstlane_b32 s11, v17
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[10:11], s[4:5], s[10:11]
	s_mul_i32 s1, s11, 24
	s_mul_hi_u32 s12, s10, 24
	s_mul_i32 s13, s10, 24
	s_and_saveexec_b32 s14, s0
	s_cbranch_execz .LBB3_266
; %bb.265:
	s_add_i32 s15, s12, s1
	s_waitcnt vmcnt(0)
	v_add_co_u32 v18, vcc_lo, v0, s13
	v_add_co_ci_u32_e32 v19, vcc_lo, s15, v1, vcc_lo
	v_dual_mov_b32 v15, s7 :: v_dual_mov_b32 v14, s6
	v_dual_mov_b32 v16, 2 :: v_dual_mov_b32 v17, 1
	global_store_b128 v[18:19], v[14:17], off offset:8
.LBB3_266:
	s_or_b32 exec_lo, exec_lo, s14
	s_lshl_b64 s[6:7], s[10:11], 12
	v_lshlrev_b64 v[9:10], 6, v[9:10]
	s_waitcnt vmcnt(0)
	v_add_co_u32 v2, vcc_lo, v2, s6
	v_add_co_ci_u32_e32 v3, vcc_lo, s7, v3, vcc_lo
	s_mov_b32 s16, 0
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_u32 v2, vcc_lo, v2, v9
	s_mov_b32 s17, s16
	s_mov_b32 s18, s16
	s_mov_b32 s19, s16
	v_dual_mov_b32 v15, 0 :: v_dual_mov_b32 v14, v4
	v_and_or_b32 v12, 0xffffff1f, v12, 32
	v_add_co_ci_u32_e32 v3, vcc_lo, v3, v10, vcc_lo
	v_dual_mov_b32 v16, s16 :: v_dual_mov_b32 v17, s17
	v_dual_mov_b32 v18, s18 :: v_dual_mov_b32 v19, s19
	s_clause 0x3
	global_store_b128 v[2:3], v[12:15], off
	global_store_b128 v[2:3], v[16:19], off offset:16
	global_store_b128 v[2:3], v[16:19], off offset:32
	global_store_b128 v[2:3], v[16:19], off offset:48
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB3_274
; %bb.267:
	v_dual_mov_b32 v4, 0 :: v_dual_mov_b32 v15, s5
	v_mov_b32_e32 v14, s4
	s_clause 0x1
	global_load_b64 v[16:17], v4, s[2:3] offset:32 glc
	global_load_b64 v[9:10], v4, s[2:3] offset:40
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s10, v9
	v_readfirstlane_b32 s11, v10
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[10:11], s[10:11], s[4:5]
	s_mul_i32 s7, s11, 24
	s_mul_hi_u32 s11, s10, 24
	s_mul_i32 s10, s10, 24
	s_add_i32 s11, s11, s7
	v_add_co_u32 v9, vcc_lo, v0, s10
	v_add_co_ci_u32_e32 v10, vcc_lo, s11, v1, vcc_lo
	s_mov_b32 s7, exec_lo
	global_store_b64 v[9:10], v[16:17], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[14:15], v4, v[14:17], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmpx_ne_u64_e64 v[14:15], v[16:17]
	s_cbranch_execz .LBB3_270
; %bb.268:                              ; %.preheader28
	s_mov_b32 s10, 0
.LBB3_269:                              ; =>This Inner Loop Header: Depth=1
	v_dual_mov_b32 v12, s4 :: v_dual_mov_b32 v13, s5
	s_sleep 1
	global_store_b64 v[9:10], v[14:15], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[12:13], v4, v[12:15], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[12:13], v[14:15]
	v_dual_mov_b32 v15, v13 :: v_dual_mov_b32 v14, v12
	s_or_b32 s10, vcc_lo, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_269
.LBB3_270:                              ; %Flow527
	s_or_b32 exec_lo, exec_lo, s7
	v_mov_b32_e32 v13, 0
	s_mov_b32 s10, exec_lo
	s_mov_b32 s7, exec_lo
	v_mbcnt_lo_u32_b32 v4, s10, 0
	global_load_b64 v[9:10], v13, s[2:3] offset:16
	v_cmpx_eq_u32_e32 0, v4
	s_cbranch_execz .LBB3_272
; %bb.271:
	s_bcnt1_i32_b32 s10, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	v_mov_b32_e32 v12, s10
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_add_u64 v[9:10], v[12:13], off offset:8
.LBB3_272:
	s_or_b32 exec_lo, exec_lo, s7
	s_waitcnt vmcnt(0)
	global_load_b64 v[12:13], v[9:10], off offset:16
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[12:13]
	s_cbranch_vccnz .LBB3_274
; %bb.273:
	global_load_b32 v9, v[9:10], off offset:24
	v_mov_b32_e32 v10, 0
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s7, v9
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_store_b64 v[12:13], v[9:10], off
	s_and_b32 m0, s7, 0xff
	s_sendmsg sendmsg(MSG_INTERRUPT)
.LBB3_274:                              ; %Flow528
	s_or_b32 exec_lo, exec_lo, s6
	s_add_i32 s12, s12, s1
	v_add_co_u32 v0, vcc_lo, v0, s13
	v_add_co_ci_u32_e32 v1, vcc_lo, s12, v1, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v0, vcc_lo, v0, 20
	v_add_co_ci_u32_e32 v1, vcc_lo, 0, v1, vcc_lo
	s_branch .LBB3_278
	.p2align	6
.LBB3_275:                              ;   in Loop: Header=BB3_278 Depth=1
	s_or_b32 exec_lo, exec_lo, s1
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_readfirstlane_b32 s1, v4
	s_cmp_eq_u32 s1, 0
	s_cbranch_scc1 .LBB3_277
; %bb.276:                              ;   in Loop: Header=BB3_278 Depth=1
	s_sleep 1
	s_cbranch_execnz .LBB3_278
	s_branch .LBB3_280
	.p2align	6
.LBB3_277:
	s_branch .LBB3_280
.LBB3_278:                              ; =>This Inner Loop Header: Depth=1
	v_mov_b32_e32 v4, 1
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_275
; %bb.279:                              ;   in Loop: Header=BB3_278 Depth=1
	global_load_b32 v4, v[0:1], off glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_and_b32_e32 v4, 1, v4
	s_branch .LBB3_275
.LBB3_280:
	global_load_b64 v[9:10], v[2:3], off
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_284
; %bb.281:
	v_mov_b32_e32 v4, 0
	s_clause 0x2
	global_load_b64 v[2:3], v4, s[2:3] offset:40
	global_load_b64 v[14:15], v4, s[2:3] offset:24 glc
	global_load_b64 v[12:13], v4, s[2:3]
	s_waitcnt vmcnt(2)
	v_add_co_u32 v16, vcc_lo, v2, 1
	v_add_co_ci_u32_e32 v17, vcc_lo, 0, v3, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v0, vcc_lo, v16, s4
	v_add_co_ci_u32_e32 v1, vcc_lo, s5, v17, vcc_lo
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[0:1]
	v_dual_cndmask_b32 v1, v1, v17 :: v_dual_cndmask_b32 v0, v0, v16
	v_and_b32_e32 v3, v1, v3
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_and_b32_e32 v2, v0, v2
	v_mul_lo_u32 v3, v3, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_mul_hi_u32 v16, v2, 24
	v_mul_lo_u32 v2, v2, 24
	v_add_nc_u32_e32 v3, v16, v3
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_3)
	v_add_co_u32 v12, vcc_lo, v12, v2
	v_mov_b32_e32 v2, v14
	v_add_co_ci_u32_e32 v13, vcc_lo, v13, v3, vcc_lo
	v_mov_b32_e32 v3, v15
	global_store_b64 v[12:13], v[14:15], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[2:3], v4, v[0:3], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_ne_u64_e32 vcc_lo, v[2:3], v[14:15]
	s_and_b32 exec_lo, exec_lo, vcc_lo
	s_cbranch_execz .LBB3_284
; %bb.282:                              ; %.preheader26
	s_mov_b32 s0, 0
.LBB3_283:                              ; =>This Inner Loop Header: Depth=1
	s_sleep 1
	global_store_b64 v[12:13], v[2:3], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[14:15], v4, v[0:3], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[14:15], v[2:3]
	v_dual_mov_b32 v2, v14 :: v_dual_mov_b32 v3, v15
	s_or_b32 s0, vcc_lo, s0
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s0
	s_cbranch_execnz .LBB3_283
.LBB3_284:
	s_or_b32 exec_lo, exec_lo, s1
	v_dual_mov_b32 v0, v5 :: v_dual_mov_b32 v1, v6
	s_mov_b64 s[0:1], 0
	s_mov_b32 s4, 0
.LBB3_285:                              ; =>This Inner Loop Header: Depth=1
	flat_load_u8 v2, v[0:1]
	v_add_co_u32 v3, vcc_lo, v0, 1
	v_add_co_ci_u32_e32 v4, vcc_lo, 0, v1, vcc_lo
	s_add_u32 s0, s0, 0
	s_addc_u32 s1, s1, 1
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_cmp_eq_u16_e32 vcc_lo, 0, v2
	v_dual_mov_b32 v2, s1 :: v_dual_mov_b32 v1, s0
	v_dual_mov_b32 v0, v3 :: v_dual_mov_b32 v1, v4
	s_or_b32 s4, vcc_lo, s4
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s4
	s_cbranch_execnz .LBB3_285
; %bb.286:
	s_or_b32 exec_lo, exec_lo, s4
                                        ; implicit-def: $vgpr0_vgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_ne_u64_e32 0, v[5:6]
	s_xor_b32 s12, exec_lo, s0
	s_cbranch_execz .LBB3_372
; %bb.287:
	v_dual_mov_b32 v35, 0 :: v_dual_and_b32 v4, 2, v9
	v_dual_mov_b32 v32, v2 :: v_dual_and_b32 v9, -3, v9
	v_ashrrev_i32_e32 v33, 31, v2
	v_dual_mov_b32 v14, 2 :: v_dual_mov_b32 v15, 1
	s_delay_alu instid0(VALU_DEP_3)
	v_dual_mov_b32 v0, v9 :: v_dual_mov_b32 v1, v10
	s_mov_b32 s14, 0
	s_mov_b32 s13, 0
	s_branch .LBB3_289
.LBB3_288:                              ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s1
	v_sub_co_u32 v32, vcc_lo, v32, v9
	v_sub_co_ci_u32_e32 v33, vcc_lo, v33, v10, vcc_lo
	v_add_co_u32 v5, s0, v5, v9
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_add_co_ci_u32_e64 v6, s0, v6, v10, s0
	v_cmp_eq_u64_e32 vcc_lo, 0, v[32:33]
	s_or_b32 s13, vcc_lo, s13
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s13
	s_cbranch_execz .LBB3_371
.LBB3_289:                              ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB3_292 Depth 2
                                        ;     Child Loop BB3_300 Depth 2
                                        ;     Child Loop BB3_308 Depth 2
                                        ;     Child Loop BB3_316 Depth 2
                                        ;     Child Loop BB3_324 Depth 2
                                        ;     Child Loop BB3_332 Depth 2
                                        ;     Child Loop BB3_340 Depth 2
                                        ;     Child Loop BB3_348 Depth 2
                                        ;     Child Loop BB3_356 Depth 2
                                        ;     Child Loop BB3_365 Depth 2
                                        ;     Child Loop BB3_370 Depth 2
	v_cmp_gt_u64_e32 vcc_lo, 56, v[32:33]
                                        ; implicit-def: $vgpr2_vgpr3
                                        ; implicit-def: $sgpr4
	s_mov_b32 s0, exec_lo
	v_dual_cndmask_b32 v10, 0, v33 :: v_dual_cndmask_b32 v9, 56, v32
	s_delay_alu instid0(VALU_DEP_1)
	v_cmpx_gt_u32_e32 8, v9
	s_xor_b32 s1, exec_lo, s0
	s_cbranch_execz .LBB3_295
; %bb.290:                              ;   in Loop: Header=BB3_289 Depth=1
	s_waitcnt vmcnt(0)
	v_mov_b32_e32 v2, 0
	v_mov_b32_e32 v3, 0
	s_mov_b64 s[4:5], 0
	s_mov_b32 s6, exec_lo
	v_cmpx_ne_u32_e32 0, v9
	s_cbranch_execz .LBB3_294
; %bb.291:                              ; %.preheader23
                                        ;   in Loop: Header=BB3_289 Depth=1
	v_lshlrev_b64 v[12:13], 3, v[9:10]
	v_dual_mov_b32 v2, 0 :: v_dual_mov_b32 v17, v6
	v_dual_mov_b32 v3, 0 :: v_dual_mov_b32 v16, v5
	s_mov_b32 s7, 0
	.p2align	6
.LBB3_292:                              ;   Parent Loop BB3_289 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	flat_load_u8 v13, v[16:17]
	v_mov_b32_e32 v19, s14
	v_add_co_u32 v16, vcc_lo, v16, 1
	v_add_co_ci_u32_e32 v17, vcc_lo, 0, v17, vcc_lo
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_and_b32_e32 v18, 0xffff, v13
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_2)
	v_lshlrev_b64 v[18:19], s4, v[18:19]
	s_add_u32 s4, s4, 8
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e64 s0, s4, v12
	v_or_b32_e32 v3, v19, v3
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_or_b32_e32 v2, v18, v2
	s_or_b32 s7, s0, s7
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s7
	s_cbranch_execnz .LBB3_292
; %bb.293:                              ; %Flow493
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s7
.LBB3_294:                              ; %Flow495
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s6
	s_mov_b32 s4, 0
.LBB3_295:                              ; %Flow497
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_saveexec_b32 s0, s1
	v_dual_mov_b32 v18, s4 :: v_dual_mov_b32 v13, v6
	v_mov_b32_e32 v12, v5
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_297
; %bb.296:                              ;   in Loop: Header=BB3_289 Depth=1
	s_waitcnt vmcnt(0)
	s_clause 0x6
	flat_load_u8 v2, v[5:6] offset:1
	flat_load_u8 v12, v[5:6] offset:2
	flat_load_u8 v16, v[5:6] offset:3
	flat_load_u8 v17, v[5:6]
	flat_load_u8 v18, v[5:6] offset:5
	flat_load_u8 v19, v[5:6] offset:4
	flat_load_u8 v20, v[5:6] offset:7
	v_mov_b32_e32 v21, v35
	v_mov_b32_e32 v3, s14
	s_waitcnt vmcnt(6) lgkmcnt(0)
	v_lshlrev_b16 v22, 8, v2
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v2, 0xffff, v12
	s_waitcnt vmcnt(4)
	v_and_b32_e32 v12, 0xffff, v16
	flat_load_d16_hi_u8 v21, v[5:6] offset:6
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v16, v22, v17
	v_mov_b32_e32 v13, s14
	v_lshlrev_b64 v[2:3], 16, v[2:3]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v17, 8, v18
	v_add_nc_u32_e32 v18, -8, v9
	v_and_b32_e32 v16, 0xffff, v16
	v_lshlrev_b64 v[12:13], 24, v[12:13]
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or3_b32 v3, 0, v3, v13
	v_or3_b32 v2, v16, v2, v12
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v12, 24, v20
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_or3_b32 v3, v3, v19, v17
	v_or3_b32 v2, v2, 0, 0
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_3)
	v_or3_b32 v2, v2, 0, 0
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_or3_b32 v3, v3, v21, v12
	v_add_co_u32 v12, vcc_lo, v5, 8
	v_add_co_ci_u32_e32 v13, vcc_lo, 0, v6, vcc_lo
.LBB3_297:                              ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $vgpr16_vgpr17
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v18
	s_xor_b32 s6, exec_lo, s0
	s_cbranch_execz .LBB3_303
; %bb.298:                              ;   in Loop: Header=BB3_289 Depth=1
	v_mov_b32_e32 v16, 0
	v_mov_b32_e32 v17, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s7, exec_lo
	v_cmpx_ne_u32_e32 0, v18
	s_cbranch_execz .LBB3_302
; %bb.299:                              ; %.preheader21
                                        ;   in Loop: Header=BB3_289 Depth=1
	v_mov_b32_e32 v16, 0
	v_mov_b32_e32 v17, 0
	s_mov_b32 s10, 0
	s_mov_b64 s[4:5], 0
	.p2align	6
.LBB3_300:                              ;   Parent Loop BB3_289 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_add_co_u32 v19, vcc_lo, v12, s4
	v_add_co_ci_u32_e32 v20, vcc_lo, s5, v13, vcc_lo
	s_add_u32 s4, s4, 1
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e32 vcc_lo, s4, v18
	flat_load_u8 v19, v[19:20]
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_dual_mov_b32 v20, s14 :: v_dual_and_b32 v19, 0xffff, v19
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[19:20], s0, v[19:20]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s10, vcc_lo, s10
	v_or_b32_e32 v17, v20, v17
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v16, v19, v16
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_300
; %bb.301:                              ; %Flow488
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s10
.LBB3_302:                              ; %Flow490
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s7
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr18
.LBB3_303:                              ; %Flow492
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_saveexec_b32 s0, s6
	v_mov_b32_e32 v20, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_305
; %bb.304:                              ;   in Loop: Header=BB3_289 Depth=1
	s_clause 0x6
	flat_load_u8 v16, v[12:13] offset:1
	flat_load_u8 v19, v[12:13] offset:2
	flat_load_u8 v21, v[12:13] offset:3
	flat_load_u8 v22, v[12:13]
	flat_load_u8 v23, v[12:13] offset:5
	flat_load_u8 v24, v[12:13] offset:4
	flat_load_u8 v25, v[12:13] offset:7
	v_dual_mov_b32 v26, v35 :: v_dual_mov_b32 v17, s14
	v_mov_b32_e32 v20, s14
	flat_load_d16_hi_u8 v26, v[12:13] offset:6
	v_add_co_u32 v12, vcc_lo, v12, 8
	v_add_co_ci_u32_e32 v13, vcc_lo, 0, v13, vcc_lo
	s_waitcnt vmcnt(7) lgkmcnt(0)
	v_lshlrev_b16 v27, 8, v16
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v16, 0xffff, v19
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v19, 0xffff, v21
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v21, v27, v22
	v_lshlrev_b64 v[16:17], 16, v[16:17]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[19:20], 24, v[19:20]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v22, 8, v23
	v_and_b32_e32 v21, 0xffff, v21
	v_or3_b32 v17, 0, v17, v20
	v_add_nc_u32_e32 v20, -8, v18
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_or3_b32 v16, v21, v16, v19
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v19, 24, v25
	v_or3_b32 v17, v17, v24, v22
	v_or3_b32 v16, v16, 0, 0
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or3_b32 v17, v17, v26, v19
	v_or3_b32 v16, v16, 0, 0
.LBB3_305:                              ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v20
	s_xor_b32 s6, exec_lo, s0
	s_cbranch_execz .LBB3_311
; %bb.306:                              ;   in Loop: Header=BB3_289 Depth=1
	v_mov_b32_e32 v18, 0
	v_mov_b32_e32 v19, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s7, exec_lo
	v_cmpx_ne_u32_e32 0, v20
	s_cbranch_execz .LBB3_310
; %bb.307:                              ; %.preheader19
                                        ;   in Loop: Header=BB3_289 Depth=1
	v_mov_b32_e32 v18, 0
	v_mov_b32_e32 v19, 0
	s_mov_b32 s10, 0
	s_mov_b64 s[4:5], 0
	.p2align	6
.LBB3_308:                              ;   Parent Loop BB3_289 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_add_co_u32 v21, vcc_lo, v12, s4
	v_add_co_ci_u32_e32 v22, vcc_lo, s5, v13, vcc_lo
	s_add_u32 s4, s4, 1
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e32 vcc_lo, s4, v20
	flat_load_u8 v21, v[21:22]
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_dual_mov_b32 v22, s14 :: v_dual_and_b32 v21, 0xffff, v21
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[21:22], s0, v[21:22]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s10, vcc_lo, s10
	v_or_b32_e32 v19, v22, v19
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v18, v21, v18
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_308
; %bb.309:                              ; %Flow483
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s10
.LBB3_310:                              ; %Flow485
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s7
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr20
.LBB3_311:                              ; %Flow487
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_saveexec_b32 s0, s6
	v_mov_b32_e32 v22, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_313
; %bb.312:                              ;   in Loop: Header=BB3_289 Depth=1
	s_clause 0x6
	flat_load_u8 v18, v[12:13] offset:1
	flat_load_u8 v21, v[12:13] offset:2
	flat_load_u8 v23, v[12:13] offset:3
	flat_load_u8 v24, v[12:13]
	flat_load_u8 v25, v[12:13] offset:5
	flat_load_u8 v26, v[12:13] offset:4
	flat_load_u8 v27, v[12:13] offset:7
	v_dual_mov_b32 v28, v35 :: v_dual_mov_b32 v19, s14
	v_mov_b32_e32 v22, s14
	flat_load_d16_hi_u8 v28, v[12:13] offset:6
	v_add_co_u32 v12, vcc_lo, v12, 8
	v_add_co_ci_u32_e32 v13, vcc_lo, 0, v13, vcc_lo
	s_waitcnt vmcnt(7) lgkmcnt(0)
	v_lshlrev_b16 v29, 8, v18
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v18, 0xffff, v21
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v21, 0xffff, v23
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v23, v29, v24
	v_lshlrev_b64 v[18:19], 16, v[18:19]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[21:22], 24, v[21:22]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v24, 8, v25
	v_and_b32_e32 v23, 0xffff, v23
	v_or3_b32 v19, 0, v19, v22
	v_add_nc_u32_e32 v22, -8, v20
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_or3_b32 v18, v23, v18, v21
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v21, 24, v27
	v_or3_b32 v19, v19, v26, v24
	v_or3_b32 v18, v18, 0, 0
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or3_b32 v19, v19, v28, v21
	v_or3_b32 v18, v18, 0, 0
.LBB3_313:                              ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $vgpr20_vgpr21
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v22
	s_xor_b32 s6, exec_lo, s0
	s_cbranch_execz .LBB3_319
; %bb.314:                              ;   in Loop: Header=BB3_289 Depth=1
	v_mov_b32_e32 v20, 0
	v_mov_b32_e32 v21, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s7, exec_lo
	v_cmpx_ne_u32_e32 0, v22
	s_cbranch_execz .LBB3_318
; %bb.315:                              ; %.preheader17
                                        ;   in Loop: Header=BB3_289 Depth=1
	v_mov_b32_e32 v20, 0
	v_mov_b32_e32 v21, 0
	s_mov_b32 s10, 0
	s_mov_b64 s[4:5], 0
	.p2align	6
.LBB3_316:                              ;   Parent Loop BB3_289 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_add_co_u32 v23, vcc_lo, v12, s4
	v_add_co_ci_u32_e32 v24, vcc_lo, s5, v13, vcc_lo
	s_add_u32 s4, s4, 1
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e32 vcc_lo, s4, v22
	flat_load_u8 v23, v[23:24]
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_dual_mov_b32 v24, s14 :: v_dual_and_b32 v23, 0xffff, v23
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[23:24], s0, v[23:24]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s10, vcc_lo, s10
	v_or_b32_e32 v21, v24, v21
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v20, v23, v20
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_316
; %bb.317:                              ; %Flow478
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s10
.LBB3_318:                              ; %Flow480
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s7
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr22
.LBB3_319:                              ; %Flow482
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_saveexec_b32 s0, s6
	v_mov_b32_e32 v24, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_321
; %bb.320:                              ;   in Loop: Header=BB3_289 Depth=1
	s_clause 0x6
	flat_load_u8 v20, v[12:13] offset:1
	flat_load_u8 v23, v[12:13] offset:2
	flat_load_u8 v25, v[12:13] offset:3
	flat_load_u8 v26, v[12:13]
	flat_load_u8 v27, v[12:13] offset:5
	flat_load_u8 v28, v[12:13] offset:4
	flat_load_u8 v29, v[12:13] offset:7
	v_dual_mov_b32 v30, v35 :: v_dual_mov_b32 v21, s14
	v_mov_b32_e32 v24, s14
	flat_load_d16_hi_u8 v30, v[12:13] offset:6
	v_add_co_u32 v12, vcc_lo, v12, 8
	v_add_co_ci_u32_e32 v13, vcc_lo, 0, v13, vcc_lo
	s_waitcnt vmcnt(7) lgkmcnt(0)
	v_lshlrev_b16 v31, 8, v20
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v20, 0xffff, v23
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v23, 0xffff, v25
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v25, v31, v26
	v_lshlrev_b64 v[20:21], 16, v[20:21]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[23:24], 24, v[23:24]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v26, 8, v27
	v_and_b32_e32 v25, 0xffff, v25
	v_or3_b32 v21, 0, v21, v24
	v_add_nc_u32_e32 v24, -8, v22
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_or3_b32 v20, v25, v20, v23
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v23, 24, v29
	v_or3_b32 v21, v21, v28, v26
	v_or3_b32 v20, v20, 0, 0
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or3_b32 v21, v21, v30, v23
	v_or3_b32 v20, v20, 0, 0
.LBB3_321:                              ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v24
	s_xor_b32 s6, exec_lo, s0
	s_cbranch_execz .LBB3_327
; %bb.322:                              ;   in Loop: Header=BB3_289 Depth=1
	v_mov_b32_e32 v22, 0
	v_mov_b32_e32 v23, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s7, exec_lo
	v_cmpx_ne_u32_e32 0, v24
	s_cbranch_execz .LBB3_326
; %bb.323:                              ; %.preheader15
                                        ;   in Loop: Header=BB3_289 Depth=1
	v_mov_b32_e32 v22, 0
	v_mov_b32_e32 v23, 0
	s_mov_b32 s10, 0
	s_mov_b64 s[4:5], 0
	.p2align	6
.LBB3_324:                              ;   Parent Loop BB3_289 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_add_co_u32 v25, vcc_lo, v12, s4
	v_add_co_ci_u32_e32 v26, vcc_lo, s5, v13, vcc_lo
	s_add_u32 s4, s4, 1
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e32 vcc_lo, s4, v24
	flat_load_u8 v25, v[25:26]
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_dual_mov_b32 v26, s14 :: v_dual_and_b32 v25, 0xffff, v25
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[25:26], s0, v[25:26]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s10, vcc_lo, s10
	v_or_b32_e32 v23, v26, v23
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v22, v25, v22
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_324
; %bb.325:                              ; %Flow473
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s10
.LBB3_326:                              ; %Flow475
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s7
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr24
.LBB3_327:                              ; %Flow477
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_saveexec_b32 s0, s6
	v_mov_b32_e32 v26, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_329
; %bb.328:                              ;   in Loop: Header=BB3_289 Depth=1
	s_clause 0x6
	flat_load_u8 v22, v[12:13] offset:1
	flat_load_u8 v25, v[12:13] offset:2
	flat_load_u8 v27, v[12:13] offset:3
	flat_load_u8 v28, v[12:13]
	flat_load_u8 v29, v[12:13] offset:5
	flat_load_u8 v30, v[12:13] offset:4
	flat_load_u8 v31, v[12:13] offset:7
	v_dual_mov_b32 v34, v35 :: v_dual_mov_b32 v23, s14
	v_mov_b32_e32 v26, s14
	flat_load_d16_hi_u8 v34, v[12:13] offset:6
	v_add_co_u32 v12, vcc_lo, v12, 8
	v_add_co_ci_u32_e32 v13, vcc_lo, 0, v13, vcc_lo
	s_waitcnt vmcnt(7) lgkmcnt(0)
	v_lshlrev_b16 v36, 8, v22
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v22, 0xffff, v25
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v25, 0xffff, v27
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v27, v36, v28
	v_lshlrev_b64 v[22:23], 16, v[22:23]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[25:26], 24, v[25:26]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v28, 8, v29
	v_and_b32_e32 v27, 0xffff, v27
	v_or3_b32 v23, 0, v23, v26
	v_add_nc_u32_e32 v26, -8, v24
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_or3_b32 v22, v27, v22, v25
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v25, 24, v31
	v_or3_b32 v23, v23, v30, v28
	v_or3_b32 v22, v22, 0, 0
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or3_b32 v23, v23, v34, v25
	v_or3_b32 v22, v22, 0, 0
.LBB3_329:                              ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $vgpr24_vgpr25
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v26
	s_xor_b32 s6, exec_lo, s0
	s_cbranch_execz .LBB3_335
; %bb.330:                              ;   in Loop: Header=BB3_289 Depth=1
	v_mov_b32_e32 v24, 0
	v_mov_b32_e32 v25, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s7, exec_lo
	v_cmpx_ne_u32_e32 0, v26
	s_cbranch_execz .LBB3_334
; %bb.331:                              ; %.preheader13
                                        ;   in Loop: Header=BB3_289 Depth=1
	v_mov_b32_e32 v24, 0
	v_mov_b32_e32 v25, 0
	s_mov_b32 s10, 0
	s_mov_b64 s[4:5], 0
	.p2align	6
.LBB3_332:                              ;   Parent Loop BB3_289 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_add_co_u32 v27, vcc_lo, v12, s4
	v_add_co_ci_u32_e32 v28, vcc_lo, s5, v13, vcc_lo
	s_add_u32 s4, s4, 1
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e32 vcc_lo, s4, v26
	flat_load_u8 v27, v[27:28]
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_dual_mov_b32 v28, s14 :: v_dual_and_b32 v27, 0xffff, v27
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[27:28], s0, v[27:28]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s10, vcc_lo, s10
	v_or_b32_e32 v25, v28, v25
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v24, v27, v24
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_332
; %bb.333:                              ; %Flow468
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s10
.LBB3_334:                              ; %Flow470
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s7
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr26
.LBB3_335:                              ; %Flow472
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_saveexec_b32 s0, s6
	v_mov_b32_e32 v28, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB3_337
; %bb.336:                              ;   in Loop: Header=BB3_289 Depth=1
	s_clause 0x6
	flat_load_u8 v24, v[12:13] offset:1
	flat_load_u8 v27, v[12:13] offset:2
	flat_load_u8 v29, v[12:13] offset:3
	flat_load_u8 v30, v[12:13]
	flat_load_u8 v31, v[12:13] offset:5
	flat_load_u8 v34, v[12:13] offset:4
	flat_load_u8 v36, v[12:13] offset:7
	v_dual_mov_b32 v38, v35 :: v_dual_mov_b32 v25, s14
	v_mov_b32_e32 v28, s14
	flat_load_d16_hi_u8 v38, v[12:13] offset:6
	v_add_co_u32 v12, vcc_lo, v12, 8
	v_add_co_ci_u32_e32 v13, vcc_lo, 0, v13, vcc_lo
	s_waitcnt vmcnt(7) lgkmcnt(0)
	v_lshlrev_b16 v39, 8, v24
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v24, 0xffff, v27
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v27, 0xffff, v29
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v29, v39, v30
	v_lshlrev_b64 v[24:25], 16, v[24:25]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[27:28], 24, v[27:28]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v30, 8, v31
	v_and_b32_e32 v29, 0xffff, v29
	v_or3_b32 v25, 0, v25, v28
	v_add_nc_u32_e32 v28, -8, v26
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_or3_b32 v24, v29, v24, v27
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v27, 24, v36
	v_or3_b32 v25, v25, v34, v30
	v_or3_b32 v24, v24, 0, 0
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or3_b32 v25, v25, v38, v27
	v_or3_b32 v24, v24, 0, 0
.LBB3_337:                              ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v28
	s_xor_b32 s4, exec_lo, s0
	s_cbranch_execz .LBB3_343
; %bb.338:                              ;   in Loop: Header=BB3_289 Depth=1
	v_mov_b32_e32 v26, 0
	v_mov_b32_e32 v27, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s5, exec_lo
	v_cmpx_ne_u32_e32 0, v28
	s_cbranch_execz .LBB3_342
; %bb.339:                              ; %.preheader11
                                        ;   in Loop: Header=BB3_289 Depth=1
	v_mov_b32_e32 v26, 0
	v_mov_b32_e32 v27, 0
	s_mov_b32 s6, 0
	.p2align	6
.LBB3_340:                              ;   Parent Loop BB3_289 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	flat_load_u8 v29, v[12:13]
	v_mov_b32_e32 v30, s14
	v_add_nc_u32_e32 v28, -1, v28
	v_add_co_u32 v12, vcc_lo, v12, 1
	v_add_co_ci_u32_e32 v13, vcc_lo, 0, v13, vcc_lo
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_2) | instid1(VALU_DEP_1)
	v_cmp_eq_u32_e32 vcc_lo, 0, v28
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_and_b32_e32 v29, 0xffff, v29
	v_lshlrev_b64 v[29:30], s0, v[29:30]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s6, vcc_lo, s6
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or_b32_e32 v27, v30, v27
	v_or_b32_e32 v26, v29, v26
	s_and_not1_b32 exec_lo, exec_lo, s6
	s_cbranch_execnz .LBB3_340
; %bb.341:                              ; %Flow463
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
.LBB3_342:                              ; %Flow465
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s5
                                        ; implicit-def: $vgpr12_vgpr13
.LBB3_343:                              ; %Flow467
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_and_not1_saveexec_b32 s0, s4
	s_cbranch_execz .LBB3_345
; %bb.344:                              ;   in Loop: Header=BB3_289 Depth=1
	s_clause 0x5
	flat_load_u8 v26, v[12:13] offset:1
	flat_load_u8 v28, v[12:13] offset:2
	flat_load_u8 v29, v[12:13] offset:3
	flat_load_u8 v30, v[12:13]
	flat_load_u8 v31, v[12:13] offset:5
	flat_load_u8 v34, v[12:13] offset:4
	v_dual_mov_b32 v36, v35 :: v_dual_mov_b32 v27, s14
	s_clause 0x1
	flat_load_u8 v38, v[12:13] offset:7
	flat_load_d16_hi_u8 v36, v[12:13] offset:6
	v_mov_b32_e32 v13, s14
	s_waitcnt vmcnt(7) lgkmcnt(0)
	v_lshlrev_b16 v39, 8, v26
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v12, 0xffff, v28
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v26, 0xffff, v29
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v28, v39, v30
	v_lshlrev_b64 v[12:13], 16, v[12:13]
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[26:27], 24, v[26:27]
	v_and_b32_e32 v28, 0xffff, v28
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v13, 0, v13, v27
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v27, 8, v31
	v_or3_b32 v12, v28, v12, v26
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v26, 24, v38
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_or3_b32 v13, v13, v34, v27
	v_or3_b32 v12, v12, 0, 0
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or3_b32 v27, v13, v36, v26
	v_or3_b32 v26, v12, 0, 0
.LBB3_345:                              ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
	v_mov_b32_e32 v34, v11
	v_mov_b32_e32 v12, 0
	v_mov_b32_e32 v13, 0
	;;#ASMSTART
	;;#ASMEND
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_readfirstlane_b32 s0, v34
	v_cmp_eq_u32_e64 s0, s0, v34
	s_delay_alu instid0(VALU_DEP_1)
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_351
; %bb.346:                              ;   in Loop: Header=BB3_289 Depth=1
	global_load_b64 v[30:31], v35, s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	s_clause 0x1
	global_load_b64 v[12:13], v35, s[2:3] offset:40
	global_load_b64 v[28:29], v35, s[2:3]
	s_mov_b32 s4, exec_lo
	s_waitcnt vmcnt(1)
	v_and_b32_e32 v13, v13, v31
	v_and_b32_e32 v12, v12, v30
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_mul_lo_u32 v13, v13, 24
	v_mul_hi_u32 v36, v12, 24
	v_mul_lo_u32 v12, v12, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_add_nc_u32_e32 v13, v36, v13
	s_waitcnt vmcnt(0)
	v_add_co_u32 v12, vcc_lo, v28, v12
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_ci_u32_e32 v13, vcc_lo, v29, v13, vcc_lo
	global_load_b64 v[28:29], v[12:13], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[12:13], v35, v[28:31], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmpx_ne_u64_e64 v[12:13], v[30:31]
	s_cbranch_execz .LBB3_350
; %bb.347:                              ; %.preheader9
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_mov_b32 s5, 0
                                        ; implicit-def: $sgpr6
	.p2align	6
.LBB3_348:                              ;   Parent Loop BB3_289 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_sleep 1
	s_clause 0x1
	global_load_b64 v[28:29], v35, s[2:3] offset:40
	global_load_b64 v[38:39], v35, s[2:3]
	v_dual_mov_b32 v31, v13 :: v_dual_mov_b32 v30, v12
	s_waitcnt vmcnt(1)
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_and_b32_e32 v28, v28, v30
	v_and_b32_e32 v36, v29, v31
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_mad_u64_u32 v[12:13], null, v28, 24, v[38:39]
	v_mad_u64_u32 v[28:29], null, v36, 24, v[13:14]
	s_delay_alu instid0(VALU_DEP_1)
	v_mov_b32_e32 v13, v28
	global_load_b64 v[28:29], v[12:13], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[12:13], v35, v[28:31], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmp_eq_u64_e32 vcc_lo, v[12:13], v[30:31]
	s_or_b32 s5, vcc_lo, s5
	s_and_not1_b32 s6, s6, exec_lo
	s_and_b32 s7, vcc_lo, exec_lo
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 s6, s6, s7
	s_and_not1_b32 exec_lo, exec_lo, s5
	s_cbranch_execnz .LBB3_348
; %bb.349:                              ; %Flow459
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s5
.LBB3_350:                              ; %Flow461
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s4
.LBB3_351:                              ; %Flow462
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s1
	s_clause 0x1
	global_load_b64 v[38:39], v35, s[2:3] offset:40
	global_load_b128 v[28:31], v35, s[2:3]
	v_readfirstlane_b32 s4, v12
	v_readfirstlane_b32 s5, v13
	s_mov_b64 s[10:11], exec
	s_waitcnt vmcnt(1)
	v_readfirstlane_b32 s6, v38
	v_readfirstlane_b32 s7, v39
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[6:7], s[4:5], s[6:7]
	s_mul_i32 s1, s7, 24
	s_mul_hi_u32 s15, s6, 24
	s_mul_i32 s16, s6, 24
	s_and_saveexec_b32 s17, s0
	s_cbranch_execz .LBB3_353
; %bb.352:                              ;   in Loop: Header=BB3_289 Depth=1
	s_add_i32 s18, s15, s1
	s_waitcnt vmcnt(0)
	v_add_co_u32 v38, vcc_lo, v28, s16
	v_add_co_ci_u32_e32 v39, vcc_lo, s18, v29, vcc_lo
	v_dual_mov_b32 v13, s11 :: v_dual_mov_b32 v12, s10
	global_store_b128 v[38:39], v[12:15], off offset:8
.LBB3_353:                              ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s17
	v_cmp_lt_u64_e32 vcc_lo, 56, v[32:33]
	v_or_b32_e32 v12, 0, v1
	v_or_b32_e32 v13, v0, v4
	v_lshl_add_u32 v36, v9, 2, 28
	s_lshl_b64 s[6:7], s[6:7], 12
	s_delay_alu instid0(VALU_DEP_2)
	v_dual_cndmask_b32 v1, v12, v1 :: v_dual_cndmask_b32 v0, v13, v0
	v_lshlrev_b64 v[12:13], 6, v[34:35]
	s_waitcnt vmcnt(0)
	v_add_co_u32 v30, vcc_lo, v30, s6
	v_and_b32_e32 v36, 0x1e0, v36
	v_add_co_ci_u32_e32 v31, vcc_lo, s7, v31, vcc_lo
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_add_co_u32 v12, vcc_lo, v30, v12
	v_and_or_b32 v0, 0xffffff1f, v0, v36
	s_delay_alu instid0(VALU_DEP_3)
	v_add_co_ci_u32_e32 v13, vcc_lo, v31, v13, vcc_lo
	s_clause 0x3
	global_store_b128 v[12:13], v[0:3], off
	global_store_b128 v[12:13], v[16:19], off offset:16
	global_store_b128 v[12:13], v[20:23], off offset:32
	global_store_b128 v[12:13], v[24:27], off offset:48
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB3_361
; %bb.354:                              ;   in Loop: Header=BB3_289 Depth=1
	s_clause 0x1
	global_load_b64 v[20:21], v35, s[2:3] offset:32 glc
	global_load_b64 v[0:1], v35, s[2:3] offset:40
	v_dual_mov_b32 v18, s4 :: v_dual_mov_b32 v19, s5
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s10, v0
	v_readfirstlane_b32 s11, v1
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[10:11], s[10:11], s[4:5]
	s_mul_i32 s7, s11, 24
	s_mul_hi_u32 s11, s10, 24
	s_mul_i32 s10, s10, 24
	s_add_i32 s11, s11, s7
	v_add_co_u32 v16, vcc_lo, v28, s10
	v_add_co_ci_u32_e32 v17, vcc_lo, s11, v29, vcc_lo
	s_mov_b32 s7, exec_lo
	global_store_b64 v[16:17], v[20:21], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[2:3], v35, v[18:21], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmpx_ne_u64_e64 v[2:3], v[20:21]
	s_cbranch_execz .LBB3_357
; %bb.355:                              ; %.preheader7
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_mov_b32 s10, 0
.LBB3_356:                              ;   Parent Loop BB3_289 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	v_dual_mov_b32 v0, s4 :: v_dual_mov_b32 v1, s5
	s_sleep 1
	global_store_b64 v[16:17], v[2:3], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[0:1], v35, v[0:3], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[0:1], v[2:3]
	v_dual_mov_b32 v3, v1 :: v_dual_mov_b32 v2, v0
	s_or_b32 s10, vcc_lo, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_356
.LBB3_357:                              ; %Flow457
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s7
	global_load_b64 v[0:1], v35, s[2:3] offset:16
	s_mov_b32 s10, exec_lo
	s_mov_b32 s7, exec_lo
	v_mbcnt_lo_u32_b32 v2, s10, 0
	s_delay_alu instid0(VALU_DEP_1)
	v_cmpx_eq_u32_e32 0, v2
	s_cbranch_execz .LBB3_359
; %bb.358:                              ;   in Loop: Header=BB3_289 Depth=1
	s_bcnt1_i32_b32 s10, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	v_mov_b32_e32 v34, s10
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_add_u64 v[0:1], v[34:35], off offset:8
.LBB3_359:                              ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s7
	s_waitcnt vmcnt(0)
	global_load_b64 v[2:3], v[0:1], off offset:16
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[2:3]
	s_cbranch_vccnz .LBB3_361
; %bb.360:                              ;   in Loop: Header=BB3_289 Depth=1
	global_load_b32 v34, v[0:1], off offset:24
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s7, v34
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_store_b64 v[2:3], v[34:35], off
	s_and_b32 m0, s7, 0xff
	s_sendmsg sendmsg(MSG_INTERRUPT)
.LBB3_361:                              ; %Flow458
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
	s_add_i32 s15, s15, s1
	v_add_co_u32 v0, vcc_lo, v28, s16
	v_add_co_ci_u32_e32 v1, vcc_lo, s15, v29, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v0, vcc_lo, v0, 20
	v_add_co_ci_u32_e32 v1, vcc_lo, 0, v1, vcc_lo
	s_branch .LBB3_365
	.p2align	6
.LBB3_362:                              ;   in Loop: Header=BB3_365 Depth=2
	s_or_b32 exec_lo, exec_lo, s1
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_readfirstlane_b32 s1, v2
	s_cmp_eq_u32 s1, 0
	s_cbranch_scc1 .LBB3_364
; %bb.363:                              ;   in Loop: Header=BB3_365 Depth=2
	s_sleep 1
	s_cbranch_execnz .LBB3_365
	s_branch .LBB3_367
	.p2align	6
.LBB3_364:                              ;   in Loop: Header=BB3_289 Depth=1
	s_branch .LBB3_367
.LBB3_365:                              ;   Parent Loop BB3_289 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	v_mov_b32_e32 v2, 1
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_362
; %bb.366:                              ;   in Loop: Header=BB3_365 Depth=2
	global_load_b32 v2, v[0:1], off glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_and_b32_e32 v2, 1, v2
	s_branch .LBB3_362
.LBB3_367:                              ;   in Loop: Header=BB3_289 Depth=1
	global_load_b128 v[0:3], v[12:13], off
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB3_288
; %bb.368:                              ;   in Loop: Header=BB3_289 Depth=1
	s_clause 0x2
	global_load_b64 v[2:3], v35, s[2:3] offset:40
	global_load_b64 v[12:13], v35, s[2:3] offset:24 glc
	global_load_b64 v[18:19], v35, s[2:3]
	s_waitcnt vmcnt(2)
	v_add_co_u32 v20, vcc_lo, v2, 1
	v_add_co_ci_u32_e32 v21, vcc_lo, 0, v3, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v16, vcc_lo, v20, s4
	v_add_co_ci_u32_e32 v17, vcc_lo, s5, v21, vcc_lo
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[16:17]
	v_dual_cndmask_b32 v17, v17, v21 :: v_dual_cndmask_b32 v16, v16, v20
	v_and_b32_e32 v3, v17, v3
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_and_b32_e32 v2, v16, v2
	v_mul_hi_u32 v20, v2, 24
	v_mul_lo_u32 v2, v2, 24
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_2) | instid1(VALU_DEP_1)
	v_add_co_u32 v2, vcc_lo, v18, v2
	v_mov_b32_e32 v18, v12
	v_mul_lo_u32 v3, v3, 24
	v_add_nc_u32_e32 v3, v20, v3
	s_delay_alu instid0(VALU_DEP_1)
	v_add_co_ci_u32_e32 v3, vcc_lo, v19, v3, vcc_lo
	v_mov_b32_e32 v19, v13
	global_store_b64 v[2:3], v[12:13], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[18:19], v35, v[16:19], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_ne_u64_e32 vcc_lo, v[18:19], v[12:13]
	s_and_b32 exec_lo, exec_lo, vcc_lo
	s_cbranch_execz .LBB3_288
; %bb.369:                              ; %.preheader5
                                        ;   in Loop: Header=BB3_289 Depth=1
	s_mov_b32 s0, 0
.LBB3_370:                              ;   Parent Loop BB3_289 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_sleep 1
	global_store_b64 v[2:3], v[18:19], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[12:13], v35, v[16:19], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[12:13], v[18:19]
	v_dual_mov_b32 v19, v13 :: v_dual_mov_b32 v18, v12
	s_or_b32 s0, vcc_lo, s0
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s0
	s_cbranch_execnz .LBB3_370
	s_branch .LBB3_288
.LBB3_371:                              ; %Flow498
	s_or_b32 exec_lo, exec_lo, s13
                                        ; implicit-def: $vgpr9_vgpr10
.LBB3_372:                              ; %Flow516
	s_and_not1_saveexec_b32 s1, s12
	s_cbranch_execz .LBB3_400
; %bb.373:
	;;#ASMSTART
	;;#ASMEND
	v_readfirstlane_b32 s0, v11
	v_mov_b32_e32 v4, 0
	v_mov_b32_e32 v5, 0
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_cmp_eq_u32_e64 s0, s0, v11
	s_and_saveexec_b32 s4, s0
	s_cbranch_execz .LBB3_379
; %bb.374:
	s_waitcnt vmcnt(0)
	v_mov_b32_e32 v0, 0
	s_mov_b32 s5, exec_lo
	global_load_b64 v[14:15], v0, s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	s_clause 0x1
	global_load_b64 v[1:2], v0, s[2:3] offset:40
	global_load_b64 v[3:4], v0, s[2:3]
	s_waitcnt vmcnt(1)
	v_and_b32_e32 v1, v1, v14
	v_and_b32_e32 v2, v2, v15
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_mul_hi_u32 v5, v1, 24
	v_mul_lo_u32 v2, v2, 24
	v_mul_lo_u32 v1, v1, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_add_nc_u32_e32 v2, v5, v2
	s_waitcnt vmcnt(0)
	v_add_co_u32 v1, vcc_lo, v3, v1
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_ci_u32_e32 v2, vcc_lo, v4, v2, vcc_lo
	global_load_b64 v[12:13], v[1:2], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[4:5], v0, v[12:15], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmpx_ne_u64_e64 v[4:5], v[14:15]
	s_cbranch_execz .LBB3_378
; %bb.375:                              ; %.preheader3
	s_mov_b32 s6, 0
                                        ; implicit-def: $sgpr7
	.p2align	6
.LBB3_376:                              ; =>This Inner Loop Header: Depth=1
	s_sleep 1
	s_clause 0x1
	global_load_b64 v[1:2], v0, s[2:3] offset:40
	global_load_b64 v[12:13], v0, s[2:3]
	v_dual_mov_b32 v15, v5 :: v_dual_mov_b32 v14, v4
	s_waitcnt vmcnt(1)
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_and_b32_e32 v1, v1, v14
	s_waitcnt vmcnt(0)
	v_mad_u64_u32 v[3:4], null, v1, 24, v[12:13]
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_dual_mov_b32 v1, v4 :: v_dual_and_b32 v2, v2, v15
	v_mad_u64_u32 v[4:5], null, v2, 24, v[1:2]
	global_load_b64 v[12:13], v[3:4], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[4:5], v0, v[12:15], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmp_eq_u64_e32 vcc_lo, v[4:5], v[14:15]
	s_or_b32 s6, vcc_lo, s6
	s_and_not1_b32 s7, s7, exec_lo
	s_and_b32 s10, vcc_lo, exec_lo
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 s7, s7, s10
	s_and_not1_b32 exec_lo, exec_lo, s6
	s_cbranch_execnz .LBB3_376
; %bb.377:                              ; %Flow511
	s_or_b32 exec_lo, exec_lo, s6
.LBB3_378:                              ; %Flow513
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s5
.LBB3_379:                              ; %Flow514
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s4
	v_mov_b32_e32 v12, 0
	v_readfirstlane_b32 s4, v4
	v_readfirstlane_b32 s5, v5
	s_mov_b64 s[6:7], exec
	s_clause 0x1
	global_load_b64 v[13:14], v12, s[2:3] offset:40
	global_load_b128 v[0:3], v12, s[2:3]
	s_waitcnt vmcnt(1)
	v_readfirstlane_b32 s10, v13
	v_readfirstlane_b32 s11, v14
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[10:11], s[4:5], s[10:11]
	s_mul_i32 s12, s11, 24
	s_mul_hi_u32 s13, s10, 24
	s_mul_i32 s14, s10, 24
	s_and_saveexec_b32 s15, s0
	s_cbranch_execz .LBB3_381
; %bb.380:
	s_add_i32 s16, s13, s12
	s_waitcnt vmcnt(0)
	v_add_co_u32 v4, vcc_lo, v0, s14
	v_add_co_ci_u32_e32 v5, vcc_lo, s16, v1, vcc_lo
	v_dual_mov_b32 v14, s7 :: v_dual_mov_b32 v13, s6
	v_dual_mov_b32 v15, 2 :: v_dual_mov_b32 v16, 1
	global_store_b128 v[4:5], v[13:16], off offset:8
.LBB3_381:
	s_or_b32 exec_lo, exec_lo, s15
	s_lshl_b64 s[6:7], s[10:11], 12
	v_lshlrev_b64 v[4:5], 6, v[11:12]
	s_waitcnt vmcnt(0)
	v_add_co_u32 v2, vcc_lo, v2, s6
	v_add_co_ci_u32_e32 v3, vcc_lo, s7, v3, vcc_lo
	s_mov_b32 s16, 0
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_add_co_u32 v13, vcc_lo, v2, v4
	s_mov_b32 s17, s16
	v_add_co_ci_u32_e32 v14, vcc_lo, v3, v5, vcc_lo
	s_mov_b32 s18, s16
	s_mov_b32 s19, s16
	v_dual_mov_b32 v11, v12 :: v_dual_mov_b32 v2, s16
	v_and_or_b32 v9, 0xffffff1f, v9, 32
	v_dual_mov_b32 v3, s17 :: v_dual_mov_b32 v4, s18
	v_mov_b32_e32 v5, s19
	s_clause 0x3
	global_store_b128 v[13:14], v[9:12], off
	global_store_b128 v[13:14], v[2:5], off offset:16
	global_store_b128 v[13:14], v[2:5], off offset:32
	global_store_b128 v[13:14], v[2:5], off offset:48
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB3_389
; %bb.382:
	v_dual_mov_b32 v6, 0 :: v_dual_mov_b32 v15, s4
	v_mov_b32_e32 v16, s5
	s_clause 0x1
	global_load_b64 v[17:18], v6, s[2:3] offset:32 glc
	global_load_b64 v[2:3], v6, s[2:3] offset:40
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s10, v2
	v_readfirstlane_b32 s11, v3
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[10:11], s[10:11], s[4:5]
	s_mul_i32 s7, s11, 24
	s_mul_hi_u32 s11, s10, 24
	s_mul_i32 s10, s10, 24
	s_add_i32 s11, s11, s7
	v_add_co_u32 v9, vcc_lo, v0, s10
	v_add_co_ci_u32_e32 v10, vcc_lo, s11, v1, vcc_lo
	s_mov_b32 s7, exec_lo
	global_store_b64 v[9:10], v[17:18], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[4:5], v6, v[15:18], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmpx_ne_u64_e64 v[4:5], v[17:18]
	s_cbranch_execz .LBB3_385
; %bb.383:                              ; %.preheader1
	s_mov_b32 s10, 0
.LBB3_384:                              ; =>This Inner Loop Header: Depth=1
	v_dual_mov_b32 v2, s4 :: v_dual_mov_b32 v3, s5
	s_sleep 1
	global_store_b64 v[9:10], v[4:5], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[2:3], v6, v[2:5], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[2:3], v[4:5]
	v_dual_mov_b32 v5, v3 :: v_dual_mov_b32 v4, v2
	s_or_b32 s10, vcc_lo, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB3_384
.LBB3_385:                              ; %Flow509
	s_or_b32 exec_lo, exec_lo, s7
	v_mov_b32_e32 v5, 0
	s_mov_b32 s10, exec_lo
	s_mov_b32 s7, exec_lo
	v_mbcnt_lo_u32_b32 v4, s10, 0
	global_load_b64 v[2:3], v5, s[2:3] offset:16
	v_cmpx_eq_u32_e32 0, v4
	s_cbranch_execz .LBB3_387
; %bb.386:
	s_bcnt1_i32_b32 s10, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	v_mov_b32_e32 v4, s10
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_add_u64 v[2:3], v[4:5], off offset:8
.LBB3_387:
	s_or_b32 exec_lo, exec_lo, s7
	s_waitcnt vmcnt(0)
	global_load_b64 v[4:5], v[2:3], off offset:16
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[4:5]
	s_cbranch_vccnz .LBB3_389
; %bb.388:
	global_load_b32 v2, v[2:3], off offset:24
	v_mov_b32_e32 v3, 0
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s7, v2
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_store_b64 v[4:5], v[2:3], off
	s_and_b32 m0, s7, 0xff
	s_sendmsg sendmsg(MSG_INTERRUPT)
.LBB3_389:                              ; %Flow510
	s_or_b32 exec_lo, exec_lo, s6
	s_add_i32 s13, s13, s12
	v_add_co_u32 v0, vcc_lo, v0, s14
	v_add_co_ci_u32_e32 v1, vcc_lo, s13, v1, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v0, vcc_lo, v0, 20
	v_add_co_ci_u32_e32 v1, vcc_lo, 0, v1, vcc_lo
	s_branch .LBB3_393
	.p2align	6
.LBB3_390:                              ;   in Loop: Header=BB3_393 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_readfirstlane_b32 s6, v2
	s_cmp_eq_u32 s6, 0
	s_cbranch_scc1 .LBB3_392
; %bb.391:                              ;   in Loop: Header=BB3_393 Depth=1
	s_sleep 1
	s_cbranch_execnz .LBB3_393
	s_branch .LBB3_395
	.p2align	6
.LBB3_392:
	s_branch .LBB3_395
.LBB3_393:                              ; =>This Inner Loop Header: Depth=1
	v_mov_b32_e32 v2, 1
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB3_390
; %bb.394:                              ;   in Loop: Header=BB3_393 Depth=1
	global_load_b32 v2, v[0:1], off glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_and_b32_e32 v2, 1, v2
	s_branch .LBB3_390
.LBB3_395:
	global_load_b64 v[0:1], v[13:14], off
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB3_399
; %bb.396:
	v_mov_b32_e32 v6, 0
	s_clause 0x2
	global_load_b64 v[4:5], v6, s[2:3] offset:40
	global_load_b64 v[11:12], v6, s[2:3] offset:24 glc
	global_load_b64 v[9:10], v6, s[2:3]
	s_waitcnt vmcnt(2)
	v_add_co_u32 v13, vcc_lo, v4, 1
	v_add_co_ci_u32_e32 v14, vcc_lo, 0, v5, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v2, vcc_lo, v13, s4
	v_add_co_ci_u32_e32 v3, vcc_lo, s5, v14, vcc_lo
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[2:3]
	v_dual_cndmask_b32 v3, v3, v14 :: v_dual_cndmask_b32 v2, v2, v13
	v_and_b32_e32 v5, v3, v5
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_and_b32_e32 v4, v2, v4
	v_mul_lo_u32 v5, v5, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_mul_hi_u32 v13, v4, 24
	v_mul_lo_u32 v4, v4, 24
	v_add_nc_u32_e32 v5, v13, v5
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_3)
	v_add_co_u32 v9, vcc_lo, v9, v4
	v_mov_b32_e32 v4, v11
	v_add_co_ci_u32_e32 v10, vcc_lo, v10, v5, vcc_lo
	v_mov_b32_e32 v5, v12
	global_store_b64 v[9:10], v[11:12], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[4:5], v6, v[2:5], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_ne_u64_e32 vcc_lo, v[4:5], v[11:12]
	s_and_b32 exec_lo, exec_lo, vcc_lo
	s_cbranch_execz .LBB3_399
; %bb.397:                              ; %.preheader
	s_mov_b32 s0, 0
.LBB3_398:                              ; =>This Inner Loop Header: Depth=1
	s_sleep 1
	global_store_b64 v[9:10], v[4:5], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[11:12], v6, v[2:5], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[11:12], v[4:5]
	v_dual_mov_b32 v4, v11 :: v_dual_mov_b32 v5, v12
	s_or_b32 s0, vcc_lo, s0
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s0
	s_cbranch_execnz .LBB3_398
.LBB3_399:                              ; %Flow502
	s_or_b32 exec_lo, exec_lo, s6
.LBB3_400:                              ; %Flow517
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s1
	s_waitcnt vmcnt(0)
	v_dual_mov_b32 v2, v7 :: v_dual_mov_b32 v3, v8
	s_mov_b64 s[0:1], 0
	s_mov_b32 s2, 0
.LBB3_401:                              ; =>This Inner Loop Header: Depth=1
	flat_load_u8 v4, v[2:3]
	v_add_co_u32 v5, vcc_lo, v2, 1
	v_add_co_ci_u32_e32 v6, vcc_lo, 0, v3, vcc_lo
	s_add_u32 s0, s0, 0
	s_addc_u32 s1, s1, 1
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_cmp_eq_u16_e32 vcc_lo, 0, v4
	v_dual_mov_b32 v4, s1 :: v_dual_mov_b32 v3, s0
	v_dual_mov_b32 v2, v5 :: v_dual_mov_b32 v3, v6
	s_or_b32 s2, vcc_lo, s2
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s2
	s_cbranch_execnz .LBB3_401
; %bb.402:
	s_or_b32 exec_lo, exec_lo, s2
	v_ashrrev_i32_e32 v5, 31, v4
	v_dual_mov_b32 v2, v7 :: v_dual_mov_b32 v3, v8
	v_mov_b32_e32 v6, 1
	s_getpc_b64 s[0:1]
	s_add_u32 s0, s0, __ockl_fprintf_append_string_n@rel32@lo+4
	s_addc_u32 s1, s1, __ockl_fprintf_append_string_n@rel32@hi+12
	s_delay_alu instid0(SALU_CYCLE_1)
	s_swappc_b64 s[30:31], s[0:1]
	s_trap 2
.Lfunc_end2:
	.size	__assert_fail, .Lfunc_end2-__assert_fail
                                        ; -- End function
	.section	.AMDGPU.csdata
; Function info:
; codeLenInByte = 21912
; NumSgprs: 36
; NumVgprs: 54
; ScratchSize: 64
; MemoryBound: 0
	.text
	.hidden	__assertfail                    ; -- Begin function __assertfail
	.weak	__assertfail
	.p2align	2
	.type	__assertfail,@function
__assertfail:                           ; @__assertfail
; %bb.0:
	s_waitcnt vmcnt(0) expcnt(0) lgkmcnt(0)
	s_waitcnt_vscnt null, 0x0
	s_trap 2
.Lfunc_end3:
	.size	__assertfail, .Lfunc_end3-__assertfail
                                        ; -- End function
	.section	.AMDGPU.csdata
; Function info:
; codeLenInByte = 12
; NumSgprs: 0
; NumVgprs: 0
; ScratchSize: 0
; MemoryBound: 0
	.text
	.hidden	_Z11make_float8ffffffff         ; -- Begin function _Z11make_float8ffffffff
	.globl	_Z11make_float8ffffffff
	.p2align	2
	.type	_Z11make_float8ffffffff,@function
_Z11make_float8ffffffff:                ; @_Z11make_float8ffffffff
; %bb.0:
	s_waitcnt vmcnt(0) expcnt(0) lgkmcnt(0)
	s_waitcnt_vscnt null, 0x0
	s_setpc_b64 s[30:31]
.Lfunc_end4:
	.size	_Z11make_float8ffffffff, .Lfunc_end4-_Z11make_float8ffffffff
                                        ; -- End function
	.section	.AMDGPU.csdata
; Function info:
; codeLenInByte = 12
; NumSgprs: 32
; NumVgprs: 8
; ScratchSize: 0
; MemoryBound: 0
	.text
	.protected	E_n2                    ; -- Begin function E_n2
	.globl	E_n2
	.p2align	8
	.type	E_n2,@function
E_n2:                                   ; @E_n2
; %bb.0:
	s_clause 0x1
	s_load_b128 s[4:7], s[0:1], 0x0
	s_load_b64 s[0:1], s[0:1], 0x10
	s_waitcnt lgkmcnt(0)
	s_load_b32 s2, s[6:7], 0x0
	s_load_b32 s0, s[0:1], 0x0
	s_waitcnt lgkmcnt(0)
	s_add_i32 s0, s0, s2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_dual_mov_b32 v0, 0 :: v_dual_mov_b32 v1, s0
	global_store_b32 v0, v1, s[4:5]
	s_nop 0
	s_sendmsg sendmsg(MSG_DEALLOC_VGPRS)
	s_endpgm
	.section	.rodata,#alloc
	.p2align	6, 0x0
	.amdhsa_kernel E_n2
		.amdhsa_group_segment_fixed_size 0
		.amdhsa_private_segment_fixed_size 0
		.amdhsa_kernarg_size 24
		.amdhsa_user_sgpr_count 15
		.amdhsa_user_sgpr_dispatch_ptr 0
		.amdhsa_user_sgpr_queue_ptr 0
		.amdhsa_user_sgpr_kernarg_segment_ptr 1
		.amdhsa_user_sgpr_dispatch_id 0
		.amdhsa_user_sgpr_private_segment_size 0
		.amdhsa_wavefront_size32 1
		.amdhsa_uses_dynamic_stack 0
		.amdhsa_enable_private_segment 0
		.amdhsa_system_sgpr_workgroup_id_x 1
		.amdhsa_system_sgpr_workgroup_id_y 0
		.amdhsa_system_sgpr_workgroup_id_z 0
		.amdhsa_system_sgpr_workgroup_info 0
		.amdhsa_system_vgpr_workitem_id 0
		.amdhsa_next_free_vgpr 2
		.amdhsa_next_free_sgpr 8
		.amdhsa_reserve_vcc 0
		.amdhsa_float_round_mode_32 0
		.amdhsa_float_round_mode_16_64 0
		.amdhsa_float_denorm_mode_32 3
		.amdhsa_float_denorm_mode_16_64 3
		.amdhsa_dx10_clamp 1
		.amdhsa_ieee_mode 1
		.amdhsa_fp16_overflow 0
		.amdhsa_workgroup_processor_mode 0
		.amdhsa_memory_ordered 1
		.amdhsa_forward_progress 0
		.amdhsa_shared_vgpr_count 0
		.amdhsa_exception_fp_ieee_invalid_op 0
		.amdhsa_exception_fp_denorm_src 0
		.amdhsa_exception_fp_ieee_div_zero 0
		.amdhsa_exception_fp_ieee_overflow 0
		.amdhsa_exception_fp_ieee_underflow 0
		.amdhsa_exception_fp_ieee_inexact 0
		.amdhsa_exception_int_div_zero 0
	.end_amdhsa_kernel
	.text
.Lfunc_end5:
	.size	E_n2, .Lfunc_end5-E_n2
                                        ; -- End function
	.section	.AMDGPU.csdata
; Kernel info:
; codeLenInByte = 80
; NumSgprs: 8
; NumVgprs: 2
; ScratchSize: 0
; MemoryBound: 0
; FloatMode: 240
; IeeeMode: 1
; LDSByteSize: 0 bytes/workgroup (compile time only)
; SGPRBlocks: 0
; VGPRBlocks: 0
; NumSGPRsForWavesPerEU: 8
; NumVGPRsForWavesPerEU: 2
; Occupancy: 16
; WaveLimiterHint : 1
; COMPUTE_PGM_RSRC2:SCRATCH_EN: 0
; COMPUTE_PGM_RSRC2:USER_SGPR: 15
; COMPUTE_PGM_RSRC2:TRAP_HANDLER: 0
; COMPUTE_PGM_RSRC2:TGID_X_EN: 1
; COMPUTE_PGM_RSRC2:TGID_Y_EN: 0
; COMPUTE_PGM_RSRC2:TGID_Z_EN: 0
; COMPUTE_PGM_RSRC2:TIDIG_COMP_CNT: 0
	.text
	.p2align	2                               ; -- Begin function __ockl_fprintf_append_string_n
	.type	__ockl_fprintf_append_string_n,@function
__ockl_fprintf_append_string_n:         ; @__ockl_fprintf_append_string_n
; %bb.0:
	s_waitcnt vmcnt(0) expcnt(0) lgkmcnt(0)
	s_waitcnt_vscnt null, 0x0
	v_dual_mov_b32 v8, v3 :: v_dual_mov_b32 v7, v2
	v_or_b32_e32 v2, 2, v0
	v_cmp_eq_u32_e32 vcc_lo, 0, v6
	s_mov_b32 s13, 0
	s_mov_b32 s0, exec_lo
	s_delay_alu instid0(VALU_DEP_2)
	v_cndmask_b32_e32 v10, v2, v0, vcc_lo
	v_mbcnt_lo_u32_b32 v2, -1, 0
	v_cmpx_ne_u64_e32 0, v[7:8]
	s_xor_b32 s12, exec_lo, s0
	s_cbranch_execz .LBB2_86
; %bb.1:
	s_load_b64 s[2:3], s[8:9], 0x50
	v_dual_mov_b32 v11, 2 :: v_dual_and_b32 v0, -3, v10
	v_dual_mov_b32 v14, v1 :: v_dual_and_b32 v3, 2, v10
	v_mov_b32_e32 v34, 0
	s_delay_alu instid0(VALU_DEP_3)
	v_dual_mov_b32 v12, 1 :: v_dual_mov_b32 v13, v0
	s_mov_b32 s14, 0
	s_branch .LBB2_3
.LBB2_2:                                ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s1
	v_sub_co_u32 v4, vcc_lo, v4, v0
	v_sub_co_ci_u32_e32 v5, vcc_lo, v5, v1, vcc_lo
	v_add_co_u32 v7, s0, v7, v0
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_add_co_ci_u32_e64 v8, s0, v8, v1, s0
	v_cmp_eq_u64_e32 vcc_lo, 0, v[4:5]
	s_or_b32 s14, vcc_lo, s14
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s14
	s_cbranch_execz .LBB2_85
.LBB2_3:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB2_6 Depth 2
                                        ;     Child Loop BB2_14 Depth 2
                                        ;     Child Loop BB2_22 Depth 2
                                        ;     Child Loop BB2_30 Depth 2
                                        ;     Child Loop BB2_38 Depth 2
                                        ;     Child Loop BB2_46 Depth 2
                                        ;     Child Loop BB2_54 Depth 2
                                        ;     Child Loop BB2_62 Depth 2
                                        ;     Child Loop BB2_70 Depth 2
                                        ;     Child Loop BB2_79 Depth 2
                                        ;     Child Loop BB2_84 Depth 2
	v_cmp_gt_u64_e32 vcc_lo, 56, v[4:5]
                                        ; implicit-def: $vgpr15_vgpr16
                                        ; implicit-def: $sgpr4
	s_mov_b32 s0, exec_lo
	v_dual_cndmask_b32 v1, 0, v5 :: v_dual_cndmask_b32 v0, 56, v4
	s_delay_alu instid0(VALU_DEP_1)
	v_cmpx_gt_u32_e32 8, v0
	s_xor_b32 s1, exec_lo, s0
	s_cbranch_execz .LBB2_9
; %bb.4:                                ;   in Loop: Header=BB2_3 Depth=1
	s_waitcnt vmcnt(0)
	v_mov_b32_e32 v15, 0
	v_mov_b32_e32 v16, 0
	s_mov_b64 s[4:5], 0
	s_mov_b32 s6, exec_lo
	v_cmpx_ne_u32_e32 0, v0
	s_cbranch_execz .LBB2_8
; %bb.5:                                ; %.preheader23
                                        ;   in Loop: Header=BB2_3 Depth=1
	v_lshlrev_b64 v[9:10], 3, v[0:1]
	v_dual_mov_b32 v15, 0 :: v_dual_mov_b32 v18, v8
	v_dual_mov_b32 v16, 0 :: v_dual_mov_b32 v17, v7
	s_mov_b32 s7, 0
	.p2align	6
.LBB2_6:                                ;   Parent Loop BB2_3 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	flat_load_u8 v6, v[17:18]
	v_mov_b32_e32 v20, s13
	v_add_co_u32 v17, vcc_lo, v17, 1
	v_add_co_ci_u32_e32 v18, vcc_lo, 0, v18, vcc_lo
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_and_b32_e32 v19, 0xffff, v6
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_2)
	v_lshlrev_b64 v[19:20], s4, v[19:20]
	s_add_u32 s4, s4, 8
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e64 s0, s4, v9
	v_or_b32_e32 v16, v20, v16
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_or_b32_e32 v15, v19, v15
	s_or_b32 s7, s0, s7
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s7
	s_cbranch_execnz .LBB2_6
; %bb.7:                                ; %Flow167
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s7
.LBB2_8:                                ; %Flow169
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s6
	s_mov_b32 s4, 0
.LBB2_9:                                ; %Flow171
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_saveexec_b32 s0, s1
	v_mov_b32_e32 v10, v8
	v_dual_mov_b32 v6, s4 :: v_dual_mov_b32 v9, v7
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB2_11
; %bb.10:                               ;   in Loop: Header=BB2_3 Depth=1
	s_clause 0x1
	flat_load_u8 v6, v[7:8] offset:1
	flat_load_u8 v9, v[7:8] offset:2
	s_waitcnt vmcnt(2)
	s_clause 0x4
	flat_load_u8 v15, v[7:8] offset:3
	flat_load_u8 v17, v[7:8]
	flat_load_u8 v18, v[7:8] offset:5
	flat_load_u8 v19, v[7:8] offset:4
	flat_load_u8 v20, v[7:8] offset:7
	v_dual_mov_b32 v21, v34 :: v_dual_mov_b32 v10, s13
	v_mov_b32_e32 v16, s13
	flat_load_d16_hi_u8 v21, v[7:8] offset:6
	s_waitcnt vmcnt(7) lgkmcnt(0)
	v_lshlrev_b16 v6, 8, v6
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v9, 0xffff, v9
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v15, 0xffff, v15
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v6, v6, v17
	v_lshlrev_b64 v[9:10], 16, v[9:10]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[15:16], 24, v[15:16]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v17, 8, v18
	v_and_b32_e32 v6, 0xffff, v6
	v_or3_b32 v10, 0, v10, v16
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v6, v6, v9, v15
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v9, 24, v20
	v_or3_b32 v10, v10, v19, v17
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v15, v6, 0, 0
	v_add_nc_u32_e32 v6, -8, v0
	s_waitcnt vmcnt(0)
	v_or3_b32 v16, v10, v21, v9
	v_add_co_u32 v9, vcc_lo, v7, 8
	v_or3_b32 v15, v15, 0, 0
	v_add_co_ci_u32_e32 v10, vcc_lo, 0, v8, vcc_lo
.LBB2_11:                               ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $vgpr17_vgpr18
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v6
	s_xor_b32 s6, exec_lo, s0
	s_cbranch_execz .LBB2_17
; %bb.12:                               ;   in Loop: Header=BB2_3 Depth=1
	v_mov_b32_e32 v17, 0
	v_mov_b32_e32 v18, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s7, exec_lo
	v_cmpx_ne_u32_e32 0, v6
	s_cbranch_execz .LBB2_16
; %bb.13:                               ; %.preheader21
                                        ;   in Loop: Header=BB2_3 Depth=1
	v_mov_b32_e32 v17, 0
	v_mov_b32_e32 v18, 0
	s_mov_b32 s10, 0
	s_mov_b64 s[4:5], 0
	.p2align	6
.LBB2_14:                               ;   Parent Loop BB2_3 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_add_co_u32 v19, vcc_lo, v9, s4
	v_add_co_ci_u32_e32 v20, vcc_lo, s5, v10, vcc_lo
	s_add_u32 s4, s4, 1
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e32 vcc_lo, s4, v6
	flat_load_u8 v19, v[19:20]
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_dual_mov_b32 v20, s13 :: v_dual_and_b32 v19, 0xffff, v19
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[19:20], s0, v[19:20]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s10, vcc_lo, s10
	v_or_b32_e32 v18, v20, v18
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v17, v19, v17
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB2_14
; %bb.15:                               ; %Flow162
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s10
.LBB2_16:                               ; %Flow164
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s7
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr6
.LBB2_17:                               ; %Flow166
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_saveexec_b32 s0, s6
	v_mov_b32_e32 v21, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB2_19
; %bb.18:                               ;   in Loop: Header=BB2_3 Depth=1
	s_clause 0x6
	flat_load_u8 v17, v[9:10] offset:1
	flat_load_u8 v19, v[9:10] offset:2
	flat_load_u8 v21, v[9:10] offset:3
	flat_load_u8 v22, v[9:10]
	flat_load_u8 v23, v[9:10] offset:5
	flat_load_u8 v24, v[9:10] offset:4
	flat_load_u8 v25, v[9:10] offset:7
	v_mov_b32_e32 v26, v34
	v_mov_b32_e32 v18, s13
	s_waitcnt vmcnt(6) lgkmcnt(0)
	v_lshlrev_b16 v27, 8, v17
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v17, 0xffff, v19
	s_waitcnt vmcnt(4)
	v_and_b32_e32 v19, 0xffff, v21
	flat_load_d16_hi_u8 v26, v[9:10] offset:6
	v_add_co_u32 v9, vcc_lo, v9, 8
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v21, v27, v22
	v_mov_b32_e32 v20, s13
	v_lshlrev_b64 v[17:18], 16, v[17:18]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v22, 8, v23
	v_add_co_ci_u32_e32 v10, vcc_lo, 0, v10, vcc_lo
	v_and_b32_e32 v21, 0xffff, v21
	v_lshlrev_b64 v[19:20], 24, v[19:20]
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or3_b32 v18, 0, v18, v20
	v_or3_b32 v17, v21, v17, v19
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v19, 24, v25
	v_add_nc_u32_e32 v21, -8, v6
	v_or3_b32 v18, v18, v24, v22
	v_or3_b32 v17, v17, 0, 0
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_3)
	v_or3_b32 v17, v17, 0, 0
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_or3_b32 v18, v18, v26, v19
.LBB2_19:                               ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v21
	s_xor_b32 s6, exec_lo, s0
	s_cbranch_execz .LBB2_25
; %bb.20:                               ;   in Loop: Header=BB2_3 Depth=1
	v_mov_b32_e32 v19, 0
	v_mov_b32_e32 v20, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s7, exec_lo
	v_cmpx_ne_u32_e32 0, v21
	s_cbranch_execz .LBB2_24
; %bb.21:                               ; %.preheader19
                                        ;   in Loop: Header=BB2_3 Depth=1
	v_mov_b32_e32 v19, 0
	v_mov_b32_e32 v20, 0
	s_mov_b32 s10, 0
	s_mov_b64 s[4:5], 0
	.p2align	6
.LBB2_22:                               ;   Parent Loop BB2_3 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_add_co_u32 v22, vcc_lo, v9, s4
	v_add_co_ci_u32_e32 v23, vcc_lo, s5, v10, vcc_lo
	s_add_u32 s4, s4, 1
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e32 vcc_lo, s4, v21
	flat_load_u8 v6, v[22:23]
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_dual_mov_b32 v23, s13 :: v_dual_and_b32 v22, 0xffff, v6
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[22:23], s0, v[22:23]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s10, vcc_lo, s10
	v_or_b32_e32 v20, v23, v20
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v19, v22, v19
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB2_22
; %bb.23:                               ; %Flow157
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s10
.LBB2_24:                               ; %Flow159
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s7
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr21
.LBB2_25:                               ; %Flow161
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_saveexec_b32 s0, s6
	v_mov_b32_e32 v6, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB2_27
; %bb.26:                               ;   in Loop: Header=BB2_3 Depth=1
	s_clause 0x6
	flat_load_u8 v6, v[9:10] offset:1
	flat_load_u8 v19, v[9:10] offset:2
	flat_load_u8 v22, v[9:10] offset:3
	flat_load_u8 v24, v[9:10]
	flat_load_u8 v25, v[9:10] offset:5
	flat_load_u8 v26, v[9:10] offset:4
	flat_load_u8 v27, v[9:10] offset:7
	v_dual_mov_b32 v28, v34 :: v_dual_mov_b32 v23, s13
	v_mov_b32_e32 v20, s13
	flat_load_d16_hi_u8 v28, v[9:10] offset:6
	v_add_co_u32 v9, vcc_lo, v9, 8
	v_add_co_ci_u32_e32 v10, vcc_lo, 0, v10, vcc_lo
	s_waitcnt vmcnt(7) lgkmcnt(0)
	v_lshlrev_b16 v6, 8, v6
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v19, 0xffff, v19
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v22, 0xffff, v22
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v6, v6, v24
	v_lshlrev_b64 v[19:20], 16, v[19:20]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[22:23], 24, v[22:23]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v24, 8, v25
	v_and_b32_e32 v6, 0xffff, v6
	v_or3_b32 v20, 0, v20, v23
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v6, v6, v19, v22
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v19, 24, v27
	v_or3_b32 v20, v20, v26, v24
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v22, v6, 0, 0
	v_add_nc_u32_e32 v6, -8, v21
	s_waitcnt vmcnt(0)
	v_or3_b32 v20, v20, v28, v19
	s_delay_alu instid0(VALU_DEP_3)
	v_or3_b32 v19, v22, 0, 0
.LBB2_27:                               ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $vgpr21_vgpr22
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v6
	s_xor_b32 s6, exec_lo, s0
	s_cbranch_execz .LBB2_33
; %bb.28:                               ;   in Loop: Header=BB2_3 Depth=1
	v_mov_b32_e32 v21, 0
	v_mov_b32_e32 v22, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s7, exec_lo
	v_cmpx_ne_u32_e32 0, v6
	s_cbranch_execz .LBB2_32
; %bb.29:                               ; %.preheader17
                                        ;   in Loop: Header=BB2_3 Depth=1
	v_mov_b32_e32 v21, 0
	v_mov_b32_e32 v22, 0
	s_mov_b32 s10, 0
	s_mov_b64 s[4:5], 0
	.p2align	6
.LBB2_30:                               ;   Parent Loop BB2_3 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_add_co_u32 v23, vcc_lo, v9, s4
	v_add_co_ci_u32_e32 v24, vcc_lo, s5, v10, vcc_lo
	s_add_u32 s4, s4, 1
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e32 vcc_lo, s4, v6
	flat_load_u8 v23, v[23:24]
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_dual_mov_b32 v24, s13 :: v_dual_and_b32 v23, 0xffff, v23
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[23:24], s0, v[23:24]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s10, vcc_lo, s10
	v_or_b32_e32 v22, v24, v22
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v21, v23, v21
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB2_30
; %bb.31:                               ; %Flow152
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s10
.LBB2_32:                               ; %Flow154
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s7
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr6
.LBB2_33:                               ; %Flow156
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_saveexec_b32 s0, s6
	v_mov_b32_e32 v25, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB2_35
; %bb.34:                               ;   in Loop: Header=BB2_3 Depth=1
	s_clause 0x6
	flat_load_u8 v21, v[9:10] offset:1
	flat_load_u8 v23, v[9:10] offset:2
	flat_load_u8 v25, v[9:10] offset:3
	flat_load_u8 v26, v[9:10]
	flat_load_u8 v27, v[9:10] offset:5
	flat_load_u8 v28, v[9:10] offset:4
	flat_load_u8 v29, v[9:10] offset:7
	v_mov_b32_e32 v30, v34
	v_mov_b32_e32 v22, s13
	s_waitcnt vmcnt(6) lgkmcnt(0)
	v_lshlrev_b16 v31, 8, v21
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v21, 0xffff, v23
	s_waitcnt vmcnt(4)
	v_and_b32_e32 v23, 0xffff, v25
	flat_load_d16_hi_u8 v30, v[9:10] offset:6
	v_add_co_u32 v9, vcc_lo, v9, 8
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v25, v31, v26
	v_mov_b32_e32 v24, s13
	v_lshlrev_b64 v[21:22], 16, v[21:22]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v26, 8, v27
	v_add_co_ci_u32_e32 v10, vcc_lo, 0, v10, vcc_lo
	v_and_b32_e32 v25, 0xffff, v25
	v_lshlrev_b64 v[23:24], 24, v[23:24]
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or3_b32 v22, 0, v22, v24
	v_or3_b32 v21, v25, v21, v23
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v23, 24, v29
	v_add_nc_u32_e32 v25, -8, v6
	v_or3_b32 v22, v22, v28, v26
	v_or3_b32 v21, v21, 0, 0
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_3)
	v_or3_b32 v21, v21, 0, 0
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_or3_b32 v22, v22, v30, v23
.LBB2_35:                               ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v25
	s_xor_b32 s6, exec_lo, s0
	s_cbranch_execz .LBB2_41
; %bb.36:                               ;   in Loop: Header=BB2_3 Depth=1
	v_mov_b32_e32 v23, 0
	v_mov_b32_e32 v24, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s7, exec_lo
	v_cmpx_ne_u32_e32 0, v25
	s_cbranch_execz .LBB2_40
; %bb.37:                               ; %.preheader15
                                        ;   in Loop: Header=BB2_3 Depth=1
	v_mov_b32_e32 v23, 0
	v_mov_b32_e32 v24, 0
	s_mov_b32 s10, 0
	s_mov_b64 s[4:5], 0
	.p2align	6
.LBB2_38:                               ;   Parent Loop BB2_3 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_add_co_u32 v26, vcc_lo, v9, s4
	v_add_co_ci_u32_e32 v27, vcc_lo, s5, v10, vcc_lo
	s_add_u32 s4, s4, 1
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e32 vcc_lo, s4, v25
	flat_load_u8 v6, v[26:27]
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_dual_mov_b32 v27, s13 :: v_dual_and_b32 v26, 0xffff, v6
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[26:27], s0, v[26:27]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s10, vcc_lo, s10
	v_or_b32_e32 v24, v27, v24
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v23, v26, v23
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB2_38
; %bb.39:                               ; %Flow147
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s10
.LBB2_40:                               ; %Flow149
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s7
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr25
.LBB2_41:                               ; %Flow151
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_saveexec_b32 s0, s6
	v_mov_b32_e32 v6, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB2_43
; %bb.42:                               ;   in Loop: Header=BB2_3 Depth=1
	s_clause 0x6
	flat_load_u8 v6, v[9:10] offset:1
	flat_load_u8 v23, v[9:10] offset:2
	flat_load_u8 v26, v[9:10] offset:3
	flat_load_u8 v28, v[9:10]
	flat_load_u8 v29, v[9:10] offset:5
	flat_load_u8 v30, v[9:10] offset:4
	flat_load_u8 v31, v[9:10] offset:7
	v_dual_mov_b32 v32, v34 :: v_dual_mov_b32 v27, s13
	v_mov_b32_e32 v24, s13
	flat_load_d16_hi_u8 v32, v[9:10] offset:6
	v_add_co_u32 v9, vcc_lo, v9, 8
	v_add_co_ci_u32_e32 v10, vcc_lo, 0, v10, vcc_lo
	s_waitcnt vmcnt(7) lgkmcnt(0)
	v_lshlrev_b16 v6, 8, v6
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v23, 0xffff, v23
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v26, 0xffff, v26
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v6, v6, v28
	v_lshlrev_b64 v[23:24], 16, v[23:24]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[26:27], 24, v[26:27]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v28, 8, v29
	v_and_b32_e32 v6, 0xffff, v6
	v_or3_b32 v24, 0, v24, v27
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v6, v6, v23, v26
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v23, 24, v31
	v_or3_b32 v24, v24, v30, v28
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v26, v6, 0, 0
	v_add_nc_u32_e32 v6, -8, v25
	s_waitcnt vmcnt(0)
	v_or3_b32 v24, v24, v32, v23
	s_delay_alu instid0(VALU_DEP_3)
	v_or3_b32 v23, v26, 0, 0
.LBB2_43:                               ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
                                        ; implicit-def: $vgpr25_vgpr26
                                        ; implicit-def: $sgpr1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v6
	s_xor_b32 s6, exec_lo, s0
	s_cbranch_execz .LBB2_49
; %bb.44:                               ;   in Loop: Header=BB2_3 Depth=1
	v_mov_b32_e32 v25, 0
	v_mov_b32_e32 v26, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s7, exec_lo
	v_cmpx_ne_u32_e32 0, v6
	s_cbranch_execz .LBB2_48
; %bb.45:                               ; %.preheader13
                                        ;   in Loop: Header=BB2_3 Depth=1
	v_mov_b32_e32 v25, 0
	v_mov_b32_e32 v26, 0
	s_mov_b32 s10, 0
	s_mov_b64 s[4:5], 0
	.p2align	6
.LBB2_46:                               ;   Parent Loop BB2_3 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_delay_alu instid0(SALU_CYCLE_1)
	v_add_co_u32 v27, vcc_lo, v9, s4
	v_add_co_ci_u32_e32 v28, vcc_lo, s5, v10, vcc_lo
	s_add_u32 s4, s4, 1
	s_addc_u32 s5, s5, 0
	v_cmp_eq_u32_e32 vcc_lo, s4, v6
	flat_load_u8 v27, v[27:28]
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_dual_mov_b32 v28, s13 :: v_dual_and_b32 v27, 0xffff, v27
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_3) | instid1(VALU_DEP_1)
	v_lshlrev_b64 v[27:28], s0, v[27:28]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s10, vcc_lo, s10
	v_or_b32_e32 v26, v28, v26
	s_delay_alu instid0(VALU_DEP_2)
	v_or_b32_e32 v25, v27, v25
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB2_46
; %bb.47:                               ; %Flow142
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s10
.LBB2_48:                               ; %Flow144
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s7
	s_mov_b32 s1, 0
                                        ; implicit-def: $vgpr6
.LBB2_49:                               ; %Flow146
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_saveexec_b32 s0, s6
	v_mov_b32_e32 v29, s1
	s_xor_b32 exec_lo, exec_lo, s0
	s_cbranch_execz .LBB2_51
; %bb.50:                               ;   in Loop: Header=BB2_3 Depth=1
	s_clause 0x6
	flat_load_u8 v25, v[9:10] offset:1
	flat_load_u8 v27, v[9:10] offset:2
	flat_load_u8 v29, v[9:10] offset:3
	flat_load_u8 v30, v[9:10]
	flat_load_u8 v31, v[9:10] offset:5
	flat_load_u8 v32, v[9:10] offset:4
	flat_load_u8 v33, v[9:10] offset:7
	v_dual_mov_b32 v35, v34 :: v_dual_mov_b32 v26, s13
	v_mov_b32_e32 v28, s13
	flat_load_d16_hi_u8 v35, v[9:10] offset:6
	v_add_co_u32 v9, vcc_lo, v9, 8
	v_add_co_ci_u32_e32 v10, vcc_lo, 0, v10, vcc_lo
	s_waitcnt vmcnt(7) lgkmcnt(0)
	v_lshlrev_b16 v36, 8, v25
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v25, 0xffff, v27
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v27, 0xffff, v29
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v29, v36, v30
	v_lshlrev_b64 v[25:26], 16, v[25:26]
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_3) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[27:28], 24, v[27:28]
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v30, 8, v31
	v_and_b32_e32 v29, 0xffff, v29
	v_or3_b32 v26, 0, v26, v28
	s_delay_alu instid0(VALU_DEP_2)
	v_or3_b32 v25, v29, v25, v27
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v27, 24, v33
	v_add_nc_u32_e32 v29, -8, v6
	v_or3_b32 v26, v26, v32, v30
	v_or3_b32 v25, v25, 0, 0
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or3_b32 v26, v26, v35, v27
	v_or3_b32 v25, v25, 0, 0
.LBB2_51:                               ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
	s_delay_alu instid0(SALU_CYCLE_1)
	s_mov_b32 s0, exec_lo
	v_cmpx_gt_u32_e32 8, v29
	s_xor_b32 s4, exec_lo, s0
	s_cbranch_execz .LBB2_57
; %bb.52:                               ;   in Loop: Header=BB2_3 Depth=1
	v_mov_b32_e32 v27, 0
	v_mov_b32_e32 v28, 0
	s_mov_b64 s[0:1], 0
	s_mov_b32 s5, exec_lo
	v_cmpx_ne_u32_e32 0, v29
	s_cbranch_execz .LBB2_56
; %bb.53:                               ; %.preheader11
                                        ;   in Loop: Header=BB2_3 Depth=1
	v_mov_b32_e32 v27, 0
	v_mov_b32_e32 v28, 0
	s_mov_b32 s6, 0
	.p2align	6
.LBB2_54:                               ;   Parent Loop BB2_3 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	flat_load_u8 v6, v[9:10]
	v_mov_b32_e32 v31, s13
	v_add_nc_u32_e32 v29, -1, v29
	v_add_co_u32 v9, vcc_lo, v9, 1
	v_add_co_ci_u32_e32 v10, vcc_lo, 0, v10, vcc_lo
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_2) | instid1(VALU_DEP_1)
	v_cmp_eq_u32_e32 vcc_lo, 0, v29
	s_waitcnt vmcnt(0) lgkmcnt(0)
	v_and_b32_e32 v30, 0xffff, v6
	v_lshlrev_b64 v[30:31], s0, v[30:31]
	s_add_u32 s0, s0, 8
	s_addc_u32 s1, s1, 0
	s_or_b32 s6, vcc_lo, s6
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_or_b32_e32 v28, v31, v28
	v_or_b32_e32 v27, v30, v27
	s_and_not1_b32 exec_lo, exec_lo, s6
	s_cbranch_execnz .LBB2_54
; %bb.55:                               ; %Flow137
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
.LBB2_56:                               ; %Flow139
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s5
                                        ; implicit-def: $vgpr9_vgpr10
.LBB2_57:                               ; %Flow141
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_and_not1_saveexec_b32 s0, s4
	s_cbranch_execz .LBB2_59
; %bb.58:                               ;   in Loop: Header=BB2_3 Depth=1
	s_clause 0x5
	flat_load_u8 v6, v[9:10] offset:1
	flat_load_u8 v27, v[9:10] offset:2
	flat_load_u8 v29, v[9:10] offset:3
	flat_load_u8 v30, v[9:10]
	flat_load_u8 v31, v[9:10] offset:5
	flat_load_u8 v32, v[9:10] offset:4
	v_dual_mov_b32 v33, v34 :: v_dual_mov_b32 v28, s13
	s_clause 0x1
	flat_load_u8 v35, v[9:10] offset:7
	flat_load_d16_hi_u8 v33, v[9:10] offset:6
	v_mov_b32_e32 v10, s13
	s_waitcnt vmcnt(7) lgkmcnt(0)
	v_lshlrev_b16 v6, 8, v6
	s_waitcnt vmcnt(6)
	v_and_b32_e32 v9, 0xffff, v27
	s_waitcnt vmcnt(5)
	v_and_b32_e32 v27, 0xffff, v29
	s_waitcnt vmcnt(4)
	v_or_b32_e32 v6, v6, v30
	v_lshlrev_b64 v[9:10], 16, v[9:10]
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_lshlrev_b64 v[27:28], 24, v[27:28]
	v_and_b32_e32 v6, 0xffff, v6
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_2) | instid1(VALU_DEP_3)
	v_or3_b32 v10, 0, v10, v28
	s_waitcnt vmcnt(3)
	v_lshlrev_b32_e32 v28, 8, v31
	v_or3_b32 v6, v6, v9, v27
	s_waitcnt vmcnt(2)
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_4) | instid1(VALU_DEP_2)
	v_or3_b32 v9, v10, v32, v28
	s_waitcnt vmcnt(1)
	v_lshlrev_b32_e32 v10, 24, v35
	v_or3_b32 v6, v6, 0, 0
	s_waitcnt vmcnt(0)
	v_or3_b32 v28, v9, v33, v10
	s_delay_alu instid0(VALU_DEP_2)
	v_or3_b32 v27, v6, 0, 0
.LBB2_59:                               ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s0
	v_mov_b32_e32 v33, v2
	v_mov_b32_e32 v9, 0
	v_mov_b32_e32 v10, 0
	;;#ASMSTART
	;;#ASMEND
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_readfirstlane_b32 s0, v33
	v_cmp_eq_u32_e64 s0, s0, v33
	s_delay_alu instid0(VALU_DEP_1)
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB2_65
; %bb.60:                               ;   in Loop: Header=BB2_3 Depth=1
	s_waitcnt lgkmcnt(0)
	global_load_b64 v[31:32], v34, s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	s_clause 0x1
	global_load_b64 v[9:10], v34, s[2:3] offset:40
	global_load_b64 v[29:30], v34, s[2:3]
	s_mov_b32 s4, exec_lo
	s_waitcnt vmcnt(1)
	v_and_b32_e32 v6, v10, v32
	v_and_b32_e32 v9, v9, v31
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_mul_lo_u32 v6, v6, 24
	v_mul_hi_u32 v10, v9, 24
	v_mul_lo_u32 v9, v9, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_add_nc_u32_e32 v6, v10, v6
	s_waitcnt vmcnt(0)
	v_add_co_u32 v9, vcc_lo, v29, v9
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_ci_u32_e32 v10, vcc_lo, v30, v6, vcc_lo
	global_load_b64 v[29:30], v[9:10], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[9:10], v34, v[29:32], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmpx_ne_u64_e64 v[9:10], v[31:32]
	s_cbranch_execz .LBB2_64
; %bb.61:                               ; %.preheader9
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_mov_b32 s5, 0
                                        ; implicit-def: $sgpr6
	.p2align	6
.LBB2_62:                               ;   Parent Loop BB2_3 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_sleep 1
	s_clause 0x1
	global_load_b64 v[29:30], v34, s[2:3] offset:40
	global_load_b64 v[35:36], v34, s[2:3]
	v_dual_mov_b32 v32, v10 :: v_dual_mov_b32 v31, v9
	s_waitcnt vmcnt(1)
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_and_b32_e32 v6, v29, v31
	s_waitcnt vmcnt(0)
	v_mad_u64_u32 v[9:10], null, v6, 24, v[35:36]
	v_and_b32_e32 v35, v30, v32
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_mov_b32_e32 v6, v10
	v_mad_u64_u32 v[29:30], null, v35, 24, v[6:7]
	s_delay_alu instid0(VALU_DEP_1)
	v_mov_b32_e32 v10, v29
	global_load_b64 v[29:30], v[9:10], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[9:10], v34, v[29:32], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmp_eq_u64_e32 vcc_lo, v[9:10], v[31:32]
	s_or_b32 s5, vcc_lo, s5
	s_and_not1_b32 s6, s6, exec_lo
	s_and_b32 s7, vcc_lo, exec_lo
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 s6, s6, s7
	s_and_not1_b32 exec_lo, exec_lo, s5
	s_cbranch_execnz .LBB2_62
; %bb.63:                               ; %Flow133
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s5
.LBB2_64:                               ; %Flow135
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s4
.LBB2_65:                               ; %Flow136
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s1
	s_waitcnt lgkmcnt(0)
	s_clause 0x1
	global_load_b64 v[35:36], v34, s[2:3] offset:40
	global_load_b128 v[29:32], v34, s[2:3]
	v_readfirstlane_b32 s4, v9
	v_readfirstlane_b32 s5, v10
	s_mov_b64 s[10:11], exec
	s_waitcnt vmcnt(1)
	v_readfirstlane_b32 s6, v35
	v_readfirstlane_b32 s7, v36
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[6:7], s[4:5], s[6:7]
	s_mul_i32 s1, s7, 24
	s_mul_hi_u32 s15, s6, 24
	s_mul_i32 s16, s6, 24
	s_and_saveexec_b32 s17, s0
	s_cbranch_execz .LBB2_67
; %bb.66:                               ;   in Loop: Header=BB2_3 Depth=1
	s_add_i32 s18, s15, s1
	s_waitcnt vmcnt(0)
	v_add_co_u32 v35, vcc_lo, v29, s16
	v_add_co_ci_u32_e32 v36, vcc_lo, s18, v30, vcc_lo
	v_dual_mov_b32 v9, s10 :: v_dual_mov_b32 v10, s11
	global_store_b128 v[35:36], v[9:12], off offset:8
.LBB2_67:                               ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s17
	v_cmp_lt_u64_e32 vcc_lo, 56, v[4:5]
	v_or_b32_e32 v6, 0, v14
	v_or_b32_e32 v9, v13, v3
	v_lshl_add_u32 v10, v0, 2, 28
	s_lshl_b64 s[6:7], s[6:7], 12
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_cndmask_b32_e32 v14, v6, v14, vcc_lo
	v_dual_cndmask_b32 v6, v9, v13 :: v_dual_and_b32 v13, 0x1e0, v10
	v_lshlrev_b64 v[9:10], 6, v[33:34]
	s_waitcnt vmcnt(0)
	v_add_co_u32 v31, vcc_lo, v31, s6
	v_add_co_ci_u32_e32 v32, vcc_lo, s7, v32, vcc_lo
	v_and_or_b32 v13, 0xffffff1f, v6, v13
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_3)
	v_add_co_u32 v9, vcc_lo, v31, v9
	v_add_co_ci_u32_e32 v10, vcc_lo, v32, v10, vcc_lo
	s_clause 0x3
	global_store_b128 v[9:10], v[13:16], off
	global_store_b128 v[9:10], v[17:20], off offset:16
	global_store_b128 v[9:10], v[21:24], off offset:32
	global_store_b128 v[9:10], v[25:28], off offset:48
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB2_75
; %bb.68:                               ;   in Loop: Header=BB2_3 Depth=1
	s_clause 0x1
	global_load_b64 v[21:22], v34, s[2:3] offset:32 glc
	global_load_b64 v[13:14], v34, s[2:3] offset:40
	v_dual_mov_b32 v19, s4 :: v_dual_mov_b32 v20, s5
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s10, v13
	v_readfirstlane_b32 s11, v14
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[10:11], s[10:11], s[4:5]
	s_mul_i32 s7, s11, 24
	s_mul_hi_u32 s11, s10, 24
	s_mul_i32 s10, s10, 24
	s_add_i32 s11, s11, s7
	v_add_co_u32 v17, vcc_lo, v29, s10
	v_add_co_ci_u32_e32 v18, vcc_lo, s11, v30, vcc_lo
	s_mov_b32 s7, exec_lo
	global_store_b64 v[17:18], v[21:22], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[15:16], v34, v[19:22], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmpx_ne_u64_e64 v[15:16], v[21:22]
	s_cbranch_execz .LBB2_71
; %bb.69:                               ; %.preheader7
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_mov_b32 s10, 0
.LBB2_70:                               ;   Parent Loop BB2_3 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	v_dual_mov_b32 v13, s4 :: v_dual_mov_b32 v14, s5
	s_sleep 1
	global_store_b64 v[17:18], v[15:16], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[13:14], v34, v[13:16], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[13:14], v[15:16]
	v_dual_mov_b32 v16, v14 :: v_dual_mov_b32 v15, v13
	s_or_b32 s10, vcc_lo, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s10
	s_cbranch_execnz .LBB2_70
.LBB2_71:                               ; %Flow131
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s7
	global_load_b64 v[13:14], v34, s[2:3] offset:16
	s_mov_b32 s10, exec_lo
	s_mov_b32 s7, exec_lo
	v_mbcnt_lo_u32_b32 v6, s10, 0
	s_delay_alu instid0(VALU_DEP_1)
	v_cmpx_eq_u32_e32 0, v6
	s_cbranch_execz .LBB2_73
; %bb.72:                               ;   in Loop: Header=BB2_3 Depth=1
	s_bcnt1_i32_b32 s10, s10
	s_delay_alu instid0(SALU_CYCLE_1)
	v_mov_b32_e32 v33, s10
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_add_u64 v[13:14], v[33:34], off offset:8
.LBB2_73:                               ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s7
	s_waitcnt vmcnt(0)
	global_load_b64 v[15:16], v[13:14], off offset:16
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[15:16]
	s_cbranch_vccnz .LBB2_75
; %bb.74:                               ;   in Loop: Header=BB2_3 Depth=1
	global_load_b32 v33, v[13:14], off offset:24
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s7, v33
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_store_b64 v[15:16], v[33:34], off
	s_and_b32 m0, s7, 0xff
	s_sendmsg sendmsg(MSG_INTERRUPT)
.LBB2_75:                               ; %Flow132
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
	s_add_i32 s15, s15, s1
	v_add_co_u32 v6, vcc_lo, v29, s16
	v_add_co_ci_u32_e32 v14, vcc_lo, s15, v30, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v13, vcc_lo, v6, 20
	v_add_co_ci_u32_e32 v14, vcc_lo, 0, v14, vcc_lo
	s_branch .LBB2_79
	.p2align	6
.LBB2_76:                               ;   in Loop: Header=BB2_79 Depth=2
	s_or_b32 exec_lo, exec_lo, s1
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_readfirstlane_b32 s1, v6
	s_cmp_eq_u32 s1, 0
	s_cbranch_scc1 .LBB2_78
; %bb.77:                               ;   in Loop: Header=BB2_79 Depth=2
	s_sleep 1
	s_cbranch_execnz .LBB2_79
	s_branch .LBB2_81
	.p2align	6
.LBB2_78:                               ;   in Loop: Header=BB2_3 Depth=1
	s_branch .LBB2_81
.LBB2_79:                               ;   Parent Loop BB2_3 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	v_mov_b32_e32 v6, 1
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB2_76
; %bb.80:                               ;   in Loop: Header=BB2_79 Depth=2
	global_load_b32 v6, v[13:14], off glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_and_b32_e32 v6, 1, v6
	s_branch .LBB2_76
.LBB2_81:                               ;   in Loop: Header=BB2_3 Depth=1
	global_load_b128 v[13:16], v[9:10], off
	s_and_saveexec_b32 s1, s0
	s_cbranch_execz .LBB2_2
; %bb.82:                               ;   in Loop: Header=BB2_3 Depth=1
	s_clause 0x2
	global_load_b64 v[9:10], v34, s[2:3] offset:40
	global_load_b64 v[19:20], v34, s[2:3] offset:24 glc
	global_load_b64 v[17:18], v34, s[2:3]
	s_waitcnt vmcnt(2)
	v_add_co_u32 v6, vcc_lo, v9, 1
	v_add_co_ci_u32_e32 v21, vcc_lo, 0, v10, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v15, vcc_lo, v6, s4
	v_add_co_ci_u32_e32 v16, vcc_lo, s5, v21, vcc_lo
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[15:16]
	v_dual_cndmask_b32 v16, v16, v21 :: v_dual_cndmask_b32 v15, v15, v6
	v_and_b32_e32 v6, v16, v10
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_and_b32_e32 v9, v15, v9
	v_mul_hi_u32 v10, v9, 24
	v_mul_lo_u32 v9, v9, 24
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_2) | instid1(VALU_DEP_1)
	v_add_co_u32 v9, vcc_lo, v17, v9
	v_mov_b32_e32 v17, v19
	v_mul_lo_u32 v6, v6, 24
	v_add_nc_u32_e32 v6, v10, v6
	s_delay_alu instid0(VALU_DEP_1)
	v_add_co_ci_u32_e32 v10, vcc_lo, v18, v6, vcc_lo
	v_mov_b32_e32 v18, v20
	global_store_b64 v[9:10], v[19:20], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[17:18], v34, v[15:18], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_ne_u64_e32 vcc_lo, v[17:18], v[19:20]
	s_and_b32 exec_lo, exec_lo, vcc_lo
	s_cbranch_execz .LBB2_2
; %bb.83:                               ; %.preheader5
                                        ;   in Loop: Header=BB2_3 Depth=1
	s_mov_b32 s0, 0
.LBB2_84:                               ;   Parent Loop BB2_3 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	s_sleep 1
	global_store_b64 v[9:10], v[17:18], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[19:20], v34, v[15:18], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[19:20], v[17:18]
	v_dual_mov_b32 v17, v19 :: v_dual_mov_b32 v18, v20
	s_or_b32 s0, vcc_lo, s0
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s0
	s_cbranch_execnz .LBB2_84
	s_branch .LBB2_2
.LBB2_85:                               ; %Flow172
	s_or_b32 exec_lo, exec_lo, s14
                                        ; implicit-def: $vgpr10
                                        ; implicit-def: $vgpr1
.LBB2_86:                               ; %Flow190
	s_and_not1_saveexec_b32 s1, s12
	s_cbranch_execz .LBB2_109
; %bb.87:
	s_load_b64 s[2:3], s[8:9], 0x50
	;;#ASMSTART
	;;#ASMEND
	v_readfirstlane_b32 s0, v2
	v_mov_b32_e32 v8, 0
	v_mov_b32_e32 v9, 0
	s_delay_alu instid0(VALU_DEP_3) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_cmp_eq_u32_e64 s0, s0, v2
	s_and_saveexec_b32 s4, s0
	s_cbranch_execz .LBB2_93
; %bb.88:
	v_mov_b32_e32 v0, 0
	s_mov_b32 s5, exec_lo
	s_waitcnt lgkmcnt(0)
	global_load_b64 v[5:6], v0, s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	s_clause 0x1
	global_load_b64 v[3:4], v0, s[2:3] offset:40
	global_load_b64 v[7:8], v0, s[2:3]
	s_waitcnt vmcnt(1)
	v_and_b32_e32 v3, v3, v5
	v_and_b32_e32 v4, v4, v6
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_mul_hi_u32 v9, v3, 24
	v_mul_lo_u32 v4, v4, 24
	v_mul_lo_u32 v3, v3, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_add_nc_u32_e32 v4, v9, v4
	s_waitcnt vmcnt(0)
	v_add_co_u32 v3, vcc_lo, v7, v3
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_ci_u32_e32 v4, vcc_lo, v8, v4, vcc_lo
	global_load_b64 v[3:4], v[3:4], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[8:9], v0, v[3:6], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmpx_ne_u64_e64 v[8:9], v[5:6]
	s_cbranch_execz .LBB2_92
; %bb.89:                               ; %.preheader3
	s_mov_b32 s6, 0
                                        ; implicit-def: $sgpr7
	.p2align	6
.LBB2_90:                               ; =>This Inner Loop Header: Depth=1
	s_sleep 1
	s_clause 0x1
	global_load_b64 v[3:4], v0, s[2:3] offset:40
	global_load_b64 v[11:12], v0, s[2:3]
	v_dual_mov_b32 v5, v8 :: v_dual_mov_b32 v6, v9
	s_waitcnt vmcnt(1)
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_and_b32_e32 v3, v3, v5
	v_and_b32_e32 v4, v4, v6
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_mad_u64_u32 v[7:8], null, v3, 24, v[11:12]
	v_mov_b32_e32 v3, v8
	s_delay_alu instid0(VALU_DEP_1)
	v_mad_u64_u32 v[8:9], null, v4, 24, v[3:4]
	global_load_b64 v[3:4], v[7:8], off glc
	s_waitcnt vmcnt(0)
	global_atomic_cmpswap_b64 v[8:9], v0, v[3:6], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_cmp_eq_u64_e32 vcc_lo, v[8:9], v[5:6]
	s_or_b32 s6, vcc_lo, s6
	s_and_not1_b32 s7, s7, exec_lo
	s_and_b32 s8, vcc_lo, exec_lo
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 s7, s7, s8
	s_and_not1_b32 exec_lo, exec_lo, s6
	s_cbranch_execnz .LBB2_90
; %bb.91:                               ; %Flow185
	s_or_b32 exec_lo, exec_lo, s6
.LBB2_92:                               ; %Flow187
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s5
.LBB2_93:                               ; %Flow188
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s4
	v_mov_b32_e32 v3, 0
	v_readfirstlane_b32 s4, v8
	v_readfirstlane_b32 s5, v9
	s_mov_b64 s[6:7], exec
	s_waitcnt lgkmcnt(0)
	s_clause 0x1
	global_load_b64 v[11:12], v3, s[2:3] offset:40
	global_load_b128 v[4:7], v3, s[2:3]
	s_waitcnt vmcnt(1)
	v_readfirstlane_b32 s8, v11
	v_readfirstlane_b32 s9, v12
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(SALU_CYCLE_1)
	s_and_b64 s[8:9], s[4:5], s[8:9]
	s_mul_i32 s10, s9, 24
	s_mul_hi_u32 s11, s8, 24
	s_mul_i32 s12, s8, 24
	s_and_saveexec_b32 s13, s0
	s_cbranch_execz .LBB2_95
; %bb.94:
	s_add_i32 s14, s11, s10
	s_waitcnt vmcnt(0)
	v_add_co_u32 v8, vcc_lo, v4, s12
	v_add_co_ci_u32_e32 v9, vcc_lo, s14, v5, vcc_lo
	v_dual_mov_b32 v12, s7 :: v_dual_mov_b32 v11, s6
	v_dual_mov_b32 v13, 2 :: v_dual_mov_b32 v14, 1
	global_store_b128 v[8:9], v[11:14], off offset:8
.LBB2_95:
	s_or_b32 exec_lo, exec_lo, s13
	s_lshl_b64 s[6:7], s[8:9], 12
	v_lshlrev_b64 v[8:9], 6, v[2:3]
	s_waitcnt vmcnt(0)
	v_add_co_u32 v2, vcc_lo, v6, s6
	v_add_co_ci_u32_e32 v6, vcc_lo, s7, v7, vcc_lo
	s_mov_b32 s16, 0
	v_and_or_b32 v0, 0xffffff1f, v10, 32
	s_delay_alu instid0(VALU_DEP_3) | instskip(SKIP_4) | instid1(SALU_CYCLE_1)
	v_add_co_u32 v10, vcc_lo, v2, v8
	s_mov_b32 s17, s16
	v_add_co_ci_u32_e32 v11, vcc_lo, v6, v9, vcc_lo
	s_mov_b32 s18, s16
	s_mov_b32 s19, s16
	v_dual_mov_b32 v6, s16 :: v_dual_mov_b32 v9, s19
	v_dual_mov_b32 v2, v3 :: v_dual_mov_b32 v7, s17
	v_mov_b32_e32 v8, s18
	s_clause 0x3
	global_store_b128 v[10:11], v[0:3], off
	global_store_b128 v[10:11], v[6:9], off offset:16
	global_store_b128 v[10:11], v[6:9], off offset:32
	global_store_b128 v[10:11], v[6:9], off offset:48
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB2_103
; %bb.96:
	v_mov_b32_e32 v8, 0
	s_mov_b32 s7, exec_lo
	s_clause 0x1
	global_load_b64 v[11:12], v8, s[2:3] offset:32 glc
	global_load_b64 v[0:1], v8, s[2:3] offset:40
	v_dual_mov_b32 v9, s4 :: v_dual_mov_b32 v10, s5
	s_waitcnt vmcnt(0)
	v_and_b32_e32 v1, s5, v1
	v_and_b32_e32 v0, s4, v0
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_mul_lo_u32 v1, v1, 24
	v_mul_hi_u32 v2, v0, 24
	v_mul_lo_u32 v0, v0, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_nc_u32_e32 v1, v2, v1
	v_add_co_u32 v6, vcc_lo, v4, v0
	s_delay_alu instid0(VALU_DEP_2)
	v_add_co_ci_u32_e32 v7, vcc_lo, v5, v1, vcc_lo
	global_store_b64 v[6:7], v[11:12], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[2:3], v8, v[9:12], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmpx_ne_u64_e64 v[2:3], v[11:12]
	s_cbranch_execz .LBB2_99
; %bb.97:                               ; %.preheader1
	s_mov_b32 s8, 0
.LBB2_98:                               ; =>This Inner Loop Header: Depth=1
	v_dual_mov_b32 v0, s4 :: v_dual_mov_b32 v1, s5
	s_sleep 1
	global_store_b64 v[6:7], v[2:3], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[0:1], v8, v[0:3], s[2:3] offset:32 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[0:1], v[2:3]
	v_dual_mov_b32 v3, v1 :: v_dual_mov_b32 v2, v0
	s_or_b32 s8, vcc_lo, s8
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s8
	s_cbranch_execnz .LBB2_98
.LBB2_99:                               ; %Flow183
	s_or_b32 exec_lo, exec_lo, s7
	v_mov_b32_e32 v3, 0
	s_mov_b32 s8, exec_lo
	s_mov_b32 s7, exec_lo
	v_mbcnt_lo_u32_b32 v2, s8, 0
	global_load_b64 v[0:1], v3, s[2:3] offset:16
	v_cmpx_eq_u32_e32 0, v2
	s_cbranch_execz .LBB2_101
; %bb.100:
	s_bcnt1_i32_b32 s8, s8
	s_delay_alu instid0(SALU_CYCLE_1)
	v_mov_b32_e32 v2, s8
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_add_u64 v[0:1], v[2:3], off offset:8
.LBB2_101:
	s_or_b32 exec_lo, exec_lo, s7
	s_waitcnt vmcnt(0)
	global_load_b64 v[2:3], v[0:1], off offset:16
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[2:3]
	s_cbranch_vccnz .LBB2_103
; %bb.102:
	global_load_b32 v0, v[0:1], off offset:24
	v_mov_b32_e32 v1, 0
	s_waitcnt vmcnt(0)
	v_readfirstlane_b32 s7, v0
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_store_b64 v[2:3], v[0:1], off
	s_and_b32 m0, s7, 0xff
	s_sendmsg sendmsg(MSG_INTERRUPT)
.LBB2_103:                              ; %Flow184
	s_or_b32 exec_lo, exec_lo, s6
	s_add_i32 s11, s11, s10
	v_add_co_u32 v0, vcc_lo, v4, s12
	v_add_co_ci_u32_e32 v1, vcc_lo, s11, v5, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v0, vcc_lo, v0, 20
	v_add_co_ci_u32_e32 v1, vcc_lo, 0, v1, vcc_lo
	s_branch .LBB2_107
	.p2align	6
.LBB2_104:                              ;   in Loop: Header=BB2_107 Depth=1
	s_or_b32 exec_lo, exec_lo, s6
	s_delay_alu instid0(VALU_DEP_1) | instskip(NEXT) | instid1(VALU_DEP_1)
	v_readfirstlane_b32 s6, v2
	s_cmp_eq_u32 s6, 0
	s_cbranch_scc1 .LBB2_106
; %bb.105:                              ;   in Loop: Header=BB2_107 Depth=1
	s_sleep 1
	s_cbranch_execnz .LBB2_107
	s_branch .LBB2_110
	.p2align	6
.LBB2_106:
	s_branch .LBB2_110
.LBB2_107:                              ; =>This Inner Loop Header: Depth=1
	v_mov_b32_e32 v2, 1
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB2_104
; %bb.108:                              ;   in Loop: Header=BB2_107 Depth=1
	global_load_b32 v2, v[0:1], off glc
	s_waitcnt vmcnt(0)
	buffer_gl0_inv
	buffer_gl1_inv
	v_and_b32_e32 v2, 1, v2
	s_branch .LBB2_104
.LBB2_109:                              ; %Flow191
	s_or_b32 exec_lo, exec_lo, s1
	s_waitcnt vmcnt(0) lgkmcnt(0)
	s_waitcnt_vscnt null, 0x0
	s_setpc_b64 s[30:31]
.LBB2_110:
	s_and_saveexec_b32 s6, s0
	s_cbranch_execz .LBB2_114
; %bb.111:
	v_mov_b32_e32 v6, 0
	s_clause 0x2
	global_load_b64 v[2:3], v6, s[2:3] offset:40
	global_load_b64 v[7:8], v6, s[2:3] offset:24 glc
	global_load_b64 v[4:5], v6, s[2:3]
	s_waitcnt vmcnt(2)
	v_add_co_u32 v9, vcc_lo, v2, 1
	v_add_co_ci_u32_e32 v10, vcc_lo, 0, v3, vcc_lo
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_add_co_u32 v0, vcc_lo, v9, s4
	v_add_co_ci_u32_e32 v1, vcc_lo, s5, v10, vcc_lo
	s_delay_alu instid0(VALU_DEP_1) | instskip(SKIP_1) | instid1(VALU_DEP_1)
	v_cmp_eq_u64_e32 vcc_lo, 0, v[0:1]
	v_dual_cndmask_b32 v1, v1, v10 :: v_dual_cndmask_b32 v0, v0, v9
	v_and_b32_e32 v3, v1, v3
	s_delay_alu instid0(VALU_DEP_2) | instskip(NEXT) | instid1(VALU_DEP_2)
	v_and_b32_e32 v2, v0, v2
	v_mul_lo_u32 v3, v3, 24
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_2)
	v_mul_hi_u32 v9, v2, 24
	v_mul_lo_u32 v2, v2, 24
	v_add_nc_u32_e32 v3, v9, v3
	s_waitcnt vmcnt(0)
	s_delay_alu instid0(VALU_DEP_2) | instskip(SKIP_1) | instid1(VALU_DEP_3)
	v_add_co_u32 v4, vcc_lo, v4, v2
	v_mov_b32_e32 v2, v7
	v_add_co_ci_u32_e32 v5, vcc_lo, v5, v3, vcc_lo
	v_mov_b32_e32 v3, v8
	global_store_b64 v[4:5], v[7:8], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[2:3], v6, v[0:3], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_ne_u64_e32 vcc_lo, v[2:3], v[7:8]
	s_and_b32 exec_lo, exec_lo, vcc_lo
	s_cbranch_execz .LBB2_114
; %bb.112:                              ; %.preheader
	s_mov_b32 s0, 0
.LBB2_113:                              ; =>This Inner Loop Header: Depth=1
	s_sleep 1
	global_store_b64 v[4:5], v[2:3], off
	s_waitcnt vmcnt(0)
	s_waitcnt_vscnt null, 0x0
	global_atomic_cmpswap_b64 v[7:8], v6, v[0:3], s[2:3] offset:24 glc
	s_waitcnt vmcnt(0)
	v_cmp_eq_u64_e32 vcc_lo, v[7:8], v[2:3]
	v_dual_mov_b32 v2, v7 :: v_dual_mov_b32 v3, v8
	s_or_b32 s0, vcc_lo, s0
	s_delay_alu instid0(SALU_CYCLE_1)
	s_and_not1_b32 exec_lo, exec_lo, s0
	s_cbranch_execnz .LBB2_113
.LBB2_114:                              ; %Flow176
	s_or_b32 exec_lo, exec_lo, s6
	s_delay_alu instid0(SALU_CYCLE_1)
	s_or_b32 exec_lo, exec_lo, s1
	s_waitcnt lgkmcnt(0)
	s_waitcnt_vscnt null, 0x0
	s_setpc_b64 s[30:31]
.Lfunc_end6:
	.size	__ockl_fprintf_append_string_n, .Lfunc_end6-__ockl_fprintf_append_string_n
                                        ; -- End function
	.section	.AMDGPU.csdata
; Function info:
; codeLenInByte = 6224
; NumSgprs: 34
; NumVgprs: 37
; ScratchSize: 0
; MemoryBound: 0
	.text
	.p2alignl 7, 3214868480
	.fill 96, 4, 3214868480
	.type	__const.__assert_fail.fmt,@object ; @__const.__assert_fail.fmt
	.section	.rodata.str1.16,"aMS",@progbits,1
	.p2align	4, 0x0
__const.__assert_fail.fmt:
	.asciz	"%s:%u: %s: Device-side assertion `%s' failed.\n"
	.size	__const.__assert_fail.fmt, 47

	.ident	"AMD clang version 17.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-6.0.0 23483 7208e8d15fbf218deb74483ea8c549c67ca4985e)"
	.section	".note.GNU-stack"
	.amdgpu_metadata
---
amdhsa.kernels:
  - .args:
      - .address_space:  global
        .offset:         0
        .size:           8
        .value_kind:     global_buffer
      - .address_space:  global
        .offset:         8
        .size:           8
        .value_kind:     global_buffer
      - .address_space:  global
        .offset:         16
        .size:           8
        .value_kind:     global_buffer
    .group_segment_fixed_size: 0
    .kernarg_segment_align: 8
    .kernarg_segment_size: 24
    .language:       OpenCL C
    .language_version:
      - 2
      - 0
    .max_flat_workgroup_size: 1
    .name:           E_n2
    .private_segment_fixed_size: 0
    .sgpr_count:     8
    .sgpr_spill_count: 0
    .symbol:         E_n2.kd
    .uniform_work_group_size: 1
    .uses_dynamic_stack: false
    .vgpr_count:     2
    .vgpr_spill_count: 0
    .wavefront_size: 32
    .workgroup_processor_mode: 0
amdhsa.target:   amdgcn-amd-amdhsa--gfx1100
amdhsa.version:
  - 1
  - 2
...

	.end_amdgpu_metadata
