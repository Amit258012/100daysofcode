# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

"""
Time complexity:- O(N)
Space Complexity:- O(H) Auxilary space
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # If the inorder list is not empty (there are nodes to construct), continue building the tree.
        if inorder:
            # Pop the first element from the preorder list to create the root node.
            root_val = preorder.pop(0)
            root = TreeNode(root_val)

            # Find the index of the root node's value in the inorder list to split it into left and right subtrees.
            index = inorder.index(root_val)

            # Recursively build the left subtree using the corresponding portions of the preorder and inorder lists.
            root.left = self.buildTree(preorder, inorder[:index])

            # Recursively build the right subtree using the corresponding portions of the preorder and inorder lists.
            root.right = self.buildTree(preorder, inorder[index + 1 :])

            return root
