# https://www.codingninjas.com/studio/problems/1062712

"""
Time complexity:- O(N logN)
Space Complexity:- O(N) 
"""

"""
Intuition:

The goal is to find the maximum number of non-overlapping activities that can be performed.
The algorithm first transforms the start and finish times into tuples and sorts them based on the finishing times.
It then iterates through the sorted activities, selecting each activity if its start time is greater than or equal to the current time.
"""


def maximumActivities(start, finish):
    n = len(start)
    activity = []

    # Create a list of tuples (finish_time, start_time) for each activity.
    for i in range(n):
        activity.append((finish[i], start[i]))

    # Sort the activities based on their finishing times.
    activity.sort()

    maxActivity = 1  # Initialize the count of maximum activities.
    # Initialize the current time with the finishing time of the first activity.
    currentTime = activity[0][0]

    for i in range(1, n):
        # Find the next meeting available.
        if activity[i][1] >= currentTime:
            maxActivity += 1
            currentTime = activity[i][0]

    return maxActivity
