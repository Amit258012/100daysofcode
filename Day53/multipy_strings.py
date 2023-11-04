# https://leetcode.com/problems/multiply-strings/

"""
Time complexity:- O(N^2)
Space Complexity:- O(N+M) 
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either of the input numbers is "0", the result is "0".
        if "0" in [num1, num2]:
            return "0"

        # Initialize a result list to store the product.
        res = [0] * (len(num1) + len(num2))

        # Reverse the input strings to make it easier to iterate from right to left.
        num1, num2 = num1[::-1], num2[::-1]

        # Multiply the digits of num1 and num2, summing them up in the result list.
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        # Reverse the result list to get the final product.
        res, beg = res[::-1], 0

        # Remove leading zeros from the result.
        while beg < len(res) and res[beg] == 0:
            beg += 1

        # Convert the result digits to strings and join them to form the final result string.
        res = map(str, res[beg:])
        return "".join(res)
