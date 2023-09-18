"""
        Move all zeroes in the 'nums' list to the end while maintaining the order of non-zero elements.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            None: The function modifies 'nums' in-place and does not return anything.
"""

"""
Time Complexity:- O(n)
Space Complexity:- O(1)
"""


class Solution:
    def moveZeroes(self, nums):
        slow = 0  # Initialize a pointer for the position to insert non-zero elements.

        for fast in range(len(nums)):
            if nums[slow] == 0 and nums[fast] != 0:
                # If the slow pointer points to a zero and the fast pointer points to a non-zero element,
                # swap the elements to move the non-zero element to the slow pointer position.
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                # If the slow pointer points to a non-zero element, increment the slow pointer.
                slow += 1
