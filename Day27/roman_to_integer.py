# https://leetcode.com/problems/roman-to-integer/

"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0  # Initialize a variable to store the result.

        # Create a dictionary to map Roman numerals to their integer values.
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        # Iterate through the characters in the Roman numeral string.
        for i in range(len(s) - 1):
            # If the value of the current symbol is less than the next symbol, subtract it.
            if symbols[s[i]] < symbols[s[i + 1]]:
                sum -= symbols[s[i]]
            else:
                # Otherwise, add the value of the current symbol to the result.
                sum += symbols[s[i]]

        # Add the value of the last symbol to the result.
        return sum + symbols[s[-1]]
