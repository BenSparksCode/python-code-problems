# https://projecteuler.net/problem=6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

nums = range(1,101) #first 100 naturals
sumSquares = 0
sumOnly = 0

for i in nums:
    sumSquares += i**2
    sumOnly += i

solution = (sumOnly**2) - sumSquares
print("SOLUTION:", solution)