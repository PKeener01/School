# Patrick Keener
#
# =======================================================
# ====================== Problem 1 ======================
# =======================================================
#
# Takes multidimensional list of any size as parameter and RETURNS sum of 
# each column as a one-dimensional list
# The number  of sublists and length of each sublist must be the same, 
# ex. 4 rows and 4 columns
# hint: use indexes and ranges
# 
# input:
# sumColumns([[14, 82, 73], [46, 26, 7], [26, 95, 21]])
#
# Output:
# [86, 203, 101]


def sumColumns(lst):
    # Find dimensions of square matrix
    numCols = len(lst)
    numRows = len(lst[0])  #This only works because numRows is consistent 
    
    # Initialize variables
    outList = []

    # Loop through each row & column, summing across the rows
    for row in range(numRows):
        addNum = 0
        for col in range(numCols): 
            addNum += lst[col][row]

        # Append sum to list after looping through every column in a single row
        outList.append(addNum)
        
    return outList


# sumColumns([[14, 82, 73], [46, 26, 7], [26, 95, 21]])


# Test Cases
#
#
# >>> sumColumns([[14, 82, 73], [46, 26, 7], [26, 95, 21]])
# [86, 203, 101]
#
#
# >>> sumColumns([[14, 82, 73, 65], [22, 46, 26, 7], [35, 26, 95, 21], [15, 18,25,36]])
# [86, 172, 219, 129]
#


# =======================================================
# ====================== Problem 2 ======================
# =======================================================

# Write a function, numLetters(), that keeps prompting user for words until 
# they hit return/enter key
# * function returns (not print) % of 3-letter words entered
# * # of 3-letter words / total words


def numLetters():
    # Initialize variables
    threeLetWds = 0
    totWords = 0
    inWord = 0

    # As long as the user input is not blank, continue looping
    while True:
        inWord = input('Please enter a word.'\
            + ' Hit enter without a word to end the game. ')
        # Exit conditions
        if inWord == '': 
            if totWords > 0:
                return threeLetWds/totWords * 100 
            else:
                return None

        # Accumulate total number of words
        totWords += 1

        # Accumulate total number of 3-letter words
        if len(inWord) == 3:
            threeLetWds += 1


pct = numLetters()

print(pct)



# Test Cases
#
# test 1 - Test functionality with no word (expect return "none")
# >>> numLetters()
# Please enter a word. Hit enter without a word to end the game. 
# >>> 
#
# test 2 - Test functionality with a few words
# Please enter a word. Hit enter without a word to end the game. pk
# Please enter a word. Hit enter without a word to end the game. pmk
# Please enter a word. Hit enter without a word to end the game. plmasdf
# Please enter a word. Hit enter without a word to end the game. 
# 0.3333333333333333




# =======================================================
# ====================== Problem 3 ======================
# =======================================================

#  Write function, getNumbers(n), that accepts positive integers and creates
# a sequence of numbers as follows:
#
# * done - if n is even, n is replaced with .floor(n**.5)
# * done - if n is odd, n is replaced with .floor(n**1.5) 
# * done - continues calculating until after n = 1
# * done - collects values in list and returns (not print)


import math

def getNumbers(n):
    outList = []
    newN = n

    # Loop as long as the number is greater than 1
    while newN != 1:
        # Append number at start to allow for capture of the 1st number 
        outList.append(newN)
        
        # The modulus of n/2 is used to identify even (0) from on (!= 0)
        if newN%2 == 0:
            newN = math.floor(newN**.5)
        else:
            newN = math.floor(newN**1.5)

    # Append number at the end since it will bypass the initial append
    outList.append(newN)

    return outList


# Testing
#
# >>> getNumbers(1)
# [1]
# >>> getNumbers(2)
# [2, 1]
# >>> getNumbers(3)
# [3, 5, 11, 36, 6, 2, 1]
# >>> getNumbers(5)
# [5, 11, 36, 6, 2, 1]
# >>> getNumbers(25)
# [25, 125, 1397, 52214, 228, 15, 58, 7, 18, 4, 2, 1]
# >>> getNumbers(10)
# [10, 3, 5, 11, 36, 6, 2, 1]
# >>> getNumbers(36)
# [36, 6, 2, 1]
# >>> getNumbers(37)
# [37, 225, 3375, 196069, 86818724, 9317, 899319, 852846071, 24906114455136
#     , 4990602, 2233, 105519, 34276462, 5854, 76, 8, 2, 1]



