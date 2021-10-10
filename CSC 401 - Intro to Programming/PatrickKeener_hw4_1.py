# Patrick Keener
# Assignment 4 Problem 1


# Specifications:
#
# Create an index for a text using line # instead of page
#
# Python function: index(fname, letter) 
#    fname: textfile name
#    letter: first letter of the words to create the line # index
# Each word beginning with 'letter', print corresponding line #s
# 
# done * Open and read text file only once
# done * Remove all punctuation except apostrophe
# done * Use p=punctuation.replace("'", " ") to replace apostrophe in p w/ empty 
#        string; use p in maketrans statement
# 
# * Create dictionary of the text in which the key-value pairs are described:
#   * Key: The keys are the individual words found in the file and stored in 
#          the dictionary in uppercase
#   * Values: 
# done      * The values are a list that contains the line number in the file 
#                where the word (key) is found;
# done      * For each word, a line should be listed only once (may use set)
# done      * In output, use commas to separate line #s (split?); can't print
#                 as lists (no brackets)
# done      * Words in output should be in alpha
#
# done * For each word w/ specified letter, find all line #s in which letter appears
# done * Print total # of words that begin w/ specified letter.  
#      * If no words print 'There are no words that begin with "[Letter]"'
# * Outputs formatted as shown in sample
# * Include exception handling


def prepText(fname):
    """Loads file and cleans text.

Keyword arguments:
fname -- The source of the text to be cleaned

Returns:
cleanedText - A string having all punctuation except apostrophe removed

"""
    
    from string import punctuation

    try:
        infile = open(fname, 'r')
        inText = infile.read()
        infile.close()
    except:
        return None


    p = punctuation.replace("'", " ")
    transTable = str.maketrans(p, ' '*len(punctuation))
    cleanedText = inText.translate(transTable)

    return cleanedText



def createIndex(cleanedText, letter):
    """ Creates a dictionary with line indexes for words with a given letter.

Keyword arguments:
cleanedText -- A string to be indexed
letter -- All words starting with this letter will be indexed

Returns:
wordDict -- A dictionary containing a word line-index

"""

    wordDict = dict()
    lineList = cleanedText.split('\n')

    lineNum = 0  # initialize accumulator
    for line in lineList:
        lineNum += 1
        wordList = line.split()

        for word in wordList:
            if word[0].upper() == letter.upper():

                if word.upper() in wordDict:
                    wordDict[word.upper()].add(lineNum)
                else:
                    wordDict.update({word.upper():{lineNum,}})
        
    return wordDict


def printIndex(wordDict, letter):
    """ Prints the location of words in a text that start with a specified \
letter.

Keyword arguments:
wordDict -- A dictionairy containing a key:value pair, where the key is a 
string and the value is a list
letter -- the letter corresponding to the created index

Output:
Prints contents of dictionary

""" 
    
    if len(letter) > 1:
        print('Please submit a single letter.')
        return

    if len(wordDict) == 0:
        print('There are no words that begin with "{}"'.format(letter))
        return
    else:
        # Print Header
        print('{:15} {}'.format('Word', 'Line Nbr.'))
        
        # Accumulate words in string then print at once
        for (word, lines) in sorted(wordDict.items()):
            lineList = list(lines)
            indexList = str(lineList[0])
            line = 0

            for line in range(1, len(lines)):
                indexList += ', {}'.format(lineList[line])

            print('{:15} {}'.format(word, indexList))

    # Print summary
    if len(wordDict) == 1: 
        print('\nThere is 1 word that begins with "{}"'.format(letter))
    else:
        print('\nThere are {} words that begin with "{}"'.format(len(wordDict)\
            , letter))

    return None


def index(fname, letter):
    """This function returns line number indexes for words corresponding to \
a specified letter."""

    # Prepare text for further opetations
    cleanedText = prepText(fname)
    if cleanedText == None: 
        print('File does not exist.  Please enter the correct filename.')
        return
    
    # Create the index/dictionary
    wordDict = createIndex(cleanedText, letter)

    # Print the output
    printIndex(wordDict, letter)
    
    return None

#index('Pride_and_prejudic.txt', 'k')


