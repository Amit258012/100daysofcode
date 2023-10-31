# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

"""
Time complexity:- O(N)
Space Complexity:- O(N)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        arr = []  # Initialize an empty array to store node values.

        # Define an in-order traversal function to populate the 'arr' with node values.
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        inorder(root)  # Populate the 'arr' by performing in-order traversal.

        res = float("inf")  # Initialize a variable to store the minimum difference.

        # Iterate through the sorted 'arr' to find the minimum difference between adjacent values.
        for i in range(1, len(arr)):
            res = min(res, arr[i] - arr[i - 1])

        return res  # Return the minimum difference.
