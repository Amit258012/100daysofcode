"""
Find the Nth root  of given number 
"""

"""
Time Complexity:- O(logn)
Space Complexity:- o(1)
"""


def NthRoot(n: int, m: int) -> int:
    # Initialize the result 'ans' to -1, and the left and right pointers for binary search.
    ans = -1
    low = 1
    high = m

    while low <= high:
        # Calculate the middle value.
        mid = (low + high) // 2

        # Calculate the value of mid raised to the power of n.
        val = mid**n

        if val == m:
            # If the calculated value matches 'm', set 'ans' and return it.
            ans = mid
            return ans
        elif val < m:
            # If val is less than 'm', update the left pointer.
            low = mid + 1
        else:
            # If val is greater than 'm', update the right pointer.
            high = mid - 1

    # Return the final result 'ans'.
    return ans
