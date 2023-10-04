# https://leetcode.com/problems/implement-stack-using-queues

"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""
from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()  # Initialize a deque to store elements for stack operations

    def push(self, x: int) -> None:
        self.q.append(x)  # Append the new element to the end of the deque
        q_len = len(self.q)  # Get the current length of the deque

        # Move all elements before the newly added element to the end
        # This operation simulates the behavior of a stack
        while q_len > 1:
            self.q.append(self.q.popleft())  # Move the front element to the end
            q_len -= 1

    def pop(self) -> int:
        return (
            self.q.popleft()
        )  # Pop the front element of the deque, which represents the top of the stack

    def top(self) -> int:
        return self.q[
            0
        ]  # Return the front element of the deque, which represents the top of the stack

    def empty(self) -> bool:
        return (
            len(self.q) == 0
        )  # Check if the deque is empty to determine if the stack is empty
