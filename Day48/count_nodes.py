# https://leetcode.com/problems/count-complete-tree-nodes/

"""
Time complexity:- O(N)
Space Complexity:- O(H) Auxilary space (Function CallStack)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from typing import Optional


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # If the root is None, the tree is empty, so return 0.
        if not root:
            return 0
        # Recursively count nodes in the left and right subtrees, and add 1 for the current node.
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
