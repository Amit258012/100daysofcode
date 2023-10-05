# https://www.codingninjas.com/studio/problems/immediate-smaller-element-_1062597?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1

"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""

from typing import List


def immediateSmaller(a: List[int]) -> None:
    n = len(a)

    # Iterate through the elements, except the last one
    for i in range(n - 1):
        # Check if the next element is smaller
        if a[i + 1] < a[i]:
            a[i] = a[i + 1]  # Replace with the smaller element
        else:
            a[i] = -1  # Set to -1 if no smaller element to the right

    # The last element is always set to -1
    a[-1] = -1
