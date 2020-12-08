# https://leetcode.com/problems/sort-array-by-parity-ii

# Attempt 1 - filter into sub arrays, then rebuild in order - slower, less memory
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odds = [i for i in A if i%2==1]
        evens = [i for i in A if i%2==0]
        result = []
        for i in range(0,len(odds)):
            result.append(evens[i])
            result.append(odds[i])
        return result

# Attempt 2 - 2 pass - faster, more memory
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        result = [None] * len(A)
        pntr = 0 #evens first
        for val in A:
            if(val%2==0):
                result[pntr] = val
                pntr += 2
        pntr = 1 #odds next
        for val in A:
            if(val%2==1):
                result[pntr] = val
                pntr += 2
        return result