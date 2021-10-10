# Written by Patrick Keener
# This program tests binary search vs hash table lookup for speed
#


import random as rd
import time

# listSizes = [10, 100, 1000, 10000, 50000, 100000, 500000, 2500000, 500000
# , 1000000, 5000000, 25000000,100000000]
numLoops = 30
listSizes = [100000000]

def gen_list2(listSize):
    """ Generates a list of T/F to be searched through """
    unsortedList = list()
        
    ts = time.clock()
    unsortedList = [False for i in range(listSize-1)]
    unsortedList.append(True)
        
    te = time.clock()
    tt = te - ts

    print('\nList completed with {} elements in {} seconds'.format(listSize, tt))
    return unsortedList


def gen_list(listSize):
    """ Generates the random numbers to be searched through """
    unsortedList = list()
    rand_low = 0
    rand_high = 100
    
    ts = time.clock()
    unsortedList = [rd.randint(rand_low, rand_high) for x in range(listSize)]
    te = time.clock()
    tt = te - ts

    print('\nList completed with {} elements in {} seconds'.format(listSize, tt))
    return unsortedList



def printResults(avgTime, loops, ttt, avgPt, tpt):
    """ Prints outputs """

    print("\nAverage time of {} seconds per loop over {} loops."\
    "\nAverage prep time of {} \nAverage Remaining Time {}"\
    "\nTotal time of {} seconds.".format(avgTime, loops, avgPt, avgTime - avgPt
    , ttt))
    return None


def testBinary(testList,testNum):
    """ Uses binary search to find the item and measures time """
    ts = time.clock() # time start
    mergeSort(testList)
    te1 = time.clock() # prep time end

    binarySearch(testList, testNum)
    te = time.clock() # time end
    
    return te - ts, te1 - ts


def testHash(testList, testNum):
    """ Uses a hash function (dictionary) to find the item and measures time """
    ts = time.clock() # time start

    boolList = [False]*(len(testList)-1)
    boolList.append(True)    
    testDict = dict(zip(testList, boolList))
    te1 = time.clock() # prep time end

    testDict[testNum] == True
    te = time.clock() # time end

    return te - ts, te1 - ts



def hashTesting(listSize, loops):
    """ Controls program flow for testing the hash function """
    testList = gen_list(listSize)
    testList2 = testList
    testNum = testList[-1]
    tt = ttt = tpt = 0 # initialize time variables

    # Hash testing
    for n in range(loops):
        testList = testList2
        tt, prepTime = testHash(testList, testNum)
        ttt += tt # total total time (all iterations)
        tpt += prepTime # total prep time
    avgTime = ttt / loops
    avgPt = tpt / loops
    printResults(avgTime, loops, ttt, avgPt, tpt)
   
    return None


def binTesting(listSize, loops):
    """ Controls program flow for testing the binary search function """
    testList = gen_list2(listSize)
    testList2 = testList
    testNum = testList[-1]
    tt = ttt = tpt = 0 # initialize time variables    

    # Binary testing
    for n in range(loops):
        testList = testList2
        tt, prepTime = testBinary(testList, testNum)      
        ttt += tt # total total time (all iterations)
        tpt += prepTime # total prep time
    avgTime = ttt / loops
    avgPt = tpt / loops
    printResults(avgTime, loops, ttt, avgPt, tpt)
    
    return None


def binarySearch(numList, searchNum):
    """ 
    Conducts a binary search to determine whether the number is in the list;
    Implementation from lecture

    Keyword Inputs:
    numList - the list of numbers to search within
    searchNum - the number being searched for

    Returns:
    Integer or Bool - The index where the number can be found, or False otherwise
    """
    
    low = 0
    high = len(numList) - 1
    
    while low <= high: # keep going as long as there is a place to search
        mid = (low + high)//2
        item = numList[mid]
    
        if searchNum == item: # number found- yay!
            return mid
        elif searchNum < item:
            high = mid - 1 # search lower half
        else:
            low = mid + 1  # search upper half; also loop to exit if not found
    
    return -1 # return False if it's not in list


def mergeSort(numList):
    """ Merge Sort takes a divide & conquer approach to sorting; 
    implementation from the lecture """

    n = len(numList)

    if n >1:
        
        # Break list into halves
        m = n //2
        numList1, numList2 = numList[:m], numList[m:]

        # Recursively call the mergeSort function
        mergeSort(numList1)
        mergeSort(numList2)

        # Merge the lists back together
        merge(numList1, numList2, numList)
            

def merge(lst1, lst2, lst3):
    """ Used in mergeSort, merges list back together"""

    # Initialize variables
    i1 = i2 = i3 = 0
    n1, n2 = len(lst1), len(lst2)

    # loop through list until all items have been accounted for
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:
            lst3[i3] = lst1[i1]
            i1 += 1
        else:
            lst3[i3] = lst2[i2]
            i2 += 1
        i3 += 1
    
    # loop/sort remaining items
    while i1 < n1:
        lst3[i3] = lst1[i1]
        i1 += 1
        i3 += 1
    
    while i2 < n2:
        lst3[i3] = lst2[i2]
        i2 += 1
        i3 += 1


for listSize in listSizes:
    loops = numLoops
    print('\nBinary...')
    binTesting(listSize, loops)
    
    # if rd.randrange(0,2) == 0:
    #     print("\n\n" + "-"*50 + "\nHash First")
    #     hashTesting(listSize, loops)
    #     print('\nBinary...')
    #     binTesting(listSize, loops)
        
    # else:
    #     print("\n\n" + "-"*50 + "\nBinary First")
    #     binTesting(listSize, loops)
    #     print('\nHash...')
    #     hashTesting(listSize, loops)
        

print("Done")