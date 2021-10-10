# Written by Patrick Keener on 9/20/2020
# Video Link: https://www.youtube.com/watch?v=0C3KRv5gI0E&ab_channel=Patrick
# Honor Statement:  "I have not given or received any unauthorized assistence 
#                    on this assignment"
#
# Coprime, from wikipedia:  
# 1. integer
# 2. GCD = 1
#
# Sources:
# Basic info coPrimes: https://en.wikipedia.org/wiki/Coprime_integers
# Basic info on GCD: https://en.wikipedia.org/wiki/Greatest_common_divisor
# Euclidean Algorithm: https://en.wikipedia.org/wiki/Euclidean_algorithm




class primeTest(float):
    """ Contains various functions used to determine if a number is prime

    Keyword arguments:
    The number to be assigned

    Methods:
    isInt - Evaluates whether the number can be expressed as an integer.
    isEven - Evaluates whether the number is even.
    """

    def isInt(self):
        """ Evaluates whether the number can be expressed as an integer.

        Returns:
        Boolean - True if the number can be expressed as an integer, false if not.
        """
        return self == self // 1

    def isEven(self):
        """ Evaluates whether the number is even.

        Returns:
        Boolean - True if the number can be expressed as an integer, false if not.
        """
        return self % 2 == 0


def Euclid(large, small):
    """  Evaluates coprimality using Euclid's algorithm.

    Keyword arguments:
    num1 - the first number to be compared
    num2 - the second number to be compared

    Returns:
    Boolean - if True, the numbers are coprime, if False, the numbers are not
    
    Description:
    This function uses Euclid's algorithm to find the GCD of two numbers.  If 
    two numbers are coPrime their GCD will be equal to 1.

    This algorithm divides the larger number by the smaller number.  If the 
    remainder is 1 then the numbers are coPrime, if the remainder is 0 then a 
    common factor greater than 1 exists and thus they are not coPrime.

    This algorithm never requires more than 5 + log(n) iterations, where n is 
    the smaller of the two numbers. This was proven by Gabriel Lame' 
    in 1844 (Wikipedia).
    """
    
    print("\nEuclid's Algorithm results in a final remainder of 1 if the numbers\
are coprime and 0 if they have a common divisor other than 1. \n")

    n = 0
    while True:
        n += 1
        print("Loops: ", n)

        if large < small:  
            large, small = small, large
        print('Dividing {} by {}'.format(int(large), int(small)))
            
        large = large % small
        print('Remainder: {}\n_____'.format(int(large)))

        if large == 1:
            return True
    
        if large == 0:
            return False
            
    return None


def coprime(num1, num2):
    """ Determines whether the two numbers are coPrime.
    
    Keyword arguments:
    num1 - the first number to be compared
    num2 - the second number to be compared

    Returns:
    Boolean - if True, the numbers are coprime, if False, the numbers are not

    """
    
    # initialize the indicator to false
    primeStatus = False 
    
    # set each variable to the primeTest class
    num1 = primeTest(num1)
    num2 = primeTest(num2)

    # coPrimes are positive
    if num1 < 0 or num2 < 0:  
        primeStatus = 2
        return primeStatus
    
    # 1 is coPrime to everything
    if num1 == 1 or num2 == 1:
        primeStatus = True
        return primeStatus
    
    # coPrimes must be integers
    if num1.isInt() != True or num2.isInt() != True: 
        primeStatus = 3
        return primeStatus

    # Test if both numbers are even (Euclid can take a while to get there)
    if num1.isEven() == True and num2.isEven() == True:
        return
    
    # Implement Euclid's algorithm
    primeStatus = Euclid(num1, num2)
    
    return primeStatus


def coprime_test_loop():
    """ This function allows the user to input two numbers, then determines 
    whether they are coprime.

    Keyword arguments:
    none

    Returns:
    None

    Prints:
    The outcome of the test or feedback if the user has entered disallowed 
    characters.

    """

    print('Welcome to the coprime calculator.  A coprime is any pair of positive\
 integers whose GCF = 1.\n')

    exitCond = False # initialize exit cond
    while exitCond == False:
        print('This function determines whether two numbers are coprime.')
        
        # Eval() throws an error if it can't evaluate to numeric, which
        # is used to identify exit conditions

        try:
            num1 = eval(input('Enter the first number to compare: '))
            num2 = eval(input('Enter the second number to compare: '))
        except:
            print('Input error, please try again: \n')
            continue
        
        primeStatus = coprime(num1, num2)

        # Cultiple output conditions to allow for user feedback
        if primeStatus == True: 
            primeStatus = 'are coprime.'
        elif primeStatus == 2:
            primeStatus = 'must be positive. Please enter only positive numbers.'
        elif primeStatus == 3:
            primeStatus = 'must be integers.  Please enter only an integers.'
        else:
            primeStatus = 'are not coprime.'
        print('The numbers {} and {} {}\n'.format(num1, num2, primeStatus))

        # Check whether user wants to do another
        cont = input('Would you like to test another pair of numbers (y/n)?\n')

        if len(cont) == 0: continue
        elif cont[0].lower() == 'n': 
            print('Thanks for using the program! \nWritten by Patrick Keener')
            break

        elif cont.lower() == 'joke':
            print('_____\n')
            print("Why can't you hear a pterodactyl use the restroom?\n")
            print("Because the 'P' is silent.")
        
        print('\n_____\n\n')
    
    return None

coprime_test_loop()









# Video Script:

# My name is Patrick Keener and this is DSC 430- Python Programming, Assignment 
# 2- CoPrimes.

# Let's start by running the program.  Here is our welcome screen as well as our 
# input screen.  I have pre-selected two 16-digit numbers to demonstrate the 
# efficiency of the approach.

# 2820777163870549
# 6576674667879490

# The program prints each step taken in Euclid's algorithm in the kernel, and 
# ultimately returns the solution. This brings us to the first question:

# How efficient is coprime(a,b)?
# The algorithm is based on Euclid's Algorithm which completes in log(n) 
# iterations, where n is the smaller of the two numbers.  The only additions to 
# the algorithm I made were to perform some pre-checks.  

# First, I check whether any of the numbers are 1, since 1 is coprime to 
# everything, and second I check to see if both numbers are even, since that 
# will rule in half of all numbers and Euclid's Algorithm does not prioritize 
# this.  

# In terms of other efficiencies, I added error checking to the code as early as 
# feasible, as well as ordering all tests by complexity: First boolean then 
# multiplication and finally Euclid's test itself, which leads us to assumptions.

# The biggest assumption I've made is that coprimes are positive integers - I 
# couldn't find anywhere that explicitly said they must be positive, however the 
# code increases in complexity substantially when factoring negative numbers is 
# involved.

# Additionally, I made the assumption that all errors thrown in the input section 
# are caused by nonnumerics getting caught in the error checker due to the eval() 
# function.  
# #############  (went off script a bit here :) )

# This behavior is intentional, and I can't think of a non-numeric character 
# that we would want to pass or give a different error for.  It also assumes 
# that if an equation is entered, the final output is what was meant to be 
# evaluated.

# Finally, the error checking provides feedback if non-integer or negative 
# numbers are input.

# That's it for Assignment 2, see you next week.


