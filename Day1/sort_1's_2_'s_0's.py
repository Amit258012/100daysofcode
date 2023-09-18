"""
    Sort an array containing 0s, 1s, and 2s in-place using the Dutch National Flag algorithm.

    Args:
        arr (List[int]): The input list containing 0s, 1s, and 2s.

    Returns:
        None: The function modifies the 'arr' in-place and does not return anything.
"""
"""
Time Complexity:- O(n)
Space Complexity:- O(1)
"""


class Solution:
    def sortColors(self, arr):
        # Initialize pointers for the low, mid, and high segments of the array.
        low = 0
        mid = 0
        high = len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                # If the current element is 0, swap it with the element at the 'low' pointer.
                arr[low], arr[mid] = arr[mid], arr[low]
                mid += 1
                low += 1
            elif arr[mid] == 1:
                # If the current element is 1, move the 'mid' pointer forward.
                mid += 1
            else:
                # If the current element is 2, swap it with the element at the 'high' pointer
                # and move the 'high' pointer backward.
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
