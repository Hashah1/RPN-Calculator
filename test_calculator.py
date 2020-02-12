from calculator import Calculator
from unittest import TestCase


class TestCalculator(TestCase):
    def test_addition(self):
        """
        Tests appropriate addition between two numbers.

        Test 1: Test basic +ve integers.
        Test 2: Test basic -ve integers.
        Test 3: Test basic floating point numbers.
        Test 4: Test a 'None' past in -> Should return an error.
        Overflow ???
        """
        calc = Calculator
        # 1:
        num1, num2 = 2, 4
        exp_result = 6
        rcvd_result = calc.addition(num1, num2)
        self.assertEqual(exp_result, rcvd_result)

        # 2:
        num1, num2 = 2, -4
        exp_result = -2
        rcvd_result = calc.addition(num1, num2)
        self.assertEqual(exp_result, rcvd_result)

        # 3:
        num1, num2 = 2.4, 1.9999901312441
        exp_result = round(num1 + num2, 2)
        rcvd_result = calc.addition(num1, num2)
        self.assertEqual(exp_result, rcvd_result)

        # 4:
        num1 = 2.4
        # Due to default param init, the addition will technically be 2.4 + 0
        exp_result = 2.4
        rcvd_result = calc.addition(num1)
        self.assertEqual(exp_result, rcvd_result)

    def test_subtraction(self):
        """
        Test subtraction operations.

        # Test 1: Basic integers
        # Test 2: Floating points.
        """
        calc = Calculator
        # 1:
        num1, num2 = -2, 4
        exp_result = -6
        rcvd_result = calc.subtraction(num1, num2)
        self.assertEqual(exp_result, rcvd_result)

        # 2:
        num1, num2 = -2.1, 4.0
        exp_result = -6.1
        rcvd_result = calc.subtraction(num1, num2)
        self.assertEqual(exp_result, rcvd_result)

    def test_multiplication(self):
        """
        Test basic multiplication.

        # Test 1: Integer multiplication
        # Test 2: Floating point multiplication
        # Test 3: Multiply by 0.
        """
        calc = Calculator
        # 1:
        num1, num2 = 2, -4
        exp_result = -8
        rcvd_result = calc.multiplication(num1, num2)
        self.assertEqual(exp_result, rcvd_result)

        # 2:
        num1, num2 = -2, -4.1
        exp_result = round(-2 * -4.1, 2)
        rcvd_result = calc.multiplication(num1, num2)
        self.assertEqual(exp_result, rcvd_result)

        # 3:
        num1, num2 = 2, 0
        exp_result = 0
        rcvd_result = calc.multiplication(num1, num2)
        self.assertEqual(exp_result, rcvd_result)

    def test_division(self):
        """
        Test division operations.

        Test 1: Normal integer division.
        Test 2: Divide by 0.
        """
        calc = Calculator
        # 1:
        num1, num2 = 2, -4
        exp_result = 2/(-4)
        rcvd_result = calc.division(num1, num2)
        self.assertEqual(exp_result, rcvd_result)

        # 2: Should raise exception.
        num1, num2 = 1, 0.0
        exp_err_output = "Invalid expression. Please try again!"
        self.assertEqual(exp_err_output, calc.division(num1, num2))


if __name__ == "__main__":
    c = TestCalculator()
    c.test_addition()
    c.test_subtraction()
    c.test_multiplication()
    c.test_division()
