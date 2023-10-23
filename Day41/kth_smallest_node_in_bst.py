# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

"""
Time complexity:- O(H+k)
Space Complexity:- O(H)
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize an empty stack and a current node 'curr' starting from the root.
        stack = []
        curr = root

        while stack or curr:
            while curr:
                # Traverse to the leftmost node, pushing all nodes encountered onto the stack.
                stack.append(curr)
                curr = curr.left

            # Pop the top node from the stack.
            curr = stack.pop()

            # Decrement 'k' to keep track of how many elements have been visited.
            k -= 1

            # If 'k' becomes 0, return the value of the current node.
            if k == 0:
                return curr.val

            # Move to the right subtree of the current node.
            curr = curr.right
