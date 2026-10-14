import unittest
from compare_codes import code_comparison

class Test_compare_code(unittest.TestCase):

    def test_independent_of_case(self):
        self.assertTrue(code_comparison(("red", "Green", "PINK", "whITe")), ("red", "green", "pink", "white"))










































if __name__ == "__main__":
    unittest.main()