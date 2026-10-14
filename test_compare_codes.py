import unittest
from compare_codes import code_comparison

class Test_compare_code(unittest.TestCase):

    def test_independent_of_case(self):
        self.assertTrue(code_comparison(("red", "Green", "PINK", "whITe")), ("red", "green", "pink", "white"))

    def test_one_correct(self):
        self.assertFalse(code_comparison(("WHITE", "black", "Olive", "purPLE")))

    def test_two_correct(self):
        self.assertFalse(code_comparison(("green", "white")))
        self.assertFalse(code_comparison(("Black", "GREEN", "purPLE", "white")))

    def test_three_correct(self):
        self.assertFalse(code_comparison(("green", "white", "red", "navy")))

    def test_colour_notIn_options(self):
        self.assertFalse(code_comparison(("red", "Green", "PINK", "orange")))

    def test_colour_inOptions(self):
        pass








































if __name__ == "__main__":
    unittest.main()