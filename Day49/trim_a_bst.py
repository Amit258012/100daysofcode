# https://leetcode.com/problems/trim-a-binary-search-tree/

"""
Time complexity:- O(N)
Space Complexity:- O(H)  H = height of BST (call stack )
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root, low, high):
        # Base case: If the root is None, return None (no tree).
        if not root:
            return None

        # If the current node's value is greater than 'high', trim the right subtree.
        if root.val > high:
            return self.trimBST(root.left, low, high)

        # If the current node's value is less than 'low', trim the left subtree.
        if root.val < low:
            return self.trimBST(root.right, low, high)

        # If the current node's value is within the [low, high] range, recursively trim both left and right subtrees.
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root  # Return the trimmed tree rooted at the current node.
