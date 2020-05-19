# https://projecteuler.net/problem=9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import time
start_time = time.time()

abcSum = 1000

def findPythagTrip(abcSum):
    for a in range(1,abcSum):
        for b in range(1,abcSum):
            if a > b: continue
            c = abcSum - a - b
            if b > c: continue
            if a**2 + b**2 == c**2: return a*b*c

solution = findPythagTrip(abcSum)
print("SOLUTION:", solution)
print("--- %s seconds ---" % (time.time() - start_time))