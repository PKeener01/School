# Written by Patrick Keener on 9/30/2020
# Video Link: https://youtu.be/agIBBYJeE94
# Honor Statement:  "I have not given or received any unauthorized assistence 
#                    on this assignment"
# note: A transcript of both videos is at the bottom of the code
#
# I went to the zoo the other day, but there was only one animal: a dog.
# it was a shitzu.
#

from math import log10
from math import ceil
from math import floor


def greetUser():
    """ This function greets the user """
    
    print('Welcome to Patrick\'s Stem & Leaf plot tool! \n'\
        'This tool takes a user input to identify a file, \n'\
        'and then creates a Stem & Leaf plot from it.\n\n'
        )
    return None


def userInput():
    """ A function so the user can input their choice of file

    Keyword arguments:
    None

    Returns:
    fileNum - an int that is the The user's input choice
    """

    while True:
        fileNum = input('Please choose the file to read: "1", "2", or "3".')

        # Originally I had this check in its own function to make it easier to
        # add additional checks, but the code was complicated enough already
        # that it made it much more readable to keep it in this function
        #    The other way would have been more extensible, but I felt the 
        # costs outweighed the benefits.


        if fileNum == '': return 10 # check for no response
        elif fileNum[0].lower() in [' ', 'e', 'q']: #check for common quit commands
            return 10

        elif fileNum in ['1', '2', '3']:  # Check that it's a usable response
            return fileNum

        else:
            print('Invalid input,  try again.\n')
    
    return None


def readFiles(fileNum):
    """ A function that reads in a file

    Keyword Inputs:
    fileNum - a string of a number 1, 2, or 3

    Outputs:
    fileData - a list of numbers read from the file
    """
    
    fileData = list() # initialize fileData variable to list
    
    # create filename from user input (function keyword); open file
    fileName = 'StemAndLeaf' + fileNum + '.txt'
    txtFile = open(fileName)

    fileData = txtFile.read().splitlines() # load data & split lines, avoid \n
    
    return fileData


def getleafLen(fileData):
    """ Finds the ideal stem length for the plot

    keyword inputs: 
    fileData - The data to be turned into a dictionary

    return:
    leafLen - the ideal stem length
    """
    
    numSpacing = list()
    intData = list()
     
    # Create a new list that is all integers for math operations below
    for num in fileData:
        intData.append(eval(num))

    intData.sort() # Sort to find the proper 

    for num in range(1, len(intData)):
        # find absolute value of difference between adjacent numbers; minimum 
        # distance is 1 (otherwise logarithms fail).  +1 should not influence
        # the outcome

        difference = abs(intData[num] - intData[num-1]) + 1 
        difference = floor(log10(difference))
        numSpacing.append(difference)
       
    leafLen = max(max(numSpacing), 1)

    return leafLen


def buildStemLeaf(fileData, leafLen):
    """ Creates the dictionary containing the stem and leaf frequencies

    keyword inputs: 
    fileData - the data to be turned into a dictionary

    return:
    stemLeaf - a dictionary containing the stems & leaves of the data
    """

    stemLeaf = dict()
           
    # Determine the stem & leaf, accounting for several special cases
    for num in fileData:
        stem = eval(num[:-leafLen])
        leaf = num[-leafLen:]
        
        # Add each stem & leaf pair to the dictionary
        if stem in stemLeaf:
            stemLeaf[stem].append(leaf)
        else:
            stemLeaf[stem] = [leaf]

    return stemLeaf


def sortDict(myDict):
    """ Sorts lists within dictionary
    
    Keyword Arguments:
    myDict - a dictionary

    Returns:
    myDict - A dictionary with all lists sorted
    sortedKeys - A sorted list of dictionary keys
    """
    
    # get list of keys
    sortedKeys = list(myDict.keys())

    # Sort the lists within the dict
    for key in sortedKeys:
        myDict[key].sort()
    
    # fill holes
    for n in range(min(sortedKeys), max(sortedKeys)):
        if n not in sortedKeys:
            myDict[n] = []
    
    # sort completed list of keys
    sortedKeys = list(myDict.keys())
    sortedKeys.sort()
    
    return myDict, sortedKeys


