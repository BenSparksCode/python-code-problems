# https://projecteuler.net/problem=7
# What is the 10 001st prime number?

# Starting with first 2 primes for
# incrementing by 2 each iteration
primes = {1:2, 2:3}
primeToFind = 10_001
cnt = 2
current = 3

while cnt < primeToFind:
    current += 2
    foundP = True
    for p in primes:
        if current % primes[p] == 0:
            foundP = False
            break
    if foundP:
        cnt += 1
        primes[cnt] = current

solution = current
print("SOLUTION:", solution)