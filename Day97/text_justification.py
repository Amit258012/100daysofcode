# https://leetcode.com/problems/text-justification/
"""
Time complexity:- O(N)
Space Complexity:- O(1)
"""

"""
Intuition:

The fullJustify method formats the words to fit within the given maxWidth while justifying the text.
It iterates through the words and builds lines (cur) with the constraint that the total length does not exceed maxWidth.
When a line is formed, it calculates the number of spaces to add between words and distributes them evenly.
The last line is left-justified with spaces between words.
"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0

        for w in words:
            # Check if adding the current word exceeds the maxWidth
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # Distribute spaces evenly between words in the current line
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += " "
                res.append("".join(cur))
                # Reset current line
                cur, num_of_letters = [], 0

            cur += [w]
            num_of_letters += len(w)

        # For the last line, left justify and add spaces between words
        return res + [" ".join(cur).ljust(maxWidth)]
