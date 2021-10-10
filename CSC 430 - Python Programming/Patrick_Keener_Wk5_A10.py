# ==================  Cups & Dice ===================
#
# Written by Patrick Keener on 10/18/2020
# Video Link: https://youtu.be/PWPDl-jjaAE
# Honor Statement:  "I have not given or received any unauthorized assistence 
#                    on this assignment"
# 
# Checks:
# 1. [x] Docstrings for all functions
# 2. [x] All requirements met
# 3. [x] Fully tested
#
# Requirements:
# Build a game
# 1.    [x] Greet user and ask name
# 2.    [x] Provide user with balance of $100
# 2b.       [x] Outputs are in dollars
# 3.    [x] Ask if they'd like to play a game
# 4.    [x] Generate random # between 1 & 100 - this will be called the 'goal'
# 5.    [x] Ask user how much they'd like to bet.
# 5b.   [x] Subtract this amount from the user's account
# 5c.       [x] How to handle negative numbers?
# 6.    [x] Ask user how many of each die they would like to roll
# 7.    [x] Create a cup filled with dice according to user's input
# 8.    [x] Roll cup & display results
# 9.    [x] if roll exactly matches goal, user receives 10x bet added to their bal
# 10.   [x] Otherwise, if within 3 but not over, user receives 5x
# 11.   [x] Otherwise, if roll within 10 of goal but not over, user receives 2x bet
# 12.   [x] Report results to user
# 12b.      [x] Message should include name & updated balance
# 13.   [x] Ask if they would like to play again.  If so, go to step 4
# 14.   [x] Submitted as single .py file (no importing previous code)


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


class User():
    """ Holds and updates the user's state data """
    
    def __init__(self, balance = 100, name = 'Player'):
        """ Sets initial states """
        self.balance = balance
        self.name = name
        self.winnings = 0
        self.playerBet = 0
        self.playerCup = Cup(0,0,0)
        self.goal = None
        self.mostRecentWinLose = None
        
    
    def bet(self, amount):
        """ Removes the bet amount from user balance"""
        self.playerBet = amount # hold the bet value
        self.balance -= self.playerBet
        
    def win(self, amount):
        """ Adds an amount to the user's balance """
        self.winnings = amount
        self.balance += self.winnings
    
    def getBalance(self):
        """ Returns the user's account balance """
        return self.balance

    def getGoal(self):
        """ Returns the current game goal """
        return self.goal
    
    def getName(self):
        """ Returns current user name """
        return self.name
    
    def getBet(self):
        """ Returns player bet """
        return self.playerBet
    
    def getWinnings(self):
        """ Returns player winnings """
        return self.winnings


def intro(player):
    """ Greets the user """
    
    player.name = input('What is your name?')

    print("Welcome, {}, to the Dice Game, written by P. Keener\n\n"
    
    # Rules
    "Rules: Players start with $100.  Each turn, a random number is selected "
    "between 1 and 100 (the goal).  The player will then make a wager and roll " 
    "a number of die of their choosing, consisting of 6, 10, and 20 sided die. "
    "If the sum of the die rolls is close they will win, otherwise the house "
    "keeps their money."
    
    # Wining conditions
    "\n\nWinning Conditions: \nIf the dice match the goal, "
    "the user receives 10x their bet.  If the dice is 3 less than the goal "
    "(but not over), theuser will receive 5x their bet.  If the roll is 10 less than "
    "the goal but not over, the user receives 2x their bet.\n\n".format(player.getName()))
    
    return None


def playGame(player):
    """ Asks the user if they'd like to play """
    
    while True: # loop to determine if user wants to play
        play = input('Would you like to play? (y/n)')

        if play[0].lower() == 'y':
            print('Good luck {}!  Your balance is ${}.\n'.format(
                player.getName()
                , player.getBalance()))
            return True

        elif play[0].lower() == 'n':
            print('Perhaps another time...\n\n')
            return False

        else:
            print('Invalid response, please try again.\n')
            pass
    return None


