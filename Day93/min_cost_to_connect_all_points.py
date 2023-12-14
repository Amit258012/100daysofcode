# https://leetcode.com/problems/min-cost-to-connect-all-points/
"""
Time complexity:- O(E * log(V)) 
Space Complexity:- O(V + E)
"""

"""
Intuition:

The algorithm uses Prim's algorithm to find the minimum cost to connect all points.
It builds a graph with edges representing the Manhattan distance between points.
A min heap is used to efficiently choose the next node to add to the Minimum Spanning Tree (MST).
The total cost is updated as nodes are visited, and the process continues until all nodes are visited.


Observation:

Prim's algorithm ensures that the next edge added to the MST has the minimum cost among all available edges.
The algorithm explores nodes with minimum costs first, gradually building the MST with the minimum total cost.
"""
from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # Create adjacency list representation of the graph
        adj = {i: [] for i in range(N)}  # i: list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                # Calculate Manhattan distance as the cost
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's Algorithm
        res = 0
        visit = set()
        minH = [[0, 0]]  # [cost, point]

        # Continue until all nodes are visited
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)

            # Add neighbors of the current node to the heap
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])

        return res
