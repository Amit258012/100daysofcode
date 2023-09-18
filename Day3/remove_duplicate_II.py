"""
        Remove duplicates from a sorted 'nums' list, allowing at most two duplicates for each unique element.

        Args:
            nums (List[int]): The input sorted list of integers with duplicates.

        Returns:
            int: The length of the resulting list after removing duplicates.
"""


class Solution:
    def removeDuplicates(self, nums):
        i = 0  # Initialize a pointer for the current position to insert elements.

        for n in nums:
            if i < 2 or n > nums[i - 2]:
                # If the current element is not a duplicate (i < 2) or it's greater than the element
                # two positions back, it's allowed to stay in the list.
                nums[i] = n
                i += 1

        return i
