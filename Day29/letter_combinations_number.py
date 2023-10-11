# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

"""
Time complexity:- O(n * 4^n)
Space Complexity:- O(n)
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Define a mapping of phone digits to corresponding letters.
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []  # Initialize an empty list to store the combinations.

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                # If the current combination has the same length as the input digits, add it to the result.
                res.append(curStr)
                return

            for ch in phone[digits[i]]:
                # Recursively explore all possible combinations.
                backtrack(i + 1, curStr + ch)

        if digits:
            backtrack(0, "")  # Start the backtracking process with an empty string.
        return res
