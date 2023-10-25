# https://leetcode.com/problems/binary-tree-maximum-path-sum/

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


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Create a list 'res' to store the result (maximum path sum).
        res = root.val

        # Define a helper function named 'dfs' to perform depth-first traversal and compute the maximum path sum.
        def dfs(root):
            nonlocal res
            if not root:
                return 0

            # Recursively calculate the maximum path sum for the left and right subtrees.
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # If the computed values are negative, set them to 0 (choose not to include the subtree).
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Update 'res' with the maximum path sum considering the current node.
            res = max(res, root.val + leftMax + rightMax)

            # Return the maximum path sum considering the current node and one of its subtrees.
            return root.val + max(leftMax, rightMax)

        # Start the depth-first traversal from the root.
        dfs(root)

        # Return the maximum path sum stored in 'res'.
        return res
