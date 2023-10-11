# https://leetcode.com/problems/group-anagrams/

"""
Time complexity:- O(n * klogk)
Space Complexity:- O(n*k)
K is the maximum length of a string.
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}  # Create a dictionary to store anagram groups.

        # Iterate through the list of strings.
        for str1 in strs:
            # Sort the characters in the string, so anagrams have the same sorted representation.
            sorted_str = "".join(sorted(str1))

            # Check if the sorted representation is already in the dictionary.
            if sorted_str in anagram_groups:
                # If yes, append the original string to the corresponding group.
                anagram_groups[sorted_str].append(str1)
            else:
                # If not, create a new group with the sorted representation as the key.
                anagram_groups[sorted_str] = [str1]

        # Convert the values (anagram groups) from the dictionary to a list and return it.
        return list(anagram_groups.values())
