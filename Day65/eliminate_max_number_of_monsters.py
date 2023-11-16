# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

"""
Time complexity:- O(N logN)
Space Complexity:- O(N) 
"""

"""
Intuition:

Calculate the time each monster takes to reach the city (distance / speed).
Sort the array of times to process monsters with the shortest arrival times first.
Iterate through the sorted array and eliminate monsters whose arrival time is greater than their index in the sorted array.
The final count represents the maximum number of monsters that can be eliminated before reaching the city.
"""
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Calculate the time each monster takes to reach the city
        arr = [dist[i] / speed[i] for i in range(len(dist))]

        # Sort the array of times in ascending order
        arr.sort()
        ans = 0

        # Iterate through the sorted array
        for i in range(len(arr)):
            # Check if the time taken by a monster is less than or equal to its index
            if arr[i] <= i:
                break

            # Increment the count of eliminated monsters
            ans += 1

        # Return the total count of eliminated monsters
        return ans
