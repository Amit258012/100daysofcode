# https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1

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


class Solution:
    def kthLargest(self, root, k):
        if not root:
            return -1  # Return -1 if the BST is empty.

        res = []  # Initialize an empty list to store BST elements.

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)  # Collect elements in ascending order.
            inorder(node.right)

        inorder(root)  # Perform in-order traversal.

        if k <= len(res):
            return res[-k]  # Return the k-th largest element from the end of the list.
        else:
            return -1  # If k is greater than the number of elements, return -1.


# space complexity can be optimized like this: O(1)
# 1) First do 1 dfs traversal and calc total number or nodes (N)
# 2) keep reference of count
# 3) If count == k retun node value :- avoide storing the inorder in array
