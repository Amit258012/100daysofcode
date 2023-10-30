# https://www.codingninjas.com/studio/problems/children-sum-property_8357239?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

"""
Time complexity:- O(N)
Space Complexity:- O(H) Auxilary space (Function CallStack)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isParentSum(self, root):
        # Base case: If the node is None or it's a leaf node, it's considered a parent sum tree.
        if root is None or (root.left is None and root.right is None):
            return True

        # Initialize the sum variable to 0.
        sum = 0

        # If the left child exists, add its val value to the sum.
        if root.left:
            sum += root.left.val

        # If the right child exists, add its val value to the sum.
        if root.right:
            sum += root.right.val

        # Check if the sum of children's values is equal to the current node's val.
        if sum == root.val:
            # Recursively check the same condition for the left and right subtrees.
            return self.isParentSum(root.left) and self.isParentSum(root.right)
        else:
            # If the condition is not satisfied, return False.
            return False
