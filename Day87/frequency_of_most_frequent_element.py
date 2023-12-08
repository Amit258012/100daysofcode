# https://leetcode.com/problems/frequency-of-the-most-frequent-element/
"""
Time complexity:- O(N logN)
Space Complexity:- O(1)
"""

"""
Intuition:

The algorithm uses a sliding window approach to find the maximum frequency of an element with the allowed difference k.
It maintains a window by adjusting the left and right pointers based on the sum of elements in the window.
The result is updated whenever a larger window is found.
Example: For the input [1, 2, 2, 3] and k=1, the maximum frequency is 2 (for element 2). The window would be [2, 2].
"""


from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the array in ascending order
        nums.sort()

        # Initialize pointers and variables
        left = 0  # Left pointer
        res = 0  # Result variable to store the maximum frequency
        cur = 0  # Variable to keep track of the current sum in the sliding window

        # Iterate through the array using the right pointer
        for right in range(len(nums)):
            target = nums[right]  # Current element in the sorted array
            cur += target  # Add the current element to the sum

            # Check if the current sum exceeds the allowed difference (k)
            while (right - left + 1) * target - cur > k:
                cur -= nums[left]  # Adjust the sum by removing the leftmost element
                left += 1  # Move the left pointer to the right

            # Update the result with the maximum window size
            res = max(res, right - left + 1)

        # The final 'res' represents the maximum frequency of an element
        return res
