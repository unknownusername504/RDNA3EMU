# Run all the unittests for the rdna3 emulator
import unittest


def run_tests():
    # Create the test suite
    suite = unittest.TestSuite()

    # Find all the test cases in this folder
    test_loader = unittest.TestLoader()
    test_loader.testMethodPrefix = "op_unittest_"
    tests = test_loader.discover("./op_unittests", pattern="op_unittest_*.py")

    # Add the tests to the suite
    suite.addTests(tests)

    # Run the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)


print("Running all tests...")
run_tests()
print("Done.")
