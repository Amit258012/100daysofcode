# https://leetcode.com/problems/bulls-and-cows/
"""
Time complexity:- O(N)
Space Complexity:- O(K) K is the number of unique digits in the secret string.
"""

"""
Intuition:

The getHint method calculates the number of bulls and cows based on the input secret and guess strings.
The first loop counts the bulls by checking for correct digits and positions.
The second loop counts the cows by considering correct digits in the wrong positions. It iterates over unique digits in the secret string and adds the minimum count of that digit in both secret and guess.
The result is formatted as a string in the format "XAYB," where X is the number of bulls and Y is the number of cows.
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Count the number of bulls (correct digit and position)
        bull = 0
        for i in range(len(secret)):
            bull += int(secret[i] == guess[i])

        # Count the number of cows (correct digit but wrong position)
        cows = 0
        for c in set(secret):
            cows += min(secret.count(c), guess.count(c))

        # Return the result in the specified format
        return f"{bull}A{cows - bull}B"
