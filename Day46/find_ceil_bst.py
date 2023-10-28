# https://practice.geeksforgeeks.org/problems/implementing-ceil-in-bst/1

"""
Time complexity:- O(H)
Space Complexity:- O(H) Auxilary space (Function CallStack)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findCeil(self, root, x, ceil=-1):
        # If the root is None, return the current 'ceil' value.
        if not root:
            return ceil

        # If the current node's val matches the input value, return the val.
        if root.val == x:
            return root.val

        # If the current node's val is greater than the input value, update 'ceil' and
        # recursively search in the left subtree.
        if root.val > x:
            ceil = root.val
            return self.findCeil(root.left, x, ceil)
        # If the current node's val is less than the input value, search in the right subtree.
        else:
            return self.findCeil(root.right, x, ceil)
