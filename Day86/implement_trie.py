# https://leetcode.com/problems/implement-trie-prefix-tree/
"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""

"""
Intuition:

The Trie data structure is used for efficient storage and retrieval of strings.
The TrieNode class represents a node in the Trie, and each node has an array of children nodes.
The Trie class provides methods to insert a word into the Trie, search for a word, and check if any word starts with a given prefix.
The insert method traverses the Trie, creating nodes as needed and marking the end of the word.
The search method checks if a given word exists in the Trie.
The startsWith method checks if there is any word in the Trie that starts with a given prefix.
"""


class TrieNode:
    def __init__(self):
        # Initialize the TrieNode with an array to represent children nodes (26 for each lowercase letter)
        self.children = [None] * 26
        # Boolean flag to indicate whether a word ends at this node
        self.end = False


class Trie:
    def __init__(self):
        # Initialize the Trie with a root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Insert a word into the Trie
        curr = self.root
        for c in word:
            # Calculate the index of the character in the children array
            i = ord(c) - ord("a")
            # Create a new TrieNode if the node does not exist
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            # Move to the next node in the Trie
            curr = curr.children[i]
        # Mark the end of the word
        curr.end = True

    def search(self, word: str) -> bool:
        # Search for a word in the Trie
        curr = self.root
        for c in word:
            # Calculate the index of the character in the children array
            i = ord(c) - ord("a")
            # Return False if the node does not exist
            if curr.children[i] == None:
                return False
            # Move to the next node in the Trie
            curr = curr.children[i]
        # Check if the word ends at this node
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        # Check if there is any word in the Trie that starts with the given prefix
        curr = self.root
        for c in prefix:
            # Calculate the index of the character in the children array
            i = ord(c) - ord("a")
            # Return False if the node does not exist
            if curr.children[i] == None:
                return False
            # Move to the next node in the Trie
            curr = curr.children[i]
        # The Trie contains words with the given prefix
        return True
