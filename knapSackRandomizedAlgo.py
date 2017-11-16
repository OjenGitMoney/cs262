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
            if bestWeight <= maxCapacity:
                bestValue = bestValue + item[1]
                knapSackBinary[items.index(item)]= 1
                knapSackFinal.append(item)
        else:
            print "Already in it..."
            
    elapsedTime = time.time() - startTime
    print knapSackBinary
    print bestValue
    return knapSackFinal, elapsedTime, bestValue





if __name__ == '__main__':

    items = []
    with open('assets/inputData2.csv') as csvFile:
        reader = csv.DictReader(csvFile)
        for line in reader:
            items.append((int(line['weight']), int(line['cost'])))
    for i in range(100):
        knapSackChosen, runtime, bestValue = knapsackRandomized(items, maxCapacity=60)
        # print "chosen : \n"
        # print knapSackChosen
        # print '\n'
        # print runtime
        f = open('RandResults.csv', 'a')
        f.write(knapSackChosen.__str__())
        f.write(',')
        f.write(runtime.__str__())
        f.write(',')
        f.write(bestValue.__str__())
        f.write('\n')
    f.close()



