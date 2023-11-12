# https://projecteuler.net/problem=55
# A Lychrel number is a natural number that cannot form a palindrome
# through the iterative process of repeatedly reversing its digits
# and adding the resulting numbers. 
# How many Lychrel numbers are there below ten-thousand?

from index import timer

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

@timer
def countLychrelNumbers(upperLimit: int) -> int:
    cnt = 0
    for i in range(upperLimit):
        if(isLychrel(i)):
            cnt += 1
    return cnt

solution = countLychrelNumbers(10_000)
print("SOLUTION:", solution)