# https://leetcode.com/problems/course-schedule-ii/
"""
Time complexity:- O(E+V) 
Space Complexity:- O(E+V)
"""

"""
Intuition:

DFS is used to traverse the graph of course prerequisites. If a cycle is detected during DFS, it means there is a dependency loop, and the courses cannot be scheduled.

Observation:

The DFS function recursively checks prerequisites for each course.
The findOrder function iterates through each course and initiates DFS to find a valid course order. The result is reversed to get the correct order.
"""
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a dictionary to store prerequisites for each course
        prereq = {c: [] for c in range(numCourses)}

        # Populate the prerequisite dictionary
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # Lists to store the final course order, visited courses, and courses in the current cycle
        output = []
        visit, cycle = set(), set()

        # Depth-First Search (DFS) function
        def dfs(crs):
            # If the course is in the current cycle, a cycle is detected
            if crs in cycle:
                return False
            # If the course is already visited, skip
            if crs in visit:
                return True

            # Add the course to the current cycle
            cycle.add(crs)

            # Recursively check prerequisites
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False

            # Remove the course from the current cycle, mark it as visited, and add it to the output list
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)

            return True

        # Iterate through each course and initiate DFS
        for c in range(numCourses):
            if dfs(c) == False:
                return []

        # Return the reversed order as the result
        return output[::-1]
