# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # If either the inorder or postorder list is empty, return None (no nodes to construct).
        if not inorder or not postorder:
            return None

        # Pop the last element from the postorder list to create the root node.
        root_val = postorder.pop()
        root = TreeNode(root_val)

        # Find the index of the root node's value in the inorder list to split it into left and right subtrees.
        idx = inorder.index(root_val)

        # Recursively build the right subtree using the corresponding portions of the inorder and postorder lists.
        root.right = self.buildTree(inorder[idx + 1 :], postorder)

        # Recursively build the left subtree using the corresponding portions of the inorder and postorder lists.
        root.left = self.buildTree(inorder[:idx], postorder)

        return root
