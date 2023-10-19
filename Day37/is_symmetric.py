# https://leetcode.com/problems/symmetric-tree/

"""
Time complexity:- O(n)
Space Complexity:- O(h) call stack height  
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isSame(self, l, r):
        # If both l and r are None, return True (empty trees are symmetric).
        if not l and not r:
            return True
        # If one of l or r is None or their values are not equal, return False (not symmetric).
        if not l or not r or l.val != r.val:
            return False
        # Recursively call isSame on the left subtree of l and the right subtree of r,
        # and on the right subtree of l and the left subtree of r, to check for symmetry.
        return self.isSame(l.left, r.right) and self.isSame(l.right, r.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # If the tree is empty (root is None), it's symmetric.
        if not root:
            return True
        # Call the isSame method to check if the left and right subtrees of the root are symmetric.
        return self.isSame(root.left, root.right)
