from functools import partialmethod
from enum import Enum


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
  reserved = partialmethod(_get, (7, 1))
  set_reserved = partialmethod(_set, (7, 1))
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
  get_reserved_17 = partialmethod(_get, (17, 1))
  skip_export = partialmethod(_get, (18, 1))
  set_skip_export = partialmethod(_set, (18, 1))
  perf_en = partialmethod(_get, (19, 1))
  set_perf_en = partialmethod(_set, (19, 1))
  cdbg_user = partialmethod(_get, (20, 1))
  set_cdbg_user = partialmethod(_set, (20, 1))
  cdbg_sys = partialmethod(_get, (21, 1))
  set_cdbg_sys = partialmethod(_set, (21, 1))
  get_reserved_22 = partialmethod(_get, (22, 1))
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
  pm = partialmethod
  def _get(self, meta): super()._get(meta)
  def _set(self, meta, val): super()._set(meta, val)
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
  pm = partialmethod
  def _get(self, meta): super()._get(meta)
  def _set(self, meta, val): super()._set(meta, val)
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


class Registers():
  def __init__(self):
    self._pc = 0
    self._vgpr = [0] * 256
    self._spgr[0] * 106
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


@property
def PC(self):
  return self._pc


def PC(self, v):
  self._pc = v


@staticmethod
def _signed(x, size):
  sign = x >> (size - 1)
  if sign == 1:
    x = x - 2**size
  return x


def _get_spgr(self, reg_id, signed=False, size=32):
  reg_val = self._spgr[reg_id] if not signed else _signed(
    self._spgr[reg_id], size)
  return reg_val % (2**size)


def _get_vgpr(self, reg_id, signed=False, size=32, type='int'):
  reg_val = self._vpgr[reg_id] if not signed else _signed(
    self._vpgr[reg_id], size)
  return reg_val % (2**size)
