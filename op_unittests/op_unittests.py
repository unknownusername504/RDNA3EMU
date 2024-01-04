import numpy as np
import unittest

from rdna3emu.isa.instruction_set import InstructionSet


class TestOps(unittest.TestCase):
    def setUp(self):
        self.isa = InstructionSet()

    # Unit test for the s_add_u32 instruction
    def op_unittest_s_add_u32(self):
        print("Running test op_unittest_s_add_u32...")
        try:
            # Reset the isa
            self.isa.reset()
        except Exception as _:
            self.fail(f"Failed to reset the ISA.\n")

        from rdna3emu.isa.registers import ScalarRegister

        # Create the executable
        executable = [
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(1), 1]),
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(2), 2]),
            (
                self.isa.scalar_ops.s_add_u32,
                [ScalarRegister(3), ScalarRegister(1), ScalarRegister(2)],
            ),
            (self.isa.scalar_ops.s_endpgm, []),
            (self.isa.scalar_ops.s_code_end, []),
        ]

        # Run the executable
        from rdna3emu.interpreter import run

        try:
            run(executable, print_instr=False, dump=False)

            # Print the result of sgpr1,2,3 as a uint32
            print(self.isa.registers.sgpr_u32(1))
            print(self.isa.registers.sgpr_u32(2))
            print(self.isa.registers.sgpr_u32(3))

            results_arr = self.isa.get_result_from_registers(
                reg_id_list=[ScalarRegister(3)],
                size=32,
                signed=False,
                floating=False,
            )
            # Convert the results to a numpy array of uint32 and shape (1,)
            emulated_result = np.array(results_arr, dtype=np.uint32).reshape(
                1,
            )
        except Exception as _:
            self.fail(f"Failed to run s_add_u32 through interpreter.\n")

        # Define the expected result which we know to be 3
        expected_result = np.array([3], dtype=np.uint32)

        # Compare the results
        np.testing.assert_allclose(
            emulated_result, expected_result, atol=1e-6, rtol=1e-6
        )