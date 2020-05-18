# https://projecteuler.net/problem=3
# What is the largest prime factor of the number 600851475143?

num = 600851475143

def primeFactors(n):
    """O(n) prime factors finder"""
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        divisor = divisor + 1
    return factors

prime_factors = primeFactors(num)
solution = max(prime_factors)
print("SOLUTION:", solution)