"""
Find how many times the sorted array is rotated
"""

"""
Time Complexity:- O(logn)
Space Complexity:- o(1)
"""
from typing import List


def findKRotation(arr: List[int]) -> int:
    # Get the length of the input array 'arr'.
    n = len(arr)

    # Initialize the left and right pointers, 'ans' to positive infinity, and 'index' to -1.
    l = 0
    h = n - 1
    ans = float("inf")
    index = -1

    while l <= h:
        # Calculate the middle index.
        mid = (l + h) // 2

        if arr[l] <= arr[mid]:
            # If the left half is sorted, update 'ans' and 'index' if necessary, and move the left pointer.
            if arr[l] < ans:
                ans = arr[l]
                index = l
            l = mid + 1
        else:
            # The right half is sorted, so update 'ans' and 'index' if necessary, and move the right pointer.
            if arr[mid] < ans:
                ans = arr[mid]
                index = mid
            h = mid - 1

    # Return the 'index,' which represents the number of rotations.
    return index
