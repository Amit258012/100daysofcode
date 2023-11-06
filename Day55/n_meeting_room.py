# https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

"""
Time complexity:- O(NlogN)
Space Complexity:- O(N) 
"""


class Solution:
    def maximumMeetings(self, n, start, end):
        # Create a list of meeting intervals, where each interval is represented as [start_time, end_time].
        meetings = []
        for i in range(n):
            meetings.append([start[i], end[i]])

        # Sort the list of meeting intervals based on the end times in ascending order.
        meetings.sort(key=lambda meeting: meeting[1])

        # Initialize variables 'lastEnd' to track the end time of the last chosen meeting, and 'maxMeetings' to count the number of meetings.
        lastEnd = meetings[0][1]
        maxMeetings = 1

        # Iterate through the sorted meeting intervals, starting from the second meeting.
        for j in range(1, n):
            currentStart, currentEnd = meetings[j]
            # If the start time of the current meeting is greater than or equal to the end time of the last chosen meeting,
            # it means they do not overlap, so we can choose the current meeting.
            if currentStart >= lastEnd:
                maxMeetings += 1
                lastEnd = currentEnd

        # Return the maximum number of non-overlapping meetings, which is stored in 'maxMeetings'.
        return maxMeetings
