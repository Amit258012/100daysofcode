# https://leetcode.com/problems/search-in-a-binary-search-tree/

"""
Time complexity:- O(logN)
Space Complexity:- O(N) Auxilary space (Function CallStack)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None

    # If the current node's value matches the target 'val', return the current node.
    if root.val == val:
        return root

    # If the target 'val' is greater than the current node's value, search in the right subtree.
    if root.val < val:
        return self.searchBST(root.right, val)
    # If the target 'val' is less than the current node's value, search in the left subtree.
    else:
        return self.searchBST(root.left, val)
