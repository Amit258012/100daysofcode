# https://leetcode.com/problems/simplify-path

"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []  # Initialize a stack to keep track of the simplified path
        cur = (
            ""  # Initialize an empty string to build the current directory or filename
        )

        # Loop through each character in the input 'path'
        for ch in path + "/":
            if ch == "/":
                # When encountering a "/", check the content of 'cur'
                if cur == "..":
                    # If 'cur' is "..", pop the top element from the stack to move up one directory
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    # If 'cur' is not empty and not ".", it represents a directory or filename, so add it to the stack
                    stack.append(cur)
                cur = ""  # Reset 'cur' for the next directory or filename
            else:
                cur += ch  # Append the character to 'cur' to build the current directory or filename

        # Construct the simplified path by joining the elements in the stack with "/"
        return "/" + "/".join(stack)
