"""
    Returns a list of elements in 'a' that are greater than all elements to their right.

    Args:
    a (List[int]): The input list of integers.

    Returns:
    List[int]: A list of superior elements in 'a'.
    
"""

from typing import List


class Solution:
    def superiorElements(a: List[int]) -> List[int]:
        # Initialize an empty list to store superior elements.
        superior_elements = []

        # Get the length of the input list.
        n = len(a)

        # Initialize the maximum element as the last element in the list.
        max_element = a[n - 1]

        # Append the maximum element to the result list since there are no elements to the right of it.
        superior_elements.append(max_element)

        # Iterate through the list in reverse order (from right to left).
        for i in range(n - 2, -1, -1):
            # Check if the current element is greater than the current maximum element.
            if a[i] > max_element:
                # If it is, append it to the result list and update the maximum element.
                superior_elements.append(a[i])
                max_element = a[i]

        # Return the list of superior elements.
        return superior_elements
