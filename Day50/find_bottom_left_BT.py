# https://leetcode.com/problems/find-bottom-left-tree-value/

"""
Time complexity:- O(N)
Space Complexity:- O(W) w= max width
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = 0  # Initialize a variable to store the leftmost value.
        q = deque([root])  # Initialize a queue with the root node.

        while q:
            level = []  # Initialize a list to store the values at the current level.
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)  # Add the left child to the queue.
                if node.right:
                    q.append(node.right)  # Add the right child to the queue.

            # Update the result with the leftmost value at the current level.
            res = level[0]

        return res  # Return the leftmost value found at the last level.
