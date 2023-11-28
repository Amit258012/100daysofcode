# https://leetcode.com/problems/solving-questions-with-brainpower/
"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""

"""
Intuition:

The code addresses the problem of finding the maximum points that can be obtained by answering a sequence of questions with certain jump constraints.
Dynamic programming is utilized to efficiently calculate the maximum points for each question, considering the points and jump values.
The 'dp' array is filled in a bottom-up manner, and at each step, the choice is made between skipping the current question or answering it and considering the next question based on the jump value.
The final result is the maximum points that can be obtained by answering the questions starting from the first question.
"""
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Get the number of questions
        n = len(questions)

        # Initialize an array 'dp' to store the maximum points for each question
        dp = [0] * (n + 1)

        # Iterate through questions in reverse order
        for i in range(n - 1, -1, -1):
            # Extract the point value and jump value for the current question
            point = questions[i][0]
            jump = questions[i][1]

            # Calculate the index of the next question considering the jump value
            nextQuestion = min(n, i + jump + 1)

            # Update 'dp' for the current question with the maximum points
            dp[i] = max(dp[i + 1], point + dp[nextQuestion])

        # The result is the maximum points for the first question (at index 0)
        return dp[0]
