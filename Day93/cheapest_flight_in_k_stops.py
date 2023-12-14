# https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
Time complexity:- O(k * |flights|) 
Space Complexity:- O(N)
"""

"""
Intuition:

The algorithm uses dynamic programming to find the cheapest price from the source to the destination with at most k stops.
It iterates through each flight, updating the minimum price for each destination node.
The process is repeated for at most k stops, considering different combinations of flights.


Observation:

The algorithm aims to find the minimum cost path, considering at most k stops.
It uses dynamic programming to iteratively update the minimum prices for each node based on the available flights.
The final result is obtained from the prices array for the destination node.
"""
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # Initialize prices array with infinite values for each node
        prices = [float("inf")] * n
        # Set the source node's price to 0
        prices[src] = 0

        # Iterate for at most k stops
        for i in range(k + 1):
            # Create a temporary copy of prices array to store the updated prices
            tmpPrices = prices.copy()

            # Iterate through each flight
            for s, d, p in flights:  # s=source, d=destination, p=price
                # If the source node has a valid price (not infinite)
                if prices[s] == float("inf"):
                    continue
                # Update the temporary prices for the destination node
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            # Update prices array with the temporary prices
            prices = tmpPrices

        # If the destination node's price is still infinite, there is no valid path
        return -1 if prices[dst] == float("inf") else prices[dst]
