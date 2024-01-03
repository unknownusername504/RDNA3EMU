import unittest

from rdna3emu.isa.instruction_set import InstructionSet


class OpUnittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.isa = InstructionSet()
        try:
            # Reset the isa
            cls.isa.reset()
        except Exception as _:
            cls.fail(f"Failed to reset the ISA.\n")
