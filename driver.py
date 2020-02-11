#!/usr/bin/env python3
from calculator import Calculator


class RPNCalculator:
    def __init__(self):
        self.history = {}

    def driver(self):
        """
        Default driver definition to handle entrance/exit of program.
        :return: result
        """
        print("*******************************")
        print("Welcome to your very own rpn calculator.")
        print("*******************************")

        while True:
            user_input = input("Please enter your values in RPN order! Press 'q' to quit any time!")
            if user_input == "q" or user_input == "":
                break
            return self.evaluator(user_input)

        # BONUS: Display history of calculations
        print("We have a record of your past evaluations. Would you like to take a look? (y, n)")
        user_input = input()
        if user_input.lower() == "y" or user_input.lower() == "n":
            print("Your history of evaluations are as follows: ")
            for k, v in self.history.items():
                print("input: {}, output: {}".format(k, v))
        print("Thank you for using our calculator. :)")

    def evaluator(self, input):
        """
        Accepts a postfix mathematical expression as an input,
        and parses it based off the rules of rpn evaluation and accordingly calls
        appropriate operations from calculator object..
        :param input:
        :return: sum
        """
        calculator = Calculator
        # Split string by whitespace to get list of tokens.
        tokens = input.split()

        # Contains the functions to call based off operator.
        operations_map = {
            '+': calculator.addition,
            '-': calculator.subtraction,
            '*': calculator.multiplication,
            '/': calculator.division
        }

        # Evaluate rpn expression by traversing left to right.
        # Technique:
        # 1. Check whether the token is a number or an operator.
        # 2. If number: Push to stack
        # 3. If operator:
        #      3-a: Pop the previous two values from stack.
        #      3-b: Evaluate the two values based off operator.
        #      3-c: Push the evaluated integer back onto the stack.
        rpn_stk = []
        invalid_output_err = "Invalid expression. Please try again!"
        for token in tokens:
            # Check if its a valid operation, if token is + - * /
            is_valid_op = True if token in operations_map else False
            # Only execute step 1 if it's a valid integer or float.
            if not token.isalpha() and not is_valid_op:
                try:  # TODO! Optimize?
                    # Try to convert to an int.
                    token = int(token)
                except Exception as e:
                    # Try to convert to a floating point.
                    try:
                        token = float(token)
                    except Exception as e:
                        return invalid_output_err
                # Execute step 1.
                rpn_stk.append(token)
            elif is_valid_op:
                # Execute step 3.
                num2, num1 = rpn_stk.pop(), rpn_stk.pop()  # Get number in reverse order due to stack nature.
                function_to_call = operations_map[token]
                res = function_to_call(num1, num2)
                rpn_stk.append(res)
            else:
                # Handle error of invalid expression.
                return invalid_output_err

        # Update history and return answer
        self.history[input] = rpn_stk[0]
        return self.history[input]


if __name__ == "__main__":
    calc = RPNCalculator()
    calc.driver()