def userInput(qString, intCheck = True, posCheck = True):
    """ Utility function to get user input and check for common errors, allows
    checking to be turned on or off.

    Errors Checked:
    1. Is an integer
    2. Is positive 
    """

    while True:
        userResponse = input(qString)
    
        try:
            userResponse = eval(userResponse)
        except:
            print('Please enter an number\n')
            continue
        
        if intCheck == True:
            if userResponse != userResponse//1: # Check if integer
                print('The number must be an integer. Please try again.\n')
                continue
        
        if posCheck == True:
            if userResponse < 0: # ensure it is positive
                print('The number must be positive\n')
                continue
        
        return userResponse


def playDice(player):
    """ Play the game.  Determine the goal & roll the dice, then get winnings """
    # I would normally have the min/max as an option to set but that's not 
    # a requirement
    player.goal = randint(1, 100)
    player.playerCup.roll()

    print("Your die are: \nSix-Sided Die: {} \nTen-Sided Die: {} \n"
    "Twenty-Sided Die: {}\n".format(
        player.playerCup.sixSidedRolls
        , player.playerCup.tenSidedRolls
        , player.playerCup.twentySidedRolls
    ))

    gameMargin = player.getGoal() - player.playerCup.getSum()
    
    # Determine whether there are winnings
    if gameMargin < 0:
        player.mostRecentWinLose = 'Lose'
        return

    elif gameMargin == 0:
        player.win(10*player.playerBet)
        player.mostRecentWinLose = 'Win'
        return
    
    elif gameMargin <= 3:
        player.win(5*player.playerBet)
        player.mostRecentWinLose = 'Win'
        return
    
    elif gameMargin <= 10:
        player.win(2*player.playerBet)
        player.mostRecentWinLose = 'Win'
        return
    
    else:
        player.mostRecentWinLose = 'Lose'
        return
    return None


def getUserInputs(player):
    """ Gets user inputs """
    
    # Get dice inputs
    sixes = userInput('How many six-sided die would you like?')
    tens = userInput('How many ten-sided die would you like?')
    twenties = userInput('How many twenty-sided die would you like?')
    player.playerCup = Cup(sixes, tens, twenties)

    # get bet & update balance
    playerBet = userInput('How much money would you like to bet?', intCheck=False)
    player.bet(playerBet)

    return None


def displayResults(player):
    """ Displays the results of the game"""
    if player.mostRecentWinLose == 'Lose':
        print("{}, you have lost your bet of ${}! Better luck next time. "
        "The goal was {} and your dice added up to {}.  Your new balance is ${}.".format(
            player.getName()
            , player.getBet()
            , player.getGoal()
            , player.playerCup.getSum()
            , player.getBalance()
            ))
    else:
        print("Congratulations {}! You have won ${} on your bet of ${}. The goal "
        "was {} and your result was {}.  Your new balance is ${}.".format(
        player.getName()
        , player.getWinnings()
        , player.getBet()
        , player.getGoal()
        , player.playerCup.getSum()
        , player.getBalance()
        ))

    return None


def dice():
    """ Dice Game """
    player = User()
    intro(player)    

    while playGame(player):
        getUserInputs(player)
        playDice(player) # play the game and determine winnings
        displayResults(player)
        player = User(balance = player.getBalance(), name = player.getName())

       # Note: the user can go negative, and continue to play while negative 

    return None

dice()



# #  =============  Testing
# def testing():
#     """ A suite of tests for the program"""
#     userTesting()

#     return None

# def userTesting():  
#     """ Automated testing for the User class"""
#     # User
#     me = User()

#     print("Initial Balance Testing, both should be 100: \nme.balance: "
#         "{} \nme.getBalance(): {}\n"\
#         .format(me.balance, me.getBalance())) # Both should be 100

#     print("Bet Testing, both should be 90: \nme.bet(10) (Expected: None): "
#         "{} \nme.balance: {} \nme.getBalance(): {}\n"\
#         .format(me.bet(10), me.balance, me.getBalance())) # Both should be 90
    
#     print("Bet Testing, both should be 190: \nme.win(100) (Expected: None): {}" 
#         "\nme.balance: {} \nme.getBalance(): {}\n"\
#         .format(me.win(100), me.balance, me.getBalance())) # Both should be 100

#     return None
# testing()
 
# userInput('test', intCheck=False)
