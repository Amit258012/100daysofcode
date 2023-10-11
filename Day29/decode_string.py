# https://leetcode.com/problems/decode-string/
"""
Time complexity:- O(N * max(M)), where N is the length of the input string, and M is the maximum number of repeats for a substring.
Space Complexity:- O(N * max(M)), as the stack can potentially hold N * max(M) characters.
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # Initialize a stack to process characters.

        for i in range(len(s)):
            # If the character is not ']', push it onto the stack.
            if s[i] != "]":
                stack.append(s[i])
            else:
                subStr = ""  # Initialize an empty string to store the substring inside the brackets.
                while stack[-1] != "[":
                    # Pop characters until '[' is encountered, reversing their order.
                    subStr = stack.pop() + subStr
                stack.pop()  # Pop the '[' character.

                k = ""  # Initialize an empty string to store the repeat count.
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k  # Pop digits to construct the repeat count.

                # Push the repeated substring back onto the stack.
                stack.append(int(k) * subStr)

        # Join the remaining characters on the stack to obtain the decoded string.
        return "".join(stack)
