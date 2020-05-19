# https://projecteuler.net/problem=4
# Find the largest palindrome made from the product of two 3-digit numbers.
import time
start_time = time.time()

max = 0

def checkPalin(n):
    strNum = str(n)
    return (strNum == "".join(reversed(strNum)))

for i in range(1000):
    for j in range(1000):
        res = i*j
        if checkPalin(res) and res > max: max = res

solution = max
print("SOLUTION:", solution)
print("--- %s seconds ---" % (time.time() - start_time))