# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

"""
Time complexity:- O(N)
Space Complexity:- O(H) Auxilary space
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # If the root is one of the nodes p or q, it is the LCA.
        if root == p or root == q:
            return root

        left = right = None

        # Recursively search for p and q in the left and right subtrees.
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are not None, the LCA is the current root.
        if left and right:
            return root
        else:
            # If either left or right is not None, return that non-null value as a candidate for LCA.
            return left or right
