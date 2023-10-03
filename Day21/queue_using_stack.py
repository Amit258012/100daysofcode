# https://leetcode.com/problems/implement-queue-using-stacks

"""
Time complexity:- O(1)
Space Complexity:- O(n)
"""
from typing import List


class MyQueue:
    def __init__(self):
        # Initialize two stacks, 'input' and 'output', for queue operations
        self.input = []  # Used for push operations
        self.output = []  # Used for pop, peek, and checking emptiness

    def push(self, x: int) -> None:
        # Push an element onto the 'input' stack
        self.input.append(x)

    def pop(self) -> int:
        if self.output:
            # If the 'output' stack is not empty, pop and return the top element
            return self.output.pop()
        else:
            # If the 'output' stack is empty, move elements from 'input' to 'output' to simulate the queue
            for _ in range(len(self.input)):
                x = self.input.pop()
                self.output.append(x)
            # Pop and return the top element from 'output'
            return self.output.pop()

    def peek(self) -> int:
        if self.output:
            # If the 'output' stack is not empty, return the top element without popping it
            return self.output[-1]
        else:
            # If the 'output' stack is empty, move elements from 'input' to 'output' to simulate the queue
            for _ in range(len(self.input)):
                x = self.input.pop()
                self.output.append(x)
            # Return the top element from 'output' without popping it
            return self.output[-1]

    def empty(self) -> bool:
        if self.input:
            # If the 'input' stack is not empty, move elements from 'input' to 'output' to check emptiness
            for _ in range(len(self.input)):
                x = self.input.pop()
                self.output.append(x)
        # Check if 'output' stack is empty, indicating the queue is empty
        return len(self.output) == 0
