# Unit test for the s_add_u32 instruction
import numpy as np

from op_unittests.testclass import OpUnittest


class TestSAddU32(OpUnittest):
    def op_unittest_s_add_u32(self):
        # Create the executable
        executable = [
            self.isa.scalar_ops.s_mov_b32,
            (self.isa.scalar_ops.s_mov_b32, [self.isa.SGPR(1), 1]),
            (self.isa.scalar_ops.s_mov_b32, [self.isa.SGPR(2), 2]),
            (
                self.isa.scalar_ops.s_add_u32,
                [self.isa.SGPR(3), self.isa.SGPR(1), self.isa.SGPR(2)],
            ),
            # Store the result in memory at address 0
            (self.isa.scalar_ops.s_store_dword, [self.isa.SGPR(3), 0]),
            self.isa.scalar_ops.s_endpgm,
            self.isa.scalar_ops.s_code_end,
        ]

        # Run the executable
        emulated_result = self.isa.run(executable, print_instr=False, dump=False)

        # Define the expected result which we know to be 3
        expected_result = np.array([3], dtype=np.uint32)

        # Compare the results
        np.testing.assert_allclose(
            emulated_result, expected_result, atol=1e-6, rtol=1e-6
        )
