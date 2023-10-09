# https://leetcode.com/problems/reverse-words-in-a-string/

"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        res = []  # Initialize a list to store the reversed words.
        temp = ""  # Initialize a temporary string to build each word.

        for c in s:
            if c != "":
                temp += c  # Append the character to the temporary string.
            elif temp != "":
                res.append(temp)  # Add the word to the result list.
                temp = ""  # Reset the temporary string for the next word.

        if temp != "":
            res.append(temp)  # Add the last word to the result if not empty.

        # Reverse the order of words and join them with spaces to form the result string.
        return " ".join(res[::-1])
