# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

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


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            # Initialize 'res' to 1 if the current node's value is greater than or equal to 'maxVal', else 0.
            res = 1 if node.val >= maxVal else 0

            # Update 'maxVal' with the maximum value encountered so far.
            maxVal = max(maxVal, node.val)

            # Recursively count the "good" nodes in the left and right subtrees and add them to 'res'.
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        # Start the traversal from the root with the initial maximum value 'maxVal' set to the root's value.
        return dfs(root, root.val)
