# https://leetcode.com/problems/plus-one/

"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""


from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Iterate through the digits in reverse order.
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is less than 9, increment it by 1 and return the result.
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                # If the current digit is 9, set it to 0 to handle the carry.
                digits[i] = 0

        # If all digits were 9 (carry all the way to the most significant digit),
        # insert a new digit '1' at the beginning of the list.
        digits.insert(0, 1)
        return digits
