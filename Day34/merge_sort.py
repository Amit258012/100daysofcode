# https://www.codingninjas.com/studio/problems/merge-sort_5846?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

"""
Time complexity:- O(n logn)
Space Complexity:- O(n)
"""


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # Create temporary arrays for the left and right halves
    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[l + i]

    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i = 0  # Initial index of the first subarray
    j = 0  # Initial index of the second subarray
    k = l  # Initial index of the merged subarray

    # Merge the two halves by comparing elements
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr: [int], l: int, r: int):
    if l < r:
        # Find the middle point of the array
        m = l + (r - l) // 2

        # Recursively sort the first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        # Merge the sorted halves
        merge(arr, l, m, r)
