import random
import csv
import time

def knapsack(items, maxCapaciy):
    knapsackFinal = []
    bestWeight= 0
    bestValue = 0
    superSet = makeSuperSet(items)
    knapsackBinary = [0] * len(superSet[len(superSet)-1])

    startTime = time.time()
    for itemSet in superSet:
        setWeight = sum([weight[0] for weight in itemSet])
        setValue = sum([value[1] for value in itemSet])
        if setValue > bestValue and setWeight <= maxCapaciy:
            bestValue = setValue
            bestWeight = setWeight
            knapsackFinal = itemSet

    elapsedTime = time.time() - startTime

    last_list = superSet[len(superSet) - 1]
    for onePicked in knapsackFinal:
        knapsackBinary[last_list.index(onePicked)] = 1
    print last_list
    print knapsackBinary
    return knapsackFinal, elapsedTime

def makeSuperSet(listOfItems):
    superSet = [[]]
    for item in listOfItems:
        newSet = [t+[item] for t in superSet]
        superSet.extend(newSet)
    return superSet[1:]

def makeDataFile(n):
    file = open('assets/inputData2.csv', 'w')
    file.writelines('weight' + ',' + 'cost' + '\n')
    for i in range(n):
        file.writelines(str(random.randint(1,50)) + ',' + str(random.randint(1,100)) + '\n')

if __name__ == '__main__':
    makeDataFile(21)
    items = []
    with open('assets/inputData2.csv') as csvFile:
        reader = csv.DictReader(csvFile)
        for line in reader:
            items.append((int(line['weight']), int(line['cost'])))
    t = makeSuperSet(items)
    print len(t)
    knapSackChosen, runtime = knapsack(items, maxCapaciy=60)

    print "chosen : \n"
    print knapSackChosen
    print '\n'
    print runtime