# https://www.codingninjas.com/studio/problems/all-root-to-leaf-paths-in-binary-tree._983599?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

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


from typing import List


# A helper function to find root-to-leaf paths and add them to the 'allPaths' list.
def find_path(root, currentPath, allPaths):
    if root.left is None and root.right is None:
        # If the current node is a leaf node, add its data to the current path and append it to 'allPaths'.
        currentPath.append(str(root.data))
        allPaths.append(" ".join(currentPath[:]))
        return

    currentPath.append(str(root.data))

    if root.left is not None:
        # Recursively find paths in the left subtree, and then remove the last added element from the current path.
        find_path(root.left, currentPath, allPaths)
        currentPath.pop()

    if root.right is not None:
        # Recursively find paths in the right subtree, and then remove the last added element from the current path.
        find_path(root.right, currentPath, allPaths)
        currentPath.pop()


# The main function to find all root-to-leaf paths.
def allRootToLeaf(root):
    allPaths = []  # Initialize an empty list to store all paths.
    currentPath = []  # Initialize an empty list to store the current path.
    find_path(root, currentPath, allPaths)  # Start the recursive process.
    return allPaths  # Return the list of root-to-leaf paths as strings.