# Test 1 - test for 'k'
# index('Pride_and_prejudice.txt', 'k')
# Word           Line Nbr.
# KEENER          2159
# KEENEST         2665, 2939, 983
# KEEP            261, 647, 4231, 1417, 3465, 653, 919, 667, 669, 1825, 2977, 2473, 311, 3641, 957, 205, 2893, 2523, 485, 3685, 103, 2027, 3567, 247, 3579
# KEEPING         1553, 3023, 3933, 1463
# KEEPS           2307, 2849, 1491
# KENILWORTH      2591
# KENT            1953, 2753, 923, 2087, 2075, 2059, 2159, 2161, 2225, 2931, 1717, 3447, 2745, 1723
# KEPT            3073, 997, 3525, 4069, 1545, 1865, 2457, 3583, 3595, 1905, 4241, 2517, 3861, 1495, 1849, 2813, 927
# KILL            3323
# KILLED          3569, 2971, 3493, 3051
# KIND            2181, 775, 1033, 3081, 1547, 2445, 1167, 3217, 3859, 2071, 2327, 1305, 2971, 4253, 545, 2977, 3367, 937, 2733, 2989, 2935, 2993, 3889, 4145, 949, 3257, 443, 2107, 4027, 2881, 3397, 2119, 2503, 1865, 1357, 1103, 977, 2129, 1491, 215, 4215, 1753, 2395, 223, 3039, 3199, 3807, 3937, 1637, 1255, 1511, 1767, 2153, 2293, 2677, 2805, 3069, 1663
# KINDER          4225, 2187
# KINDEST         2849
# KINDLED         3575
# KINDLY          1861, 1259, 2159, 2287, 1457, 1687, 927
# KINDNESS        3201, 137, 269, 3985, 2325, 3221, 665, 3613, 2337, 2339, 1705, 3241, 1071, 2353, 1337, 2239, 2243, 1737, 2257, 467, 1491, 469, 601, 1755, 4199, 2035, 117, 2301, 3711
# KINDRED         3957
# KINDS           2393
# KING            1761, 1765, 2377, 2379, 1743, 175, 2263, 221
# NGDOM         1801, 163, 3273, 1287
# KISS            2945
# KISSED          3461, 3735
# KITCHEN         957
# KITTY           3715, 1413, 1541, 135, 2565, 1421, 2573, 3215, 3981, 2577, 2961, 1171, 2579, 3217, 3729, 3983, 4241, 3097, 4121, 3227, 4123, 2845, 2849, 3745, 3107, 4131, 3109, 2983, 3111, 3113, 1325, 1331, 2485, 2359, 3001, 4155, 3777, 2501, 3527, 2507, 3531, 1743, 2391, 2519, 985, 3039, 3679, 2401, 3681, 3685, 103, 3687, 105, 107, 3693, 3695, 1011, 1017
# KITTY'S         2393, 2389
# KNEES           2855
# KNEW            4225, 133, 3461, 2695, 2831, 2449, 3217, 2067, 2707, 3989, 2711, 3613, 3741, 3999, 2981, 3367, 1067, 2219, 1837, 2863, 3763, 4019, 1977, 3001, 2235, 2875, 3065, 3259, 3385, 961, 2241, 3011, 585, 1865, 2895, 3535, 209, 4177, 2771, 2391, 4183, 3929, 2267, 3547, 1129, 3049, 4077, 2927, 3567, 371, 4213, 1143, 1017, 123, 767
# KNIGHTHOOD      1753, 221
# KNOW            2561, 4103, 4105, 1035, 3597, 4109, 4125, 31, 2079, 2593, 1059, 37, 2091, 2093, 4141, 2095, 4143, 49, 4145, 3123, 565, 1597, 65, 2115, 1605, 2117, 2631, 3143, 77, 3149, 2639, 3661, 4087, 1111, 1115, 93, 609, 1121, 2145, 2659, 1125, 1127, 1639, 4201, 2669, 3693, 111, 3183, 625, 117, 121, 1153, 2177, 1667, 3201, 645, 3713, 137, 3215, 2199, 3223, 2713, 161, 2721, 1699, 2725, 1703, 1195, 2731, 3243, 175, 2229, 1723, 3261, 705, 2241, 2245, 199, 2247, 1737, 203, 2775, 217, 733, 3299, 1765, 231, 1255, 1767, 2791, 235, 2285, 1263, 2799, 753, 1265, 1267, 3825, 1781, 3833, 1791, 2303, 3331, 3333, 775, 3337, 3849, 3851, 275, 789, 2325, 2837, 3349, 795, 2845, 287, 289, 2849, 3363, 293, 3367, 1833, 299, 2861, 2355, 309, 3381, 2871, 3895, 3903, 833, 1345, 2881, 3397, 1351, 1353, 3913, 843, 3409, 2391, 1369, 1371, 3419, 3933, 2915, 2919, 3943, 2923, 3947, 2925, 2927, 2929, 2425, 2427, 385, 899, 2435, 2437, 3459, 1417, 3471, 3475, 2971, 2975, 2465, 2977, 3491, 4001, 3493, 4007, 3497, 3499, 1453, 1455, 1967, 2995, 1975, 953, 3515, 445, 957, 1469, 1981, 1983, 3007, 3517, 3519, 1477, 3529, 3023, 2001, 4049, 3033, 987, 3035, 2013, 2015, 3045, 1001, 3561, 3565, 4081, 1011, 1523, 3059, 4085, 3575, 1531
# KNOWING         2311, 3861, 2457, 1181, 3997, 2847, 3247, 2997, 567, 953, 3001, 1857, 1985, 579, 2629, 3013, 1229, 2253, 2255, 3661, 2129, 3281, 2781, 1783, 2555, 2557
# KNOWLEDGE       385, 2435, 1925, 2067, 2461, 4259, 1839, 1841, 2233, 313, 3257, 2239, 3263, 575, 1983, 2243, 89, 4075, 2931, 1535
# KNOWN           129, 2817, 3073, 3971, 2823, 3207, 2697, 3083, 1935, 3985, 4241, 1683, 21, 281, 1049, 287, 2591, 1441, 2849, 1443, 2213, 3365, 2729, 3373, 2095, 2863, 3001, 2235, 2875, 2125, 2511, 3535, 2257, 1491, 2259, 2519, 1753, 1627, 2523, 2527, 2273, 2529, 2787, 1125, 2789, 1639, 2663, 2791, 4069, 1899, 4077, 3825, 1017
# KNOWS           1155, 3491, 2663, 1737, 2923, 3023, 2195, 3513, 2719
# KYMPTON         3439
# There are 34 words that begin with "k"

# Test 2 - Not a single letter
# index('Pride_and_prejudice.txt', 'ke')
# Please submit a single letter.
# >>> 

# Test 3 - 'no words' functionality
# index('testing.txt', 'h')
# Word           Line Nbr.
# HE              2
# HELLO           1
# There are 2 words that begin with "h"
# >>> 
# index('testing.txt', 'z')
# There are no words that begin with "z"

# Test 4 - proper plurality
# >>> index('testing.txt', 's')
# Word           Line Nbr.
# SAID            2
# There is 1 word that begin with "s"
# >>> 

# Test 5 - file does not exist/is empty
# >>> index('Pride_and_prejudic.txt', 'k')
# File does not exist or has no contents.
# >>> 
