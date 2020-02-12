# RPN-Calculator
A reverse polish-notation calculator implemented on the command line designed for users who are comfortable using the command line as opposed to a GUI interface.

This calculator supports basic arithmetic operations: Addition, Subtraction, Multiplication and Division.

Expressions should be added in a postfix or reversed polish notation order in one line like: 

-> 1 2 3 + -
 
-> -4

For more information on how rpn-calculators work, visit: https://en.wikipedia.org/wiki/Reverse_Polish_notation

As a bonus, the user will also be able to take a look at their history of calculations (from the same session) once they're done using the calculator.

The input expression is taken in with one line of input, followed by an output because it is clearer intuitively in my opinion.

Once an input is evaluated, the user can keep entering other expressions to evaluate.

Incorrect input expressions do not crash the program. Instead, an error message is returned and the user can enter another expression.
 
The user can exit the tool upon providing a SIGINT or a Keyboard interrupt. 
 If they hit the enter key or press 'q', the user will exit the calculator and can optionally view their history of calculations.

The program is structured into two modules:

- A basic calculator, which supports arithmetic logic
- A wrapper rpn_calculator module, which handles the parsing/evaluation logic and error handling.

This makes it easier to add further arithmetic logic, with minimal change to what's already implemented.

In the wrapper module, I've implemented a wrapper -> function mapping which makes it easier to call the appropriate
operation on the operands in O(1) complexity (with the help of a dictionary) and makes it easier to further implement more operations on operands.
 
If given more time, some additional features would also be accommodated like:

- Support more operations like exponential operations. 
- Support conversion of calculations to a CSV file to view it later or send to respective peers.
- Support storing calculations in memory to be worked on in a later session. 
---
Instructions to run (Please ensure python3 is installed in user system to run successfully): 

type to run program: 

./rpn_calc_tool.py

type to run unit tests for program modules: 
python3 -m unittest tests/<filename>