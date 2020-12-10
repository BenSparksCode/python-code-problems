# https://leetcode.com/problems/remove-outermost-parentheses/

# Elegant solution from comments:
# https://leetcode.com/problems/remove-outermost-parentheses/discuss/270022/JavaC%2B%2BPython-Count-Opened-Parenthesis
# Based on intuition that all primitives have equal num of ( as )
# Loops, keeping track of open/closed count, adding only brackets inside primitive to a result []
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, opened = [], 0
        for char in S:
            if(opened > 0 and char == "("):res.append(char)
            if(opened > 1 and char == ")"):res.append(char)
            opened += 1 if char == "(" else -1
        return "".join(res)