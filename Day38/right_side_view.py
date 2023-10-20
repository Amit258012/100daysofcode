# https://leetcode.com/problems/binary-tree-right-side-view/

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize a deque called 'queue'.
        queue = deque()

        # If the tree is empty (root is None), return an empty list.
        if root is None:
            return []

        # If the root has no left or right children, return a list containing the root's value.
        if root.left is None and root.right is None:
            return [root.val]

        # Initialize an empty list 'result' to store the right side view.
        result = []

        # Initialize the queue with the root node.
        queue.append(root)

        # Perform a level-order traversal while keeping track of the rightmost node at each level.
        while queue:
            # Create a child_queue for the next level.
            child_queue = deque()

            # Initialize 'prev' to keep track of the rightmost node.
            prev = -1

            # Process nodes at the current level.
            while queue:
                curr = queue.popleft()

                # Add left and right children to the child_queue if they exist.
                if curr.left is not None:
                    child_queue.append(curr.left)

                if curr.right is not None:
                    child_queue.append(curr.right)

                # Update 'prev' with the current node.
                prev = curr

            # Append the value of the rightmost node to the 'result'.
            result.append(prev.val)

            # Update the 'queue' with the child_queue for the next level.
            queue = child_queue

        # Return the list containing the right side view of the tree.
        return result
