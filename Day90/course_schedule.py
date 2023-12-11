# https://leetcode.com/problems/course-schedule/
"""
Time complexity:- O(E+V) 
Space Complexity:- O(E+V)
"""

"""
Intuition:

DFS is used to traverse the graph of course prerequisites. If a cycle is detected during DFS, it means there is a dependency loop, and the courses cannot be finished.

Observation:

The DFS function recursively checks prerequisites for each course.
The canFinish function iterates through each course and initiates DFS to check if it can be finished.
"""
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a map to store prerequisites for each course
        preMap = {i: [] for i in range(numCourses)}

        # Populate the prerequisite map
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Set to keep track of courses being visited during DFS
        visiting = set()

        # Depth-First Search (DFS) function
        def dfs(crs):
            # If the course is currently being visited, a cycle is detected
            if crs in visiting:
                return False

            # If there are no prerequisites for the current course, it can be finished
            if preMap[crs] == []:
                return True

            # Mark the current course as visiting
            visiting.add(crs)

            # Recursively check prerequisites
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # Remove the course from the visiting set and mark it as having no prerequisites
            visiting.remove(crs)
            preMap[crs] = []

            return True

        # Iterate through each course and check if it can be finished
        for c in range(numCourses):
            if not dfs(c):
                return False

        # All courses can be finished without a cycle
        return True
