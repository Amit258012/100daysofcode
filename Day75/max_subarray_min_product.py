# https://leetcode.com/problems/maximum-subarray-min-product/
"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""

"""
Intuition:

The code aims to find the maximum sum of the product of the minimum element in a subarray and the sum of the subarray.
It uses a stack to efficiently calculate the sum of the product by maintaining the increasing order of elements.
The stack keeps track of the index and prefix sum of each element in a non-decreasing subarray. Whenever a smaller element is encountered, the algorithm calculates the product with the sum of the corresponding subarray, updating the result if necessary.
The final result is the maximum sum of the product of the minimum element and subarray sum, modulo 10^9 + 7.
"""

from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod = int(1e9 + 7)
        stack = []  # Stack to store (index, prefix sum at index)
        rsum = 0  # Running sum of the array
        res = 0  # Result to be returned

        # Add a sentinel element to handle the case where the entire array is non-decreasing.
        nums.append(0)

        for i, v in enumerate(nums):
            while stack and nums[stack[-1][0]] >= v:
                index, _ = stack.pop()

                # If the stack is empty, the subarray sum is the current prefix sum
                arrSum = rsum

                if stack:
                    arrSum = rsum - stack[-1][1]

                # Update res with the product of the minimum element and subarray sum
                res = max(res, nums[index] * arrSum)

            rsum += v
            stack.append((i, rsum))

        # Return the result modulo 10^9 + 7
        return res % mod
