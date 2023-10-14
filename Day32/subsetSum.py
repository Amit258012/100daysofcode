# https://practice.geeksforgeeks.org/problems/subset-sums2234/1

"""
Time complexity:- O(2^n)
Space Complexity:- O(2^n)
"""


class Solution:
    def subsetSums(self, arr, N):
        res = []  # List to store the subset sums

        def helper(i, sumVal):
            if i == N:  # If we reach the end of the list
                res.append(sumVal)  # Add the current sum to the result
                return

            # Include the element at index i (left tree)
            helper(i + 1, sumVal + arr[i])

            # Exclude the element at index i (right tree)
            helper(i + 1, sumVal)

        helper(0, 0)  # Start the helper function with index 0 and initial sum 0

        return res  # Return the list of subset sums
