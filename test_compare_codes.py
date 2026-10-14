import unittest
from compare_codes import code_comparison

class Test_compare_code(unittest.TestCase):

    def test_independent_of_case(self):
        self.assertTrue(code_comparison(("red", "Green", "PINK", "whITe")), ("red", "green", "pink", "white"))

    def test_one_correct(self):
        self.asserFale(code_comparison())

    def test_two_correct(self):
        self.asserFale(code_comparison())

    def test_three_correct(self):
        self.asserFale(code_comparison())








































if __name__ == "__main__":
    unittest.main()