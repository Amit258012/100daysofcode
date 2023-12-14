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
