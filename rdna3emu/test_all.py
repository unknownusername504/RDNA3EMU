import unittest

from rdna3emu.isa.instruction_set import InstructionSet


class TestSequences(unittest.TestCase):
    pass


def make_test_func(test_file_name, isa):
    def test_func(self):
        import os
        from rdna3emu.isa.utils import find_unimplemented_instructions

        # Print that we are running this test
        print()
        print(f"Running test {test_file_name}...")

        # Get the file path
        folder_path = os.path.dirname(os.path.abspath(__file__))
        # Go up one directory and then into Data
        folder_path = os.path.join(folder_path, "..", "Data")
        test_file_path = os.path.join(folder_path, test_file_name)

        # Assert that the file exists
        try:
            assert os.path.exists(test_file_path)
        except AssertionError:
            self.fail(f"The file {test_file_path} does not exist.")

        try:
            # Reset the isa
            isa.reset()

            # Get the instructions
            instructions = isa.instructions

            # Find the unimplemented instructions
            unimplemented_instructions = find_unimplemented_instructions(
                test_file_path, instructions
            )
        except Exception as _:
            self.fail(
                f"Failed to parse {test_file_name} for unimplemented instructions.\n"
            )

        # Check if there are any unimplemented instructions
        try:
            assert len(unimplemented_instructions) == 0
        except AssertionError:
            self.fail(
                f"There are unimplemented instructions in {test_file_name}:\n{unimplemented_instructions}"
            )

        from rdna3emu.parser import parse
        from rdna3emu.interpreter import build_executable, run

        try:
            # These functions print a lot redirect stdout and stderr to io.StringIO
            import contextlib
            import io

            with contextlib.redirect_stdout(io.StringIO()):
                with contextlib.redirect_stderr(io.StringIO()):
                    # Test runnability through interpreter
                    with open(test_file_path, "r") as f:
                        for _ in range(6):
                            next(f)
                        data = f.read()

                    instructions = parse(data)
                    run(build_executable(instructions), False, False)
        except Exception as _:
            self.fail(f"Failed to run {test_file_name} through interpreter.\n")

    # Set the name of the test
    test_func.__name__ = "test_" + test_file_name

    return test_func


def make_all_tests():
    # Unit test for rdna3emu
    test_file_names = [
        "add_tensors.txt",
        "exp_tensors.txt",
        "log_tensors.txt",
        "mul_tensors.txt",
        "neg_tensors.txt",
        "reciprocal_tensors.txt",
        "sin_tensors.txt",
        "sqrt_tensors.txt",
        "sub_tensors.txt",
        "zero_tensors.txt",
    ]

    isa = InstructionSet()
    # Create a unit test for each file
    for test_file_name in test_file_names:
        test_func = make_test_func(test_file_name, isa)

        # Add the test to the test class
        setattr(TestSequences, test_func.__name__, test_func)


# Make all the tests
make_all_tests()
