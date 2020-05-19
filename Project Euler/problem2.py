# https://projecteuler.net/problem=2
# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, find the
# sum of the even-valued terms.
import time
start_time = time.time()

i = 1
sum = 0
fibNums = {1: 1, 2: 1}

def getFib(n):
    if (n and n > 0):
        if (n in fibNums): return fibNums[n]
        fibNums[n-1] = getFib(n-1)
        fibNums[n-2] = getFib(n-2)
        return fibNums[n-1] + fibNums[n-2]
    else: return 0

fibNum = getFib(i)
while( fibNum < 4_000_000):
    sum += fibNum if (fibNum % 2 == 0) else 0
    i += 1
    fibNum = getFib(i)

solution = sum
print("SOLUTION:", solution)
print("--- %s seconds ---" % (time.time() - start_time))
