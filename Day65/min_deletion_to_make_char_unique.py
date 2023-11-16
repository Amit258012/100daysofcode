# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

"""
Time complexity:- O(N)
Space Complexity:- O(K) k is the number of unique frequencies in the string 
"""

"""
Intuition:

Count the frequency of each character using the Counter class.
Iterate through characters and their frequencies.
Ensure that the current frequency is unique by decrementing it until it is not already used.
Keep track of used frequencies in a set.
The total deletions represent the number of characters that need to be removed to make the frequencies unique.
"""

from typing import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        # Count the frequency of each character in the string
        cnt = Counter(s)
        deletions = 0
        used_frequencies = set()

        # Iterate through characters and their frequencies
        for char, freq in cnt.items():
            # Ensure the current frequency is not already used
            while freq > 0 and freq in used_frequencies:
                freq -= 1
                deletions += 1
            # Add the current frequency to the set of used frequencies
            used_frequencies.add(freq)

        # Return the total number of deletions needed to make frequencies unique
        return deletions
