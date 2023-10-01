# https://leetcode.com/problems/min-stack/

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""
"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""


class MinStack:
    def __init__(self):
        # Initialize two stacks: one for the main elements and one for tracking the minimum elements
        self.stack = []  # Main stack to store elements
        self.minStack = []  # Stack to store the minimum elements

    def push(self, val: int) -> None:
        # Push the element onto the main stack
        self.stack.append(val)

        # Calculate the minimum between the current value and the previous minimum (if any)
        min_val = min(val, self.minStack[-1] if self.minStack else val)

        # Push the minimum value onto the minStack
        self.minStack.append(min_val)

    def pop(self) -> None:
        # Pop an element from both the main stack and the minStack
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top element of the minStack, which is the minimum value in the stack
        return self.minStack[-1]
