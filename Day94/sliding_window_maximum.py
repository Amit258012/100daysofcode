# https://leetcode.com/problems/sliding-window-maximum/
"""
Time complexity:- O(N)
Space Complexity:- O(k)
"""

"""
Intuition:

The code uses a sliding window approach with a deque to efficiently find the maximum values in each window.
The deque (q) stores indices of elements in the current window.
While moving the window to the right, we maintain the deque such that it only contains indices of elements in descending order of values.
The left pointer (l) is incremented to simulate the movement of the window, and the right pointer (r) is incremented to process the next element.
The maximum value in each window is obtained from the front of the deque (nums[q[0]]) and appended to the output list when the window size is equal to k.
"""


import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []  # List to store the maximum values in each sliding window
        # Deque to store indices of elements in the current window
        q = collections.deque()
        l = r = 0  # Pointers for the left and right ends of the window

        while r < len(nums):
            # Pop indices of smaller values from the back of the deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)  # Append the current index to the deque

            # Remove the leftmost index if it's outside the current window
            if l > q[0]:
                q.popleft()

            # If the window size is equal to k, append the maximum value to the output
            if (r + 1) >= k:
                output.append(nums[q[0]])

            # Move the window to the right
            l += 1
            r += 1

        return output
