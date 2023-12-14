# https://leetcode.com/problems/network-delay-time/
"""
Time complexity:- O((V + E) * log(V)) 
Space Complexity:- O(V + E)
"""

"""
Intuition:

The algorithm uses Dijkstra's algorithm to find the minimum time to reach all nodes from the source node.
It maintains a min heap to prioritize nodes with minimum weights.
The total time is updated as nodes are visited, and the process continues until all nodes are visited or the heap is empty.
Observation:

The algorithm focuses on exploring nodes with the minimum accumulated weight, gradually updating the total time.
Using a min heap helps efficiently choose the next node to explore, ensuring the shortest path is considered first.
"""
from typing import List
import collections
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create a defaultdict to represent the graph using an adjacency list
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        # Initialize a min heap with the starting node and its weight
        minHeap = [(0, k)]
        # Set to keep track of visited nodes
        visit = set()
        # Variable to store the total time
        t = 0

        # Continue until the minHeap is not empty
        while minHeap:
            # Extract the node with the minimum weight from the heap
            w1, n1 = heapq.heappop(minHeap)

            # Check if the node is already visited, skip to the next iteration
            if n1 in visit:
                continue

            # Mark the node as visited and update the total time
            visit.add(n1)
            t = w1

            # Iterate through the neighbors of the current node
            for n2, w2 in edges[n1]:
                # Check if the neighbor is not visited, add to the heap with updated weight
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        # If all nodes are visited, return the total time; otherwise, return -1
        return t if len(visit) == n else -1
