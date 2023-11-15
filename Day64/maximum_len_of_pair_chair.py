# https://leetcode.com/problems/maximum-length-of-pair-chain/

"""
Time complexity:- O(N logN)
Space Complexity:- O(1) 
"""

"""
Intuition:

The code sorts the pairs based on the second element (tail) in ascending order.
It iterates through the sorted pairs, selecting pairs such that the head is greater than the current tail.
The length of the longest chain is updated accordingly.
"""


import math
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Get the length of the pairs.
        N = len(pairs)

        # Sort the pairs based on the second element (tail) in ascending order.
        pairs.sort(key=lambda x: x[1])

        # Initialize variables to keep track of the answer and the current tail value.
        longest_chain = 0
        current_tail = -math.inf

        # Iterate through the sorted pairs.
        for head, tail in pairs:
            # If the head is greater than the current tail, update the current tail and increment the answer.
            if head > current_tail:
                current_tail = tail
                longest_chain += 1

        # Return the length of the longest chain.
        return longest_chain
