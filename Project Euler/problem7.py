# https://projecteuler.net/problem=7
# What is the 10 001st prime number?
import math 
import time
start_time = time.time()

primes = {1:2, 2:3}
primeToFind = 10_001
cnt = 2
current = 3

while cnt < primeToFind:
    current += 2
    foundP = True
    for p in primes:
        if math.sqrt(current) < primes[p]: break
        if current % primes[p] == 0:
            foundP = False
            break
    if foundP:
        cnt += 1
        primes[cnt] = current

solution = current
print("SOLUTION:", solution)
print("--- %s seconds ---" % (time.time() - start_time))