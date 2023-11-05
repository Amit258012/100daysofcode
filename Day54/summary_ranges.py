# https://leetcode.com/problems/summary-ranges

"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""


from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Initialize an empty list to store the summary ranges.
        ranges = []

        for n in nums:
            # Check if the 'ranges' list is empty or if the current number 'n' is not consecutive to the last range.
            if not ranges or n > ranges[-1][-1] + 1:
                # If not consecutive, add a new range as a list with the current number 'n'.
                ranges += []

            # Append the current number 'n' to the last range.
            ranges[-1][1:] = n

        # Convert the list of ranges into a list of strings, where each string represents a summary range.
        # Join the range using '->' and convert the numbers to strings using 'map'.
        return ["->".join(map(str, r)) for r in ranges]
