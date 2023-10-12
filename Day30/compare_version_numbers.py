# https://leetcode.com/problems/compare-version-numbers/
"""
Time complexity:- O(max(m,n))
Space Complexity:- O(m+n)
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the input version strings into a list of integers using '.' as the separator.
        version1, version2 = version1.split("."), version2.split(".")
        m, n = len(version1), len(version2)  # Get the lengths of the two version lists.

        i = j = 0  # Initialize pointers for the two lists.

        while i < m or j < n:
            # Extract the parts of the version numbers, or set to 0 if we've reached the end of a version.
            r1 = int(version1[i]) if i < m else 0
            r2 = int(version2[j]) if j < n else 0

            if r1 < r2:
                return -1  # Version 1 is lower.
            if r1 > r2:
                return 1  # Version 1 is higher.

            i += 1
            j += 1  # Move to the next part of the version numbers.

        return 0  # Both version numbers are equal.
