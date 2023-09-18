"""
        Merge two sorted arrays 'nums1' and 'nums2' into 'nums1' in sorted order.

        Args:
            nums1 (List[int]): The first sorted array with extra space to accommodate 'nums2'.
            m (int): The number of elements in 'nums1'.
            nums2 (List[int]): The second sorted array.
            n (int): The number of elements in 'nums2'.

        Returns:
            None: The function modifies 'nums1' in-place.
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1  # Initialize a pointer for the last element of 'nums1'.
        j = n - 1  # Initialize a pointer for the last element of 'nums2'.
        k = m + n - 1  # Initialize a pointer for the last position of 'nums1'.

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                # If the current element in 'nums1' is greater, copy it to the end of 'nums1'.
                nums1[k] = nums1[i]
                i -= 1
            else:
                # If the current element in 'nums2' is greater or 'nums1' is exhausted,
                # copy the current element in 'nums2' to the end of 'nums1'.
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
