from functools import partialmethod
import numpy as np


class Bitfield:
    def __init__(self):
        self._bitfield = 0

    def _get(self, meta):
        pos, w = meta
        return (self._bitfield & (((1 << w) - 1) << pos)) >> pos

    def _set(self, meta, val):
        pos, w = meta
        m = ((1 << w) - 1) << pos
        f_val = (val << pos) & m
        self._bitfield = (self._bitfield & ~m) | f_val

    # Get all the bitfields as a dictionary keyed by the bitfield name
    def get_all(self):
        return {
            name: getattr(self, name)()
            for name in dir(self)
            if not name.startswith("_")
            if not name.startswith("pm")
            if not name.startswith("partialmethod")
            and not name.startswith("set_")
            and name not in ["get_all"]
            and callable(getattr(self, name))
        }


class StatusRegister(Bitfield):
    def __init__(self):
        super().__init__()
        self.read, self.write = True, self._writeable()
        # Set the default values
        self._bitfield = 0

    def _writeable(self):
        return self.priv() == 1

    def _get(self, meta):
        return super()._get(meta)

    def _set(self, meta, val):
        super()._set(meta, val)

    scc = partialmethod(_get, (0, 1))
    set_scc = partialmethod(_set, (0, 1))
    sys_prio = partialmethod(_get, (1, 2))
    set_sys_prio = partialmethod(_set, (1, 2))
    user_prio = partialmethod(_get, (3, 2))
    set_user_prio = partialmethod(_set, (3, 2))
    priv = partialmethod(_get, (5, 1))
    set_priv = partialmethod(_set, (5, 1))
    trap_en = partialmethod(_get, (6, 1))
    set_trap_en = partialmethod(_set, (6, 1))
    reserved_7 = partialmethod(_get, (7, 1))
    export_rdy = partialmethod(_get, (8, 1))
    set_export_rdy = partialmethod(_set, (8, 1))
    execz = partialmethod(_get, (9, 1))
    set_execz = partialmethod(_set, (9, 1))
    vccz = partialmethod(_get, (10, 1))
    set_vccz = partialmethod(_set, (10, 1))
    in_wg = partialmethod(_get, (11, 1))
    set_in_wg = partialmethod(_set, (11, 1))
    in_barrier = partialmethod(_get, (12, 1))
    set_in_barrier = partialmethod(_set, (12, 1))
    halt = partialmethod(_get, (13, 1))
    set_halt = partialmethod(_set, (13, 1))
    trap = partialmethod(_get, (14, 1))
    set_trap = partialmethod(_set, (14, 1))
    reserved_15 = partialmethod(_get, (15, 1))
    valid = partialmethod(_get, (16, 1))
    set_valid = partialmethod(_set, (16, 1))
    reserved_17 = partialmethod(_get, (17, 1))
    skip_export = partialmethod(_get, (18, 1))
    set_skip_export = partialmethod(_set, (18, 1))
    perf_en = partialmethod(_get, (19, 1))
    set_perf_en = partialmethod(_set, (19, 1))
    cdbg_user = partialmethod(_get, (20, 1))
    set_cdbg_user = partialmethod(_set, (20, 1))
    cdbg_sys = partialmethod(_get, (21, 1))
    set_cdbg_sys = partialmethod(_set, (21, 1))
    reserved_22 = partialmethod(_get, (22, 1))
    fatal_halt = partialmethod(_get, (23, 1))
    set_fatal_halt = partialmethod(_set, (23, 1))
    no_vpgrs = partialmethod(_get, (24, 1))
    set_no_vpgrs = partialmethod(_set, (24, 1))
    lds_param_rdy = partialmethod(_get, (25, 1))
    set_lds_param_rdy = partialmethod(_set, (25, 1))
    must_gs_alloc = partialmethod(_get, (26, 1))
    set_must_gs_alloc = partialmethod(_set, (26, 1))
    must_export = partialmethod(_get, (27, 1))
    set_must_export = partialmethod(_set, (27, 1))
    idle = partialmethod(_get, (28, 1))
    set_idle = partialmethod(_set, (28, 1))
    scratch_en = partialmethod(_get, (29, 1))
    set_scratch_en = partialmethod(_set, (29, 1))
    reserved_30_31 = partialmethod(_get, (30, 2))


