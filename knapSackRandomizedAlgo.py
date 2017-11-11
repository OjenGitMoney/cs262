import random
import csv
import time


def knapsackRandomized(items, maxCapacity):
    print len(items)
    knapSackFinal = []
    knapSackBinary = [0] * len(items)
    bestWeight = 0
    bestValue = 0
    i = 0
    startTime = time.time()
    print items
    while bestWeight <= maxCapacity:
        i+=1
        print i
        item = random.choice(items)
        if item not in knapSackFinal:
            bestWeight = bestWeight + item[0]
            bestValue = bestValue + item[1]
            if bestWeight <= maxCapacity:
                knapSackBinary[items.index(item)]= 1
                knapSackFinal.append(item)
        else:
            print "Already in it..."
            
    elapsedTime = time.time() - startTime
    print knapSackBinary
    return knapSackFinal, elapsedTime





if __name__ == '__main__':

    items = []
    with open('assets/inputData2.csv') as csvFile:
        reader = csv.DictReader(csvFile)
        for line in reader:
            items.append((int(line['weight']), int(line['cost'])))

    knapSackChosen, runtime = knapsackRandomized(items, maxCapacity=60)

    print "chosen : \n"
    print knapSackChosen
    print '\n'
    print runtime





