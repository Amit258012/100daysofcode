"""
There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.
"""
"""
Time complexity:- O(1)
Space Complexity:- O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteNode(self, node):
        """
        Delete a node from a singly-linked list.

        Args:
            node (ListNode): The node to be deleted.

        Returns:
            None: The method modifies the linked list in-place and does not return anything.
        """
        # Update the current node's value with the value of the next node
        node.val = node.next.val

        # Bypass the next node by updating the 'next' reference
        node.next = node.next.next
