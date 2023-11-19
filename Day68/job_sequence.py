# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1
"""
Time complexity:- O(N logN)
Space Complexity:- O(N) 
"""

"""
Intuition:

The goal is to maximize the profit by selecting jobs with higher profit first.
The algorithm sorts the jobs in descending order of profit.
It then iterates through each job and assigns it to the last possible time slot, prioritizing higher profit jobs.
"""


class Job:
    """
    Job class which stores profit and deadline.
    """

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


class Solution:
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        res, count = 0, 0

        # Sorting all jobs according to decreasing order of profit.
        Jobs = sorted(Jobs, key=lambda x: x.profit, reverse=True)

        # Array to store the result (Sequence of jobs).
        result = [0 for i in range(n)]
        # Boolean array to keep track of free time slots
        # and initializing all slots to free.
        slot = [False for i in range(n)]

        # Iterating through all given jobs.
        for i in range(n):
            # Finding a free slot for the current job (Note that we start
            # from the last possible slot).
            for j in range(min(n, Jobs[i].deadline) - 1, -1, -1):
                # If a free slot is found, we add the current job to the result array
                # and make the current slot occupied.
                if not slot[j]:
                    result[j] = i
                    slot[j] = True
                    break

        # If a slot is occupied, we update the counter and
        # add its profit in the final result.
        for i in range(n):
            if slot[i]:
                res += Jobs[result[i]].profit
                count += 1

        # Storing the count of jobs and max profit in a list and returning it.
        ans = []
        ans.append(count)
        ans.append(res)
        return ans
