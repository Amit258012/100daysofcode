# https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1
"""
Time complexity:- O(N^2)
Space Complexity:- O(N)
"""

"""
Intuition:

The algorithm uses dynamic programming to find the maximum sum increasing subsequence.
The 'dp' array is used to store the maximum sum increasing subsequence ending at each index.
For each element in the array, it is compared with the previous elements, and if adding the current element to the previous subsequence results in a higher sum, the 'dp' array is updated.
The result is the maximum sum increasing subsequence in the entire array, stored in the 'ans' variable.
"""


class Solution:
    def maxSumIS(self, arr, n):
        # Initialize an array 'dp' to store the maximum sum increasing subsequence ending at each index
        dp = arr[:]  # Initialize with the original array values
        ans = arr[0]  # Initialize the result with the first element of the array

        # Iterate over the elements of the array starting from the second element
        for i in range(1, n):
            # Compare the current element with previous elements
            for j in range(i):
                # If the current element is greater than the previous element and
                # adding the current element to the previous subsequence gives a higher sum,
                # update the maximum sum increasing subsequence ending at the current index
                if arr[i] > arr[j] and dp[i] < arr[i] + dp[j]:
                    dp[i] = arr[i] + dp[j]

            # Update the overall maximum sum by considering the maximum sum ending at the current index
            ans = max(ans, dp[i])

        # The result is the maximum sum increasing subsequence in the entire array
        return ans
