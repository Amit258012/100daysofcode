# https://leetcode.com/problems/dota2-senate/

"""
Time complexity:- O(N^2)
Space Complexity:- O(N) 
"""

"""
Intuition:

The process simulates the senators casting their votes to eliminate senators from the opposing party in a cyclic manner.
Senators who have not voted yet are at the front of their respective party queues.
The senator who arrived earlier in the original order is given the chance to vote first.
The process continues until one party runs out of senators, and the other party is declared the winner.
"""


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Get the length of the senate
        n = len(senate)

        # Create lists to store the indices of 'R' and 'D' senators
        r_arr = [i for i in range(len(senate)) if senate[i] == "R"]
        d_arr = [j for j in range(len(senate)) if senate[j] == "D"]

        # Continue the elimination process until one party has no senators left
        while r_arr and d_arr:
            # Get the indices of the front senators of each party
            r = r_arr.pop(0)
            d = d_arr.pop(0)

            # Check which senator came first
            if r < d:
                # If the 'R' senator came first, add it to the end of the 'R' queue
                r_arr.append(n + r)
            else:
                # If the 'D' senator came first, add it to the end of the 'D' queue
                d_arr.append(n + d)

        # Return the winner based on which queue is non-empty
        return "Radiant" if r_arr else "Dire"
