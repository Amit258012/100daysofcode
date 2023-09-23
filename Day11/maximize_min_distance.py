"""
You are given an array ‘arr’ of size ‘n’ which denotes the position of stalls.
You are also given an integer ‘k’ which denotes the number of aggressive cows.
You are given the task of assigning stalls to ‘k’ cows such that the minimum distance between any two of them is the maximum possible.
Find the maximum possible minimum distance.
"""

"""
Time Complexity:- O(NlogN) + O(N * log(max(stalls[])-min(stalls[])))
Space Complexity:- o(1)
"""


class Solutions:
    def can_place_cows(self, stalls, dist, k):
        count_cows = 1
        last = stalls[0]
        n = len(stalls)

        for i in range(1, n):
            if stalls[i] - last >= dist:
                count_cows += 1
                last = stalls[i]
            if count_cows >= k:
                return True
        return False

    def max_min_distance(self, stalls, k):
        stalls.sort()  # Sort the stalls in ascending order.
        l = 1
        h = (
            stalls[-1] - stalls[0]
        )  # Set the search range based on the minimum and maximum stall positions.
        result = 0  # Initialize a variable to store the maximum distance.

        while l <= h:
            mid = (l + h) // 2

            if self.can_place_cows(mid, k):
                result = mid  # Update the maximum distance if it's possible to place cows with this distance.
                l = mid + 1
            else:
                h = mid - 1

        return (
            result  # Return the maximum minimum distance where you can place 'k' cows.
        )
