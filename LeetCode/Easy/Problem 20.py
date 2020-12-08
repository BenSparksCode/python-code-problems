# https://leetcode.com/problems/valid-parentheses/

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(","}":"{","]":"["}
        stack = deque()

        if len(s)%2!=0:
            return False

        for char in s:
            if char in mapping:
                # If stack is empty, don't pop
                if stack:
                    top_char = stack.popleft()
                else:
                    top_char = "#"
                # Now check if pair matches - if not, return False
                if mapping[char] != top_char:
                    return False
            else:
                stack.appendleft(char)
        if len(stack) == 0:
            return True
        else:
            return False