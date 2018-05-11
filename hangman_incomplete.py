
import random # we need the random library to pick a random word from list

# Function that converts a list to a string split up be delim
# Ex) lst_to_str(["a","b","c"],"") returns "abc"
# Ex) lst_to_str(["a","b","c"]," ") returns "a b c"
# Ex) lst_to_str(["a","b","c"],",") returns "a,b,c"
def lst_to_str(lst, delim):
	return delim.join(lst)

# Function th
def replace_with_input(lst_current_guess, user_input, chosen_word):
	for i in range(len(chosen_word)):
		if chosen_word[i] == user_input:
			lst_current_guess[i] = chosen_word[i]
	return lst_current_guess

# Opening text file with 1000 words
text_file = open("words.txt", "r")

# Making a list of words from that file
words = text_file.read().split('\n')

# picking random index in list
index = random.randint(0, len(words)-1)

# picking word
chosen_word = words[index]
len_chosen_word = len(chosen_word)
print("The chosen word has " + str(len_chosen_word) + " characters")

# setting up difficulty of game 
num_guesses = 12

#starting game
game_over = False
guessed_letters = []
guessed_words = []
player_current_guess = ["?"]*len_chosen_word

while (not game_over):
	print("********************** PLAYER TURN **********************")
	print("You have " + str(num_guesses) + " guesses left")
	print("Here are all the characters you guessed so far: " + lst_to_str(guessed_letters, ','))
	print("Here are all the words you guessed so far: " + lst_to_str(guessed_words, ','))
	print("Your current guess is: " + lst_to_str(player_current_guess, ''))
	valid_user_input = False
	while(not valid_user_input):
		user_input = raw_input("What is your guess?\n")
		if len(user_input) == 1:
			valid_user_input = True
			have_letter_guesses = True
			player_current_guess = # TODO: set this
			guessed_letters.append(user_input)
			print(lst_to_str(player_current_guess, ''))
		elif len(user_input) == len_chosen_word:
			valid_user_input = True
			if user_input == chosen_word:
				player_current_guess = chosen_word.split("(?!^)")
			else:
				print("Incorrect Guess")
			# TODO: What else do we need to update?

		else:
			print("Invalid input (either 0 characters or too long)")

	# TODO We need to update something
	num_guesses = num_guesses - 1
	if (sum([i=='?' for i in player_current_guess]) == 0):
		print("*********************** GAME OVER ***********************")
		print("You did it!!! the word was " + chosen_word)
		game_over = True
	# TODO write the if statement for losing the game