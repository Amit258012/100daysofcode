# https://leetcode.com/problems/count-and-say

"""
Time complexity:- O(2^n)
Space Complexity:- O(n)
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case: when n is 1, return "1"
        if n == 1:
            return "1"

        # Recursively calculate the (n-1)-th term of the count-and-say sequence
        temp = self.countAndSay(n - 1)
        res = ""
        val = temp[0]  # Initialize the current value to the first character
        freq = 1  # Initialize the frequency of the current value to 1

        # Iterate through the characters in the (n-1)-th term
        for i in range(1, len(temp)):
            if temp[i] == val:
                freq += 1
            else:
                # Append the frequency and value of the previous group to the result
                res += str(freq)
                res += str(val)
                val = temp[i]  # Update the current value
                freq = 1  # Reset the frequency for the new value

        # Append the frequency and value of the last group to the result
        res += str(freq)
        res += str(val)

        return res
