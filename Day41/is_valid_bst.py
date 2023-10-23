# https://leetcode.com/problems/validate-binary-search-tree/

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Define a helper method named 'valid' that checks if a given node is a valid BST node within a given range.
        def valid(node, left, right):
            # If the current node is None, it is a valid BST node.
            if not node:
                return True
            # If the current node's value is not within the specified range, it is not a valid BST node.
            if not (left < node.val < right):
                return False

            # Recursively check the left and right subtrees, updating the range accordingly.
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        # Start the validation process with an initial range from negative infinity to positive infinity.
        return valid(root, float("-inf"), float("inf"))
