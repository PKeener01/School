# ================== Dice and Cups  ===================
#
# Written by Patrick Keener on 10/18/2020
# Video Link: https://youtu.be/WXMKdstx8TQ
# Honor Statement:  "I have not given or received any unauthorized assistence 
#                    on this assignment"
# 
# Checks:
# 1. [x] Docstrings for all functions
# 2. [x] All requirements met
# 3. [x] Fully tested
#
# Requirements
# 1. [x] Write class SixSidedDie
# 2. [x] Include methods: roll(), getFaceValue(), and __repr__()
# 3. [x] Create a TenSidedDie and a TwentySidedDie class
# 3b.[x]      These classes must EXTEND SixSidedDie, only code where necessary
# 4. [x] Create a Cup class that will hold several dice to roll at once
# 4b [x]      Must hold any number of 6-, 10-, or 20-sided die
#            All die:  cup = cup(1,1,1), 3 6-sided: cup = cup(3,0,0)
# 4c [x]      Default cup will have one of each type fo die
# 4d [x]      Contains methods: roll(), getSum(), __repr__()
#

from random import randint

class SixSidedDie():
    """ A class that represents a die; includes 2 methods
    1. roll() - simulates a roll of the die
    2. getFaceValue() - returns the value of the die
    """

    def __init__(self):
        """ initial setup for die """
        self.face = 6
        self.value = 1 # initialized to 1 since objects must obey the laws of physics (no nulls)
        self.reprString = "Six"
    
    def __repr__(self):
        """ Fulfilling the contract pt 1 """
        return "{}SidedDie({})".format(self.reprString, self.value)
    
    def __eq__(self, target):
        """ Fulfilling the contract pt 2 """ 
        # I still don't understand this contract thing, but it all sounds very serious
        if type(target) == int:  
            return self.value == target # Just in case...

        elif type(target) == list:
            # added to see if I can...
            raise invalidComparisonError('Cannot compare list and int') 
            
        return self.value == target.value
    
    def roll(self):
        """ Rolls the die! """
        self.value = randint(1, self.face)
        return self.value
    
    def getFaceValue(self):
        """ Returns the value of the die """
        return self.value


class TenSidedDie(SixSidedDie):
    """ A class that represents a die; it extends the 6-sided die class"""
    
    def __init__(self):
        """ initial setup for die """
        self.face = 10
        self.value = 1 # initialized to 1 since objects must obey the laws of physics (no nulls)
        self.reprString = "Ten"


class TwentySidedDie(SixSidedDie):
    """ A class that represents a die; it extends the 6-sided die class"""
    
    def __init__(self):
        """ initial setup for die """
        self.face = 20
        self.value = 1 # initialized to 1 since objects must obey the laws of physics (no nulls)
        self.reprString = "Twenty"


class invalidComparisonError(Exception):
    """ error for when list and int are compared """
    pass  # Just to see if I can :)  


class Cup():
    """ Holds a cup of dice so we can play yahtzee! 
    By default, has one of each die.  Can add or remove. """

    def __init__(self, numSixSidedDie = 1, numTenSidedDie = 1\
        , numTwentySidedDie = 1):
        """ initialize class by creating one die for each specified """
        
        # Records number of die of each type
        self.numSixSidedDie = numSixSidedDie
        self.numTenSidedDie = numTenSidedDie
        self.numTwentySidedDie = numTwentySidedDie

        # Use list comprehensions to fill a list of die for each die type
        self.Sixes = [SixSidedDie() for i in range(self.numSixSidedDie)]
        self.Tens = [TenSidedDie() for i in range(self.numTenSidedDie)]
        self.Twenties = [TwentySidedDie() for i in range(self.numTwentySidedDie)]

        # Initialize rolls (otherwise getSum won't work without first rolling)
        self.sixSidedRolls = []  
        self.tenSidedRolls = []
        self.twentySidedRolls = []

        # Sets value as a tuple of the number of die of each type
        self.value = (self.numSixSidedDie, self.numTenSidedDie\
            , self.numTwentySidedDie)

    def __repr__(self):
        """ Returns 'Cup' and a tuple with (Six-, Ten-, Twenty-sided die) """

        # This intentionally returns the number of die 
        return "Cup(numSixSidedDie({}), numTenSidedDie({}), numTwentySidedDie({}))".format(
            self.numSixSidedDie, self.numTenSidedDie, self.numTwentySidedDie)
    
    def __eq__(self, target):
        """ setting up identity """
        return self.value == target.value
    
    def roll(self):
        """ Roll each of the die in the cup; the results are saved in a list """
        self.sixSidedRolls = [die.roll() for die in self.Sixes]
        self.tenSidedRolls = [die.roll() for die in self.Tens]
        self.twentySidedRolls = [die.roll() for die in self.Twenties]

    def getRolls(self):
        """ Return the values of all rolls """
        print(self.sixSidedRolls)
        print(self.tenSidedRolls)
        print(self.twentySidedRolls)
    
    def getSum(self):
        """ returns the sum of all the face values of the die """
        return sum(self.sixSidedRolls + self.tenSidedRolls + self.twentySidedRolls)



# Testing
def tests():
    ssd = SixSidedDie()
    tsd = TenSidedDie()
    twsd = TwentySidedDie()

    print(ssd == tsd == twsd)
    print(ssd.getFaceValue(), ssd.value)
    print(tsd.getFaceValue(), tsd.value)
    print(twsd.getFaceValue(), twsd.value)
    print(ssd.roll(), ssd.getFaceValue())
    print(tsd.roll(), tsd.getFaceValue())
    print(twsd.roll(), twsd.getFaceValue())

    print(ssd == tsd)
    print(ssd == twsd)
    print(tsd == twsd)

    return None


# Testing part deux
def tests2():

    theCup = Cup()
    print(theCup)
    print(theCup.numSixSidedDie, theCup.numTenSidedDie, theCup.numTwentySidedDie)

    print(theCup.Sixes)
    print(theCup.Tens)
    print(theCup.Twenties)
    print()

    theCup = Cup(4, 5, 6)
    print(theCup.Sixes)
    print()
    print(theCup.Tens)
    print()
    print(theCup.Twenties)
    print()

    theCup.roll()
    print()
    print(theCup.Sixes)
    print()
    print(theCup.Tens)
    print()
    print(theCup.Twenties)
    print()
    print(theCup.getSum())

    print(theCup.getRolls())

    return

tests()
tests2()