# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

"""
Time complexity:- O(N)
Space Complexity:- O(N) Auxilary space (Function CallStack)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


def flatten(self, root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    self.prevRight = None

    # Define a helper function named 'helper' for recursive processing.
    def helper(root):
        if root:
            # Recursive call to process the right subtree first.
            helper(root.right)
            # Recursive call to process the left subtree.
            helper(root.left)
            # Reorder the tree nodes to make the current node the right child of 'self.prevRight'.
            root.right, self.prevRight = self.prevRight, root
            root.left = None

    # Start the recursion from the root node.
    helper(root)
