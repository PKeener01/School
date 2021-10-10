# Patrick Keener
# Problem 1

# Please grade this script; the original may have used some methods/functions from section 3.2.


scoreList = list()                      # Initialize list variable


scoreList.append(eval(input('Enter score 1: ')))
scoreList.append(eval(input('Enter score 2: ')))
scoreList.append(eval(input('Enter score 3: ')))
scoreList.append(eval(input('Enter score 4: ')))

scoreList.remove(min(scoreList))        # Remove the lowest score
gradeAverage = sum(scoreList)/150       # Sum the list then divide by 150 (# of tests * 50)

print('The average is ' + str(int(round(gradeAverage,2)*100)) + '%')


# ===== Testing =====

# scores are 25, 15, 35, 50
# predicted results is 73%
# Log:
#       Enter score 1: 25
#       Enter score 2: 15
#       Enter score 3: 35
#       Enter score 4: 50
#       The average is 73%

# scores are 37.5, 22.5, 50, 49
# predicted results is 91%
# Log:
#       Enter score 1: 37.5
#       Enter score 2: 22.5
#       Enter score 3: 50
#       Enter score 4: 49
#       The average is 91%

# Test that min works as expected when all values are same
# Log:
#       Enter score 1: 30
#       Enter score 2: 30
#       Enter score 3: 30
#       Enter score 4: 30
#       The average is 60%

# Test that output is expected when values > denomenator (150)
# Log:
#       Enter score 1: 65
#       Enter score 2: 75
#       Enter score 3: 85
#       Enter score 4: 95
#       The average is 170%

# Ensure fractions are addressed as expected
# Log:
#       Enter score 1: 0
#       Enter score 2: 145
#       Enter score 3: 2
#       Enter score 4: 2
#       The average is 99%
# (149/150 = 0.9933333333333333)

