# https://leetcode.com/problems/self-dividing-numbers/

# First attempt
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            numStrList = list(str(i))
            if('0' in numStrList): continue
            isSelfDivNum = str(i).replace("0","") == "".join([j for j in numStrList if i % int(j) == 0])
            if(isSelfDivNum): res.append(i)
        return res

# Second attempt - learnt For/Else in Python
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            for char in str(i):
                if(char == '0' or i % int(char) != 0): break
            else:
                res.append(i)
        return res
    