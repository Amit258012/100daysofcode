# https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
"""
Time complexity:- O(E+V) , where V is the number of vertices (nodes) and E is the number of edges in the graph.
Space Complexity:- O(V)
"""

"""
Intuition:

BFS explores all the neighbors of a node before moving on to the next level. It uses a queue to keep track of the order in which nodes are visited.

Observation:

The Queue is used to implement the FIFO (First-In-First-Out) order in BFS.
The visited array is crucial to prevent revisiting already explored nodes and avoid infinite loops.
The res list accumulates the nodes in the order they are visited, providing the BFS traversal result.
"""
from typing import List
from queue import Queue


class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # Initialize a queue for BFS traversal
        q = Queue(maxsize=V)
        # Initialize a list to store the BFS traversal result
        res = []
        # Initialize a list to keep track of visited nodes
        visited = [False] * V

        # Start BFS from the first node (0 index)
        q.put(0)
        visited[0] = True

        # Continue BFS until the queue is empty
        while not q.empty():
            # Get the front element from the queue
            temp = q.get()
            # Append the current node to the result list
            res.append(temp)

            # Explore neighbors of the current node
            for neighbor in adj[temp]:
                # If the neighbor is not visited, enqueue it and mark it as visited
                if not visited[neighbor]:
                    q.put(neighbor)
                    visited[neighbor] = True

        # Return the BFS traversal result
        return res
