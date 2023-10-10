# https://leetcode.com/problems/longest-palindromic-substring/

"""
Time complexity:- O(n^2)
Space Complexity:- O(n)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        n = len(s)
        res = ""

        for i in range(n):
            # Odd Length Palindrome
            palindrome1 = expandAroundCenter(i, i)

            # Even Length Palindrome
            palindrome2 = expandAroundCenter(i, i + 1)

            # Update result with the longer palindrome
            if len(palindrome1) > len(res):
                res = palindrome1
            if len(palindrome2) > len(res):
                res = palindrome2

        return res
