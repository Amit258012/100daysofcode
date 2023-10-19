# https://leetcode.com/problems/diameter-of-binary-tree/

"""
Time complexity:- O(n)
Space Complexity:- O(h) call stack height  
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize a variable maxRes to store the maximum diameter encountered.
        maxRes = 0

        # Define a helper function named diameter that calculates the diameter of the binary tree.
        def diameter(root):
            # Use the nonlocal keyword to modify the maxRes variable from the outer scope.
            nonlocal maxRes

            # If the current node is None, return 0.
            if not root:
                return 0

            # Recursively calculate the heights of the left and right subtrees.
            lh = diameter(root.left)
            rh = diameter(root.right)

            # Update maxRes with the maximum diameter found so far, which can be the sum of
            # heights of the left and right subtrees.
            maxRes = max(maxRes, lh + rh)

            # Return the height of the current subtree (the longer path).
            return 1 + max(lh, rh)

        # Call the diameter function on the root node to calculate the diameter of the tree.
        diameter(root)

        # Return the maximum diameter encountered during the traversal.
        return maxRes
