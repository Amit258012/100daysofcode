# https://leetcode.com/problems/next-greater-element-i/

"""
Time complexity:- O(n+m)
Space Complexity:- O(n)
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a dictionary to store the indices of elements in nums1
        nums1Idx = {n: i for i, n in enumerate(nums1)}

        # Initialize the result list with -1 for each element in nums1
        res = [-1] * len(nums1)

        # Initialize an empty stack to help with finding the next greater element
        stack = []

        # Iterate through the elements in nums2
        for i in range(len(nums2)):
            cur = nums2[i]  # Current element in nums2

            # While the stack is not empty and the current element is greater than
            # the top element of the stack, pop elements from the stack and update
            # their next greater element in the result list.
            while stack and cur > stack[-1]:
                val = stack.pop()  # Take the top element from the stack
                idx = nums1Idx[val]  # Get its index in nums1
                res[idx] = cur  # Update the result for that index

            # If the current element is in nums1, push it onto the stack.
            if cur in nums1Idx:
                stack.append(cur)

        # Return the result list containing the next greater elements for nums1.
        return res
