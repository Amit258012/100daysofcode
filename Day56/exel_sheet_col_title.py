# https://leetcode.com/problems/excel-sheet-column-title/

"""
Time complexity:- O(logN)
Space Complexity:- O(1) 
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""  # Initialize the result as an empty string

        # Continue the loop until columnNumber is greater than 0
        while columnNumber > 0:
            r = columnNumber % 26  # Calculate the remainder when divided by 26
            if r == 0:
                r = 26  # If remainder is 0, set it to 26
                # Convert the remainder to a character and prepend it to the result
            res = chr(64 + r) + res
            # Update columnNumber for the next iteration
            columnNumber = int((columnNumber - r) / 26)
        return res  # Return the final result
