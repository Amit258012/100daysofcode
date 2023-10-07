# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters

"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0  # Initialize a count to keep track of good substrings

        # Iterate through the string 's' up to the third-to-last character
        for i in range(len(s) - 2):
            # Check if the current character and the next two characters are all different
            if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]:
                count += 1  # If it's a good substring, increment the count

        return count  # Return the count of good substrings
