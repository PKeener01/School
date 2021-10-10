# Patrick Keener
# Problem 2
#
# (read file, for loop, UDF)
#
# This program is a game: two words are randomly selected from the book 
# Pride & Prejudice, and the user must select which was used more frequently.
# The program then returns whether the user was correct, and the word count for
# each 
# UDF - wordGame()
# * Reads text file pride_and_prejudice.txt from d2l- saved in location as this file
# * Code should retrieve 2 random words from the file
# * Ask the user to guess which words the author used more often in the text
# * If the user picks the word w/ the higher count, they have guessed correctly
# * Include a statement verifying the results
# * Enclose chosen word with double quotes (") so they are easily distinguishable 
#		from the rest of the message
#
# * random.choice() to pick a random word
# * 
# * Use count method to determine frequency
# * Use a logical condition to determine if user guess correctly
# * be sure to use chosen words in quotes 
# * Note: only one function in this program


import random

def wordGame():
	# Initial conditions set up
	infile = open('Pride_and_Prejudice.txt','r')
	book = infile.read()
	infile.close()

	# Select words for game
	wordList = book.split()
	word1 = random.choice(wordList)
	word2 = random.choice(wordList)

	# Determine which word occurs more frequently
	word1Cnt = wordList.count(word1)
	word2Cnt = wordList.count(word2)

	if word1Cnt > word2Cnt:
		higher = word1
	else:
		higher = word2

	# Let user guess between the two words
	guess = input('Which word did the writer use more often "{}" or "{}"? '
		.format(word1, word2))

	# If user guesses correctly, tell them
	if guess == higher:
		print('You are correct')
	else:
		print('You are incorrect')
    
    # Verify results for user
	print('Verification: "{}" occurs {} times, "{}" occurs {}'
		.format(word1, word1Cnt, word2, word2Cnt))

	return None

wordGame()




# Test Cases
#
# Which word did the writer use more often "hate" or "diversion."? hate
# You are correct
# Verification: "hate" occurs 7 times, "diversion." occurs 1
# >>> 
# Which word did the writer use more often "he" or "that"? he
# You are incorrect
# Verification: "he" occurs 1046 times, "that" occurs 1423
# >>> 
# Which word did the writer use more often "piece" or "not"? a
# You are incorrect
# Verification: "piece" occurs 5 times, "not" occurs 1344
# >>> 