# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

"""
Time complexity:- O(N)
Space Complexity:- O(N)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        res = []  # Initialize an empty list to store the serialized data.

        def dfs(node):
            if not node:
                res.append("N")  # "N" represents a null node.
                return
            # Append the value of the current node as a string.
            res.append(str(node.val))
            dfs(node.left)  # Recursively serialize the left subtree.
            dfs(node.right)  # Recursively serialize the right subtree.

        dfs(root)  # Start the serialization process with the root node.
        # Join the serialized data with commas and return as a string.
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")  # Split the serialized data by commas.
        # Initialize an index variable to keep track of the current position.
        self.i = 0

        def dfs():
            if vals[self.i] == "N":  # If the current value is "N," it's a null node.
                self.i += 1
                return None
            # Create a node with the parsed integer value.
            node = TreeNode(int(vals[self.i]))
            self.i += 1  # Move to the next value.
            node.left = dfs()  # Recursively deserialize the left subtree.
            node.right = dfs()  # Recursively deserialize the right subtree.
            return node

        # Start the deserialization process and return the reconstructed tree.
        return dfs()
