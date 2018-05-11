import random

options = ["rock", "paper", "scissors"]
computer_wins = 0 # start of game computer has no wins
human_wins = 0 # start of game human has no wins
count_to_win = 3 # how many wins you a player needs until they WIN

game_over = False # initially, game is not over

def pick_winner(human_choice, computer_choice):
	if human_choice == "rock" and computer_choice == "scissors":
		return "human"
	if human_choice == "paper" and computer_choice == "rock":
		return "human"
	if human_choice == "scissors" and computer_choice == "paper":
		return "human"
	if human_choice == computer_choice:
		return "draw"
	return "computer"

def get_comp_choice():
	return options[random.randint(0, 2)]

def get_human_choice():
	return raw_input("Pick rock, paper, or scissors:\n")


while not game_over:
	print("*********** Starting new round ***********")
	# randomly choose computer choice
	computer_choice = get_comp_choice()

	# let player input choice
	human_choice = get_human_choice()

	# Print out what each player chose
	print("Computer chose " + computer_choice)
	print("Human chose " + human_choice)

	winner = pick_winner(human_choice, computer_choice)

	# Add 1 to winner
	if winner == "human":
		print("Human won this round")
		human_wins = human_wins + 1
	elif winner == "computer":
		print("Computer won this round")
		computer_wins = computer_wins + 1
	else:
		print("This round was a draw")


	# check for game over
	if human_wins >= count_to_win:
		game_over = True
		print("You Won!")

	if computer_wins >= count_to_win:
		game_over = True
		print("Computer won :(")
