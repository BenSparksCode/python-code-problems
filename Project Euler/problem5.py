# https://projecteuler.net/problem=5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

divNums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
allPFactLists = []
finalNum = 1

def primeFactors(n):
    """O(n) prime factors finder from problem3"""
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        divisor = divisor + 1
    return factors

# get list of all prime factors for all divNums
for i in divNums:
    allPFactLists.append(primeFactors(i))

# flatten and take only unique nums in allPFactLists
allPFactors = [i for sublist in allPFactLists for i in sublist]
uniquePFactors = set(allPFactors)

# taking max appearance of each prime factor
for i in uniquePFactors:
    maxCnt = 0
    for j in allPFactLists:
        cnt = j.count(i)
        if (cnt > maxCnt): maxCnt = cnt
    finalNum *= (i**maxCnt)

solution = finalNum
print("SOLUTION:", solution)