def groupData(fileData):
    """ groups data together so it can be plotted

    Keyword Inputs:
    fileData - a list of strings of numbers 

    Returns:
    stemLeaf - a dictionary, grouped for display
    sortedKeys - A list of keys in the dictionary, sorted ascending
    """
    # is this too abstracted?  It's only two lines... 

    # build & sort the dictionary
    leafLen = getleafLen(fileData)
    stemLeaf = buildStemLeaf(fileData, leafLen) 
    stemLeaf, sortedKeys = sortDict(stemLeaf) 
    
    return stemLeaf, sortedKeys


def createPlot(stemLeaf, sortedKeys):
    """ organizes data then creates stem & leaf plot

    Keyword Inputs:
    stemLeaf - a dictionary sorted in the manner to be printed

    Outputs:
    Stem and Leaf Plot in a print statement.s

    No returns.
    """
    
    # Determine key display precision; use log 10 to determine number of digits
    precision = ceil(log10(max(sortedKeys)))

    for stem in sortedKeys:
        print('\n{:>{}d} | '.format(stem, precision), end = '') # print stem
        
        if stemLeaf[stem] == []: continue # if no leaf then goto next stem

        for leaf in stemLeaf[stem]: # print leaves
            print(' {}'.format(eval(leaf)), end = '')
    
    print('\n\n')
    return None


def stemAndLeaf():
    """ A function for creating Stem and Leaf plots from files

    Outputs:
    Stem and Leaf Plot in a print statement.

    No returns.
    """
    greetUser() # greets the user.  Hello! :)

    while True:
        
        
        # Take user input, check for errors, then return file
        fileNum = userInput()
        if fileNum == 10: break # exit early when common exit conditions are met

        # load files into memory
        fileData = readFiles(fileNum) 

        # organize the data
        stemLeaf, sortedKeys = groupData(fileData) 

        #  create the plot
        createPlot(stemLeaf, sortedKeys)

        # exit or continue
        cont = input('Do you wish to exit? (y/n)')
        if cont == '': continue
        if cont[0].lower() == 'y': break
    
    print ('Thanks for using the tool.  Have a great day!')
    return None

stemAndLeaf()


# ==== Assignment 3 - Design ====

# My name is Patrick Keener and this is DSC 430- Python Programming, 
# assignment 3 - Stem And Leaf Design.  A transcript of this video can be found
# at the bottom of the code.


# The most important steps in displaying a stem & leaf plot are as follows:

# First, we greet the user.  Is it important?  Well, politeness is always
#  important, so yes.

# Next, we ask the user to input which file to use, then pull from it.

# After this we need to organize the data in some manner that will prepare it
# for display.

# Then finally, we display the plot itself.


# The main function is organized using a spoke & wheel approach.  The function 
# is called stemAndLeaf, which has five child-functions that each perform one of
# the main steps.  One of these steps is the groupData() function, which is the 
# function that organizes and prepares data for display and has three 
# child-functions, therefore program has two levels.

# # === sort dict

# Going into more detail on the deepest level, the getLeafLen(), 
# buildStemLeaf(), and sortDict() functions work together to format the output 
# for printing.  

# I will skip discussion of the getLeafLen() function since we will go over it 
# in detail in the next video.

# The buildStemLeaf() function is where the magic happens.  It accepts the file 
# data and leaf length variables, and creates a dictionary.  At this point, the 
# file data is still a list of strings, which allows the use of slicing to 
# easily break the numbers apart.  Two variables are created: the stem is 
# converted to an integer using the eval function while the leaf variable 
# remains a string; both numberlengths are dictated by the leafLen variable, 
# which indicates where to start or end the slice.  Finally, these two variables 
# are added to the dictionary with the leaf being added as a list.  If the stem 
# already exists then the leaf is appended to the list.

