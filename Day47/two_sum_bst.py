# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

"""
Time complexity:- O(N)
Space Complexity:- O(N)
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Create a dictionary 'vals' to store values encountered during traversal.
        vals = {}

        # Define a helper function for DFS.
        def helper(node):
            if not node:
                return False
            if node.val in vals:
                return True  # If a complement exists, return True.

            # Store the complement of the current node's value.
            vals[k - node.val] = True

            # Recursively search in the left and right subtrees.
            return helper(node.left) or helper(node.right)

        return helper(root)
