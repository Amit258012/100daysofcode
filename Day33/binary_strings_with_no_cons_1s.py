# https://www.codingninjas.com/studio/problems/-binary-strings-with-no-consecutive-1s._893001?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

"""
Time complexity:- O(2^n)
Space Complexity:- O(2^n)
"""
from typing import List


class Solution:
    def generateString(self, N: int) -> List[str]:
        if N == 0:
            return [""]  # Base case: an empty string

        if N == 1:
            return ["0", "1"]  # Base case: strings "0" and "1" for N=1

        result = []
        for s in self.generateString(N - 1):
            # For each binary string of length N-1, append "0" and "1" to create new strings.
            result.append(s + "0")
            if s[-1] != "1":
                result.append(s + "1")

        return result
