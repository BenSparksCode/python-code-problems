# https://leetcode.com/problems/coin-change/

# ATTEMPT 1 - Backtracking by Brute Force
# TIME = 
# SPACE = 

# TODO



# ATTEMP 2 - Backtracking faster with top down dynamic programming
# TIME = 
# SPACE = 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(coins, rem, count):
            if rem < 0: return -1
            if rem == 0: return 0
            if count[rem-1] != 0: return count[rem-1]
            min = float('inf')
            for coin in coins:
                res = helper(coins, rem-coin, count)
                if res >= 0 and res < min: min = 1 + res
            count[rem-1] = -1 if min == float('inf') else min
            return count[rem - 1]
