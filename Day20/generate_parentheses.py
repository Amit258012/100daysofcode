# https://leetcode.com/problems/generate-parentheses/

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""
"""
Time complexity:- O(~2^n)
Space Complexity:- O(n)
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []  # Initialize a stack to keep track of parentheses combinations
        res = []  # Initialize a list to store the final results

        def backtrack(openN, closeN):
            # If both openN and closeN are equal to n, it means we have formed a valid combination.
            if openN == closeN == n:
                res.append("".join(stack))
                return

            # If we have more open parentheses than close parentheses, we can add a closing parenthesis.
            if openN > closeN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()

            # If we have not used all the open parentheses, we can add an opening parenthesis.
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()

        # Start the backtracking process with openN and closeN initially set to 0.
        backtrack(0, 0)
        return res
