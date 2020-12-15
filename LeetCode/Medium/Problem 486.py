# https://leetcode.com/problems/predict-the-winner/

# ATTEMPT 1 - Recursive Minimax, no memo
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def winner(nums, s, e, turn):
            if s == e: return turn * nums[s]
            a = turn * nums[s] + winner(nums, s+1, e, -turn)
            b = turn * nums[e] + winner(nums, s, e-1, -turn)
            return max(a,b) if turn==1 else min(a,b) 
        return winner(nums, 0, len(nums)-1, 1) >= 0
