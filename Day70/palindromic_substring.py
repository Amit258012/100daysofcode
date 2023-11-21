# https://leetcode.com/problems/palindromic-substrings/
"""
Time complexity:- O(N^2)
Space Complexity:- O(1) 
"""

"""
Intuition:

The countSubstrings function counts palindromic substrings by iterating through each character in the string.
For each character, it calls the countPali function to expand around the character and count palindromes with both odd and even lengths.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        # Iterate through each character in the string and expand around it to find palindromes.
        for i in range(len(s)):
            # Count palindromes with odd length (centered at i).
            res += self.countPali(s, i, i)
            # Count palindromes with even length (centered between i and i+1).
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        # Expand around the center (l, r) to find palindromes.
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
