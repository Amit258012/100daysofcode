# https://leetcode.com/problems/binary-tree-preorder-traversal/

"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # Initialize a list to store the traversal result.

        if not root:
            return res  # If the tree is empty, return an empty list.

        def preorder(root):
            if root:
                res.append(
                    root.val
                )  # Visit the current node and add its value to the result.
                preorder(root.left)  # Recursively traverse the left subtree.
                preorder(root.right)  # Recursively traverse the right subtree.

        preorder(root)  # Start the traversal with the root node.

        return res  # Return the list containing the preorder traversal result.
