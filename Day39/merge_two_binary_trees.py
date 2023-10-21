# https://leetcode.com/problems/merge-two-binary-trees/

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
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]):
        # If both t1 and t2 are None (empty trees), return None (no merging needed).
        if not t1 and not t2:
            return None

        # Create a new TreeNode 'ans' with the value equal to the sum of values of t1 and t2
        # (if they exist, otherwise use 0 for empty trees).
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))

        # Recursively merge the left and right subtrees of t1 and t2 and assign them to 'ans'.
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)

        # Return the merged TreeNode 'ans'.
        return ans
