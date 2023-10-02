# https://leetcode.com/problems/car-fleet/

"""
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.
"""
"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of pairs, each containing a car's position and speed
        pairs = [(p, s) for p, s in zip(position, speed)]
        stack = []  # Initialize a stack to keep track of car fleets

        # Sort the pairs in descending order of position
        pairs.sort(reverse=True)

        for p, s in pairs:
            # Calculate the time it takes for the car to reach the target
            time_to_target = (target - p) / s
            # Append the time to the stack
            stack.append(time_to_target)

            # Check if there are at least two cars in the stack and the car behind can't catch up to the car in front
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                # Remove the car behind from the stack
                stack.pop()

        # The length of the stack represents the number of car fleets
        return len(stack)
