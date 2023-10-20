# https://leetcode.com/problems/subtree-of-another-tree/

"""
Time complexity:- O(N*M) N is the number of nodes in the tree s, and M is the number of nodes in the tree t
Space Complexity:- O(max(N,M))
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        # If t is None (empty tree), it is considered a subtree of any tree.
        if not t:
            return True

        # If s is None (empty tree) but t is not, t cannot be a subtree of s.
        if not s:
            return False

        # Check if t is the same as the current tree rooted at s, or if t is a subtree of the left or right subtree of s.
        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    # Define a helper method named sameTree that checks if two binary trees, s and t, are the same.
    def sameTree(self, s, t):
        # If both s and t are None (empty trees), they are considered the same.
        if not s and not t:
            return True

        # If both s and t exist and have the same value at the current node,
        # check if their left and right subtrees are the same.
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)

        # If the conditions above are not met, the trees are not the same.
        return False
