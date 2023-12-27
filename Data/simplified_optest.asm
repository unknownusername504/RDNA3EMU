0000000000001600 <E_>:
    s_clause 0x1                                               // 000000001600: BF850001
    s_load_b128 s[4:7], s[0:1], null                           // 000000001604: F4080100 F8000000
    s_load_b64 s[0:1], s[0:1], 0x10                            // 00000000160C: F4040000 F8000010
    s_waitcnt lgkmcnt(0)                                       // 000000001614: BF89FC07
    s_load_b32 s2, s[6:7], null                                // 000000001618: F4000083 F8000000
    s_load_b32 s0, s[0:1], null                                // 000000001620: F4000000 F8000000
    s_waitcnt lgkmcnt(0)                                       // 000000001628: BF89FC07
    s_add_i32 s0, s0, s2                                       // 00000000162C: 81000200
    s_delay_alu instid0(SALU_CYCLE_1)                          // 000000001630: BF870009
    v_dual_mov_b32 v0, 0 :: v_dual_mov_b32 v1, s0              // 000000001634: CA100080 00000000
    global_store_b32 v0, v1, s[4:5]                            // 00000000163C: DC6A0000 00040100
    s_nop 0                                                    // 000000001644: BF800000
    s_sendmsg sendmsg(MSG_DEALLOC_VGPRS)                       // 000000001648: BFB60003
    s_endpgm                                                   // 00000000164C: BFB00000
    s_code_end                                                 // 000000001650: BF9F0000
    s_code_end                                                 // 000000001654: BF9F0000
    s_code_end                                                 // 000000001658: BF9F0000