# https://leetcode.com/problems/maximum-width-of-binary-tree/

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


from collections import deque
from typing import List, Optional


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Create a queue 'q' to keep track of nodes, starting with an index of 0 for the root node.
        q = [(0, root)]
        ans = 0

        # Start a loop while there are nodes in the queue.
        while q:
            n = len(q)
            # Create a list 'nodes' to store indexes of all nodes at the current level.
            nodes = []

            # Process nodes at the current level.
            for _ in range(n):
                idx, node = q.pop(0)
                nodes.append(idx)

                # Add left and right children to the queue with updated indexes.
                if node.left:
                    q.append((2 * idx + 1, node.left))
                if node.right:
                    q.append((2 * idx + 2, node.right))

            # Update 'ans' with the maximum width of the current level.
            ans = max(ans, max(nodes) - min(nodes) + 1)

        # Return the maximum width found in the binary tree.
        return ans
