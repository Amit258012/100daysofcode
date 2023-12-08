# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""

"""
Intuition:

The function aims to count the number of subarrays of size k in the given array arr such that the average of the subarray is greater than or equal to the provided threshold.
It uses a sliding window approach to efficiently compute the sum of each subarray.
The variable curSum is used to keep track of the sum of the current window.
The function iterates through the array, updating the current sum for each window and checking the average.
The result is the count of subarrays satisfying the given condition.
"""


from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Initialize variables to store the result, current sum, and length of the array
        res = 0
        curSum = sum(arr[: k - 1])  # Initialize the sum of the first k-1 elements
        n = len(arr)

        # Iterate through the array, considering each window of size k
        for l in range(n - k + 1):
            curSum += arr[l + k - 1]  # Add the next element to the current sum
            # Check if the average of the current window is greater than or equal to the threshold
            if (curSum / k) >= threshold:
                res += 1  # Increment the result counter
            curSum -= arr[l]  # Subtract the leftmost element of the current window

        # Return the final result
        return res