class ModeRegister(Bitfield):
    def __init__(self):
        self.read, self.write = True, True
        # Set the default values
        self._bitfield = 0

    pm = partialmethod

    def _get(self, meta):
        return super()._get(meta)

    def _set(self, meta, val):
        super()._set(meta, val)

    fp_round = pm(_get, (0, 4))
    set_fp_round = pm(_set, (0, 4))
    fp_denorm = pm(_get, (4, 4))
    set_fp_denorm = pm(_set, (4, 4))
    dx10_clamp = pm(_get, (8, 1))
    set_dx10_clamp = pm(_set, (8, 1))
    ieee = pm(_get, (9, 1))
    set_ieee = pm(_set, (9, 1))
    lod_clamped = pm(_get, (10, 1))
    set_lod_clamped = pm(_set, (10, 1))
    trap_after_inst = pm(_get, (11, 1))
    set_trap_after_inst = pm(_set, (11, 1))
    excp_en = pm(_get, (12, 10))
    set_excp_en = pm(_get, (12, 10))
    fp16_ovl = pm(_get, (23, 1))
    set_fp16_ovl = pm(_set, (23, 1))
    disable_perf = pm(_get, (27, 1))
    set_disable_perf = pm(_set, (27, 1))


class TrapStatusRegister(Bitfield):
    def __init__(self):
        self.read, self.write = True, True
        # Set the default values
        self._bitfield = 0

    pm = partialmethod

    def _get(self, meta):
        return super()._get(meta)

    def _set(self, meta, val):
        super()._set(meta, val)

    excp = pm(_get, (0, 9))
    set_excp = pm(_set, (0, 9))
    savectx = pm(_get, (10, 1))
    set_savectx = pm(_set, (10, 1))
    illegal_inst = pm(_get, (11, 1))
    set_illegal_inst = pm(_set, (11, 1))
    addr_watch_1_3 = pm(_get, (12, 3))
    set_addr_watch_1_3 = pm(_set, (12, 3))
    buffer_oob = pm(_get, (15, 1))
    set_buffer_oob = pm(_set, (15, 1))
    host_trap = pm(_get, (16, 1))
    set_host_trap = pm(_set, (16, 1))
    wave_start = pm(_get, (17, 1))
    set_wave_start = pm(_set, (17, 1))
    wave_end = pm(_get, (18, 1))
    set_wave_end = pm(_set, (18, 1))
    trap_after_inst = pm(_get, (20, 1))
    set_trap_after_inst = pm(_set, (20, 1))


