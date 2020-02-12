from unittest import TestCase
from rpn_calc_tool import RPNCalculator

class TestRPNCalculator(TestCase):
    def test_evaluator(self):
        """
        Tests evaluator definition to see how expression is parsed and solved.

        Test 1: Solve a basic expression with all four operands.
        Test 2: Solve an invalid expression with words.
        Test 3: Solve an invalid expression given in infix notation.
        Test 4: Solve an expression which has more operators than digits.
        Test 5: Test expression with a punctuation mark hidden within expr.
        """
        rpn = RPNCalculator()
        exp_err_output = "Invalid expression. Please try again!"
        # 1:
        input_exp = "12 2 -"
        exp_output = 10
        rcvd_output = rpn.evaluator(input_exp)
        self.assertEqual(rcvd_output, exp_output)

        # 2: -> Should raise an exception.
        input_exp = "oop23s wqe2w -l"
        self.assertEqual(exp_err_output, rpn.evaluator(input_exp))

        # 3: -> Should raise an exception.
        input_exp = "1 + 2 - 3"
        self.assertEqual(exp_err_output, rpn.evaluator(input_exp))

        # 4: -> Should raise an exception.
        input_exp = " 1 + + + + +                "
        self.assertEqual(exp_err_output, rpn.evaluator(input_exp))

        # 5:
        input_exp = " 1 2 ,"
        self.assertEqual(exp_err_output, rpn.evaluator(input_exp))
