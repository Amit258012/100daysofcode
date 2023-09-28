"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
"""
"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.bottom = None


def mergeTwoLists(a, b):
    # Initialize a temporary node and result node
    temp = Node(0)
    res = temp

    # Merge the linked lists while maintaining the order
    while a and b:
        if a.data < b.data:
            temp.bottom = a
            temp = temp.bottom
            a = a.bottom
        else:
            temp.bottom = b
            temp = temp.bottom
            b = b.bottom

    # Append any remaining elements from either list
    if a:
        temp.bottom = a
    else:
        temp.bottom = b

    # Return the merged result
    return res.bottom


def flatten(root):
    # Base cases: If the root is None or has no next element, return the root itself
    if root is None or root.next is None:
        return root

    # Recursively flatten the list on the right
    root.next = flatten(root.next)

    # Merge the current list with the flattened right list
    root = mergeTwoLists(root, root.next)

    # Return the merged result
    return root
