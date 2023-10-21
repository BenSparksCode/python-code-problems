# https://projecteuler.net/problem=22
# Using names.txt, work out the alphabetical value for each name,
# multiply this value by its alphabetical position in
# the list to obtain a name score.
# What is the total of all the name scores in the file?

import time
start_time = time.time()

namesFileDir = "./assets/names.txt"
totalNameScores = 0
nameList = []

def loadNameListAndSort(dir: string) -> list:

    return []

def calculateLetterScore(word: string) -> int:

    return 0

def calculateSumOfNameScores(names: list) -> int:

    return 0

nameList = loadNameListAndSort(namesFileDir)
totalNameScores = calculateSumOfNameScores(nameList)

solution = totalNameScores
print("SOLUTION:", solution)
print("--- %s seconds ---" % (time.time() - start_time))