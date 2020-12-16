# https://leetcode.com/problems/predict-the-winner/

# ATTEMPT 1 - Recursive Minimax, no memo
# TIME: O(2^n)
# SPACE: O(n)
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def winner(nums, s, e, turn):
            if s == e: return turn * nums[s]
            a = turn * nums[s] + winner(nums, s+1, e, -turn)
            b = turn * nums[e] + winner(nums, s, e-1, -turn)
            return max(a,b) if turn==1 else min(a,b) 
        return winner(nums, 0, len(nums)-1, 1) >= 0

# ATTEMPT 2 - Recursive Minimax, with memo
# TIME: O(n^2) - nxn memo dict filled only once
# SPACE: O(n^2) - nxn dictionary
# 160x improvement in runtime speed on LeetCode over ATTEMPT 1
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def winner(s,e):
            if s == e: return nums[s]
            if (s,e) in memo: return memo[(s,e)]
            score = max(nums[e]-winner(s,e-1), nums[s] - winner(s+1, e))
            memo[(s,e)] = score
            return score
        memo = {}
        return winner(0, len(nums)-1) >= 0