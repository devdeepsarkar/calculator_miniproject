import unittest
import calculator


class TestCalculator(unittest.TestCase):

    # Square root tests
    def test_square_root_positive(self):
        self.assertEqual(calculator.square_root(16), 4)

    def test_square_root_zero(self):
        self.assertEqual(calculator.square_root(0), 0)

    def test_square_root_decimal(self):
        self.assertAlmostEqual(calculator.square_root(2.25), 1.5)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-9)


    # Factorial tests
    def test_factorial_positive(self):
        self.assertEqual(calculator.factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(calculator.factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            calculator.factorial(-3)

    def test_factorial_decimal(self):
        with self.assertRaises(ValueError):
            calculator.factorial(2.5)


    # Natural log tests
    def test_log_positive(self):
        self.assertAlmostEqual(calculator.natural_log(1), 0)

    def test_log_decimal(self):
        self.assertAlmostEqual(calculator.natural_log(2.5), 0.91629, places=5)

    def test_log_zero(self):
        with self.assertRaises(ValueError):
            calculator.natural_log(0)

    def test_log_negative(self):
        with self.assertRaises(ValueError):
            calculator.natural_log(-5)


    # Power tests
    def test_power_positive(self):
        self.assertEqual(calculator.power(2, 3), 8)

    def test_power_decimal_exponent(self):
        self.assertAlmostEqual(calculator.power(4, 2.1), 18.37917367995256)

    def test_power_decimal_base(self):
        self.assertAlmostEqual(calculator.power(2.5, 2), 6.25)

    def test_power_zero_exponent(self):
        self.assertEqual(calculator.power(5, 0), 1)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(calculator.power(2, -2), 0.25)


if __name__ == '__main__':
    unittest.main()