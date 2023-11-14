# https://leetcode.com/problems/valid-parenthesis-string/

"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:

The code uses a greedy approach to find the last occurrence of each character in the string.
It then iterates through the string, extending the current partition until reaching the last occurrence of the current character.
When the current index reaches the goal, it means a partition is complete, and its length is appended to the result list.
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Initialize a dictionary to store the last index of each character.
        count = {}
        # Initialize the result list to store the lengths of partitions.
        res = []
        i, length = 0, len(s)

        # Iterate through the string to populate the 'count' dictionary.
        for j in range(length):
            c = s[j]
            count[c] = j

        # Initialize variables for current partition length and goal index.
        curLen = 0
        goal = 0

        # Iterate through the string to find and record partitions.
        while i < length:
            c = s[i]
            goal = max(goal, count[c])
            curLen += 1

            # If the current index reaches the goal, record the partition length.
            if goal == i:
                res.append(curLen)
                curLen = 0
            i += 1

        return res
