# https://leetcode.com/problems/sort-array-by-parity-ii

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odds = [i for i in A if i%2==1]
        evens = [i for i in A if i%2==0]
        result = []
        for i in range(0,len(odds)):
            result.append(evens[i])
            result.append(odds[i])
        return result