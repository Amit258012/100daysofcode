# https://leetcode.com/problems/task-scheduler/

"""
Time complexity:- O(N logN) + O(n * maxHeapSize) N:- tasks
Space Complexity:- O(N) 
"""

import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count occurrences of each task
        count = Counter(tasks)
        # Create a max heap with negative counts
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # Initialize time
        time = 0
        # Queue to store pairs of [-cnt, idleTime]
        q = deque()

        # Continue the process until both the max heap and the queue are empty
        while maxHeap or q:
            time += 1

            # If the max heap is empty, update the time to the next scheduled idle time
            if not maxHeap:
                time = q[0][1]
            else:
                # Pop the task with the highest count
                cnt = 1 + heapq.heappop(maxHeap)
                # If the count is still positive, enqueue it with the next scheduled idle time
                if cnt:
                    q.append([cnt, time + n])

            # If there are tasks in the queue and the current time matches the idle time,
            # push the task back into the max heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time


# Time Complexity (TC):
# - Constructing the max heap: O(t * log(t)), where t is the number of unique tasks.
# - Processing the tasks and idle times: O(n * maxHeapSize)
# - Overall: O(t * log(t)) + O(n * maxHeapSize)

# Space Complexity (SC):
# - O(t) for the max heap and queue, where t is the number of unique tasks.
