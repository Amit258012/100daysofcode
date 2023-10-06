# https://leetcode.com/problems/remove-k-digits

"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""

from typing import List


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []  # Initialize an empty stack to store the digits

        for n in num:  # Iterate through the digits of the input number
            while stack and k and stack[-1] > n:
                # While the stack is not empty, there are remaining removals (k),
                # and the top of the stack is greater than the current digit 'n',
                # pop elements from the stack and decrement 'k'.
                stack.pop()
                k -= 1

            if stack or n != "0":
                # If the stack is not empty or the current digit is not '0',
                # append the current digit to the stack.
                stack.append(n)

        if k:
            # If there are remaining removals (k), remove the last 'k' digits from the stack.
            stack = stack[0:-k]

        # Return the result as a string or '0' if the stack is empty
        return "".join(stack) or "0"
