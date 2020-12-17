# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ATTEMPT 1 - DFS with Stack
# TIME = O(n)
# SPACE = O(n)

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        stack = [(root, root.val)]
        while stack:
            currNode, accVal = stack.pop()
            if currNode.left == None and currNode.right == None and accVal == sum:
                return True
            if currNode.left:
                stack.append((currNode.left, accVal + currNode.left.val))
            if currNode.right:
                stack.append((currNode.right, accVal + currNode.right.val))
        return False


# ATTEMPT 2 - BFS with Queue
# TIME = O(n)
# SPACE = O(n)

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        queue = [(root, sum-root.val)]
        while queue:
            currNode, netVal = queue.pop(0)
            if currNode.left == None and currNode.right == None and netVal == 0:
                return True
            if currNode.left:
                queue.append((currNode.left, netVal - currNode.left.val))
            if currNode.right:
                queue.append((currNode.right, netVal - currNode.right.val))
        return False

