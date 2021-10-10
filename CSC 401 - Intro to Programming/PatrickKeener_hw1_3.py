# Patrick Keener
# Problem 3
#
# Please grade this script; the original may have used some methods/functions from section 3.2+

calcString = input('Enter calculation to be performed, e.g. 5+9: ')     # Input string

if calcString[1] == '/' and calcString[2] == '0':    # Check for division by 0; if found, print error
	print('Division by zero is not allowed')
else:
        # English name for each digit use in a string.  The index in conjunction with the number will provide
        # the equivalent of a dictionary lookup
	numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	num1 = eval(calcString[0]) # Use variables rather than evaluating directly in print statement to 
	num2 = eval(calcString[2]) # help with readability

	# Determine the english name for the operator
	if calcString[1] == '+':
		operator = ' plus '
	elif calcString[1] == '-':
		operator = ' minus '
	elif calcString[1] == '*':
		operator = ' multiplied by '
	elif calcString[1] == '/': 
		operator = ' divided by '

	# Print the english name and then the numeric output.
	print(numbers[num1] + operator + numbers[num2] + ' is ' + str(eval(calcString)))



# ===== Testing =====

# Ensure proper assignment of all values
# tests: 1+2, 3-4, 5*6, 7/9, 9/0
#
# Test 1:
# Enter calculation to be performed, e.g. 5+9: 1+2
# one plus two is 3
#
# Test 2:
# Enter calculation to be performed, e.g. 5+9: 3-4
# three minus four is -1
#
# Test 3:
# Enter calculation to be performed, e.g. 5+9: 5*6
# five multiplied by six is 30
#
# Test 4:
# Enter calculation to be performed, e.g. 5+9: 7/9
# seven divided by nine is 0.7777777777777778
#
# Test 5:
# Enter calculation to be performed, e.g. 5+9: 9/7
# nine divided by seven is 1.2857142857142858
#
# Test 6:
# Enter calculation to be performed, e.g. 5+9: 9/0
# Division by zero is not allowed
#
# Test 7:
# Ensure having 0 in numerator doesn't trigger divide by zero logic
# Enter calculation to be performed, e.g. 5+9: 0/9
# zero divided by nine is 0.0
#
# Test 8:
# Ensure having 0 in second numeric position w/o division doesn't trigger divide by zero logic
# Enter calculation to be performed, e.g. 5+9: 7+0
# seven plus zero is 7

# All values retrieved and displayed properly.
