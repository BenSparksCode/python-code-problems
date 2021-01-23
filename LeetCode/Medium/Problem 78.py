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

# ATTEMPT 2 - Backtracking. Recursively build subsets,
# grouped by subset length. Use backtracking to replace
# numbers starting from end of a built subset, after
# adding the completed subset
# TIME = O(N * 2^N) -> because subsets of n items is 2^n 
# SPACE = O(N * 2^N)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            if len(curr) == k:
                out.append(curr[:]) #add [:] if breaks

            for i in range(first, len(nums)):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()
        
        out = []
        for k in range(len(nums)+1):
            backtrack()
        return out