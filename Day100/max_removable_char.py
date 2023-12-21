# https://leetcode.com/problems/maximum-number-of-removable-characters/
"""
Time complexity:- O(N logM)
Space Complexity:- O(N) 
"""

"""
Intuition:

The maximumRemovals method uses binary search to find the maximum number of removals such that p is still a subsequence of s.
The isEnough function checks if removing a certain number of characters is enough to make p a subsequence of the modified string.
The binary search is performed on the range of possible numbers of removals, adjusting the search space based on the result of the isEnough function.
"""


from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        # Initialize the binary search range
        l, r = 0, len(removable)

        # Function to check if removing k characters is enough to make p a subsequence of s
        def isEnough(k):
            # Convert string to list for easier character removal
            s_arr = list(s)

            # Remove the first k characters in the removable list
            for i in removable[:k]:
                s_arr[i] = ""

            # Check if p is a subsequence of the modified string
            return isSubsequence(p, s_arr)

        # Function to check if s2 is a subsequence of s1
        def isSubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)

        # Perform binary search to find the maximum number of removals
        while l < r:
            m = (l + r + 1) // 2

            # If removing k characters is enough, look for a larger k
            if isEnough(m):
                l = m
            # If removing k characters is not enough, look for a smaller k
            else:
                r = m - 1

        # The final result is the maximum number of removals
        return l