# =======================================================
# ====================== Problem 4 ======================
# =======================================================

# * done - create dictionary entry for each member
# * done - keep prompting for first & last name until user hits enter (blank submit)
# * done - Allow user to enter 4-digit member ID 
# * done - Dictionary key is a tuple consisting of first & last name; data = ID
# * done - If no ID, sask for it then store in dictionary.  If has ID, display ID and ask
#          whether a new ID should be assigned (then ask to enter)
# * done - After loop exits, print report listing all members by last name, first name, &
#          member ID
# * Note: no validation for member IDs (always 4 digits)



def member():

    # Initialize Variables
    memberDict = dict()
    update = str()


    # While loop
    while True:
        firstName = input('Enter the member\'s first name: ')
        # Exit condition
        if firstName == '':    break

        sirName = input('Enter the member\'s surnmae: ')

        nameKey = (sirName, firstName)

        # If key exists, ask to update, if not, ask for new member ID
        if nameKey in memberDict.keys():
            update = input('The Member ID is {}.  Update Member ID (Y/N)? '\
                .format(memberDict[nameKey]))
            if update.upper() == 'Y':
                newID = input('What is the new 4-digit Member ID? ')
                memberDict.update({nameKey:newID})
            else:
                print('The ID will not be updated.')
        else:
            newID = input('Please enter a 4-digit Member ID for the new'\
                          + ' account: ')
            memberDict.update({nameKey:newID})

    # Print the output
    for key in memberDict.keys():
        print('{}, {} has id {}'.format(key[0],key[1],memberDict[key]))

    return None

member()


# ** Testing
#
# Test 1: Adding entries and exit conditions works as intended
#
# Enter the member's first name: patrick
# Enter the member's surnmae: keener
# Please enter a 4-digit Member ID for the new account: 1234
# Enter the member's first name: alex
# Enter the member's surnmae: kulka
# Please enter a 4-digit Member ID for the new account: 2789
# Enter the member's first name: kristin
# Enter the member's surnmae: kosic
# Please enter a 4-digit Member ID for the new account: 5823
# Enter the member's first name: Paulina Kulka
# Enter the member's surnmae: 3847  **ID 10 T error in entry
# Please enter a 4-digit Member ID for the new account: 
# Enter the member's first name: 
# Enter the member's surnmae: 
# keener, patrick has id 1234
# kulka, alex has id 2789
# kosic, kristin has id 5823
# 3847, Paulina Kulka has id   **ID 10 T error in entry; behaves as expected
# >>> 
#
#
# Test 2: Adding identical entries but selecting 'no' works as intended
#
# Enter the member's first name: p
# Enter the member's surnmae: k
# Please enter a 4-digit Member ID for the new account: 1234
# Enter the member's first name: p
# Enter the member's surnmae: k
# The Member ID is 1234.  Update Member ID (Y/N)? n
# The ID will not be updated.
# Enter the member's first name: pk
# Enter the member's surnmae: keener
# Please enter a 4-digit Member ID for the new account: 1234
# Enter the member's first name: 
# Enter the member's surnmae: 
# k, p has id 1234
# keener, pk has id 1234
# >>> 
# 
# 
# Test 3: Replacement of identical key/ID combos works as intended
#
# Enter the member's first name: patrick
# Enter the member's surnmae: keener
# Please enter a 4-digit Member ID for the new account: 1234
# Enter the member's first name: alex
# Enter the member's surnmae: kulka
# Please enter a 4-digit Member ID for the new account: 5789
# Enter the member's first name: patrick
# Enter the member's surnmae: keener
# The Member ID is 1234.  Update Member ID (Y/N)? y
# What is the new 4-digit Member ID? 5678
# Enter the member's first name: 
# Enter the member's surnmae: 
# keener, patrick has id 5678
# kulka, alex has id 5789
# >>> 
