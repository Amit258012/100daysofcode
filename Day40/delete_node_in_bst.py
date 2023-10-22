# https://leetcode.com/problems/delete-node-in-a-bst/

"""
Time complexity:- O(H)
Space Complexity:- O(H)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root, key):
        # If the tree is empty (root is None), return None (no node to delete).
        if not root:
            return root

        # If the key is greater than the current node's value, traverse the right subtree.
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # If the key is less than the current node's value, traverse the left subtree.
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # If the key matches the current node's value:
            if not root.left:
                # If there is no left subtree, return the right subtree as the new root.
                return root.right
            elif not root.right:
                # If there is no right subtree, return the left subtree as the new root.
                return root.left

            # If both left and right subtrees exist, find the minimum value in the right subtree.
            cur = root.right
            while cur.left:
                cur = cur.left
            # Replace the current node's value with the minimum value found.
            root.val = cur.val
            # Delete the node with the minimum value from the right subtree.
            root.right = self.deleteNode(root.right, root.val)

        # Return the root of the modified BST.
        return root
