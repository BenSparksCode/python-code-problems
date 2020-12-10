# https://leetcode.com/problems/single-number/

# Attempt 1 - Using dict for count - O(n) but needs extra memory
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnts = {}
        for i in nums:
            if (i in cnts):
                cnts[i] += 1
            else: #can use defaultdict to default each value to 0 (int default)
                cnts[i] = 1
        for key in cnts:
            if (cnts[key]==1): return key
        return

# Attempt 2 - Using bit manipulation (XOR) to null out duplicates and find unique
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a

