# https://leetcode.com/problems/subsets/

# ATTEMPT 1 - Cascading. Build subsets in an output list
# by updating them iteratively for every new number you
# explore in the input list
# TIME = O(N * 2^N) -> because subsets of n items is 2^n 
# SPACE = O(N * 2^N)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        
        for num in nums:
            out += [curr + [num] for curr in out]
            
        return out
