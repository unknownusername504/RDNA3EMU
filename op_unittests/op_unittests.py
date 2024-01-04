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
            # Convert the results to a numpy array of uint32 and 1d shape
            emulated_result = np.array(results_arr, dtype=np.uint32).flatten()
        except Exception as _:
            self.fail(f"Failed to run s_add_u32 through interpreter.\n")

        # Define the expected result which we know to be 3
        expected_result = np.array([3], dtype=np.uint32)

        # Compare the results
        np.testing.assert_allclose(
            emulated_result, expected_result, atol=1e-6, rtol=1e-6
        )

    def op_unittest_v_fmac_f32(self):
        print("Running test op_unittest_v_fmac_f32...")
        try:
            # Reset the isa
            self.isa.reset()
        except Exception as _:
            self.fail(f"Failed to reset the ISA.\n")

        from rdna3emu.isa.registers import VectorRegister

        # Create the executable
        executable = [
            (self.isa.vector_ops.v_mov_b32, [VectorRegister(1), 1.0]),
            (self.isa.vector_ops.v_mov_b32, [VectorRegister(2), 2.0]),
            (self.isa.vector_ops.v_mov_b32, [VectorRegister(3), 3.0]),
            (self.isa.vector_ops.v_mov_b32, [VectorRegister(4), 0.0]),
            (
                self.isa.vector_ops.v_fmac_f32,
                [VectorRegister(4), VectorRegister(1), VectorRegister(2)],
            ),
            (
                self.isa.vector_ops.v_fmac_f32,
                [VectorRegister(4), VectorRegister(1), VectorRegister(3)],
            ),
            (self.isa.scalar_ops.s_endpgm, []),
            (self.isa.scalar_ops.s_code_end, []),
        ]

        # Run the executable
        from rdna3emu.interpreter import run

        try:
            run(executable, print_instr=False, dump=False)

            # Print the result of vgpr1,2,3,4 as a float32
            print(self.isa.registers.vgpr_f32(1))
            print(self.isa.registers.vgpr_f32(2))
            print(self.isa.registers.vgpr_f32(3))
            print(self.isa.registers.vgpr_f32(4))

            results_arr = self.isa.get_result_from_registers(
                reg_id_list=[VectorRegister(4)],
                size=32,
                signed=False,
                floating=True,
            )
            # Convert the results to a numpy array of float32 and 1d shape
            emulated_result = np.array(results_arr, dtype=np.float32).flatten()
        except Exception as _:
            self.fail(f"Failed to run v_fmac_f32 through interpreter.\n")

        # Define the expected result which we know to be 5
        expected_result = np.array([5.0], dtype=np.float32)

        # Compare the results
        np.testing.assert_allclose(
            emulated_result, expected_result, atol=1e-6, rtol=1e-6
        )

    def op_unittest_s_mul_i32(self):
        print("Running test op_unittest_s_mul_i32...")
        try:
            # Reset the isa
            self.isa.reset()
        except Exception as _:
            self.fail(f"Failed to reset the ISA.\n")

        from rdna3emu.isa.registers import ScalarRegister

        # Create the executable
        executable = [
            # Positive x positive
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(1), 2]),
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(2), 3]),
            (
                self.isa.scalar_ops.s_mul_i32,
                [ScalarRegister(3), ScalarRegister(1), ScalarRegister(2)],
            ),
            # Negative x negative
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(1), -2]),
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(2), -3]),
            (
                self.isa.scalar_ops.s_mul_i32,
                [ScalarRegister(4), ScalarRegister(1), ScalarRegister(2)],
            ),
            # Positive x negative
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(1), 2]),
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(2), -3]),
            (
                self.isa.scalar_ops.s_mul_i32,
                [ScalarRegister(5), ScalarRegister(1), ScalarRegister(2)],
            ),
            # Negative x positive
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(1), -2]),
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(2), 3]),
            (
                self.isa.scalar_ops.s_mul_i32,
                [ScalarRegister(6), ScalarRegister(1), ScalarRegister(2)],
            ),
            # 0 x 0
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(1), 0]),
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(2), 0]),
            (
                self.isa.scalar_ops.s_mul_i32,
                [ScalarRegister(7), ScalarRegister(1), ScalarRegister(2)],
            ),
            # 0 x positive
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(1), 0]),
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(2), 3]),
            (
                self.isa.scalar_ops.s_mul_i32,
                [ScalarRegister(8), ScalarRegister(1), ScalarRegister(2)],
            ),
            # 0 x negative
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(1), 0]),
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(2), -3]),
            (
                self.isa.scalar_ops.s_mul_i32,
                [ScalarRegister(9), ScalarRegister(1), ScalarRegister(2)],
            ),
            (self.isa.scalar_ops.s_endpgm, []),
            (self.isa.scalar_ops.s_code_end, []),
        ]

        # Run the executable
        from rdna3emu.interpreter import run

        try:
            run(executable, print_instr=False, dump=False)

            # Print the result of sgpr1,2,3,4,5,6,7,8,9 as a int32
            print(self.isa.registers.sgpr_i32(1))
            print(self.isa.registers.sgpr_i32(2))
            print(self.isa.registers.sgpr_i32(3))
            print(self.isa.registers.sgpr_i32(4))
            print(self.isa.registers.sgpr_i32(5))
            print(self.isa.registers.sgpr_i32(6))
            print(self.isa.registers.sgpr_i32(7))
            print(self.isa.registers.sgpr_i32(8))
            print(self.isa.registers.sgpr_i32(9))

            results_arr = self.isa.get_result_from_registers(
                reg_id_list=[
                    ScalarRegister(3),
                    ScalarRegister(4),
                    ScalarRegister(5),
                    ScalarRegister(6),
                    ScalarRegister(7),
                    ScalarRegister(8),
                    ScalarRegister(9),
                ],
                size=32,
                signed=True,
                floating=False,
            )
            # Convert the results to a numpy array of int32 and 1d shape
            emulated_result = np.array(results_arr, dtype=np.int32).flatten()
        except Exception as _:
            self.fail(f"Failed to run s_mul_i32 through interpreter.\n")

        # Define the expected result which we know to be [6, 6, -6, -6, 0, 0, 0]
        expected_result = np.array([6, 6, -6, -6, 0, 0, 0], dtype=np.int32)

        # Compare the results
        np.testing.assert_allclose(
            emulated_result, expected_result, atol=1e-6, rtol=1e-6
        )
