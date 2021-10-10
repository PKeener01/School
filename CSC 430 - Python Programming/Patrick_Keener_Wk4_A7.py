# ================== GoldBach Deuce ===================
#
# Written by Patrick Keener on 10/10/2020
# Video Link: https://youtu.be/v-OKd5o6_S8
# Honor Statement:  "I have not given or received any unauthorized assistence 
#                    on this assignment"
# 
# Checks:
# 1. [x] Docstrings for all functions
# 2. [x] All requirements met
# 3. [x] Fully tested
#
#  Requirements:
#  1. [x] Ask user for length and sum 
#  2. [x] Create list of [length] random numbers between 0 and 100
#  3. [x] Determine if two of the numbers sum to [sum] in O(n.log(n)) time
#  4. [x] Output appropriate results

import random as rd

def printVerification(sumNum, num1, num2):
    """ This function displays the verification of for the requested number"""

    if -1 in (num1, num2):  # Will be set to false if no good numbers
        print("No number pairs in the list sum to {}.".format(sumNum))
    else:
        print('{:>5} = {:>5} + {:>5}'.format(sumNum, num1, num2))
        
    return None


def userInput(qString):
    """ Utility function to get user input and check for common errors"""

    while True:
        userResponse = input(qString)
    
        try:
            userResponse = eval(userResponse)
        except:
            print('Please enter a number')
            continue
        
        if userResponse == userResponse//1: # Check if integer
            return userResponse
        print('\nThe number must be an integer. Please try again.')
    
    return userResponse


def getUserInputs():
    """ Gets user inputs for the main functions
    
    Keyword arguments:
    None

    Returns:
    listLen - the length of the list to be generated
    number - the number that is to be summed to
    """

    print("Welcome to Goldbach Deuce.  This program takes a number and a list "\
    "length, then generates a list that has the number of items specified by "\
    "the list length and determines if any numbers sum to the number provided."\
    "Please enter only integers when prompted.\n")
    
    while True:
        sumNum = userInput("What number should be summed to? "\
        "This must be between 0 and 198 (inclusive).")
        if 0 <= sumNum <= 198:
            break
        else:
            print('Please enter a number between 0 and 198.\n ')
        
    listLen = userInput("How many numbers should be in the list")

    return listLen, sumNum


def binarySearch(numList, searchNum):
    """ 
    Conducts a binary search to determine whether the number is in the list

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
            high = mid -1 # search lower half
        else:
            low = mid + 1  # search upper half; also loop to exit if not found
    
    return -1 # return False if it's not in list


def mergeSort(numList):
    """ Merge Sort sorts a list in ascensing order in-place.
    
    Keyword arguments: 
    numList - a list of numbers to be sorted

    Returns:
    None - Sorts in-place
    """
    # Shamelessly stolen from Professor Gemmel's lecture; minor changes
    # to make it fit in with my code (variable names), iterate using +=, 
    # comments made in my style, and added return None to the end to make it
    # easier to tell when the function ends.

    n = len(numList)

    if n >1:
        # Break list into halves (divide & conquer)
        m = n //2
        numList1, numList2 = numList[:m], numList[m:]

        # Recursively call the mergeSort function
        mergeSort(numList1)
        mergeSort(numList2)

        # Merge the lists back together
        merge(numList1, numList2, numList)
    
    return None
            

def merge(lst1, lst2, lst3):
    """ Used in mergeSort, merges list back together"""
    # Shamelessly stolen from Professor Gemmel's lecture; minor changes
    # to make it fit in with my code (variable names), iterate using +=, 
    # comments made in my style, and added return None to the end to make it
    # easier to tell when the function ends.

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

    return None


def numberCheck(numList, sumNum):
    """" Checks to determine whether numbers add to the target number """
    num1 = num2 = int()

    mergeSort(numList)

    # Loop throuhg each number in list to find if it has a pair that adds to
    # the sum number.
    for n in numList:
        # Find number to test for
        testNum = sumNum - n
        
        # Check if num is in list using binary search
        numIndex = binarySearch(numList,testNum)

        if numIndex != -1:
            return n, numList[numIndex]

    return num1, num2


def goldBachDeuce():
    """ This function determines whether two numbers within a list sum to a third

    Keyword Inputs:
    maxTest - The maximum number that should be tested for

    Returns:
    None

    Output:
    Printed verification of results for each number, 4 to maxTest
    """

    # Ask for length and sum
    listLen, sumNum = getUserInputs()

    # Generate a list of random numbers between 0 and 100
    numList = [rd.randrange(0,100) for n in range(listLen)]

    # Determine if 2 of the numbers sum to [number] in O(n log(n)) time
    num1, num2 = numberCheck(numList, sumNum)

    # Print outcome
    printVerification(sumNum, num1, num2)
    
    return None



goldBachDeuce()