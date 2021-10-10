# Patrick Keener
# Problem 3

# read/write file, accumulator (for loop), UDF

# Determine following statistics for the input file, fname, and write results to the text 
# file, FileStats.txt


def getStats(fname):
    """ 
    getStats(<fname>); where fname is a filepath

    This function calculates summary statistics about the input text file
    then outputs them to a the FileStats.txt file.
    
    Statistics include:
      * Frequency of Day of Week mentions
      * Count of number of lines
      * Count of number of words
      * Count of number of characters (excluding spaces between words)
    """

    # Load book into memory
    inFile = open(fname,'r')
    book = inFile.read()
    inFile.close()

    # Establish output file
    outFile = open('FileStats.txt', 'w')
    outFile.write('Statistics for {} created by P. Keener'.format(fname))

    # Initialize variables
    dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'
        ,'Saturday', 'Sunday']
    noun = 'times'
    charCount = 0
    

    # Cycle through days of week, counting occurances of each day then
    #     printing them to the file
    for day in dayList:
    	dayCount = book.count(day)
    	if dayCount == 1: noun = 'time'  # Make noun singular if needed

    	outFile.write('\n{} occurs {} {}'.format(day, dayCount, noun))


    # Accumulation loop to count words & characters (excluding spaces)
    wordList = book.split()
    for word in wordList:
        charCount += len(word)

    wordCount = len(wordList)
    lineCount = book.count('\n')

    # Write final three outputs & close file
    outFile.write("""
There are {:,} lines
There are {:,} words
There are {:,} characters (excludes spaces between words)
""".format(lineCount, wordCount, charCount))
    outFile.close()

    # Print instructions for retrieval and thank user
    print("""
To view the results go to FileStats.txt

'Thanks for using the getStats() function'
""")
    return None



getStats('Pride_and_Prejudice.txt')


# Outputs Testing
#
#
# In Shell:
#
# To view the results go to FileStats.txt
#
# 'Thanks for using the getStats() function'
#
#
# In File:
#
# Statistics for Pride_and_Prejudice.txt created by P. Keener
# Monday occurs 9 times
# Tuesday occurs 12 times
# Wednesday occurs 9 times
# Thursday occurs 4 times
# Friday occurs 1 time
# Saturday occurs 17 time
# Sunday occurs 9 time
# There are 4,270 lines
# There are 121,565 words
# There are 559,985 characters (excludes spaces between words)
