# https://leetcode.com/problems/maximum-product-subarray/
"""
Time complexity:- O(N) 
Space Complexity:- O(1) 
"""

"""
Intuition:

The maxProduct function iterates through the array, keeping track of the current minimum and maximum products.
At each step, it updates these values considering the current element.
The result is continuously updated with the maximum product encountered so far.
"""


from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the current minimum and maximum products.
        res = nums[0]
        curMin, curMax = 1, 1

        # Iterate through the array.
        for n in nums:
            # Update the current maximum and minimum products considering the current element.
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)

            # Update the overall result with the maximum product encountered so far.
            res = max(res, curMax)

        # Return the maximum product.
        return res
