# https://projecteuler.net/problem=25
# What is the index of the first term in the Fibonacci
# sequence to contain 1000 digits?

# Time to solve:
# - For loop without memoization:   ~0.628 seconds
# - Recursion with memoization:     ~0.023 seconds

from index import *

fibCache = {}

# Returns the fibonacci sequence number at index n,
# using an iterative for-loop approach without memoization
def slowFib(n: int) -> int:
    if n <= 2: return 1
    curr = 1
    prev = 1
    for i in range(n - 2):
        temp = curr
        curr = prev + curr
        prev = temp
    return curr

# Returns the fibonacci sequence number at index n,
# using a recursive approach with memoization
def fastFib(n: int) -> int:
    if n <= 2: return 1
    if n in fibCache:
        return fibCache[n]
    else:
        ans = fastFib(n-1) + fastFib(n-2)
        fibCache[n] = ans
        return ans

@timer
def findSmallestFibOfDigits(digits: int) -> (int, int):
    index = 1
    while True:
        latestFib = fastFib(index)
        if latestFib > 10 ** (digits - 1):
            return (index, latestFib)
        index += 1 

index, fibNum = findSmallestFibOfDigits(1000)

solution = index
print("SOLUTION:", solution)