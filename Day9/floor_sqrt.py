"""
Find the floor sqrt of the given number 
"""

"""
Time Complexity:- O(logn)
Space Complexity:- o(1)
"""


def floorSqrt(n):
    # Initialize the left and right pointers for binary search.
    low = 1
    high = n

    while low <= high:
        # Calculate the middle value.
        mid = (low + high) // 2

        if mid * mid <= n:
            # If mid^2 is less than or equal to 'n', update the left pointer.
            low = mid + 1
        else:
            # Otherwise, update the right pointer.
            high = mid - 1

    # The 'high' pointer represents the floor square root of 'n'.
    return high
