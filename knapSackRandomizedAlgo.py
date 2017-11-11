import random
import csv
import time


def knapsackRandomized(items, maxCapacity):
    print len(items)
    knapSackFinal = [0] * len(items)
    bestWeight = 0
    bestValue = 0

    runtime = time.time()
    # for item in items:
    #
    #     knapSackFinal.append(item)

    print len(knapSackFinal)
    return knapSackFinal, runtime








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





