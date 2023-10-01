# https://leetcode.com/problems/evaluate-reverse-polish-notation/

"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""
"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Initialize a stack to store operands

        for ch in tokens:
            if ch == "+":
                # If the token is '+', pop the last two operands from the stack,
                # add them, and push the result back onto the stack.
                stack.append(stack.pop() + stack.pop())
            elif ch == "-":
                # If the token is '-', pop the last two operands from the stack,
                # subtract them, and push the result back onto the stack.
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif ch == "*":
                # If the token is '*', pop the last two operands from the stack,
                # multiply them, and push the result back onto the stack.
                stack.append(stack.pop() * stack.pop())
            elif ch == "/":
                # If the token is '/', pop the last two operands from the stack,
                # perform integer division, and push the result back onto the stack.
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                # If the token is a number, push it onto the stack.
                stack.append(int(ch))

        # The final result is at the top of the stack.
        return stack[0]
