# https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

"""
Time complexity:- O( Nlog(N) )
Space Complexity:- O(N) Auxilary space (Function CallStack)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def bottomView(self, root):
        # Create a dictionary 'mp' to store the last seen node at each level.
        mp = {}
        # Create a deque 'q' to perform a breadth-first traversal, starting with the root and its level.
        q = deque()
        q.append((root, 0))

        while q:
            node, level = q.popleft()
            # Update the 'mp' dictionary with the node's value for the current level.
            mp[level] = node.data

            # Add the left child to the queue with a decreased level.
            if node.left:
                q.append((node.left, level - 1))

            # Add the right child to the queue with an increased level.
            if node.right:
                q.append((node.right, level + 1))

        # Sort the items of the 'mp' dictionary by level and create a list 'lis'.
        lis = sorted(mp.items())
        ans = []

        for i in range(len(lis)):
            # Extract the values and add them to the 'ans' list.
            ans.append(lis[i][1])

        # Return the 'ans' list containing the values of nodes in the bottom view.
        return ans
