"""
        Search for the target element in the sorted 'nums' list and return its index or the index
        where it should be inserted to maintain the sorted order.

        Args:
            nums (List[int]): The input sorted list of integers.
            target (int): The target integer to search for.

        Returns:
            int: The index of the target element if found, or the index where it should be inserted.
"""

"""
Time Complexity:- O(nlog(n))
Space Complexity:- O(1)
"""


class Solution:
    def searchInsert(self, nums, target):
        # Handle the case where the 'nums' list is empty.
        if not nums:
            return 0

        n = len(nums)
        left = 0
        right = n - 1
        ans = n  # Initialize the answer to the last index in case the target is greater than all elements.

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                # If the middle element is greater or equal to the target, update the answer
                # and search in the left half.
                ans = mid
                right = mid - 1
            else:
                # If the middle element is less than the target, search in the right half.
                left = mid + 1

        return ans
