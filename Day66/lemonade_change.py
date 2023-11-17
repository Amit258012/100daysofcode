# https://leetcode.com/problems/lemonade-change/

"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:

Maintain counts for $5 and $10 bills.
Iterate through each customer's bill.
Provide change using available $5 and $10 bills.
Return True if all customers are served; otherwise, return False.
"""
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Initialize counts for $5 and $10 bills
        five = ten = 0

        # Iterate through each customer's bill
        for bill in bills:
            if bill == 5:
                # Handle $5 bill
                five += 1
            elif bill == 10:
                # Handle $10 bill
                if not five:
                    # If no $5 bill is available, cannot provide change
                    return False
                five -= 1
                ten += 1
            else:
                # Handle $20 bill
                if ten and five:
                    # Use $10 and $5 bills if available
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    # Use three $5 bills if $10 is not available
                    five -= 3
                else:
                    # If no suitable change, cannot provide change
                    return False

        # If all customers are served, return True
        return True
