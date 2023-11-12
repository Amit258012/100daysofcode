# https://leetcode.com/problems/hand-of-straights/

"""
Time complexity:- O(N logN)
Space Complexity:- O(N) 
"""

"""
Intuition:

First, the code checks if it's possible to evenly divide the hand into groups of the given size. If not, the function returns False.
It uses a frequency dictionary to count the occurrences of each unique number in the hand.
The code maintains a minHeap to keep track of the unique numbers in ascending order.
It iterates through each unique number, checks consecutive numbers, and updates the frequency information.
If the loop completes without any issues, it means the hand can be divided into groups satisfying the conditions, and the function returns True.
"""

import collections
import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Check if the length of the hand is divisible by the groupSize
        if len(hand) % groupSize:
            return False

        # Dictionary to store the frequency of each unique number in the hand
        freq = collections.defaultdict(int)

        # Count the frequency of each unique number in the hand
        for num in hand:
            freq[num] += 1

        # Min heap to store unique numbers in ascending order
        minHeap = list(freq.keys())
        heapq.heapify(minHeap)

        # Iterate until the minHeap is not empty
        while minHeap:
            # Get the smallest number from the heap
            smallest = minHeap[0]

            # Iterate through consecutive numbers in the group
            for num in range(smallest, smallest + groupSize):
                # Check if the current number is present in the frequency dictionary
                if num not in freq:
                    return False

                # Decrease the frequency of the current number
                freq[num] -= 1

                # Remove the number from the heap if its frequency becomes zero
                if freq[num] == 0:
                    if num != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        # If the loop completes, the hand can be divided into groups satisfying the conditions
        return True
