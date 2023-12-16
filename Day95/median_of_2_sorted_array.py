# https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
Time complexity:- O(log(min(M,N)))
Space Complexity:- O(1)
"""

"""
Intuition:

The code uses a binary search approach to find the correct partition in the smaller array (nums1), such that the elements on the left side of both partitions are smaller than the elements on the right side.
It calculates the corresponding partition in the larger array (nums2) to maintain balance.
The algorithm adjusts the partitions based on the values of the elements around them until a valid partition is found.
The median is then calculated based on the positions of the middle elements.
"""


from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to simplify partitioning
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            # Perform binary search on the smaller array (nums1)
            partitionA = (left + right) // 2
            # Calculate partition for the larger array (nums2)
            partitionB = (m + n + 1) // 2 - partitionA

            # Determine values for the four elements around partitions
            maxLeftA = float("-inf") if partitionA == 0 else nums1[partitionA - 1]
            minRightA = float("inf") if partitionA == m else nums1[partitionA]
            maxLeftB = float("-inf") if partitionB == 0 else nums2[partitionB - 1]
            minRightB = float("inf") if partitionB == n else nums2[partitionB]

            # Check if the current partitions are correct
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                # If the total number of elements is even, return the average of middle elements
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                # If the total number of elements is odd, return the larger of the two middle elements
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                # Adjust the partition for nums1 to the left
                right = partitionA - 1
            else:
                # Adjust the partition for nums1 to the right
                left = partitionA + 1
