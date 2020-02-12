class Calculator:
    """
    Calculator class responsible for RPN-calculation functionality
    pertaining to four basic arithmetic operations: +, -, *, /
    """
    def __init__(self):
        pass

    @staticmethod
    def addition(num1= 0.0, num2=0.0):
        return round(num1 + num2, 2)

    @staticmethod
    def subtraction(num1=0.0, num2=0.0):
        return round(num1 - num2, 2)

    @staticmethod
    def multiplication(num1=0.0, num2=0.0):
        return round(num1 * num2, 2)

    @staticmethod
    def division(num1=0.0, num2=1.0):
        # Handle divide by zero error.
        if num2 == 0:
            return "Invalid expression. Please try again!"
        return round(num1/num2, 2)
