# https://leetcode.com/problems/operations-on-tree/

"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import List


class LockingTree:
    def __init__(self, parent: List[int]):
        self.parent = parent  # List of parent nodes for each node.
        self.locked = [None] * len(parent)  # List to track locked nodes.
        # Dictionary to store children of each node.
        self.child = {i: [] for i in range(len(parent))}

        # Populate the 'child' dictionary based on parent-child relationships.
        for i in range(1, len(parent)):
            self.child[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:  # TC:- O(1)
        if self.locked[num]:
            return False  # Node is already locked by another user.
        self.locked[num] = user  # Lock the node.
        return True

    def unlock(self, num: int, user: int) -> bool:  # TC:-  O(1)
        if self.locked[num] != user:
            return False  # Node is not locked by the specified user.
        self.locked[num] = None  # Unlock the node.
        return True

    def upgrade(self, num: int, user: int) -> bool:  # TC:- O(N)
        i = num

        # Check the ancestors of the node to ensure no locked ancestor exists.
        while i != -1:
            if self.locked[i]:
                return False  # Ancestor is locked.

            i = self.parent[i]  # Move to the parent.

        lockedCount, q = 0, deque([num])
        while q:
            n = q.popleft()
            if self.locked[n]:
                self.locked[n] = None  # Unlock the node.
                lockedCount += 1
            q.extend(self.child[n])  # Add the children to the queue for unlocking.

        if lockedCount > 0:
            self.locked[num] = user  # Lock the specified node.
        return lockedCount > 0  # Return True if any nodes were unlocked.
