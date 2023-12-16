# https://leetcode.com/problems/copy-list-with-random-pointer/
"""
Time complexity:- O(N)
Space Complexity:- O(1)
"""

"""
Intuition:

The code performs a two-pass approach to create a deep copy of the linked list with random pointers.
In the first pass, it creates copy nodes for each original node and maps the original nodes to their corresponding copy nodes using a dictionary (oldToCopy).
In the second pass, it updates the next and random pointers of the copy nodes based on the mapping in the dictionary.
"""


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        # Dictionary to map each original node to its corresponding copy node
        oldToCopy = {None: None}

        # First pass: Create copy nodes and map original nodes to their copies
        cur = head
        while cur:
            copy = Node(cur.val)  # Create a copy node with the same value
            oldToCopy[cur] = copy  # Map the original node to its copy
            cur = cur.next

        # Second pass: Update next and random pointers of copy nodes
        cur = head
        while cur:
            copy = oldToCopy[
                cur
            ]  # Get the copy node corresponding to the current original node
            copy.next = oldToCopy[cur.next]  # Update the next pointer
            copy.random = oldToCopy[cur.random]  # Update the random pointer
            cur = cur.next

        # Return the head of the copied linked list
        return oldToCopy[head]
