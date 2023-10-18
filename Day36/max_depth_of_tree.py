# https://leetcode.com/problems/maximum-depth-of-binary-tree/

"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0  # If the tree is empty (root is None), the depth is 0.

        # Recursively calculate the maximum depth of the left and right subtrees.
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Return the maximum depth among the left and right subtrees, plus 1 for the current node.
        return max(left_depth, right_depth) + 1