# Next we move to the sortDict() function, which effectively sorts the 
# dictionary.  Dictionaries are unordered so this required a some problem 
# solving to get the display correct.

# The dictionary used in this program contains an integer key which has a list 
# as its pair.  So, a list of the keys is created first, then each key in the 
# dictionary is cycled through and the lists sorted. it is possible to iterate 
# on the keys in the dictionary directly but I chose not to since it's not 
# substantially more efficient computationally and iterating on the list makes 
# the logic slightly easier to follow in the code.

# Next, since we want complete output, I ran through the keys and added any 
# missing numbers.  For example, if I had the keys 18 and 20, I added a stem of 
# 19 with no leaves.  Finally, the list of keys is sorted, that way when I 
# iterate on it later it will be in ascending order- thus quote-"ordering" the 
# dictionary.

# That's it for this video, see you in the next video!


# ==== Assignment 4 - Code & Walkthrough ====

# My name is Patrick Keener and this is DSC 430- Python Programming, 
# Assignment 4 - Stem And Leaf Design Implementation.
# A transcript of this video can be found at the bottom of the code.

# How is the main function organized? The main function is organized using a 
# spoke & wheel-style approach.  The control function first calls a function to 
# greet the user, then enters into a while loop that successively calls the 
# tasks to complete the program: userInput(), where the user selects the file, 
# readFiles(), which returns fileData which is a list containing the contents of
#  the file, groupData(), which organizes the data for plotting, and finally 
# createPlot(), which plots the chart. After the plot is created, it asks the 
# user if they'd like to do it again then takes action accordingly.

# The groupData() function calls three sub-functions, one that determines the 
# leaf length, one that builds the dictionary, and one that sorts the 
# dictionary.  The functions that build and sort the dictionary were covered in 
# the previous video, so we'll dive into the function that determines leaf 
# length now.

# # ======== Code line 80 for getLeafLen()
# the function getLeafLen() finds the ideal length of the leaf by finding the 
# difference between adjacent numbers, then taking the logarithm of the 
# difference and flooring it.  It then takes the maximum of these numbers or 1, 
# which effectively means that the largest-allowed gap is 10 steps, at which 
# point the stem length increases and the gap closes.


# # ======== Code line 190 for createPlot()
# Jumping into the plotting process itself, we can see that it displays by 
# iterating through the dictionary on a list of keys.  Remember from the 
# previous video, these keys were sorted to allow for correct display.  

# First, it prints the stem, then it prints each leaf in the stem.

# There are two features beyond printing in this function.

# # ===== Precision
# The first is precision which determines how many characters should be 
# displayed of the stem.  This is determined by looking at the largest stem, 
# taking it's base 10 logarithm, then looking at the next larger integer.  
# The precision amount is then fed into the print statement for stems, which 
# ensures that each number is properly aligned.

# # ===== empty leaf logic
# The second notable feature is empty leaf handling, which is accomplished using 
# an if/continue pattern to move to the next stem if an empty leaf is found.

# # =============== show output ===================
# Notice that in output two there is a blank stem- this is because there were no 
# numbers here, but we need it present to maintain the overall shape of the 
# data, and this leads us to robustness and confounding data sets.  

# It would be easy to create a file that doesn't display well- all that's 
# required is to have a data set that includes numbers spaced more than a few 
# stems apart, which is easy when working with large numbers or numbers 
# separated by orders of magnitude- for example, having a data set with 1, 100, 
# and 1000 would result in 997 empty rows if using a leaf length of 1.  This 
# code attacks this by scaling the leaf length to the size of the gaps, however 
# a plot could still look quite odd if there were a series of numbers close 
# together and then a single one quite far away, which would cause the numbers 
# to group together and the graph to losei its usefullness.

# And that's stem and leaf!  Thanks for your time.