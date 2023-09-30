"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""
"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # Initialize the LRUCache with a given capacity
        self.dic = dict()  # key to node
        self.capacity = capacity
        self.head = ListNode(0, 0)  # Dummy head node
        self.tail = ListNode(-1, -1)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            # If the key exists in the cache, move it to the front of the list (most recently used)
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            # If the key is not in the cache, return -1
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            # If the key already exists, update its value, move it to the front (most recently used)
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value
        else:
            if len(self.dic) >= self.capacity:
                # If the cache is full, remove the least recently used item (from the tail)
                self.removeFromTail()
            node = ListNode(key, value)
            self.dic[key] = node
            self.insertIntoHead(node)

    def removeFromList(self, node):
        # Remove a node from the linked list
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertIntoHead(self, node):
        # Insert a node at the beginning of the linked list (most recently used)
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node

    def removeFromTail(self):
        if len(self.dic) == 0:
            return
        # Remove the least recently used item (from the tail)
        tail_node = self.tail.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)
