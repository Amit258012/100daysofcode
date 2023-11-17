# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:

The goal is to find the maximum score by choosing a subarray of size k to remove from the original array.
By utilizing a sliding window, the algorithm efficiently updates the sum (S) based on the addition and removal of elements at the window's boundaries.
The final result (ans) represents the maximum score achievable after removing k cards.
"""


from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Calculate the size of the subarray to be removed
        size = len(cardPoints) - k
        # Initialize S with the sum of the elements in the subarray to be removed
        S = sum(cardPoints[size:])
        # Initialize ans with the current value of S
        ans = S

        # Iterate over the range [0, k) using a sliding window approach
        for i in range(0, k):
            # Add the current element at index i to S
            S += cardPoints[i]
            # Subtract the element at index i+size from S (removing it from the subarray)
            S -= cardPoints[i + size]
            # Update ans to be the maximum of its current value and the updated S
            ans = max(ans, S)

        # The final result is the maximum value of ans, representing the maximum score
        return ans
