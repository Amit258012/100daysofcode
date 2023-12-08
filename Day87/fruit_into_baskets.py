# https://leetcode.com/problems/fruit-into-baskets/
"""
Time complexity:- O(N)
Space Complexity:- O(1)
"""

"""
Intuition:

The algorithm employs a sliding window approach to find the longest subarray with at most two distinct fruits.
The 'count' dictionary keeps track of fruit occurrences in the current window.
When the count exceeds 2, the left pointer is moved to maintain a window with only two distinct fruits.
The result is the length of the longest valid subarray.

This algorithm efficiently explores all possible windows and adjusts the window size to find the longest subarray with the given constraint.
"""

from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Initialize a dictionary to count fruit occurrences and a pointer 'i'
        count = {}
        i = 0

        for j, v in enumerate(fruits):
            count[v] = count.get(v, 0) + 1  # Update the count of the current fruit

            # Check if the count of unique fruits exceeds 2
            if len(count) > 2:
                count[fruits[i]] -= 1  # Decrease the count of the fruit at pointer 'i'
                if count[fruits[i]] == 0:
                    # Remove the fruit from the dictionary if count becomes 0
                    del count[fruits[i]]
                i += 1  # Move the left pointer to the right

        # The result is the length of the longest subarray with at most two distinct fruits
        return j - i + 1
