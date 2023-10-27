# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

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


from typing import List, Optional


class Solution:
    def buildTree(self, preorder, bound):
        # If the preorder list is empty or the last element is greater than the bound,
        # return None (no node to construct).
        if not preorder or preorder[-1] > bound:
            return None
        # Create a TreeNode using the last element in the preorder list.
        node = TreeNode(preorder.pop())
        # Recursively build the left subtree and set it as the left child of the current node.
        node.left = self.buildTree(preorder, node.val)
        # Recursively build the right subtree and set it as the right child of the current node.
        node.right = self.buildTree(preorder, bound)
        return node

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Reverse the preorder list to process it from right to left and start building the BST.
        return self.buildTree(preorder[::-1], float("inf"))
