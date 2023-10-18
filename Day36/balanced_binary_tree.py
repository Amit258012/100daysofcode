# https://leetcode.com/problems/balanced-binary-tree/

"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True  # An empty tree is considered balanced.

        # Check if the left and right subtrees are balanced and their heights differ by at most 1.
        left_height = self.depth(root.left)
        right_height = self.depth(root.right)
        is_left_balanced = self.isBalanced(root.left)
        is_right_balanced = self.isBalanced(root.right)

        return (
            (abs(left_height - right_height) < 2)
            and is_left_balanced
            and is_right_balanced
        )

    def depth(self, node):
        if node == None:
            return 0  # The height of an empty subtree is 0.

        # Calculate the height of the subtree recursively as the maximum height of the left and right subtrees plus 1.
        return max(self.depth(node.left), self.depth(node.right)) + 1
