# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""
Time complexity:- O(N )
Space Complexity:- O(W), where W is the maximum number of nodes at the same level in the deque.
"""

"""
Intuition:

The connect method uses a level-order traversal (BFS) to traverse the tree and connect nodes at the same level.
It uses a deque to maintain the nodes at the current level.
The dummy node is used to initialize a not-null prev pointer.
The prev pointer is updated as nodes are processed, connecting them horizontally at the same level.
"""
from collections import deque


# Definition for a Node.
class Node:
    def __init__(
        self,
        val=0,
        left=None,
        right=None,
        next=None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        # Check if the tree is empty
        if not root:
            return None

        # Use a deque for level-order traversal
        q = deque()
        q.append(root)

        # Dummy node to initialize with a not null prev
        dummy = Node(-999)

        while q:
            length = len(q)  # Find the number of nodes at the current level

            prev = dummy
            for _ in range(length):
                popped = q.popleft()

                # Enqueue the left child and update the next pointer
                if popped.left:
                    q.append(popped.left)
                    prev.next = popped.left
                    prev = prev.next

                # Enqueue the right child and update the next pointer
                if popped.right:
                    q.append(popped.right)
                    prev.next = popped.right
                    prev = prev.next

        return root
