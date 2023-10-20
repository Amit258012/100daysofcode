# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

"""
Time complexity:- O(n)
Space Complexity:- O(M) maximum number of nodes at any level 
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import List, Optional


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty (root is None), return an empty list.
        if not root:
            return []

        # Initialize a deque called 'queue' with the root node.
        queue = deque([root])

        # Initialize 'result' to store the final zigzag level order traversal and 'direction' for zigzag direction.
        result, direction = [], 1

        # Perform level order traversal with zigzag direction.
        while queue:
            level = []

            # Process nodes at the current level.
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                # Add left and right children to the queue if they exist.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Append the current level with the appropriate direction to the 'result'.
            result.append(level[::direction])

            # Change the direction for the next level (zigzag).
            direction *= -1

        # Return the final zigzag level order traversal.
        return result
