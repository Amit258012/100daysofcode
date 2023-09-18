"""
        Remove duplicates from a sorted 'nums' list in-place and return the length of the resulting unique list.

        Args:
            nums (List[int]): The input sorted list of integers with duplicates.

        Returns:
            int: The length of the resulting unique list after removing duplicates.
        """


class Solution:
    def removeDuplicates(self, nums):
        unique_count = 1  # Initialize a count for unique elements.
        last_unique = nums[0]  # Initialize with the first element.

        for i in range(1, len(nums)):
            current = nums[i]

            if current != last_unique:
                # If the current element is different from the last unique element,
                # update the next unique position, copy the current element there,
                # and update the last unique element.
                nums[unique_count] = current
                unique_count += 1
                last_unique = current

        return unique_count
