# https://www.codingninjas.com/studio/problems/893000?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0
"""
Time complexity:- O(max(m,n))
Space Complexity:- O(m+n)
"""


def minCharsforPalindrome(s):
    i, j, trim = 0, len(s) - 1, len(s) - 1  # Initialize pointers and trim size.
    cnt = 0  # Initialize a count of characters to be added.

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1  # If characters match, move the pointers inward.
        else:
            cnt += 1  # If characters don't match, increment the count.
            i = 0
            trim -= 1  # Reset i and reduce the trim size.
            j = trim  # Reset j to the new trim size.

    return cnt  # Return the count of characters needed.
