# https://leetcode.com/problems/sort-characters-by-frequency/

"""
Time complexity:- O()
Space Complexity:- O(n)
"""
from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, s: str) -> str:
        # Create a Counter dictionary to count the frequency of each character in 's'.
        hashD = Counter(s)
        res = ""  # Initialize an empty string to store the result.

        # Iterate through the characters in descending order of frequency.
        for k, v in hashD.most_common():
            res += k * v  # Append the character 'k' repeated 'v' times to the result.

        return res
