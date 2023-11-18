# https://leetcode.com/problems/frequency-of-the-most-frequent-element/
"""
Time complexity:- O(N logN)
Space Complexity:- O(1) 
"""

"""
Intuition:

The algorithm implements the fractional knapsack problem, where items can be included fractionally.
It sorts the items based on their value-to-weight ratio in descending order to maximize the total value.
"""


class Item:
    def __init__(self, val, w):
        # Constructor to create an Item with a given value and weight.
        self.value = val
        self.weight = w


class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W, arr, n):
        # Sort the items based on their value-to-weight ratio in descending order.
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)

        # Initialize variables to keep track of current weight and final value.
        curWeight = 0
        finalVal = 0.0

        # Iterate through the sorted items.
        for i in range(n):
            # Check if adding the entire item won't exceed the weight limit.
            if curWeight + arr[i].weight <= W:
                # Include the entire item in the knapsack.
                curWeight += arr[i].weight
                finalVal += arr[i].value
            else:
                # Calculate the remaining weight that can be included fractionally.
                rem = W - curWeight
                # Include a fraction of the current item to fill the remaining weight.
                finalVal += (arr[i].value / arr[i].weight) * rem
                break

        return finalVal
