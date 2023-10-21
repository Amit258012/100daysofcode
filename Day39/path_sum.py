# https://leetcode.com/problems/path-sum/

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


from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # If the tree is empty (root is None), there's no path with the target sum.
        if not root:
            return False

        # If the current node is a leaf node and its value matches the target sum, return True.
        if not root.left and not root.right and root.val == targetSum:
            return True

        # Update the targetSum by subtracting the current node's value.
        targetSum -= root.val

        # Recursively call hasPathSum on the left and right subtrees with the updated targetSum.
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )
