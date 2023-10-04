# https://practice.geeksforgeeks.org/problems/implement-queue-using-array/1

"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""


class MyQueue:
    def __init__(self):
        self.arr = []  # Initialize an empty list to represent the queue.

    # Function to push an element x in a queue.
    def push(self, x):
        # Append the element 'x' to the end of the list, simulating a queue.
        self.arr.append(x)

    # Function to pop an element from the queue and return that element.
    def pop(self):
        if len(self.arr) < 1:
            # If the queue is empty, return -1 as there's nothing to pop.
            return -1
        else:
            # Remove and return the element at the front of the list, simulating a queue.
            return self.arr.pop(0)
