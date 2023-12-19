# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:

The longestSubstring method iterates over the possible unique characters in the substring (from 1 to 26) and calls the helper method for each case.
The helper method uses a sliding window approach to find the maximum length of a substring with at most numUniqueTarget unique characters and each character appearing at least k times.
The method returns the maximum length of such substrings.
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        count = 0
        # Iterate over the possible unique characters in the substring
        for i in range(1, 27):
            count = max(count, self.helper(s, k, i))
        return count

    def helper(self, s, k, numUniqueTarget):
        start = end = numUnique = numNoLessThanK = count = 0
        # Use an array to track the count of each character in the substring
        chMap = [0] * 128

        while end < len(s):
            # Update counts for the current character
            if chMap[ord(s[end])] == 0:
                numUnique += 1
            chMap[ord(s[end])] += 1
            if chMap[ord(s[end])] == k:
                numNoLessThanK += 1
            end += 1

            # Adjust the window to maintain the required conditions
            while numUnique > numUniqueTarget:
                if chMap[ord(s[start])] == k:
                    numNoLessThanK -= 1
                chMap[ord(s[start])] -= 1
                if chMap[ord(s[start])] == 0:
                    numUnique -= 1
                start += 1

            # Update the maximum length of the substring
            if numUnique == numNoLessThanK:
                count = max(count, end - start)

        return count
