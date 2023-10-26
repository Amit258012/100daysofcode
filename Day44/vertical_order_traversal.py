# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

"""
Time complexity:- O( Nlog(N) )
Space Complexity:- O(N) Auxilary space (Function CallStack)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict
from typing import List, Optional


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Create a defaultdict to store nodes based on their (position, depth) tuples.
        results = defaultdict(list)
        # Initialize a queue with the root node and its position and depth.
        queue = [(root, 0, 0)]

        while queue:
            node, pos, depth = queue.pop(0)
            if not node:
                continue
            # Append the value of the node to the corresponding (pos, depth) key and sort the values.
            results[(pos, depth)].append(node.val)
            results[(pos, depth)].sort()
            # Add the left and right children of the node to the queue with updated positions and depths.
            queue.extend(
                [(node.left, pos - 1, depth + 1), (node.right, pos + 1, depth + 1)]
            )

        # Create a defaultdict to store the final results based on positions.
        res = defaultdict(list)
        # Sort the keys based on position and depth.
        keys = sorted(list(results.keys()), key=lambda x: (x[0], x[1]))

        for k in keys:
            pos, depth = k
            # Extend the values of each position to the result dictionary.
            res[pos].extend(results[k])

        # Return the values from the result dictionary as a list of lists.
        return res.values()
