# https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
"""
Time complexity:- O(E+V) , where V is the number of vertices (nodes) and E is the number of edges in the graph.
Space Complexity:- O(V)
"""

"""
Intuition:

DFS is a graph traversal algorithm that explores as far as possible along each branch before backtracking. In this implementation, the dfsOfGraph function initializes the visited array and the result list, and then calls the dfs function to perform the actual DFS traversal starting from the first node. The dfs function recursively explores the neighbors of each node, marking them as visited and appending them to the result list.

Observation:

The DFS traversal order depends on the structure of the graph.
The visited array is crucial to prevent revisiting already explored nodes and avoid infinite loops.
The values list accumulates the nodes in the order they are visited, providing the DFS traversal result.
"""


class Solution:
    def dfsOfGraph(self, V, adj):
        # Initialize a list to keep track of visited nodes
        visited = [0] * V
        # Initialize a list to store the DFS traversal result
        values = []  # to return as the answer
        # Start DFS from the first node (0 index)
        self.dfs(0, adj, visited, values)
        # Return the DFS traversal result
        return values

    def dfs(self, node, adj, visited, values):
        # Mark the current node as visited
        visited[node] = 1
        # Append the current node to the result list
        values.append(node)
        # Explore neighbors of the current node
        for i in adj[node]:
            # If the neighbor is not visited, recursively call DFS on it
            if visited[i] == 0:
                self.dfs(i, adj, visited, values)
