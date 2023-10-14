# https://leetcode.com/problems/longest-repeating-character-replacement

"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Initialize a dictionary to store character counts

        l = 0  # Initialize the left pointer of the sliding window
        maxf = 0  # Initialize the maximum character frequency

        # Iterate through the string 's' using a sliding window with the right pointer 'r'
        for r in range(len(s)):
            # Increment the count of the character at position 'r' in the dictionary
            count[s[r]] = 1 + count.get(s[r], 0)

            # Update 'maxf' with the maximum character frequency encountered so far
            maxf = max(maxf, count[s[r]])

            # Check if the length of the current substring (r - l + 1) minus 'maxf'
            # exceeds the allowed number of replacements 'k'
            if (r - l + 1) - maxf > k:
                # Decrement the count of the character at the left pointer 'l'
                count[s[l]] -= 1
                # Move the left pointer 'l' one position to the right
                l += 1

        # The result is the length of the longest valid substring found
        return r - l + 1
