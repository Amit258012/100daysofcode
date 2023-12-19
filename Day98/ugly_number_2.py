# https://leetcode.com/problems/ugly-number-ii/
"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""

"""
Intuition:

The method uses three pointers (t1, t2, and t3) to keep track of multiples of 2, 3, and 5.
It iteratively calculates the next ugly number by choosing the minimum among the multiples of 2, 3, and 5.
The pointers are updated based on which multiple was chosen to generate the next ugly number.
The method returns the nth ugly number.
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Initialize an array to store the ugly numbers
        k = [0] * n
        # Initialize pointers for 2, 3, and 5 multiples
        t1 = t2 = t3 = 0
        # Set the first ugly number as 1
        k[0] = 1

        # Generate ugly numbers
        for i in range(1, n):
            # Choose the minimum among the multiples of 2, 3, and 5
            k[i] = min(k[t1] * 2, k[t2] * 3, k[t3] * 5)
            # Move the pointer for the chosen multiple
            if k[i] == k[t1] * 2:
                t1 += 1
            if k[i] == k[t2] * 3:
                t2 += 1
            if k[i] == k[t3] * 5:
                t3 += 1

        # Return the nth ugly number
        return k[n - 1]
