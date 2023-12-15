# https://leetcode.com/problems/minimum-window-substring/
"""
Time complexity:- O(N+M) N-len(s), M- len(t)
Space Complexity:- O(N+M)
"""

"""
Intuition:

The code uses a sliding window approach to find the minimum window containing all characters from string t in string s.
The countT dictionary is used to store the count of characters in string t.
The window dictionary is used to store the count of characters in the current window.
The have variable represents the number of characters in the window that match the required count.
The need variable represents the total number of characters needed in the window.
The res variable stores the final result, and resLen stores its length.
The left pointer (l) is moved to minimize the window size whenever a valid window is found.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Check if the target string t is empty
        if t == "":
            return ""

        # Initialize dictionaries to count characters in t and the current window
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Variables to track the number of characters needed and currently in the window
        have, need = 0, len(countT)

        # Variables to store the final result and its length
        res, resLen = [-1, -1], float("infinity")

        # Left pointer for the window
        l = 0

        # Iterate over the characters in s using the right pointer (r)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # Check if the character in the window matches the required count from t
            if c in countT and window[c] == countT[c]:
                have += 1

            # Try to minimize the window size by moving the left pointer
            while have == need:
                # Update the result if the current window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Pop the character from the left of the window
                window[s[l]] -= 1

                # Check if the removal affects the character count needed
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                # Move the left pointer to the right
                l += 1

        # Extract the substring based on the final result
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
