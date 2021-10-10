# Written by Patrick Keener on 9/16/2020
# Video Link: https://www.youtube.com/watch?v=YvXX_ooryAM&feature=youtu.be&ab_channel=Patrick
# Honor Statement:  "I have not given or received any unauthorized assistence 
#                    on this assignment"
#




def gradingLogic():
    """ A function for inputting the rubric and receiving a total grade.

    Keyword arguments:
    None

    Returns:
    finalGrade - the final grade as a float out of 40.

    """
    # Code variables that may be adjusted for other assignments
    #    If permitted, these would be user inputs

    totalPoints = 40.0 # Maximum possible points for the assignment
    latePctOff = .01 # % lost per hour late
    finalScorePosOnly = True # Can the final score go below 0?
    
    
    grades = list() # initialize list that grades will be added to
    finalGrade = float() #initialize final grade to 0.0 (float)
    lateDelta = latePctOff * totalPoints # points lost/hr late
    
    if passFail(): # contains early fail conditions
        return 0.0
    
    itemsToGrade = gradeItems() # Retrieve questions and point values

    for item in itemsToGrade:  # Cycle through each question
        grades.append(pointsInput(item))
    
    grades.append(late(lateDelta)) # Calculate points lost for lateness

    if finalScorePosOnly:  # Make sure points don't go below 0
        finalGrade = max(0.0, sum(grades))
        
    return finalGrade


def passFail():
    """ Checks the 4 pass/fail requirements, returns True if any failed

    Keyword arguments:
    None

    Returns:
    boolean - True if the student failed any requirements, True if not
    """

    fileTest = input('Was the assignment submitted as a single,\
         uncompressed.py file? (y/n)')
    if fileTest[0].lower() == 'n': 
        return True
    
    nameTest = input('Did the student include the name AND date? (y/n)')
    if nameTest[0].lower() == 'n': 
        return True

    honorTest = input('Did the student include the honor statement? (y/n)')
    if honorTest[0].lower() == 'n': 
        return True

    videoTest = input('Did the student include a link to a 3-minute youTube \
        video? (y/n)')
    if videoTest[0].lower() == 'n': 
        return True

    return False


def gradeItems():
    """ A function containing the items to be graded, as a list.  It is designed
    to allow for more or fewer grading items to be added quickly and easily.

    Keyword arguments:
    None

    Returns:
    itemsList - a list of items to be graded

    """
    # In real life this would be stored in a separate file and loaded in, and 
    # this function would give the user the ability to add or remove items

    itemsList = list()

    itemsList.append(
        ['How many points will the student receive for code correctness?'
        , 10  # Max Points
        , 0   # Min Points
        ])
        
    itemsList.append(
        ['How many points will the student receive for code Elegance (data \
            structure selection, algorithm efficiency, function implementation'
        , 10  # Max Points
        , 0   # Min Points
        ])
    
    itemsList.append(
        ['How many points will the student receive for code hygiene?'
        , 10  # Max Points
        , 0   # Min Points
        ])

    itemsList.append(
        ['How many points will the student receive based on the quality of \
            discussion on the youTube video?'
        , 10  # Max Points
        , 0   # Min Points
        ])
 
    return itemsList


def pointsInput(item):
    """ Each metric to be graded may be entered here

    Keyword arguments:
    item[a, b, c] - a list containing the following variables:
        a - Str containing the question to be asked. What is being graded?
        b - Int or Float containing the maximum number of points on the 
            question
        c - Int or Float containing the minimum number of points on the 
            question, default 0

    Returns:
    A float containing the number of points the student received.
    """

    while True:
            try:
                pointsReceived = eval(input('{} (out of {})'
                .format(item[0], item[1]))) # question, max points

            except:
                print('Please input a number.')
                continue
        
            if item[2] <= pointsReceived <= item[1]: # min points, max points
                return float(pointsReceived)
            else: 
                print('Please input a number between {} and {} (inclusive).'
                .format(item[2], item[1])) # max points, min points

    return None


def late(lateDelta):
    """ Asks whether the assignment was late then modifies points

    Keyword arguments:
    lateDelta - the number of points the student loses per hour late

    Returns:
    The number of points to be subtracted from the final grade
    """
    hoursLate = float()

    wasLate = input('Was the assignment late? (y/n)')
    if wasLate[0].lower() == 'y':
        while True:
            try:
                hoursLate = eval(input('How many hours late was the assignment?'))
                return float(-lateDelta*hoursLate) # Negative so it will sum properly
            except:
                print('Please input a number.')
    else:
        return 0.0
    
    return None
            


gradingLogic()






# Video Script:

# My name is Patrick Keener and this is DSC 430- Python Programming
# , Assignment 1 - Grading Logic.

# Step 1- execute the code.  The code begins with the first four, early fail 
# conditions.  If I say no to the first, you will see that the program ends and it
# returns 0.0.  This is true for all early fails.

# Next, we'll skip those four by entering yes, then go to the next group: How many
# points will the student receive for [whatever they're doing].  if we say 15 we 
# can see that it requests to answer a number between 0 and 10, if we leave it 
# blank or give it a non-numeric, it will ask us to input a new number.  
# We'll enter numbers for the remaining questions here.

# Next we get to code lateness.  If I hit n or type no it will not reduce the 
# final score, but let's say yes because it's more fun.


# The code is broken into 5 functions: gradingLogic(), which controls program 
# flow, passFail(), which is the input function for pass/fail items, gradeItems(),
# which contains rubric data, pointsInput(), which is the input function for 
# non-pass/fail items, and late(), which asks about lateness and calculates any 
# impacts.

# The first question is about exiting early.  This code contains several functions
# to assist.  At the top level, in gradingLogic, we see that if passFail returns 
# true it will exit and return 0.0.  Within passFail itself we can see that each 
# question has a similar exit condition attached.  This allows the code to exit 
# early if any of the fail conditions become true.

# The code is designed so that any number of questions may be added to the 
# gradeItems function, which is itself the input for the pointsInput function.  
# The pointsInput function takes a string input that contains a question, a 
# maximum number of points, and a minimum number of points.  

# We can see that the function contains a while statement as well as two error 
# handling statements, which brings us to question number 2: how does it deal w/ 
# the fact that input() returns a string?  We can see that input is enclosed in 
# the eval() statement which will treat a string like a number.  If a non-numeric 
# is entered this will cause an error, hence the error handling.  Next, it checks 
# that the input is within the allowed range of points and requests a new number 
# if it is not.

# The final question is: why do we return the score instead of print it? And this 
# is simply so that this function can be incorporated into another program.


# # Ran out of time so couldn't do this part, but...

# The Late function takes lateDelta as an input, which is the number of points 
# lost per hour late.  If the assignment was late then lateDelta is multiplied by 
# the number of late ours and returned as a negative number.  This is done so 
# that, when added to the string containing all of the grades, it can be summed to
# result in the output.