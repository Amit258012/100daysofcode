# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

"""
Time complexity:- O(N logN)
Space Complexity:- O(1) 
"""

"""
Intuition:

The algorithm aims to find the minimum number of platforms required to accommodate all trains without any waiting time.
It uses two pointers to traverse the sorted arrival and departure times, dynamically adjusting the count of platforms needed.
"""


class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, n, arr, dep):
        # Sort the arrival and departure times to easily track the intervals.
        arr.sort()
        dep.sort()

        ans = 1  # Initialize the result with at least one platform.
        count = 1  # Initialize the count of platforms needed.
        i = 1  # Pointer for arrival times.
        j = 0  # Pointer for departure times.

        # Iterate through the intervals.
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:
                # If the next train arrives before or at the same time as the
                # departure of the current train, one more platform is needed.
                count += 1
                i += 1
            else:
                # If the next train arrives after the departure of the current
                # train, one platform can be reduced.
                count -= 1
                j += 1
            ans = max(ans, count)  # Update the result with the current maximum.

        return ans
