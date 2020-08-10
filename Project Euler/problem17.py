# https://projecteuler.net/problem=17
# If all the numbers from 1 to 1000 (one thousand)
# inclusive were written out in words, how many letters would be used?

import time
start_time = time.time()

letterSum = 0

def generateNumWord(num):
    if(num<1 or not num or num > 1000): return ''
    if(num == 1000): return "one thousand"

    word = ''
    units = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    teens = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
    tens = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }

    digit1 = num%10 # 1, 3, 5, 9
    digit2 = (num-digit1)%100 #20, 50
    digit3 = (num-digit1-digit2)%1000 #100, 400
    digit3Cnt = digit3//100

    # hundreds
    if(digit3):
        word += units[digit3Cnt] + " hundred"
        if(digit2 or digit1): word += " and "
    # tens
    if(digit2):
        if(digit2>=20):
            word += tens[digit2]
            if(digit1): word += " "
        else:
            word += teens[digit2+digit1]
            return word #skip units if teens
    # units
    if(digit1):
        word += units[digit1]
    return word

for i in range(1,1001):
    letterSum += len(generateNumWord(i).replace(" ",""))

solution = letterSum
print("SOLUTION:", solution)
print("--- %s seconds ---" % (time.time() - start_time))