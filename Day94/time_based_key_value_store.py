# https://leetcode.com/problems/time-based-key-value-store/
"""
Time complexity:- O(1) - set , O(log N)- get
Space Complexity:- O(N)
"""

"""
Intuition:

The TimeMap class is designed to store key-value pairs with timestamps.
The set method is used to add a new [value, timestamp] pair to the list associated with a given key.
The get method is used to retrieve the value associated with a key at a specific timestamp.
Binary search is applied in the get method to efficiently find the maximum timestamp that is less than or equal to the given timestamp.
The result (res) is updated during the binary search based on the conditions.
"""


class TimeMap:
    def __init__(self):
        # Dictionary to store key-value pairs with timestamps
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key is not in the dictionary, add it with an empty list
        if key not in self.keyStore:
            self.keyStore[key] = []

        # Append the new [value, timestamp] pair to the list of the key
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1

        # Binary search to find the maximum timestamp that is less than or equal to the given timestamp
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
