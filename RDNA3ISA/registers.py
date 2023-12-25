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


class StatusRegister(Bitfield):
  def __init__(self):
    super().__init__()
    self.read, self.write = True, self._writeable()

  def _writeable(self):
    return self.priv() == 1

  def _get(self, meta): super()._get(meta)
  def _set(self, meta, val): super()._set(meta, val)
  get_scc = partialmethod(_get, (0, 1))
  set_scc = partialmethod(_set, (0, 1))
  get_sys_prio = partialmethod(_get, (1, 2))
  set_sys_prio = partialmethod(_set, (1, 2))
  get_user_prio = partialmethod(_get, (3, 2))
  set_user_prio = partialmethod(_set, (3, 2))
  get_priv = partialmethod(_get, (5, 1))
  set_priv = partialmethod(_set, (5, 1))
  get_trap_en = partialmethod(_get, (6, 1))
  set_trap_en = partialmethod(_set, (6, 1))
  get_reserved_7 = partialmethod(_get, (7, 1))
  get_export_rdy = partialmethod(_get, (8, 1))
  set_export_rdy = partialmethod(_set, (8, 1))
  get_execz = partialmethod(_get, (9, 1))
  set_execz = partialmethod(_set, (9, 1))
  get_vccz = partialmethod(_get, (10, 1))
  set_vccz = partialmethod(_set, (10, 1))
  get_in_wg = partialmethod(_get, (11, 1))
  set_in_wg = partialmethod(_set, (11, 1))
  get_in_barrier = partialmethod(_get, (12, 1))
  set_in_barrier = partialmethod(_set, (12, 1))
  get_halt = partialmethod(_get, (13, 1))
  set_halt = partialmethod(_set, (13, 1))
  get_trap = partialmethod(_get, (14, 1))
  set_trap = partialmethod(_set, (14, 1))
  get_reserved_15 = partialmethod(_get, (15, 1))
  get_valid = partialmethod(_get, (16, 1))
  set_valid = partialmethod(_set, (16, 1))
  get_reserved_17 = partialmethod(_get, (17, 1))
  get_skip_export = partialmethod(_get, (18, 1))
  set_skip_export = partialmethod(_set, (18, 1))
  get_perf_en = partialmethod(_get, (19, 1))
  set_perf_en = partialmethod(_set, (19, 1))
  get_cdbg_user = partialmethod(_get, (20, 1))
  set_cdbg_user = partialmethod(_set, (20, 1))
  get_cdbg_sys = partialmethod(_get, (21, 1))
  set_cdbg_sys = partialmethod(_set, (21, 1))
  get_reserved_22 = partialmethod(_get, (22, 1))
  get_fatal_halt = partialmethod(_get, (23, 1))
  set_fatal_halt = partialmethod(_set, (23, 1))
  get_no_vpgrs = partialmethod(_get, (24, 1))
  set_no_vpgrs = partialmethod(_set, (24, 1))
  get_lds_param_rdy = partialmethod(_get, (25, 1))
  set_lds_param_rdy = partialmethod(_set, (25, 1))
  get_must_gs_alloc = partialmethod(_get, (26, 1))
  set_must_gs_alloc = partialmethod(_set, (26, 1))
  get_must_export = partialmethod(_get, (27, 1))
  set_must_export = partialmethod(_set, (27, 1))
  get_idle = partialmethod(_get, (28, 1))
  set_idle = partialmethod(_set, (28, 1))
  get_scratch_en = partialmethod(_get, (29, 1))
  set_scratch_en = partialmethod(_set, (29, 1))
  get_reserved_30_31 = partialmethod(_get, (30, 2))


class ModeRegister(Bitfield):
  def __init__(self):
    self.read, self.write = True, True
  pm = partialmethod
  def _get(self, meta): super()._get(meta)
  def _set(self, meta, val): super()._set(meta, val)
  get_fp_round = pm(_get, (0, 4))
  set_fp_round = pm(_set, (0, 4))
  get_fp_denorm = pm(_get, (4, 4))
  set_fp_denorm = pm(_set, (4, 4))
  get_dx10_clamp = pm(_get, (8, 1))
  set_dx10_clamp = pm(_set, (8, 1))
  get_ieee = pm(_get, (9, 1))
  set_ieee = pm(_set, (9, 1))
  get_lod_clamped = pm(_get, (10, 1))
  set_lod_clamped = pm(_set, (10, 1))
  get_trap_after_inst = pm(_get, (11, 1))
  set_trap_after_inst = pm(_set, (11, 1))
  get_excp_en = pm(_get, (12, 10))
  set_excp_en = pm(_get, (12, 10))
  get_fp16_ovl = pm(_get, (23, 1))
  set_fp16_ovl = pm(_set, (23, 1))
  get_disable_perf = pm(_get, (27, 1))
  set_disable_perf = pm(_set, (27, 1))


