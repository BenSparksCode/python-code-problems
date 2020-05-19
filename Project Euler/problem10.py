# https://projecteuler.net/problem=10
# Find the sum of all the primes below two million.
import time
import math

start_time = time.time()

primes = [2,3]
primeThreshold = 2_000_000
pSum = sum(primes)
current = 3

while current < primeThreshold:
    current += 2
    foundP = True
    for p in primes:
        if math.sqrt(current) < p: break
        if current % p == 0:
            foundP = False
            break
    if foundP:
        pSum += current
        primes.append(current)

solution = pSum
print("SOLUTION:", solution)
print("--- %s seconds ---" % (time.time() - start_time))
