# https://leetcode.com/problems/binary-tree-level-order-traversal/

"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []  # Initialize a list to store the level-order traversal result.

        # Create a deque (double-ended queue) for performing level-order traversal.
        q = collections.deque()
        if root:
            q.append(root)  # If the root exists, add it to the deque.

        while q:
            levelVal = []  # Initialize a list to store values at the current level.

            for i in range(len(q)):
                node = q.popleft()  # Remove the leftmost node from the deque.
                # Add the value of the current node to the level values list.
                levelVal.append(node.val)
                if node.left:
                    q.append(node.left)  # Add the left child to the deque if it exists.
                if node.right:
                    # Add the right child to the deque if it exists.

                    q.append(node.right)
            # Add the values at the current level to the result list.
            res.append(levelVal)

        return res  # Return the list containing the level-order traversal result.
