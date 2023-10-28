# https://practice.geeksforgeeks.org/problems/floor-in-bst/1

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
    def floor(self, root, x, floor=-1):
        # If the current node is None, return the current 'floor' value.
        if not root:
            return floor

        # If the current node's val matches the input 'x', return the val.
        if root.val == x:
            return root.val

        # If the current node's val is less than 'x', update 'floor' and
        # recursively search in the right subtree.
        if root.val < x:
            floor = root.val
            return self.floor(root.right, x, floor)
        # If the current node's val is greater than 'x', search in the left subtree.
        else:
            return self.floor(root.left, x, floor)
