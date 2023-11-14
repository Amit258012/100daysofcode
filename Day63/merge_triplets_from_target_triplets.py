# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:

The code iterates through each triplet in the list.
It checks if any value in the triplet exceeds the corresponding value in the target triplet. If yes, it skips to the next triplet.
For each triplet, it checks if any value matches the corresponding value in the target triplet. If yes, it marks the index as matched in the set.
"""

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Initialize a set to keep track of which elements have been matched.
        good = set()

        # Iterate through the triplets.
        for t in triplets:
            # Check if the triplet's values exceed the target values.
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            # Iterate through the triplet's values.
            for i, v in enumerate(t):
                # If a value matches the target, mark the index as matched in the set.
                if v == target[i]:
                    good.add(i)

        # Check if all three indices have been matched.
        return len(good) == 3
