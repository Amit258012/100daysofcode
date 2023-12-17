# https://leetcode.com/problems/word-search-ii/
"""
Time complexity:- O(N * M * W), where N and M are the dimensions of the board and W is the total number of characters in the words.
Space Complexity:- O(W)
"""

"""
Intuition:

The findWords method uses a Trie data structure to efficiently search for words on the board.
It iterates through the board cells and starts the search from each cell if it is a prefix in the Trie.
The find_str function performs a depth-first search (DFS) on the board to find words in the Trie.
The unique words found are stored in the res set.
"""
from collections import defaultdict
from functools import reduce
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Create a Trie data structure
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = True

        # Build the trie using the given words
        for word in words:
            reduce(dict.__getitem__, word, trie)[END] = word

        # Set to store unique results
        res = set()

        def find_str(i, j, t):
            # Helper function to explore the board and find words
            if END in t:
                res.add(t[END])

            letter = board[i][j]
            board[i][j] = ""  # Mark the cell as visited

            # Check adjacent cells and continue the search
            if i > 0 and board[i - 1][j] in t:
                find_str(i - 1, j, t[board[i - 1][j]])
            if j > 0 and board[i][j - 1] in t:
                find_str(i, j - 1, t[board[i][j - 1]])
            if i < len(board) - 1 and board[i + 1][j] in t:
                find_str(i + 1, j, t[board[i + 1][j]])
            if j < len(board[0]) - 1 and board[i][j + 1] in t:
                find_str(i, j + 1, t[board[i][j + 1]])

            board[i][j] = letter  # Restore the original cell value

            return

        # Iterate through the board
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                # If the current cell is a prefix in the trie, start the search
                if board[i][j] in trie:
                    find_str(i, j, trie[board[i][j]])

        return list(res)
