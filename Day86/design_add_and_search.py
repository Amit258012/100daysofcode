# https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""

"""
Intuition:

The WordDictionary uses a Trie data structure to efficiently store and search for words.
The TrieNode class represents a node in the Trie, with a dictionary for children nodes and a boolean flag indicating the end of a word.
The WordDictionary class provides methods to add a word to the dictionary and search for words, allowing wildcard "." characters.
The addWord method inserts a word into the Trie, creating nodes as needed and marking the end of the word.
The search method uses a depth-first search (DFS) to traverse the Trie, handling wildcard characters when encountered.
"""


class TrieNode:
    def __init__(self):
        # Initialize the TrieNode with a dictionary to represent children nodes (character to TrieNode mapping)
        self.children = {}
        # Boolean flag to indicate whether a complete word ends at this node
        self.word = False


class WordDictionary:
    def __init__(self):
        # Initialize the WordDictionary with a root TrieNode
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Add a word to the WordDictionary
        cur = self.root
        for c in word:
            # Create a new TrieNode if the node does not exist
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move to the next node in the Trie
            cur = cur.children[c]
        # Mark the end of the word
        cur.word = True

    def search(self, word: str) -> bool:
        # Search for a word in the WordDictionary using depth-first search
        def dfs(j, root):
            cur = root

            # Traverse the characters of the word starting from index j
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # If the character is ".", recursively search all children nodes
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    # If the character is not ".", move to the next node in the Trie
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            # Check if the current node represents the end of a complete word
            return cur.word

        # Start the depth-first search from the root TrieNode
        return dfs(0, self.root)
