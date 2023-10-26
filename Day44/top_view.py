# https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1

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


class Solution:
    def topView(self, root):
        if not root:
            return []

        # Dictionary to store nodes at each horizontal distance.
        node_dict = {}

        # Queue for level-order traversal.
        queue = []

        # Initialize the root node with a horizontal distance of 0.
        root.horizontal_distance = 0
        queue.append(root)

        while queue:
            current_node = queue.pop(0)
            hd = current_node.horizontal_distance

            # If the horizontal distance is not in the dictionary, add it.
            if hd not in node_dict:
                node_dict[hd] = current_node.data

            # Queue the left child with a decreased horizontal distance.
            if current_node.left:
                current_node.left.horizontal_distance = hd - 1
                queue.append(current_node.left)

            # Queue the right child with an increased horizontal distance.
            if current_node.right:
                current_node.right.horizontal_distance = hd + 1
                queue.append(current_node.right)

        # Sort the dictionary by horizontal distance and store the values in an array.
        sorted_nodes = [node_dict[key] for key in sorted(node_dict)]

        return sorted_nodes
