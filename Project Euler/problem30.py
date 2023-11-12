# https://projecteuler.net/problem=30
# Find the sum of all the numbers that
# can be written as the sum of fifth powers of their digits.

import functools
from index import timer

@timer
def solveProblem30() -> int:
    power = 5
    unitsToThePow = {}
    allSumPowNums = []

    # populate unitPow5s
    for i in range(10):
        unitsToThePow[i] = i**power

    for i in range(10,200_000):
        # turn num into list of digits
        digits = [unitsToThePow[int(j)] for j in str(i)]
        if(i == functools.reduce(
            lambda a,b : a+b, digits
            )): allSumPowNums.append(i)
        
    return sum(allSumPowNums)

solution = solveProblem30()
print("SOLUTION:", solution)