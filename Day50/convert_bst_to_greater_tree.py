# https://leetcode.com/problems/convert-bst-to-greater-tree/

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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum = 0  # Initialize a variable to keep track of the cumulative sum.

        # Define a recursive in-order traversal function.
        def dfs(node):
            if not node:
                return

            nonlocal curSum  # Use the 'curSum' variable from the outer scope.

            # Traverse the right subtree first, as it contains greater values.
            dfs(node.right)

            temp = node.val  # Store the current node's value in 'temp'.
            node.val += curSum  # Update the current node's value.
            curSum += temp  # Update the cumulative sum with 'temp'.

            # Traverse the left subtree, using the updated value for 'node.val'.
            dfs(node.left)

        dfs(root)  # Start the in-order traversal with the root node.
        return root  # Return the converted Greater Tree.
