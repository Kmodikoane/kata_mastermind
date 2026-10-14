import unittest
from compare_codes import code_comparison

class Test_compare_code(unittest.TestCase):

    def test_independent_of_case(self):
        with self.assertTrue(code_comparison("red", "Green", "PINK", "whITe"), ("red", "green", "pink", "white")):
            code_comparison()









































if __name__ == "__main__":
    unittest.main()