import gameutils  # contains a few useful things to re-use

def load_wordlist_from_file(wordfile):
    """
    Reads a list of words from a file on disk.
    :param wordfile: a string giving the path to the wordlist file
    :return: a list of strings, one for each word in the file. Whitespace is stripped from each word.
    """

    # TODO: fill in code here to load and return the list of words  (Task 1)

    with open(wordfile, 'r') as f:
        wordlist = []
        for line in f:
            ind_words = line.strip("\n")
            wordlist.append(ind_words)
    return wordlist

def filter_wordlist_for_difficulty(wordlist, difficulty):
    """
    Looks at a list of words and returns a subset of them according to their length and the requested difficulty.
    :param wordlist: A list of strings (words)
    :param difficulty: a string ['easy', 'medium', or 'hard'].  Defaults to 'hard' if not either 'easy' or 'medium'.
    :return: A list of strings with the requested difficulty levels.
    """

    # TODO: fill in code here to return a list of only those strings with correct
    # length, between min_len & max_len inclusive (Task 2)

    difficulty_list = []
    for word in wordlist:
        if difficulty == "easy":
            if 1 <= len(word) <= 5:
                difficulty_list.append(word)
        elif difficulty == "medium":
            if 6 <= len(word) <= 9:
                difficulty_list.append(word)
        else:
            if 10 <= len(word) <= 100:
                difficulty_list.append(word)
    return difficulty_list

def get_wordlist(wordfile, difficulty):
    if wordfile:
        wordlist = load_wordlist_from_file(wordfile)
    else:
        wordlist = gameutils.wordlist  # TODO: change this to use a better default list (one from gameutils module) (Task 3)
    return filter_wordlist_for_difficulty(wordlist, difficulty)

previous_guesses = []
def get_user_guess(previous_guesses):
    """
    Prompt the user for their guess.  They must enter a single alphabetic character.  We also check whether
    they've already entered their guess before, and warn them if they have, printing:

    "You already guessed that (X times now!)"  (where X is the number of times they've guessed in total)

    Only a guess that is new and is a single alphabetic is returned, and we keep asking until the user enters one.

    :param previous_guesses: a list of strings- one for each guess that has previously been made (updated here too).
    :return: the guess that meets all criteria, made lowercase for consistency.
    """
    while True:
        guess = input('What letter would you like to guess? (a-z): ')

        # TODO: make sure the user enters a valid guess, so roughly the following steps...  (Task 4)
        # then check it hasn't been entered before
        # if it has, print the warning and make them guess again)
        if guess in previous_guesses:
            no_of_guesses = previous_guesses.count(guess)
            print(f"You already guessed that {no_of_guesses} times now!")
        # check the guess is a single alphabetic character, and...
        # ...if so, add it to the record of previous guesses
        # - if it's a new guess, success - we make it lower case for consistency and return it
        elif (len(guess) != 1) or (guess.isalpha() is False):
            print("Your guess must be a single letter - try again!")
        else:
            guess.lower()
            previous_guesses.append(guess)
            return guess


# TODO: need to add a function which can be called like "find_matches(word, letter)", which takes a word and a letter
#  and returns a list of all the indices that character is found.  For example, find_matches('arab', 'a') should return
#  [0, 2]...  (Task 5)

def find_matches(word, letter):
    matches = []
    for n in range(len(word)):
        if word.find(letter, n) == n:
            matches.append(n)
    return matches

def get_turn_string(turn):
    """
    Format the turn number into a nice header to display to the user.  The number should be a two-digit integer, padded
    with zeros, centred in a field of '=' characters a total of 40 wide.  For example, for turn=2, we return:

    '================Turn 02================='

    :param turn: an int for how many turns the user has taken
    :return:  a nicely formatted string to display
    """

    turn_header = f"{'Turn ' f'{turn:02}' :=^40}"  #TODO: need to format better (Task 6)
    return turn_header

def display_turn_dialog(turn, correct_letters, lives_left):
    print(get_turn_string(turn))
    print(gameutils.hangman[len(gameutils.hangman)-lives_left-1])
    print(f"Mystery word: {' '.join(correct_letters)}")

def word_is_complete(letters):
    """
    Check all the letters in the given list to see whether the word is now complete (i.e. no "_" left)
    :param letters: the list of strings (each a single letter) to check
    :return: True if the word is complete, or otherwise False.
    """

    # TODO: fill in code here (Task 7)
    if "_" in letters:
        return False
    else:
        return True

# The main driver function.  No need to change anything in this function (just read it to understand it though!)
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
        display_turn_dialog(turns_taken, letters, lives_left)

        # get a valid guess from the user
        guess = get_user_guess(guess_history)

        # check their guess against the secret word and act accordingly...
        inds = find_matches(secret_word, guess)
        if not inds:
            print("Incorrect - you lose a life!")
            lives_left -= 1
        else:
            print("Correct - that letter is in the secret word!")
            for i in inds:
                letters[i] = guess
            if word_is_complete(letters):
                print(f"Congratulations, you got the word - '{secret_word}'!")
                return

    # if we reach this point, the user failed, so tell them the word
    print(f"{' Game Over ':*^40}")
    print(gameutils.hangman[len(gameutils.hangman)-lives_left-1])
    print("Too bad - you didn't get the word :(")
    print(f"The word was '{secret_word}'")


# finally, run the game with some test parameters!
play(wordfile='wordlist.txt', difficulty='difficult')
