# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

"""
Time complexity:- O(H)
Space Complexity:- O(1)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while True:
            # If the current root value is less than both p and q, the LCA must be in the right subtree.
            if root.val < p.val and root.val < q.val:
                root = root.right
            # If the current root value is greater than both p and q, the LCA must be in the left subtree.
            elif root.val > p.val and root.val > q.val:
                root = root.left
            # If the current root value is between p and q, or equal to either of them, it is the LCA.
            else:
                return root
