# https://projecteuler.net/problem=20
# Find the sum of the digits in the number 100!

import time
start_time = time.time()

solution = 0
cumulativeFactorial = 1

# First calculate 100!
for i in range(1, 101):
    cumulativeFactorial *= i

# Then sum the digits
for i in str(cumulativeFactorial):
    solution += int(i)

print("SOLUTION:", solution)
print("--- %s seconds ---" % (time.time() - start_time))
