# https://leetcode.com/problems/redundant-connection/
"""
Time complexity:- O(N^2)
Space Complexity:- O(N)
"""

"""
Intuition:

The findRedundantConnection method uses a depth-first search (DFS) to check if there's already a path from u to v in the graph.
If a path is found, the current edge [u, v] is redundant, and it is returned as the result.
The undirected graph is represented using a defaultdict where each node has a set of neighbors.
The method iterates through the given edges, adding them to the graph and checking for redundancy.
"""


import collections
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Create a defaultdict to represent an undirected graph
        graph = collections.defaultdict(set)

        def dfs(source, target):
            # Depth-first search to check if there's a path from source to target
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            # Check if there's already a path from u to v
            if u in graph and v in graph and dfs(u, v):
                return [u, v]

            # Add the edge to the graph
            graph[u].add(v)
            graph[v].add(u)
