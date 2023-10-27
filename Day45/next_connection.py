# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

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
    def connect(self, root):
        # Define a helper function 'dfs' for depth-first search.

        ## (1). left child -> right child
        ## (2). right child -> next.left child
        def dfs(root):
            # If the current node is None or it doesn't have a left child, return.
            if root == None or root.left == None:
                return
            # Connect the left child to the right child of the current node.
            root.left.next = root.right
            # If there's a next node at the same level, connect the right child to its left child.
            if root.next != None:
                root.right.next = root.next.left
            # Recursively traverse the left and right subtrees.
            dfs(root.left)
            dfs(root.right)

        # Start the depth-first search from the root node.
        dfs(root)
        return root
