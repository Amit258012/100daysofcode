# https://leetcode.com/problems/binary-search-tree-iterator/

"""
Time complexity:- O(N)
Space Complexity:- O(N)
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        # Initialize the stack to store nodes for in-order traversal.
        self.stack = []
        # Start by pushing left nodes of the root onto the stack.
        self.pushLeftNodes(root)

    def next(self) -> int:
        # Pop the top node from the stack.
        temp = self.stack.pop()
        # Push the left nodes of the right child of the popped node onto the stack.
        self.pushLeftNodes(temp.right)
        # Return the value of the popped node.
        return temp.val

    def hasNext(self) -> bool:
        # Check if there are still elements in the stack to visit.
        return bool(self.stack)

    def pushLeftNodes(self, node):
        # Helper method to push all left nodes onto the stack.
        while node:
            self.stack.append(node)
            node = node.left
