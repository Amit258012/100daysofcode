# https://www.codingninjas.com/studio/problems/1072980
"""
Time complexity:- O(N*W)
Space Complexity:- O(W) 
"""

"""
Intuition:

The code implements the bottom-up approach for the 0/1 Knapsack problem using dynamic programming.
The 'prev' list is used to keep track of the maximum value that can be obtained for each capacity. It is updated iteratively based on whether the current item is taken or not.
The final result is stored in 'prev[W]', representing the maximum value of items the thief can steal within the given capacity.
"""

import sys


def maxProfit(val, wt, n, W):
    # Initialize a list 'prev' to store the maximum value for each capacity
    prev = [0] * (W + 1)

    # Base condition: Fill in the first row of 'prev' based on the capacity 'W'.
    for i in range(wt[0], W + 1):
        prev[i] = val[0]

    # Iterate through the items and capacities in reverse order.
    for ind in range(1, n):
        for cap in range(W, -1, -1):
            # Calculate the maximum value when the current item is not taken.
            notTaken = 0 + prev[cap]

            # Calculate the maximum value when the current item is taken (if its weight allows).
            taken = -sys.maxsize
            if wt[ind] <= cap:
                taken = val[ind] + prev[cap - wt[ind]]

            # Update the 'prev' list with the maximum of notTaken and taken values.
            prev[cap] = max(notTaken, taken)

    # The result is stored in 'prev[W]', representing the maximum value of items the thief can steal.
    return prev[W]
