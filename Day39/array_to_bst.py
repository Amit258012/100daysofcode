# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

"""
Time complexity:- O(N)
Space Complexity:- O(H)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        # If the list is empty, return None (an empty tree).
        if not n:
            return None

        # Calculate the index of the middle element in the sorted array.
        midNode = n // 2

        # Create a TreeNode with the value of the middle element and
        # recursively build the left and right subtrees using slices of the input list.
        return TreeNode(
            nums[midNode],
            self.sortedArrayToBST(nums[:midNode]),
            self.sortedArrayToBST(nums[midNode + 1 :]),
        )
