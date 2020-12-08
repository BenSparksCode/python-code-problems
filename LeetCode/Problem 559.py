# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
#      if no node was passed in (error) - reject with 0
        if not root: return 0
#      if this node has no children - end of depth - return 1
        if not root.children: return 1
#      if children, for each child:
#        -call maxDepth to recursively get depth of child node
#      then find max depths of all children and choose biggest, then return depth
        return max(self.maxDepth(node) for node in root.children)+1