import gameutils 
import os

def get_wordlist(wordfile, difficulty):
    if wordfile:
        wordlist = gameutils.load_wordlist_from_file(wordfile)
    else:
        wordlist = gameutils.wordlist
    return gameutils.filter_wordlist_for_difficulty(wordlist, difficulty)

previous_guesses = []

def get_user_guess(previous_guesses):
    """
    Prompt the user for their guess.  They must enter a single alphabetic character.  We also check whether
    they've already entered their guess before, and warn them.
    Only a guess that is new and is a single alphabetic is returned, and we keep asking until the user enters one.

    :param previous_guesses: a list of strings (updated here too).
    :return: the guess that meets all criteria.
    """
    checking_guess = True
    while checking_guess:
        if len(previous_guesses) == 0:
            guess = input('\nGuess a letter (a-z): ')
        else: 
            guess = input('\nGuess another letter (a-z): ')
        
        if len(guess) != 1 or not guess.isalpha():
            print("Your guess must be a single letter - try again!")
        elif guess in previous_guesses:
            no_of_guesses = previous_guesses.count(guess)
            previous_guesses.append(guess.lower())
            print(f"You've already guessed that! No. of previous {guess} guesses: {no_of_guesses}")
        else:
            previous_guesses.append(guess.lower())
            checking_guess = False
            return guess

def find_matches(word, letter):
    matches = [n for n in range(len(word)) if word.find(letter, n) == n]
    return matches


def word_is_complete(letters, secret_word):
    """
    Check all the letters in the given list to see whether the word is now complete (i.e. no "_" left)
    :param letters: the list of strings (each a single letter) to check
    :return: True if the word is complete, or otherwise False.
    """
    letters = ''.join(letters)
    if letters.rstrip().lower() != secret_word:
        return False
    return True

def play(wordfile=None, difficulty='hard'):
    """
    Play one round of hangman.
    :param wordfile: path (a string) to a file containing a list of words to choose from (one per line)
    :param difficulty: string to set difficulty - either "easy", "medium" or "hard"
    :return:
    """

    # get a list of words to use, according to the requested difficulty level
    wordlist = get_wordlist(wordfile, difficulty)

    # choose a random entry to use as the secret word
    secret_word = gameutils.random_choice(wordlist)

    # initialise house-keeping variables, then run the main game loop
    letters = ['_'] * len(secret_word)
    guess_history = []
    turns_taken = 0
    lives_left = 7

    while lives_left:
        turns_taken += 1
        # display current game state to the user
        gameutils.display_turn_dialog(turns_taken, letters, lives_left, hangman_pic=True)
        # get a valid guess from the user
        guess = get_user_guess(guess_history)
        # check their guess against the secret word and act accordingly...
        inds = find_matches(secret_word, guess)
        if not inds:
            lives_left -= 1
            print(f"\nIncorrect - you lose a life!\nYou have {lives_left} lives left.")
        else:
            print("Correct - that letter is in the secret word!\n")
            for i in inds:
                letters[i] = guess
            if word_is_complete(letters, secret_word):
                    print(f"Congratulations, you got the word - '{secret_word}'!")
                    return
            gameutils.display_turn_dialog(turns_taken, letters, lives_left, hangman_pic=False)
            guess_whole_word = input("Do you want to guess the entire word? Enter Y or N: \n")
            if guess_whole_word == "Y":
                guessed_letters = input("Enter your guess: ")
                if word_is_complete(guessed_letters, secret_word):
                    print(f"Congratulations, you got the word - '{secret_word}'!")
                    return
                else:
                    lives_left -= 1
                    print(f"\nIncorrect - you lose a life!\nYou have {lives_left} lives left.")

    # if we reach this point, the user failed, so tell them the word
    print(f"{' Game Over ':*^40}")
    print(gameutils.hangman[len(gameutils.hangman)-lives_left-1])
    print("Too bad - you didn't get the word :(")
    print(f"The word was '{secret_word}'")

# finally, run the game with some test parameters!
play(wordfile='wordlist.txt', difficulty='hard')
