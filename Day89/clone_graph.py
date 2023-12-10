# https://leetcode.com/problems/clone-graph/
"""
Time complexity:- O(E+V) , where V is the number of vertices (nodes) and E is the number of edges in the graph.
Space Complexity:- O(V)
"""

"""
Intuition:

DFS is used to traverse the graph and create a deep copy of each node along with its neighbors. The oldToNew dictionary ensures that nodes are not cloned multiple times.

Observation:

The Node class is assumed to have a neighbors attribute representing the list of adjacent nodes.
The DFS approach recursively explores each node and its neighbors, creating a new copy for each node and maintaining the mapping in the oldToNew dictionary.
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # Dictionary to map old nodes to their corresponding new nodes
        oldToNew = {}

        def dfs(node):
            # If the node has already been cloned, return the cloned copy
            if node in oldToNew:
                return oldToNew[node]

            # Create a new node with the same value as the original node
            copy = Node(node.val)
            # Store the mapping of the original node to its cloned copy
            oldToNew[node] = copy

            # Recursively clone the neighbors of the original node
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            # Return the cloned copy of the current node
            return copy

        # Start the DFS from the given node (or return None if the graph is empty)
        return dfs(node) if node else None
