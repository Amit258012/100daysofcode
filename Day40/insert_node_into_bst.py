# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

"""
Time complexity:- O(H)
Space Complexity:- O(H)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root, val):
        # If the tree is empty (root is None), create a new node with the given value 'val'.
        if not root:
            return TreeNode(val)

        # Compare the value 'val' with the current node's value to determine whether to insert it in the left or right subtree.
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        # Return the root of the modified BST.
        return root