class TrapStatusRegister(Bitfield):
  def __init__(self):
    self.read, self.write = True, True
  pm = partialmethod
  def _get(self, meta): super()._get(meta)
  def _set(self, meta, val): super()._set(meta, val)
  get_excp = pm(_get, (0, 9))
  set_excp = pm(_set, (0, 9))
  get_savectx = pm(_get, (10, 1))
  set_savectx = pm(_set, (10, 1))
  get_illegal_inst = pm(_get, (11, 1))
  set_illegal_inst = pm(_set, (11, 1))
  get_addr_watch_1_3 = pm(_get, (12, 3))
  set_addr_watch_1_3 = pm(_set, (12, 3))
  get_buffer_oob = pm(_get, (15, 1))
  set_buffer_oob = pm(_set, (15, 1))
  get_host_trap = pm(_get, (16, 1))
  set_host_trap = pm(_set, (16, 1))
  get_wave_start = pm(_get, (17, 1))
  set_wave_start = pm(_set, (17, 1))
  get_wave_end = pm(_get, (18, 1))
  set_wave_end = pm(_set, (18, 1))
  get_trap_after_inst = pm(_get, (20, 1))
  set_trap_after_inst = pm(_set, (20, 1))


class Registers:
  def __init__(self):
    self._pc = 0
    self._vgpr = [0] * 256
    self._sgpr = [0] * 106
    self._exec = 0  # 64-bit
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

  pc = property(lambda self: self._pc, lambda self, val: setattr(self, '_pc', val))
  exec = property(lambda self: self._exec, lambda self, val: setattr(self, '_exec', val))
  status = property(lambda self: self._status, lambda self, val: setattr(self, '_status', val))
  vcc = property(lambda self: self._vcc, lambda self, val: setattr(self, '_vcc', val))
  flat_scratch = property(lambda self: self._flat_scratch, lambda self, val: setattr(self, '_flat_scratch', val))
  m0 = property(lambda self: self._m0, lambda self, val: setattr(self, '_m0', val))
  tba = property(lambda self: self._tba, lambda self, val: setattr(self, '_tba', val))
  tma = property(lambda self: self._tma, lambda self, val: setattr(self, '_tma', val))
  ttmp = property(lambda self: self._ttmp, lambda self, val: setattr(self, '_ttmp', val))
  flush_ib = property(lambda self: self._flush_ib, lambda self, val: setattr(self, '_flush_ib', val))
  sh_mem_bases = property(lambda self: self._sh_mem_bases, lambda self, val: setattr(self, '_sh_mem_bases', val))
  flat_scratch_lo = property(lambda self: self._flat_scratch_lo, lambda self, val: setattr(self, '_flat_scratch_lo', val))
  flat_scratch_hi = property(lambda self: self._flat_scratch_hi, lambda self, val: setattr(self, '_flat_scratch_hi', val))
  hw_id1 = property(lambda self: self._hw_id1, lambda self, val: setattr(self, '_hw_id1', val))
  hw_id2 = property(lambda self: self._hw_id2, lambda self, val: setattr(self, '_hw_id2', val))
  shader_cycles = property(lambda self: self._shader_cycles, lambda self, val: setattr(self, '_shader_cycles', val))
  vmcnt = property(lambda self: self._vmcnt, lambda self, val: setattr(self, '_vmcnt', val))
  vscnt = property(lambda self: self._vscnt, lambda self, val: setattr(self, '_vscnt', val))
  expcnt = property(lambda self: self._expcnt, lambda self, val: setattr(self, '_expcnt', val))
  lgrmcnt = property(lambda self: self._lgrmcnt, lambda self, val: setattr(self, '_lgrmcnt', val))

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
    elif size == 128:
      return np.float128(val)
    else:
      raise Exception(f'Float size {size} not supported.')

  def _get(self, reg_id, attr=None, signed=False, size=None, f=False):
    val = getattr(self, attr)[reg_id]
    if f:
      return Registers.floating(val, size)
    if signed:
      val = Registers._signed(val, size)
    return val % (2**size)

  def _set(self, reg_id, val, attr=None, signed=None, size=None, f=False):
    reg = getattr(self, attr)
    if f:
      reg[reg_id] = Registers.floating(val, size)
      return
    if signed:
      val = Registers._signed(val, size)
    reg[reg_id] = val % (2**size)

  pm = partialmethod
  get_vgpr_i8 = pm(_get, attr='_vgpr', signed=True, size=8)
  set_vgpr_i8 = pm(_set, attr='_vgpr', signed=True, size=8)

  get_vgpr_i16 = pm(_get, attr='_vgpr', signed=True, size=16)
  set_vgpr_i16 = pm(_set, attr='_vgpr', signed=True, size=16)

  get_vgpr_i32 = pm(_get, attr='_vgpr', signed=True, size=32)
  set_vgpr_i32 = pm(_set, attr='_vgpr', signed=True, size=32)

  get_vgpr_i64 = pm(_get, attr='_vgpr', signed=True, size=64)
  set_vgpr_i64 = pm(_set, attr='_vgpr', signed=True, size=64)

  get_vgpr_u8 = pm(_get, attr='_vgpr', signed=False, size=8)
  set_vgpr_u8 = pm(_set, attr='_vgpr', signed=False, size=8)

  get_vgpr_u16 = pm(_get, attr='_vgpr', signed=False, size=16)
  set_vgpr_u16 = pm(_set, attr='_vgpr', signed=False, size=16)

  get_vgpr_u32 = pm(_get, attr='_vgpr', signed=False, size=32)
  set_vgpr_u32 = pm(_set, attr='_vgpr', signed=False, size=32)

  get_vgpr_u64 = pm(_get, attr='_vgpr', signed=False, size=64)
  set_vgpr_u64 = pm(_set, attr='_vgpr', signed=False, size=64)

  get_vgpr_u128 = pm(_get, attr='_vgpr', signed=False, size=128)
  set_vgpr_u128 = pm(_set, attr='_vgpr', signed=False, size=128)

  get_vgpr_f16 = pm(_get, attr='_vgpr', size=16, f=True)
  set_vgpr_f16 = pm(_set, attr='_vgpr', size=16, f=True)

  get_vgpr_f32 = pm(_get, attr='_vgpr', size=32, f=True)
  set_vgpr_f32 = pm(_set, attr='_vgpr', size=32, f=True)

  get_vgpr_f64 = pm(_get, attr='_vgpr', size=64, f=True)
  set_vgpr_f64 = pm(_set, attr='_vgpr', size=64, f=True)

  get_vgpr_f128 = pm(_get, attr='_vgpr', size=128, f=True)
  set_vgpr_f128 = pm(_set, attr='_vgpr', size=128, f=True)

  get_sgpr_i8 = pm(_get, attr='_sgpr', signed=True, size=8)
  set_sgpr_i8 = pm(_set, attr='_sgpr', signed=True, size=8)

  get_sgpr_i16 = pm(_get, attr='_sgpr', signed=True, size=16)
  set_sgpr_i16 = pm(_set, attr='_sgpr', signed=True, size=16)

  get_sgpr_i32 = pm(_get, attr='_sgpr', signed=True, size=32)
  set_sgpr_i32 = pm(_set, attr='_sgpr', signed=True, size=32)

  get_sgpr_i64 = pm(_get, attr='_sgpr', signed=True, size=64)
  set_sgpr_i64 = pm(_set, attr='_sgpr', signed=True, size=64)

  get_sgpr_u8 = pm(_get, attr='_sgpr', signed=False, size=8)
  set_sgpr_u8 = pm(_set, attr='_sgpr', signed=False, size=8)

  get_sgpr_u16 = pm(_get, attr='_sgpr', signed=False, size=16)
  set_sgpr_u16 = pm(_set, attr='_sgpr', signed=False, size=16)

  get_sgpr_u32 = pm(_get, attr='_sgpr', signed=False, size=32)
  set_sgpr_u32 = pm(_set, attr='_sgpr', signed=False, size=32)

  get_sgpr_u64 = pm(_get, attr='_sgpr', signed=False, size=64)
  set_sgpr_u64 = pm(_set, attr='_sgpr', signed=False, size=64)

  get_sgpr_u128 = pm(_get, attr='_sgpr', signed=False, size=128)
  set_sgpr_u128 = pm(_set, attr='_sgpr', signed=False, size=128)

  set_scc_value = pm(_set, attr='_status', reg_id=0)
  get_scc_value = pm(_get, attr='_status', reg_id=0)