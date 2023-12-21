# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
"""
Time complexity:- O(N logM)
Space Complexity:- O(1) 
"""

"""
Intuition:

The minimizeMax method uses binary search to find the minimum threshold such that there are at least p valid pairs.
The countValidPairs function counts the number of valid pairs with a given threshold.
The binary search is performed on the range of possible thresholds, adjusting the search space based on the count of valid pairs.
"""


from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # Sort the given array in ascending order
        nums.sort()
        n = len(nums)

        # Function to count the number of valid pairs with a given threshold
        def countValidPairs(threshold):
            index, count = 0, 0
            while index < n - 1:
                # If a valid pair is found, skip both numbers.
                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            return count

        # Initialize the binary search range
        left, right = 0, nums[-1] - nums[0]

        # Perform binary search to find the minimum threshold
        while left < right:
            mid = left + (right - left) // 2

            # If there are enough pairs, look for a smaller threshold.
            # Otherwise, look for a larger threshold.
            if countValidPairs(mid) >= p:
                right = mid
            else:
                left = mid + 1

        # The final result is the left boundary of the binary search range
        return left
