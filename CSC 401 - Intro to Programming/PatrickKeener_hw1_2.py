# Patrick Keener
# Problem 2
#
# Please grade this script; the original may have used some methods/functions from section 3.2.



# Variable used to track pass/fail state of password
meetsCriteria = True

# Assign numbers as strings to a list and top of program to allow for easier
# maintenance and cleaner code
numbersStr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Input password
password = input('Enter password: ')

# Test 1: Password is less than 9 characters        
if len(password) < 9:
        meetsCriteria = False
        print(password + ' is less than 9 characters')

# Test 2: Non-alphanumeric characters present in password
if password.isalnum() == False:
        meetsCriteria = False
        print(password + ' contains a non-alphanumeric character')

# Test 3: Second character is numeric
if password[1] not in numbersStr:
        meetsCriteria = False
        print('The second character ' + password[1] + ' is not numeric')

# Test 4: Last character is non-alpha
if password[-1].isalnum() == False or password[-1] in numbersStr:
        meetsCriteria = False
        print('The last character ' + password[-1] + ' must be an alpha character')

# Test 5:  Password that meets all rules
if meetsCriteria == True:
        print('Congratulations, ' + password + ' meets all of the criteria')



# ===== Testing =====

# Test Case 1: "a2c"
# Expectation: Fail test 1
# Outcome: Fails test 1
#
# Enter password: a2c
# a2c is less than 9 characters


# Test Case 2: "A1234_678b"
# Expectation: Fail test 2
# Outcome: Failed test 2
#
# Enter password: A1234_678b
# A1234_678b contains a non-alphanumeric character


# Test Case 3: "Ab2345678b"
# Expectation: Fail test 3
# Outcome: Failed test 3
#
# Enter password: Ab2345678b
# The second character b is not numeric


# Test Case 4: "A123456789"
# Expectation: Fail test 4
# Outcome: Failed test 4
#
# Enter password: A123456789
# The last character 9 must be an alpha character


# Test Case 5: "ab_2"
# Expectation: Fail all tests
# Outcome: All tests failed
#
# Enter password: ab_2
# ab_2 is less than 9 characters
# ab_2 contains a non-alphanumeric character
# The second character b is not numeric
# The last character 2 must be an alpha character


# Test Case 6: "A12345678b"
# Expectation: Pass all tests
# Outcome: All tests passed
#
# Enter password: A12345678b
# Congratulations, A12345678b meets all of the criteria
