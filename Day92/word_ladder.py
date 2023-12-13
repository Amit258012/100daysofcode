# https://leetcode.com/problems/word-ladder/
"""
Time complexity:- O(n * L^2)  for building the dictionary + O(n * L * n) for BFS traversal, which simplifies to O(n * L^2).
Space Complexity:- O(n * L^2) dominated by the all_combo_dict + O(n) for the queue and visited set.

"""

"""
Intuition:

Preprocess the wordList to create a dictionary mapping each word's intermediate forms to a list of words.
Use BFS to explore transformation possibilities level by level, starting from beginWord.
The level represents the minimum number of transformations needed to reach a word.
Return the level when the endWord is found.

Observations:
Efficiently uses intermediate forms to group words that can be transformed into each other.
BFS traversal explores transformation possibilities level by level.
Visited set avoids revisiting words and prevents cycles.
Returns 0 if the endWord is not in the wordList or if any input word is empty.
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Check for edge cases
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Length of the words
        L = len(beginWord)

        # Dictionary to store all combinations of words with a common intermediate
        all_combo_dict = defaultdict(list)

        # Preprocess the wordList to create a mapping of words with a common intermediate
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

        # Queue for BFS traversal and a set to keep track of visited words
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        # BFS traversal
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i + 1 :]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        # If the target word is found, return the level + 1
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))

        # If no transformation sequence is found, return 0
        return 0
