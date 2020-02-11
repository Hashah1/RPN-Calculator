class Calculator:
    """
    Calculator class responsible for RPN-calculation functionality
    pertaining to four basic arithmetic operations: +, -, *, /
    """
    def __init__(self):
        pass

    @staticmethod
    def addition(num1, num2):
        return num1 + num2

    @staticmethod
    def subtraction(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplication(num1, num2):
        return num1 * num2

    @staticmethod
    def division(num1, num2):
        # Handle divide by zero error.
        try:
            return num1 / num2
        except ZeroDivisionError as err:
            return err
