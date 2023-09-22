import random

wordlist = 'telecommunication party flump succulent tension' \
           ' willow broaden aerial astronomical beat'.split()

hangman = [
    '''\n|\n|\n|\n===\n''',
    '''+---+\n|\n|\n|\n===\n''',
    '''+---+\n|   O\n|\n|\n===\n''',
    '''+---+\n|   O\n|   |\n|\n===\n''',
    '''+---+\n|   O\n|  /|\n|\n===\n''',
    '''+---+\n|   O\n|  /|\\\n|\n===\n''',
    '''+---+\n|   O\n|  /|\\\n|  /\n===\n''',
    '''+---+\n|   O\n|  /|\\\n|  / \\\n===\n''',
]

def random_choice(seq):
    if len(seq) == 1:
        return seq[0]
    return random.choice(seq)

def load_wordlist_from_file(wordfile):
    """
    Reads a list of words from a file on disk.
    :param wordfile: a string giving the path to the wordlist file
    :return: a list of strings, one for each word in the file. Whitespace is stripped from each word.
    """
    with open(wordfile, 'r') as f:
        wordlist = f.readlines()
    wordlist = [word.strip() for word in wordlist]
    return wordlist

def filter_wordlist_for_difficulty(wordlist, difficulty):
    """
    Looks at a list of words and returns a subset of them according to their length and the requested difficulty.
    :param wordlist: A list of strings (words)
    :param difficulty: a string ['easy', 'medium', or 'hard'].  Defaults to 'hard' if not either 'easy' or 'medium'.
    :return: A list of strings with the requested difficulty levels.
    """
    difficulty = difficulty.lower()

    if difficulty == "easy":
        return list(filter(lambda word: 1 <= len(word) <= 5, wordlist))
    elif difficulty == "medium":
        return list(filter(lambda word: 6 <= len(word) <= 9, wordlist))
    elif difficulty == "hard":
        return list(filter(lambda word: 10 <= len(word) <= 100, wordlist))
    else:
        print("Please enter difficulty level as either 'easy', 'medium' or 'hard'")
        exit()

def get_turn_string(turn):
    """
    Format the turn number into a nice header to display to the user.  For turn=2, we return:
    '================Turn 02================='
    :param turn: an int for how many turns the user has taken
    :return:  a nicely formatted string to display
    """
    turn_header = f"\n\n{'Turn ' f'{turn:02}' :=^40}"
    return turn_header

def display_turn_dialog(turn, correct_letters, lives_left, hangman_pic=False):
    if hangman_pic:
        print(get_turn_string(turn))
        print(hangman[len(hangman)-lives_left-1])
        print(f"Mystery word: {' '.join(correct_letters)}")
    else:
        print(f"Mystery word: {' '.join(correct_letters)}")




