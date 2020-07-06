'''This is a user generated word hangman game'''
print("Welcome to Hangman in Python!")
guess_word = input("Please enter a word to guess:\n")
print("-----------------------------NO CHEATING PLEASE----------------------------\n"*100)
list_word = list('*'*len(guess_word))
num_guess = 0
while True:
	try:
		incorrect_guesses = int(input("How many incorrect attempts do you want? [0,20]\n"))
		if type(incorrect_guesses) == int and incorrect_guesses >=0 and incorrect_guesses <=20:
			break
	except ValueError:
		print("that is not a valid integer!")
num_incorrect = 0
guesses = []
while num_incorrect < incorrect_guesses:
	guess = input("Please enter a letter to guess:\n")
	if guess in guesses:
		print("You have already guessed that letter")
		continue
	elif guess in guess_word and len(guess) == 1:
		guesses.append(guess)
		index = [num for num in range(len(guess_word)) if guess_word[num] == guess]
		for i in index:
			list_word[i] = guess_word[i]
	elif guess not in guess_word and len(guess) == 1:
		guesses.append(guess)
		print("Sorry, that letter is not in the word")
		num_incorrect += 1
	else:
		print("Sorry that's not a valid letter")
		continue
	num_guess += 1
	print_word = "".join(list_word)
	print(f'WORD: {print_word}\n# OF GUESSES MADE: {num_guess}\n# OF INCORRECT GUESSES: {num_incorrect}\nGUESSES:{guesses}')
	if print_word == guess_word:
		print(f"Good Job! You guessed the word correctly. It took you {num_guess} guesses")
		break
if not print_word == guess_word:
	print("Sorry, you lost. Better luck next time :P")


