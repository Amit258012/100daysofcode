# https://leetcode.com/problems/valid-parentheses/

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize an empty stack to store open brackets

        for c in s:
            if c in "({[":
                # If the character is an open bracket, push its corresponding closing bracket onto the stack
                if c == "(":
                    stack.append(")")
                elif c == "[":
                    stack.append("]")
                else:
                    stack.append("}")
            else:
                # If the character is a closing bracket
                if not stack or c != stack.pop():
                    # If the stack is empty or the popped bracket doesn't match the current closing bracket, it's invalid
                    return False

        # After processing all characters, if the stack is empty, the string is valid
        return len(stack) == 0
