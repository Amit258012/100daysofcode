# https://leetcode.com/problems/binary-tree-postorder-traversal/

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []  # If the tree is empty, return an empty list.

        res = []  # Initialize a list to store the traversal result.

        def postorder(root):
            if root:
                postorder(root.left)  # Recursively traverse the left subtree.
                postorder(root.right)  # Recursively traverse the right subtree.
                # Visit the current node and add its value to the result.
                res.append(root.val)

        postorder(root)  # Start the traversal with the root node.

        return res  # Return the list containing the postorder traversal result.
