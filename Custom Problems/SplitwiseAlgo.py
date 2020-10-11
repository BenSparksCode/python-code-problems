import random

def generatePeopleSet(numPeople, maxAmount):
    # numPeople = people in the debt system
    # maxAmount = max net amount owed between 2 people

    peopleSet = []
    maxAmount = abs(maxAmount) # to accomodate the 0-symmetric RNG
    numPeople += 1 # adjusted to start people at "1"

    # Set up peopleSet array
    for i in range(1, numPeople):
        peopleSet.append({"name": str(i), "owes": [], "owed": []})

    for personA in range(1, numPeople):
        for personB in range(personA + 1, numPeople):
            # generate random int for tx amount
            amount = random.randint(-maxAmount, maxAmount)
            if(amount > 0):
                # positive balance for A -> A owed, B owes
                peopleSet[personA - 1]['owed'].append({"name": str(personB), "amount": amount})
                peopleSet[personB - 1]['owes'].append({"name": str(personA), "amount": amount})
            else:
                # negative balance for A -> A owes, B owed
                peopleSet[personA - 1]['owes'].append({"name": str(personB), "amount": abs(amount)})
                peopleSet[personB - 1]['owed'].append({"name": str(personA), "amount": abs(amount)})

    return peopleSet


def compressToNet(people):

    netPositions = {}

    for person in people:
        netOwes = [a["amount"] for a in person["owes"]]
        netOwed = [a["amount"] for a in person["owed"]]
        netPositions[person['name']] = sum(netOwed) - sum(netOwes)

    return netPositions

def testDataSystem(netPositions):
    sum = 0
    for i in netPositions:
        sum += netPositions[i]
    return sum == 0

def solveMinTransactions(netPositions):
    posNets = []
    negNets = []
    txs = []

    for person in netPositions:
        if (netPositions[person] > 0):
            posNets.append({'name': person, 'net': netPositions[person]})
        elif (netPositions[person] < 0):
            negNets.append({'name': person, 'net': netPositions[person]})
    
    print("positives", posNets)
    print("negatives", negNets)

    if (len(posNets) < len(negNets)):
        shortest, longest = posNets, negNets
    else:
        shortest, longest = negNets, posNets

    
    





randomPeepsArr = generatePeopleSet(5, 1000)
print(randomPeepsArr)

netPositions = compressToNet(randomPeepsArr)
print("Net positions:\n",netPositions)


solveMinTransactions(netPositions)

# print("All net positions sum to 0:\n", testDataSystem(answer))