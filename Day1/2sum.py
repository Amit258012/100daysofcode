"""
    Find two numbers in the 'nums' list that add up to the 'target' value.

    Args:
        nums (List[int]): List of integers.
        target (int): The target sum.

    Returns:
    List[int]: A list containing the indices of the two numbers that add up to the target.
"""


def twoSum(self, nums, target):
    # Create a dictionary to store the mapping of values to their indices.
    value_index_dict = {}

    # Iterate through the list 'nums' with both the value and its index.
    for i, num in enumerate(nums):
        # Calculate the remaining value needed to reach the target.
        remaining = target - num

        # Check if the remaining value is in the dictionary.
        if remaining in value_index_dict:
            # If found, return the indices of the two numbers that add up to the target.
            return [value_index_dict[remaining], i]

        # Add the current number and its index to the dictionary.
        value_index_dict[num] = i

    # If no solution is found, return an empty list.
    return []
