# Patrick Keener
# Problem 1
#
# This program generates a list of 100 random numbers, then selects
# n of these numbers, defined in the calling statement, and displays
# them in 3 columns with 5 spaces between them.
#
#  * Utilizes range function to iterate by 3
#  * Utilizes end="" statemetn to print multiple statements per line

import random

def dollarOutput(n):
    lst = []
    # lst is a list that containa 100 float numbers
    for i in range(100):
        lst.append(random.uniform(0,100))

    # Select numbers to add
    numList = lst[:n]

    	# iterate from 0 to n in increments of 3 (3 columns)
    	#     x will be offset by 0, 1, or 2 in order to get 3 index numbers
    	#     If the index would not exist, don't output anything
    	#     Only print once per column (3 numbers)

    for x in range(0, n, 3):
        print('${:5.2f}     '.format(numList[x]), end="")

        if x+1 <= n-1:
            print('${:5.2f}     '.format(numList[x+1]), end="")

        if x+2 <= n-1:
            print('${:5.2f}'.format(numList[x+2]))
    
    return None
            

dollarOutput(100)



# Test cases
#
# >>> dollarOutput(1)
# $92.54     
#
# >>> dollarOutput(3)
# $51.28     $99.76     $33.04
#
# >>> dollarOutput(15)
# $89.32     $31.69     $55.67
# $27.52     $76.43     $17.61
# $95.06     $ 4.25     $ 8.12
# $ 7.18     $68.97     $33.60
# $72.63     $30.33     $82.53
# >>> 