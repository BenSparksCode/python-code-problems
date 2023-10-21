# https://projecteuler.net/problem=22
# Using names.txt, work out the alphabetical value for each name,
# multiply this value by its alphabetical position in
# the list to obtain a name score.
# What is the total of all the name scores in the file?

import os
import time
start_time = time.time()

namesFileDir = '/Project Euler/assets/problem22 - names.txt'
totalNameScores = 0
nameList = []

def loadNameListAndSort(dir: str) -> list:
    rawTextString = ""
    with open(os.getcwd() + dir) as f:
        rawTextString = f.readline()
    return sorted(rawTextString.replace('"',"").split(","))

def calculateLetterScore(word: str) -> int:
    return sum([ord(c) - 64 for c in word])

def calculateSumOfNameScores(names: list) -> int:
    sumScores = 0
    for i, name in enumerate(names, start = 1):
        sumScores += i * calculateLetterScore(name)
    return sumScores

nameList = loadNameListAndSort(namesFileDir)
totalNameScores = calculateSumOfNameScores(nameList)

solution = totalNameScores
print("SOLUTION:", solution)
print("--- %s seconds ---" % (time.time() - start_time))