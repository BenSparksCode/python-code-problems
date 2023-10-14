# https://projecteuler.net/problem=55
# A Lychrel number is a natural number that cannot form a palindrome
# through the iterative process of repeatedly reversing its digits
# and adding the resulting numbers. 
# How many Lychrel numbers are there below ten-thousand?

import time
start_time = time.time()

# SOLUTION CODE STARTS HERE

def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]

def reverseDigitsAndAdd(n: int) -> int:
    return n + int(str(n)[::-1])

def isLychrel(n: int) -> bool:
    for i in range(1,51):
        n = reverseDigitsAndAdd(n)
        if(is_palindrome(n)):
            return False
    return True

def countLychrelNumbers(upperLimit: int) -> int:
    cnt = 0
    for i in range(upperLimit):
        if(isLychrel(i)):
            cnt += 1
    return cnt

# SOLUTION CODE ENDS HERE

solution = countLychrelNumbers(10_000)
print("SOLUTION:", solution)
print("--- %s seconds ---" % (time.time() - start_time))