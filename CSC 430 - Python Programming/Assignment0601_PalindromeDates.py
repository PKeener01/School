# Written by Patrick Keener on 10/27/2020
# Video Link: https://youtu.be/N-OSt009k08
# Honor Statement:  "I have not given or received any unauthorized assistence 
#                    on this assignment"
#
# DSC 430: Python Programming
# Assignment 0601: Palindrome Dates
#
# Requirements:
# Write a program that identifies and saves to a file all the palindrome dates
# in the 21st century using DD/MM/YYYY format.  No recursion.  No built-in calendar-ish packages.
# treat leap years as regular years.
#
# [x] identify palindrome dates
# [x] save all palindrome dates in file
# [x] examine all dates in 21st century
# [x] format DD/MM/YYYY
# [x] No recursion
# [x] No calendar/ish programs
# [x] leap years are regular years
#
# [x] 28 dates



def palindromeDates():
    """
    The purpose of this program is to test each date in the 21st century to
    determine whether it is a palindrome date.  
    """
    fName = 'palindrome.txt'

    palStr = []
    palStr = genPalindromeList() # Generate list of palindromes

    print('There were {} palindromes found'.format(len(palStr)))

    saveToFile(palStr, fName) # Save list to file

    return None


def saveToFile(palStr, fName):
    """
    Saves palindrome to file by writing each date on its own line as a string,
    separated by a comma.
    """
    
    palFile = open(fName, 'w')
    
    numPals = len(palStr) 

    for pal in range(numPals - 1): # index 0 to the second to last date
        palFile.write(palStr[pal] + ',\n') # write palindromes on own comma-sep line
    
    palFile.write(palStr[-1]) # Write the final palindrome
    palFile.close()

    return None


def genPalindromeList():
    """
    Create a list of palindromes
    Returns a list of strings, each string containing a date

    Note 1: in the 21st century (2000 to 2099) only February may have palindromes
    because xx0220xx must be a palindrome.  

    Note 2: Since feb only has 28 days, the highest potential palindrome is 2091 
    (19th day), so we only need to look through 2091.
    """

    palStr = []

    # Run through each day in the century and check if it is a palindrome
    # if it is, append to list
    for year in range(2000,2092): # only 28 days in feb, so don't need to go beyond 2091
            for day in range(1, 29):  # 28 days in feb + 1 extra to loop
               date = '{:02d}02{:04d}'.format(day,year) 
               if date == date[::-1]: # Check if string is same reversed
                   palStr.append('{:02d}/02/{:04d}'.format(day, year))
    
    return palStr

palindromeDates()



# def test():
#     x = isPalindrome(date)
#     y = isPalindrome(date2)

#     print('Output should be True: {}\nOutput should be False: {}'.format(x,y))

#     return None

# test()