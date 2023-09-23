"""
URL :- https://www.codingninjas.com/studio/problems/allocate-books_1090540?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
"""
"""
Time Complexity:- O(N * log(sum(arr[])-max(arr[])+1))
Space Complexity:- o(1)
"""


def findPages(arr: [int], n: int, m: int) -> int:
    def countStudents(arr, n, pages):
        students = 1
        pages_students = 0

        for i in range(n):
            if pages_students + arr[i] <= pages:
                pages_students += arr[i]
            else:
                students += 1
                pages_students = arr[i]
        return students

    if m > n:
        return (
            -1
        )  # If the number of students is greater than the number of books, it's not possible.

    l = max(
        arr
    )  # Minimum possible maximum pages per student is the maximum page count of a single book.
    h = sum(
        arr
    )  # Maximum possible maximum pages per student is the sum of all book pages.

    while l <= h:
        mid = (l + h) // 2
        students = countStudents(arr, n, mid)

        if students > m:
            l = mid + 1
        else:
            h = mid - 1

    return l  # Return the minimum maximum pages allocated per student.
