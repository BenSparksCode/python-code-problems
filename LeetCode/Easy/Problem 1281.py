# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

import functools

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = functools.reduce(lambda x,y: int(x)*int(y), str(n))
        sm = functools.reduce(lambda x,y: int(x)+int(y), str(n))
        return int(prod) - int(sm)