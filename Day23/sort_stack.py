# https://www.codingninjas.com/studio/problems/sort-a-stack_985275?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&count=25&page=2&search=&sort_entity=order&sort_order=ASC

"""
Time complexity:- O(n^2)
Space Complexity:- O(n)
"""


# Function to pop an element from the stack.
def pop(stack):
    stack.pop()


# Function to push an element onto the stack.
def push(stack, element):
    stack.append(element)


# Function to return the top element of the stack.
def top(stack):
    return stack[-1]


# Function to check if the stack is empty.
def isEmpty(stack):
    return len(stack) == 0


# Recursive function to sort the stack using insertion sort.
def sort(stack, lastIndex):
    # Base case: if the last index is 0, return.
    if lastIndex == 0:
        return

    # Get the top element of the stack.
    temp = top(stack)
    pop(stack)

    # Recursively sort the stack with one less element.
    sort(stack, lastIndex - 1)

    # Insert the temporary element into the sorted stack.
    insert(stack, temp)


# Function to insert an element into the correct position in the stack.
def insert(stack, temp):
    # If the stack is empty or the top element is less than or equal to the temp element, push temp onto the stack.
    if isEmpty(stack) or top(stack) <= temp:
        push(stack, temp)
        return

    # Otherwise, pop the top element, recursively insert temp, and then push the popped element back onto the stack.
    lastVal = top(stack)
    pop(stack)
    insert(stack, temp)
    push(stack, lastVal)


# Function to sort the given stack in ascending order.
def sortStack(stack):
    # Call the recursive sort function with the initial last index (length of stack - 1).
    sort(stack, len(stack) - 1)
