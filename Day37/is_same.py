# https://leetcode.com/problems/same-tree/

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if both p and q are None (empty trees).
        if not p and not q:
            return True
        # If one of p or q is None, or their values are not equal, the trees are not the same.
        if not p or not q or p.val != q.val:
            return False
        # Recursively call isSameTree on the left and right subtrees of p and q,
        # to check if they are the same.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
