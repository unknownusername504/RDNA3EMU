import numpy as np
import unittest

from rdna3emu.isa.instruction_set import InstructionSet


class TestOps(unittest.TestCase):
    def setUp(self):
        self.isa = InstructionSet()

    def test_op_unittest_s_mov_b32(self):
        print("Running test op_unittest_s_mov_b32...")
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
            # End the program
            (self.isa.scalar_ops.s_endpgm, []),
            (self.isa.scalar_ops.s_code_end, []),
        ]

        # Run the executable
        from rdna3emu.interpreter import run

        try:
            run(executable, print_instr=False, dump=False)

            # Print the result of sgpr1,2 as a uint32
            print(self.isa.registers.sgpr_u32(1))
            print(self.isa.registers.sgpr_u32(2))

            results_arr = self.isa.get_result_from_registers(
                reg_id_list=[ScalarRegister(1), ScalarRegister(2)],
                size=32,
                signed=False,
                floating=False,
            )
            # Convert the results to a numpy array of uint32 and 1d shape
            emulated_result = np.array(results_arr, dtype=np.uint32).flatten()
        except Exception as _:
            self.fail(f"Failed to run s_mov_b32 through interpreter.\n")

        # Define the expected result which we know to be [1, 2]
        expected_result = np.array([1, 2], dtype=np.uint32)

        # Compare the results
        np.testing.assert_allclose(
            emulated_result, expected_result, atol=1e-6, rtol=1e-6
        )

    def test_op_unittest_v_mov_b32(self):
        print("Running test op_unittest_v_mov_b32...")
        try:
            # Reset the isa
            self.isa.reset()
        except Exception as _:
            self.fail(f"Failed to reset the ISA.\n")

        from rdna3emu.isa.registers import VectorRegister

        # Create the executable
        executable = [
            (self.isa.vector_ops.v_mov_b32, [VectorRegister(1), 1]),
            (self.isa.vector_ops.v_mov_b32, [VectorRegister(2), 2]),
            # End the program
            (self.isa.scalar_ops.s_endpgm, []),
            (self.isa.scalar_ops.s_code_end, []),
        ]

        # Run the executable
        from rdna3emu.interpreter import run

        try:
            run(executable, print_instr=False, dump=False)

            # Print the result of vgpr1,2 as a uint32
            print(self.isa.registers.vgpr_u32(1))
            print(self.isa.registers.vgpr_u32(2))

            results_arr = self.isa.get_result_from_registers(
                reg_id_list=[VectorRegister(1), VectorRegister(2)],
                size=32,
                signed=False,
                floating=False,
            )
            # Convert the results to a numpy array of uint32 and 1d shape
            emulated_result = np.array(results_arr, dtype=np.uint32).flatten()
        except Exception as _:
            self.fail(f"Failed to run v_mov_b32 through interpreter.\n")

        # Define the expected result which we know to be [1, 2]
        expected_result = np.array([1, 2], dtype=np.uint32)

        # Compare the results
        np.testing.assert_allclose(
            emulated_result, expected_result, atol=1e-6, rtol=1e-6
        )

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

    def op_unittest_s_cselect_b32(self):
        print("Running test op_unittest_s_cselect_b32...")
        try:
            # Reset the isa
            self.isa.reset()
        except Exception as _:
            self.fail(f"Failed to reset the ISA.\n")

        from rdna3emu.isa.registers import ScalarRegister

        # Create the executable
        # Select the first input if SCC is true otherwise select the second input, then store the selected input into a scalar register.
        executable = [
            # Perform an operation that sets SCC to true
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(1), 1]),
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(2), 1]),
            (self.isa.scalar_ops.s_cmp_eq_u32, [ScalarRegister(1), ScalarRegister(2)]),
            # They are equal so SCC should be true
            # Select the first input
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(3), 3]),
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(4), 4]),
            (
                self.isa.scalar_ops.s_cselect_b32,
                [ScalarRegister(5), ScalarRegister(3), ScalarRegister(4)],
            ),
            # Perform an operation that sets SCC to false
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(2), 2]),
            (self.isa.scalar_ops.s_cmp_eq_u32, [ScalarRegister(1), ScalarRegister(2)]),
            # They are not equal so SCC should be false
            # Select the second input
            (
                self.isa.scalar_ops.s_cselect_b32,
                [ScalarRegister(6), ScalarRegister(3), ScalarRegister(4)],
            ),
            # End the program
            (self.isa.scalar_ops.s_endpgm, []),
            (self.isa.scalar_ops.s_code_end, []),
        ]

        # Run the executable
        from rdna3emu.interpreter import run

        try:
            run(executable, print_instr=False, dump=False)

            # Print the result of sgpr5,6 as a uint32
            print(self.isa.registers.sgpr_u32(5))
            print(self.isa.registers.sgpr_u32(6))

            results_arr = self.isa.get_result_from_registers(
                reg_id_list=[ScalarRegister(5), ScalarRegister(6)],
                size=32,
                signed=False,
                floating=False,
            )
            # Convert the results to a numpy array of uint32 and 1d shape
            emulated_result = np.array(results_arr, dtype=np.uint32).flatten()
        except Exception as _:
            self.fail(f"Failed to run s_cselect_b32 through interpreter.\n")

        # Define the expected result which we know to be [3, 4]
        expected_result = np.array([3, 4], dtype=np.uint32)

        # Compare the results
        np.testing.assert_allclose(
            emulated_result, expected_result, atol=1e-6, rtol=1e-6
        )

    def op_unittest_v_add_co_ci_u32(self):
        print("Running test op_unittest_v_add_co_ci_u32...")
        try:
            # Reset the isa
            self.isa.reset()
        except Exception as _:
            self.fail(f"Failed to reset the ISA.\n")

        from rdna3emu.isa.registers import VectorRegister, ScalarRegister

        # Create the executable
        # Add two unsigned inputs and a bit from a carry-in mask, store the result into a vector register and store the carry-out mask into a scalar register.
        # v_add_co_ci_u32_e32 v1, vcc_lo, s5, v1, vcc_lo
        # In VOP3 the VCC destination may be an arbitrary SGPR-pair, and the VCC source comes from the SGPR-pair at S2.u.
        executable = [
            # Set the carry-in mask to 0
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(1), 0]),
            # Perform an addition that will set the carry-out mask to 1
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(2), int("0xFFFFFFFF", 16)]),
            (self.isa.vector_ops.v_mov_b32, [VectorRegister(3), 1]),
            (
                self.isa.vector_ops.v_add_co_ci_u32,
                [
                    VectorRegister(4),
                    "vcc_lo",
                    ScalarRegister(2),
                    VectorRegister(3),
                    ScalarRegister(1),
                ],
            ),
            # Now the carry-in mask should be 1, perform an addition that will set the carry-out mask to 1 but into a register that is not vcc_lo
            (
                self.isa.vector_ops.v_add_co_ci_u32,
                [
                    VectorRegister(5),
                    ScalarRegister(1),
                    ScalarRegister(2),
                    VectorRegister(3),
                    "vcc_lo",
                ],
            ),
            # Perform an addition that will set the carry-out mask to 0 and test reuse of the carry-in mask
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(2), 1]),
            (self.isa.scalar_ops.s_mov_b32, [ScalarRegister(3), 0]),
            (
                self.isa.vector_ops.v_add_co_ci_u32,
                [
                    VectorRegister(6),
                    ScalarRegister(3),
                    ScalarRegister(2),
                    VectorRegister(3),
                    ScalarRegister(3),
                ],
            ),
            # End the program
            (self.isa.scalar_ops.s_endpgm, []),
            (self.isa.scalar_ops.s_code_end, []),
        ]

        # Run the executable
        from rdna3emu.interpreter import run

        try:
            run(executable, print_instr=False, dump=False)

            # Print the result of vgpr4,5,6 as a uint32
            print(self.isa.registers.vgpr_u32(4))
            print(self.isa.registers.vgpr_u32(5))
            print(self.isa.registers.vgpr_u32(6))

            # Print the result of sgpr1,3 as a uint32
            print(self.isa.registers.sgpr_u32(1))
            print(self.isa.registers.sgpr_u32(3))

            results_arr = self.isa.get_result_from_registers(
                reg_id_list=[
                    VectorRegister(4),
                    VectorRegister(5),
                    VectorRegister(6),
                    ScalarRegister(1),
                    ScalarRegister(3),
                ],
                size=32,
                signed=False,
                floating=False,
            )
            # Convert the results to a numpy array of uint32 and 1d shape
            emulated_result = np.array(results_arr, dtype=np.uint32).flatten()
        except Exception as _:
            self.fail(f"Failed to run v_add_co_ci_u32 through interpreter.\n")

        # Define the expected result which we know to be [0, 1, 2, 1, 0]
        expected_result = np.array([0, 1, 2, 1, 0], dtype=np.uint32)

        # Compare the results
        np.testing.assert_allclose(
            emulated_result, expected_result, atol=1e-6, rtol=1e-6
        )

    def op_unittest_global_preload_b64(self):
        print("Running test op_unittest_global_preload_b64...")
        try:
            # Reset the isa
            self.isa.reset()
        except Exception as _:
            self.fail(f"Failed to reset the ISA.\n")

        # Create the executable
        # global_preload_b64 0xDEADDEADDEADDEAD offset:0x5c8
        executable = [
            (
                self.isa.memory.global_preload_b64,
                [int("0xDEADDEADDEADDEAD", 16), int("0x5c8", 16)],
            ),
            # End the program
            (self.isa.scalar_ops.s_endpgm, []),
            (self.isa.scalar_ops.s_code_end, []),
        ]

        # Create the data
        data = np.array([1, 2], dtype=np.uint64)

        # Run the executable
        from rdna3emu.interpreter import run

        try:
            run(executable, print_instr=False, dump=False)
            # Print the result of global_memory_location(0x5C8, 8) as a uint64
            self.isa.memory.print_global_memory_location(0x5C8, 8)

            results_arr = self.isa.get_result_from_memory(address_list=[0x5C8], size=8)
            # Convert the results to a numpy array of uint64 and 1d shape
            emulated_result = np.array(results_arr, dtype=np.uint64).flatten()
        except Exception as _:
            self.fail(f"Failed to run global_preload_b64 through interpreter.\n")

        # Define the expected result which we know to be [0xDEADDEADDEADDEAD]
        expected_result = np.array([0xDEADDEADDEADDEAD], dtype=np.uint64)

        # Compare the results
        np.testing.assert_allclose(
            emulated_result, expected_result, atol=1e-6, rtol=1e-6
        )
