# https://leetcode.com/problems/valid-parenthesis-string/

"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:

The code uses two counters (leftMin and leftMax) to track the minimum and maximum number of open parentheses, respectively.
It iterates through the string and updates the counters based on the type of character encountered.
If leftMax becomes negative at any point, it means there are unmatched closing parentheses, so the function returns False.
To handle asterisks, the code considers them as both open and close parentheses, updating the counters accordingly.
After the iteration, it checks if all parentheses are closed by ensuring leftMin is zero.
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        # Initialize counters for the minimum and maximum number of open parentheses.
        leftMin, leftMax = 0, 0

        # Iterate through the characters in the string.
        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:  # Asterisk case
                leftMin, leftMax = leftMin - 1, leftMax + 1

            # Check if the maximum number of open parentheses is negative.
            if leftMax < 0:
                return False

            # Ensure leftMin is non-negative.
            if leftMin < 0:
                leftMin = 0  # Required because of cases like s = ( * ) (

        # Check if all parentheses are closed by the end.
        return leftMin == 0
