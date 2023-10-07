# https://leetcode.com/problems/longest-repeating-character-replacement

"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)  # Get the length of the string 's1'
        s1_count = Counter(s1)  # Count the characters in string 's1'
        n = len(s2)  # Get the length of the string 's2'

        # Iterate through 's2' using a sliding window of size 'window'
        for i in range(n - window + 1):
            # Count the characters in the current substring of 's2'
            s2_count = Counter(s2[i : i + window])

            # Check if the character counts of the current substring match 's1_count'
            if s2_count == s1_count:
                return True  # If a match is found, return True

        return False  # If no match is found, return False
