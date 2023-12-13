# https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
"""
Time complexity:- O((V + E) * log(V)) 
Space Complexity:- O(V)
"""

"""
Intuition:

The dis list is used to store the shortest distances from the source node to all other nodes.
The q deque acts as a priority queue, where elements are added based on their distance from the source.
The algorithm iteratively selects the node with the minimum distance from the priority queue, relaxes its neighbors, and updates the distances accordingly.
Note:

The implementation assumes that the input graph is represented as an adjacency list (adj) where each edge is represented as a tuple (adjacent_node, edge_weight).
"""
from collections import deque


class Solution:
    def dijkstra(self, V, adj, S):
        # Initialize a list to store the shortest distances
        dis = [float("inf") for i in range(V)]

        # Initialize a deque for the priority queue
        q = deque([])

        # Add the source node to the priority queue with distance 0
        q.append([0, S])
        dis[S] = 0

        # Dijkstra's algorithm
        while len(q) != 0:
            # Get the current element from the priority queue
            cur = q.popleft()
            cur_dis = cur[0]
            node = cur[-1]

            # Iterate through adjacent nodes
            for i in adj[node]:
                adj_node = i[0]  # Adjacent node
                node_weight = i[-1]  # Weight of the edge

                # Relaxation step: Update the distance if a shorter path is found
                if cur_dis + node_weight < dis[adj_node]:
                    q.append([cur_dis + node_weight, adj_node])
                    dis[adj_node] = cur_dis + node_weight

        return dis