class Registers:
    def __init__(self):
        self._pc = 0
        self._vgpr = [0] * 256
        self._sgpr = [0] * 106
        self._exec = 0  # 64-bit
        self._exec_lo = self._exec & 0x00000000FFFFFFFF 
        self._exec_hi = self._exec & 0xFFFFFFFF00000000 
        self._status = StatusRegister()
        self._vcc = 0  # 64-bit
        self._flat_scratch = 0  # 48-bit
        self._mode = ModeRegister()
        self._m0 = 0  # 32-bit
        self._trap_sts = TrapStatusRegister()
        self._tba = 0  # 48-bit
        self._tma = 0  # 48-bit
        self._ttmp = [0] * 16
        self._flush_ib = 0  # w
        self._sh_mem_bases = 0  # r, privbase = [15:0], sharbase=[16:31]
        self._flat_scratch_lo = 0  # r, w(trap)
        self._flat_scratch_hi = 0  # r, w(trap)
        self._hw_id1 = 0  # r, dbg
        self._hw_id2 = 0  # r, dbg
        self._shader_cycles = 0
        # May be unnecessary
        self._vmcnt = 0  # 6-bit
        self._vscnt = 0  # 6-bit
        self._expcnt = 0  # 3-bit
        self._lgrmcnt = 0  # 6-bit

        # Track accesses to vgpr and sgpr as a dictionary of tuples keyed by register ID
        self.vgpr_accesses = {}
        self.sgpr_accesses = {}

    pc = property(lambda self: self._pc, lambda self, val: setattr(self, "_pc", val))
    exec = property(
        lambda self: self._exec, lambda self, val: setattr(self, "_exec", val)
    )
    exec_lo = property(lambda self: self._exec_lo, lambda self, val: setattr(self, "_exec_lo", val))
    exec_hi = property(lambda self: self._exec_hi, lambda self, val: setattr(self, "_exec_hi", val))
    status = property(
        lambda self: self._status, lambda self, val: setattr(self, "_status", val)
    )
    mode = property(
        lambda self: self._mode, lambda self, val: setattr(self, "_mode", val)
    )
    trap_sts = property(
        lambda self: self._trap_sts, lambda self, val: setattr(self, "_trap_sts", val)
    )
    vcc = property(lambda self: self._vcc, lambda self, val: setattr(self, "_vcc", val))
    flat_scratch = property(
        lambda self: self._flat_scratch,
        lambda self, val: setattr(self, "_flat_scratch", val),
    )
    m0 = property(lambda self: self._m0, lambda self, val: setattr(self, "_m0", val))
    tba = property(lambda self: self._tba, lambda self, val: setattr(self, "_tba", val))
    tma = property(lambda self: self._tma, lambda self, val: setattr(self, "_tma", val))
    ttmp = property(
        lambda self: self._ttmp, lambda self, val: setattr(self, "_ttmp", val)
    )
    flush_ib = property(
        lambda self: self._flush_ib, lambda self, val: setattr(self, "_flush_ib", val)
    )
    sh_mem_bases = property(
        lambda self: self._sh_mem_bases,
        lambda self, val: setattr(self, "_sh_mem_bases", val),
    )
    flat_scratch_lo = property(
        lambda self: self._flat_scratch_lo,
        lambda self, val: setattr(self, "_flat_scratch_lo", val),
    )
    flat_scratch_hi = property(
        lambda self: self._flat_scratch_hi,
        lambda self, val: setattr(self, "_flat_scratch_hi", val),
    )
    hw_id1 = property(
        lambda self: self._hw_id1, lambda self, val: setattr(self, "_hw_id1", val)
    )
    hw_id2 = property(
        lambda self: self._hw_id2, lambda self, val: setattr(self, "_hw_id2", val)
    )
    shader_cycles = property(
        lambda self: self._shader_cycles,
        lambda self, val: setattr(self, "_shader_cycles", val),
    )
    vmcnt = property(
        lambda self: self._vmcnt, lambda self, val: setattr(self, "_vmcnt", val)
    )
    vscnt = property(
        lambda self: self._vscnt, lambda self, val: setattr(self, "_vscnt", val)
    )
    expcnt = property(
        lambda self: self._expcnt, lambda self, val: setattr(self, "_expcnt", val)
    )
    lgrmcnt = property(
        lambda self: self._lgrmcnt, lambda self, val: setattr(self, "_lgrmcnt", val)
    )

    def _signed(x, size):
        sign = x >> (size - 1)
        if sign == 1:
            x = x - 2**size
        return x

    def floating(val, size):
        if size == 16:
            return np.float16(val)
        elif size == 32:
            return np.float32(val)
        elif size == 64:
            return np.float64(val)
        else:
            raise Exception(f"Float size {size} not supported.")

    def integer(val, size, signed):
        val = int(val) % (2**size)
        if signed:
            val = Registers._signed(val, size)
        if size == 8:
            val = np.int8(val) if signed else np.uint8(val)
        elif size == 16:
            val = np.int16(val) if signed else np.uint16(val)
        elif size == 24:
            val = np.int32(val & 0xFFFFFF) if signed else np.uint32(val & 0xFFFFFF)
        elif size == 32:
            val = np.int32(val) if signed else np.uint32(val)
        elif size == 64:
            val = np.int64(val) if signed else np.uint64(val)
        # else:
        #     raise Exception(f"Integer size {size} not supported.")
        # Cast back to int so that we can use native Python functions
        return int(val)

    def _get(self, reg_id, attr=None, signed=False, size=None, f=False):
        attr_value = getattr(self, attr)
        if reg_id < len(attr_value):
            val = attr_value[reg_id]
        else:
            # Handle the case where reg_id is out of range
            raise IndexError(f"Register {reg_id} is out of range for attribute {attr}.")
        val = attr_value[reg_id]
        if f:
            return Registers.floating(val, size)
        else:
            return Registers.integer(val, size, signed)

    def _set(self, reg_id, val, attr=None, signed=None, size=None, f=False):
        attr_value = getattr(self, attr)
        if reg_id < len(attr_value):
            val = attr_value[reg_id]
        else:
            # Handle the case where reg_id is out of range
            raise IndexError(f"Register {reg_id} is out of range for attribute {attr}.")
        if f:
            val = Registers.floating(val, size)
        else:
            val = Registers.integer(val, size, signed)
        attr_value[reg_id] = val
        # Track the access
        if attr == "_vgpr":
            # Only replace the size if it is bigger than the current size
            old_size = self.vgpr_accesses.get(reg_id, (attr, signed, size, f))[2]
            new_size = max(old_size, size)
            self.vgpr_accesses[reg_id] = (attr, signed, new_size, f)
        elif attr == "_sgpr":
            # Only replace the size if it is bigger than the current size
            old_size = self.sgpr_accesses.get(reg_id, (attr, signed, size, f))[2]
            new_size = max(old_size, size)
            self.sgpr_accesses[reg_id] = (attr, signed, new_size, f)

    def set_register(
        self, reg_type, reg_id, value, size=32, signed=True, floating=False
    ):
        """
        Set the value of a register based on type, size, and sign.

        :param reg_type: 'vgpr' or 'sgpr' to specify the register type
        :param reg_id: The identifier of the register to set
        :param value: The value to set in the register
        :param size: The size of the register in bits (e.g., 8, 16, 32, 64, 128)
        :param signed: True for signed integers, False for unsigned integers
        :param floating: True for floating-point numbers, False otherwise
        :return: None
        """

        # Determine the prefix based on the register type and whether it's floating-point
        prefix = "vgpr" if "VGPR" in reg_type.upper() else "sgpr"
        type_char = "f" if floating else "i" if signed else "u"

        # Construct the method name based on the parameters
        method_name = f"set_{prefix}_{type_char}{size}"

        # Ensure the method exists
        if not hasattr(self, method_name):
            raise ValueError(
                f"Method {method_name} does not exist for setting register values."
            )

        # Call the appropriate method to set the register value
        getattr(self, method_name)(reg_id, value)

    def get_register(self, reg_type, reg_id, size=32, signed=True, floating=False):
        """
        Get the value of a register based on type, size, and sign.

        :param reg_type: 'vgpr' or 'sgpr' to specify the register type
        :param reg_id: The identifier of the register to get
        :param size: The size of the register in bits (e.g., 8, 16, 32, 64, 128)
        :param signed: True for signed integers, False for unsigned integers
        :param floating: True for floating-point numbers, False otherwise
        :return: The value from the specified register
        """

        # Determine the prefix based on the register type and whether it's floating-point
        prefix = "vgpr" if "VGPR" in reg_type.upper() else "sgpr"
        type_char = "f" if floating else "i" if signed else "u"

        # Construct the method name based on the parameters
        method_name = f"{prefix}_{type_char}{size}"

        # Ensure the method exists
        if not hasattr(self, method_name):
            raise ValueError(
                f"Method {method_name} does not exist for getting register values."
            )

        # Call the appropriate method to get the register value
        return getattr(self, method_name)(reg_id)

    def dump_registers(self, non_zero=False):
        # Lambda function to output to file using the same format as the print statements
        # fprint = lambda x: print(x, file=open("registers.txt", "a"))
        """
        Dump the register values to the console.
        """
        print("==== State Registers: ====")
        print("PC: ", self.pc)
        print("Exec: ", self.exec)
        print("VCC: ", self.vcc)
        print("Flat Scratch: ", self.flat_scratch)
        print("M0: ", self.m0)
        print("TBA: ", self.tba)
        print("TMA: ", self.tma)
        print("Ttmp: ", self.ttmp)
        print("Flush IB: ", self.flush_ib)
        print("SH_MEM_BASES: ", self.sh_mem_bases)
        print("Flat Scratch Lo: ", self.flat_scratch_lo)
        print("Flat Scratch Hi: ", self.flat_scratch_hi)
        print("HW_ID1: ", self.hw_id1)
        print("HW_ID2: ", self.hw_id2)
        print("Shader Cycles: ", self.shader_cycles)
        print("VMCNT: ", self.vmcnt)
        print("VSCNT: ", self.vscnt)
        print("EXPCNT: ", self.expcnt)
        print("LGRMCNT: ", self.lgrmcnt)

        print("==== Field Registers: ====")
        print("Status: ", self.status.get_all())
        print("Mode: ", self.mode.get_all())
        print("Trap Status: ", self.trap_sts.get_all())

        print("==== VGPRs: ====")
        # Sort the accesses by register ID
        vgpr_accesses = sorted(self.vgpr_accesses.items(), key=lambda x: x[0])
        for reg_id, (attr, signed, size, f) in vgpr_accesses:
            # Read the current value given the register ID and size
            value = self._get(reg_id, attr=attr, signed=signed, size=size, f=f)
            if non_zero and value == 0:
                continue
            if type(value) not in [float, np.float16, np.float32, np.float64]:
                print(f"Register: {reg_id} Value: {value:#x}")
            else:
                print(f"Register: {reg_id} Value: {value}")

        print("==== SGPRs: ====")
        # Sort the accesses by register ID
        sgpr_accesses = sorted(self.sgpr_accesses.items(), key=lambda x: x[0])
        for reg_id, (attr, signed, size, f) in sgpr_accesses:
            # Read the current value given the register ID and size
            value = self._get(reg_id, attr=attr, signed=signed, size=size, f=f)
            if non_zero and value == 0:
                continue
            if type(value) not in [float, np.float16, np.float32, np.float64]:
                print(f"Register: {reg_id} Value: {value:#x}")
            else:
                print(f"Register: {reg_id} Value: {value}")

    pm = partialmethod
    vgpr_i8 = pm(_get, attr="_vgpr", signed=True, size=8)
    set_vgpr_i8 = pm(_set, attr="_vgpr", signed=True, size=8)

    vgpr_i16 = pm(_get, attr="_vgpr", signed=True, size=16)
    set_vgpr_i16 = pm(_set, attr="_vgpr", signed=True, size=16)

    vgpr_i32 = pm(_get, attr="_vgpr", signed=True, size=32)
    set_vgpr_i32 = pm(_set, attr="_vgpr", signed=True, size=32)

    vgpr_i64 = pm(_get, attr="_vgpr", signed=True, size=64)
    set_vgpr_i64 = pm(_set, attr="_vgpr", signed=True, size=64)

    vgpr_u8 = pm(_get, attr="_vgpr", signed=False, size=8)
    set_vgpr_u8 = pm(_set, attr="_vgpr", signed=False, size=8)

    vgpr_u16 = pm(_get, attr="_vgpr", signed=False, size=16)
    set_vgpr_u16 = pm(_set, attr="_vgpr", signed=False, size=16)

    vgpr_u32 = pm(_get, attr="_vgpr", signed=False, size=32)
    set_vgpr_u32 = pm(_set, attr="_vgpr", signed=False, size=32)

    vgpr_u64 = pm(_get, attr="_vgpr", signed=False, size=64)
    set_vgpr_u64 = pm(_set, attr="_vgpr", signed=False, size=64)

    vgpr_f16 = pm(_get, attr="_vgpr", size=16, f=True)
    set_vgpr_f16 = pm(_set, attr="_vgpr", size=16, f=True)

    vgpr_f32 = pm(_get, attr="_vgpr", size=32, f=True)
    set_vgpr_f32 = pm(_set, attr="_vgpr", size=32, f=True)

    vgpr_f64 = pm(_get, attr="_vgpr", size=64, f=True)
    set_vgpr_f64 = pm(_set, attr="_vgpr", size=64, f=True)

    sgpr_i8 = pm(_get, attr="_sgpr", signed=True, size=8)
    set_sgpr_i8 = pm(_set, attr="_sgpr", signed=True, size=8)

    sgpr_i16 = pm(_get, attr="_sgpr", signed=True, size=16)
    set_sgpr_i16 = pm(_set, attr="_sgpr", signed=True, size=16)

    sgpr_i32 = pm(_get, attr="_sgpr", signed=True, size=32)
    set_sgpr_i32 = pm(_set, attr="_sgpr", signed=True, size=32)

    sgpr_i64 = pm(_get, attr="_sgpr", signed=True, size=64)
    set_sgpr_i64 = pm(_set, attr="_sgpr", signed=True, size=64)

    sgpr_u8 = pm(_get, attr="_sgpr", signed=False, size=8)
    set_sgpr_u8 = pm(_set, attr="_sgpr", signed=False, size=8)

    sgpr_u16 = pm(_get, attr="_sgpr", signed=False, size=16)
    set_sgpr_u16 = pm(_set, attr="_sgpr", signed=False, size=16)

    sgpr_u32 = pm(_get, attr="_sgpr", signed=False, size=32)
    set_sgpr_u32 = pm(_set, attr="_sgpr", signed=False, size=32)

    sgpr_u64 = pm(_get, attr="_sgpr", signed=False, size=64)
    set_sgpr_u64 = pm(_set, attr="_sgpr", signed=False, size=64)

    # Special 24-bit access
    sgpr_u24 = pm(_get, attr="_sgpr", signed=False, size=24)
    set_sgpr_u24 = pm(_set, attr="_sgpr", signed=False, size=24)

    sgpr_i24 = pm(_get, attr="_sgpr", signed=True, size=24)
    set_sgpr_i24 = pm(_set, attr="_sgpr", signed=True, size=24)

    vgpr_u24 = pm(_get, attr="_vgpr", signed=False, size=24)
    set_vgpr_u24 = pm(_set, attr="_vgpr", signed=False, size=24)

    vgpr_i24 = pm(_get, attr="_vgpr", signed=True, size=24)
    set_vgpr_i24 = pm(_set, attr="_vgpr", signed=True, size=24)
