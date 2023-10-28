# https://practice.geeksforgeeks.org/problems/predecessor-and-successor/1

"""
Time complexity:- O(H)
Space Complexity:- O(H) Auxilary space (Function CallStack)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Helper method to copy properties of one node to another.
    def copy_node(self, a, b):
        a.val = b.val
        a.left = b.left
        a.right = b.right

    def findPreSuc(self, root, pre, suc, val):
        while root:
            if root.val == val:
                if root.left:
                    # Find the rightmost node in the left subtree as the predecessor.
                    tmp = root.left
                    while tmp.right:
                        tmp = tmp.right
                    self.copy_node(pre, tmp)

                if root.right:
                    # Find the leftmost node in the right subtree as the successor.
                    tmp = root.right
                    while tmp.left:
                        tmp = tmp.left
                    self.copy_node(suc, tmp)

                return pre, suc

            if root.val > val:
                # Update 'suc' and move to the left subtree.
                self.copy_node(suc, root)
                root = root.left
            else:
                # Update 'pre' and move to the right subtree.
                self.copy_node(pre, root)
                root = root.right
