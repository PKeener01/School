# Patrick Keener
# Problem 2


# Simulate simple ATM w/ a full keyboard
# User should be able to:
# * enter pin # & select from menu of transactions:
#    * Deposit
#    * Withdraw
#    * Balance
#    * Quit
# * Assume user has only one account on which transactions may be performed
#     * Account is associated w/ pin (dictionary)
#
# * ATM Retrieves info from file (accounts.csv)
#
# "Code the exception" means use code for try/except block
#
# * Use the [below] main() function to control program.  
#     * May NOT change names of functions or arguments or modify main() at all
#     * Use only local variables



# 1. Write function startUp(fname) that takes as input a filename that contains 
#    acct owner (user) info and current acct balance
#    * Initialize the dictionary in the function.  All variables in prog must 
#        be local
#    * If filename is invalid, code exception Code an exception:
#            ('Cannot get to the file') and return None
#    * If filename is valid, read the file & store each line in dict
#        * The key is the 4-digit code (pin) & value is a list w/ 
#             user first name, last name, and balance. Balance is float.
#             * Explicit conversion to float on balance list item
#        * Function returns the dictionary if file was successfully read &
#             dict filled w/ data; if not, return None

def startUp(fname):
    try:
        acctDict = dict()
        inFile = open(fname, 'r')
        inFile.close
        
        # Decided not to remove the space in Alexander Hamilton's name, but 
        # would have done that in the loop below using:
        # word = line.replace('\n','').replace(' ','').split(',')  

        for line in inFile:
            word = line.replace('\n','').split(',')  
            acctDict[word[0]] = [word[1], word[2], float(word[3])]
            
    except IOError: 
        print('Cannot get to the file')
        return None

    except ValueError:
    	print('Invalid input type, check that the balance entered is a float.')
    	return None
    
    except:
        print('Unknown error detected.')
        return None
    
    return acctDict


# 2. Write function verifyPin() that takes dictionary as input
#    * Prompt user to enter a pin
#    * If pin is valid, (is 4 digits & in dict), return pin & first name 
#      * If invalid, print('Incorrect pin') and return(None, None)

def verifyPin(acctDict):
    pin = input('Welcome-- Please enter your 4-digit pin: ')

    if pin in acctDict.keys() and len(pin) == 4:
        return pin, acctDict[pin][0]
    else:
        print('Incorrect pin')
        return None, None

    return


# 3. Write function menu(name) that takes as input user's first name then
#    displays user's name and the menu options:
#    * Options:  D:Depost    W: Withdraw    B: Balance   Q: Quiet
#      * If user enters value not D, W, B, Q, then print 
#             'Valid choices are D, W, B, Q, try again' & go back to menu 
#      * When valid # is entered, return the number of the chosen option

def menu(firstName):
    while True:
        print('\n{}:'.format(firstName))
        print('D: Deposit \nW: Withdraw \nB: Balance \nQ: Quit')
        choice = input('\nEnter choice: ')

        if choice.upper() == '':
                pass
        elif choice.upper() in 'DWBQ':
            return choice
        
        print('Valid choices are D, W, B, Q, try again')

    return None


# 4. Write function verifyAmount() that takes no input
#    * Inside loop, prompt user for an a mount to be deposited or withdrawn.  
#      * Convert to float
#      * If negative, print 'Negative amount.  Please try again.'
#      * Code an exception('Invalid amount.  Use digits only.')  
#        (exception caused if user enters string/blank instead of numeric)
#      * Stay in loop until valid # is entered then return amount

def verifyAmount():
    while True:
        try:
            amount = float(input('Amount: '))
            if amount >= 0:
                return amount
            else:
                print('Negative amount. Please try again.')

        except ValueError:
            print('Invalid amount.  Use digits only.')

    return None


# 5. Write function depost(pin, d) that accepts user's pin & dictionary
#    * Calls getAmount(), calculates new balance and updates dictionary
#    * Does not return anything, but should have return statement

def deposit(pin, acctDict):
    
    depAmt = verifyAmount()
    acctDict[pin][2] += depAmt

    return None


# 6. Write function withdraw(pin, d) that takes user's pin & dict
#    * Calls getAmount().  If amt to withdraw > balance print
#        'Insufficient funds to complete the transaction'
#      * Prompt user to enter new amt till amt entered < balance or 0
#      * Function uses balance in dict to calc new balance
#      * Balance updated in dict. 
#      * Does not return value but should have return statement

def withdraw(pin, acctDict):    
    while True:
        withdrawAmt = verifyAmount()

        if withdrawAmt in (0, '', None): 
            return None
        elif withdrawAmt <= acctDict[pin][2] :
            acctDict[pin][2] -= withdrawAmt
            return None
        else:
            print('Insufficient funds to complete the transaction')

    return None


# 7. Write function balance(pin, d) that takes user's pin & dict & returns 
#    balance

def balance(pin, acctDict):
    return acctDict[pin][2]


# 8. Write function quit(pin, d) that takes pin & dict
#    * User prompted as to whether they want to leave transaction.
#      * If yes, function return first & last name & message
#        'Thanks for using ABC Bank.'  <- Break
#      * If no, return(None,None)

def quit(pin, acctDict):
    if input('Do you want to leave transation? y/n: ').upper() == 'Y':
        return acctDict[pin][0], acctDict[pin][1]

    return None, None


def main():
    dict = startUp('accounts.csv') # dict dictionary name in main()
    if dict == None:
        return
    pin, name = verifyPin(dict)
    if pin != None and name != None:
        while True:
            print()
            choice = menu(name)
            if choice in 'Dd':
                deposit(pin, dict)
            elif choice in 'Ww':
                withdraw(pin, dict)
            elif choice in 'Bb':
                b = balance(pin, dict)
                msg = 'You current balance is ${:,.2f}'
                print(msg.format(b))
            elif choice in 'Qq':
                fname, lname = quit(pin, dict)
                if fname == None and lname == None:
                    pass
                else:
                    str = '\n{} {}, thanks for using the ABC Bank'
                    print(str.format(fname, lname))
                    break
    return



