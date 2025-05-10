# comp_math_testing
import unittest
import comp_math

class TestNormalizedNumber(unittest.TestCase):
    quick_msg = "The value computed is incorrect."
    x = comp_math.Propogation()
    def test_unicode_check(self):
        unicode_string_items = ["\u00b9", "3\u00b9", "3\u00b93"]
        for string in unicode_string_items:
            self.assertEqual(self.x.unicode_check(string), True, self.quick_msg)
    def test_basic_normalized(self):
        self.assertEqual(self.x.normalized(1, 10, 3), 100.0, self.quick_msg)
    def test_basic_negative_normalized(self):
        self.assertEqual(self.x.normalized(-1, 10, 3), -100.0, self.quick_msg)
    def test_basic_fractional_normalized(self):
        self.assertEqual(self.x.normalized(0.1, 10, 3), 100.0, self.quick_msg)
    def test_basic_negative_fractional_normalized(self):
        self.assertEqual(self.x.normalized(-0.1, 10, 3), -100.0, self.quick_msg)
    def test_basic_x_hat(self):
        self.assertEqual(self.x.x_hat(10000, 10, 3, 2), 100.0, self.quick_msg)
    def test_round_x_hat(self):
        self.assertEqual(self.x.x_hat(13579, 10, 3, 2), 140.0, self.quick_msg)
        self.assertEqual(self.x.x_hat(13579, 10, 3, 3), 136.0, self.quick_msg)
    def test_to_normalized(self):
        self.assertEqual(self.x.to_normalized(13579, 10, 2, 3), 1360000.0, self.quick_msg)
    def test_to_normalized_default(self):
        self.assertEqual(self.x.to_normalized(13579, 10, 2), 1357900.0, self.quick_msg)
    def test_to_normalized_form(self):
        self.assertEqual(self.x.to_normalized(13579, 10, 2, form = True), "0.13579x10\u2077", self.quick_msg)

if __name__ == "__main__":
    unittest.main()