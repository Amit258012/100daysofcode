# https://leetcode.com/problems/search-suggestions-system/
"""
Time complexity:- O(N * M)
Space Complexity:- O(N * M) 
"""

"""
Intuition:

The TrieNode class represents a node in the Trie with children, words, and a counter.
The Trie class represents the Trie structure with methods to add words and find words by prefix.
The suggestedProducts method initializes a Trie, adds each product to it, and then uses the Trie to find suggested products for each character in the searchWord.
"""


class TrieNode:
    def __init__(self):
        # Initialize TrieNode with children dictionary, words list, and a counter n
        self.children = dict()
        self.words = list()
        self.n = 0


class Trie:
    def __init__(self):
        # Initialize Trie with a root node and set the current node to the root
        self.root = TrieNode()
        self.node = self.root

    def add_word(self, word):
        # Add a word to the Trie, updating nodes and counters
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if node.n < 3:
                node.words.append(word)
                node.n += 1

    def find_word_by_prefix(self, c):
        # Find words with a given prefix in the Trie and update the current node
        if self.node and c in self.node.children:
            self.node = self.node.children[c]
            return self.node.words
        else:
            self.node = None
            return []


class Solution:
    def suggestedProducts(self, products, searchWord):
        # Sort the products list for efficient searching
        products.sort()

        # Create a Trie and add each product to it
        trie = Trie()
        for word in products:
            trie.add_word(word)

        # Use the Trie to find suggested products for each character in the searchWord
        return [trie.find_word_by_prefix(c) for c in searchWord]
