# https://leetcode.com/problems/basic-calculator

"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""


class Solution:
    def calculate(self, s: str) -> int:
        num = 0  # Initialize a variable to store the current numeric value
        sign = 1  # Initialize a sign variable (1 for positive, -1 for negative)
        res = 0  # Initialize the result
        stack = []  # Initialize a stack to handle parentheses

        for i in range(len(s)):  # Iterate through each character in the input string
            c = s[i]

            if c.isdigit():  # If the character is a digit, process it
                # Handle consecutive digits (e.g., "98" => 9 * 10 + 8 = 98)
                num = num * 10 + int(c)

            # If the character is '-' or '+', calculate the result
            elif c in "-+":
                # Add the current numeric value to the result with the appropriate sign
                res += num * sign
                # Update the sign based on the character
                sign = -1 if c == "-" else 1
                num = 0  # Reset the numeric value

            # If the character is '(', push the current result and sign onto the stack
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0  # Reset the result and sign
                sign = 1

            # If the character is ')', calculate the result within parentheses
            elif c == ")":
                # Add the current numeric value within parentheses to the result
                res += sign * num
                # Multiply the result by the sign from the stack
                res *= stack.pop()
                # Add the result to the previous result (outside parentheses)
                res += stack.pop()
                num = 0  # Reset the numeric value

        return res + num * sign  # Return the final result
