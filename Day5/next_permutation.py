"""
        Modify 'nums' in-place to find the next lexicographically greater permutation.
        
        Args:
            nums (List[int]): The input list of integers.

        Returns:
            None: The function modifies 'nums' in-place and does not return anything.
"""


from typing import List  # Import the List data type from the typing module.


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        index = -1

        # Step 1: Find the break point.
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:  # Break point found.
                index = i
                break

        # If the break point doesn't exist, reverse the entire list (e.g., [3, 2, 1]).
        if index == -1:
            nums.reverse()
            return

        # Step 2: Find the next greater number in the right part and swap it with the number at the break point.
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        # Step 3: Reverse the right part to make it in ascending order.
        nums[index + 1 :] = reversed(nums[index + 1 :])
