# ================  Goldbach Conjecture  ===================
# Written by Patrick Keener on 10/04/2020
# Video Link: https://youtu.be/S6fsV5VvcI8
# Honor Statement:  "I have not given or received any unauthorized assistence 
#                    on this assignment"

# Specifications: 
# Test Goldbach's conjecture on all integers < 100
# For each ineger, print a single line showing the two primes summing to the num
# ex. 4 = 2 + 2
#
# Goldbach's Conjecture: Every even integer > 2 can be expressed as the sum of 
#                        two primes




# ================ Print Step ============================

def printVerification(num, prime1, prime2):
    """ This function displays the verification of the Goldbach Conjecture"""
    print('{:>5} = {:>5} + {:>5}'.format(num, prime1, prime2))
    return None


def genPrimes(maxTest):
    """ This function generates the list of primes Less than or equal to maxNum

    Keyword Inputs:
    maxTest - The maximum number that should be tested for

    Returns:
    primeList - a list containing the prime numbers
    """
    
    # initialize default variables
    primeList = []
    isPrime = True
    #print('Beginning Prime Generation...')

    # Loop through each odd number >2 to determine if it's prime
    for testNum in range(3, maxTest - 1, 2):

        # Divide each number by all known primes smaller than it
        for prime in primeList:
            if testNum % prime == 0: # if mod 0 then it's composite
                isPrime = False
                break

        if isPrime == True: 
            primeList.append(testNum)
        
        isPrime = True # reset counter to default state
    
    primeList.insert(0, 2) # adding 2 since it's prime

    #print('Prime Generation Complete\n')
    return primeList


def goldbachTest(primeSubset, testNum):
    """ executes goldbach test """

    # initial variables
    verified = False
    prime1 = int()

    for prime in primeSubset:
        if testNum - prime in primeSubset:
            prime1 = prime
            return prime1, True

    return prime1, verified


def noPrimes():
    """ Calls attention to failed test """

    noPrimes = '  Uh oh... No matching primes  '
    print('\n {} \n'.format(noPrimes.center(80, '=')))
    prime1 = prime2 = '*** No Matching Prime ***'

    return prime1, prime2


def goldBachAlgo(primeList, testNum):
    """ This function executes the algorithm to test the goldbach conjecture

    Keyword Inputs:
    primeList - a Tuple containing a list of possible primes 
    num - an integer to which the conjecture will be tested against

    Returns:
    prime1, prime2 - the two primes that satisfy Goldbach's Conjecture
    """

    prime1 = prime2 = 0  # Initiate variables

    # subset primeList
    # x < testNum -1 because 1 and 0 are not prime
    primeSubset = set(x for x in primeList if x < testNum - 1)
    
    # Note that sets are unordered; order in this case is irrelevant
    # This check will allow use to directly check the presence and save
    # large amounts of times if lists are large

    prime1, verified = goldbachTest(primeSubset, testNum)

    if verified == True:
        prime2 = testNum - prime1 # We can derive prime2 to minimize variables
        return prime1, prime2
    else:
        prime1, prime2 = noPrimes() # notify if no primes found
        return prime1, prime2

    return None


def goldBach(maxTest):
    """ This function verifies the Goldbach conjecture up to a given number

    Keyword Inputs:
    maxTest - The maximum number that should be tested for

    Returns:
    None

    Output:
    Printed verification of results for each number, 4 to maxTest
    """

    # Generate a list of primes
    primeList = genPrimes(maxTest)

    # Loop through each number, 4 to maxTest, to prove conjecture conformity
    for testNum in range(4, maxTest + 1, 2):
        prime1, prime2 = goldBachAlgo(primeList, testNum)
        printVerification(testNum, prime1, prime2)

    return None

goldBach(100)




# Video Script

# My name is Patrick Keener and this is DSC 430- Python Programming
# , Assignment 5 - the Goldbach Conjecture.  A transcript of this video can be 
# found at the bottom of the code.

# The program input is the maxTest variable, which is the largest number to be 
# tested.  We will use 100 for this.

# As we can see, primes were found for each number.  In the event that a prime 
# isn't found a note will be printed before it continues with the rest of the 
# test.

# The main function begins by calling the genPrimes function where it generates 
# a list of all primes less than the number being tested.  It's only executed 
# once, then passed to the Goldbach algorithm for use.  It does this by 
# iterating through each odd number up to maxTest - 1 and testing it for 
# primality. 

# I used maxTest - 1 for the number of iterations because 0 and 1 are not prime, 
# and therefore cannot be part of the solution to the Goldbach test.

# A prime number is defined as a number only divisble by 1 and itself.  
# When testing for primes, we don't have to test to see if the subject number 
# is divisble by each number smaller than it.  Any smaller composite number 
# would also be divisble by some prime, and through the commutative property we 
# can assert that we only need to test divisibility by smaller primes.  Since 
# all primes >2 are odd, we iterate only on odd numbers, and we don't have to 
# test 2, therefore in the last step of the function, 2 is inserted at the 
# beginning of the list.

# I researched methods of finding the next prime but most were either 
# probabilistic or poorly supported, both of which were insufficient for our 
# purposes. 

# # main loop
# The main loop simply iterates on even numbers from 4 up to the maxTest number 
# and executes the Goldbach algorithm and the printing function during each 
# iteration.

# # Goldbach algo
# The Goldbach Algorithm begins by subsetting the list of primes to be no larger 
# than the number being tested, which is accomplished through the set 
# comprehension on line 100.  I chose to use a set because it scales better with 
# larger values.  For comparison, testing the first 100,000 numbers takes 
# approximately 43 seconds with a set, 55 seconds with a list, and 55 seconds 
# with a tuple.  With smaller values, it is slightly less performant, but the 
# difference is in milliseconds and not noticeable.

# # goldbachTest
# The test itself is conducted in a child function that loops through each prime 
# in the subset.  To take advantage of the hash table, it it starts with the 
# number being tested then subtracts a prime drawn from the set.  If the number 
# tested meets the conjecture, the remainder will be found in the set.  If not, 
# it will try another number until every number in the set has been tested.  

# Assuming the conjecture is verified it returns to the top most statement via a 
# series of return statements and prints the results before moving to the next loop.

# Thanks for your time, see you in the next assignment!