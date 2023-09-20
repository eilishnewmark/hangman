import random

def random_choice(seq):
    if len(seq) == 1:
        return seq[0]

    return random.choice(seq)

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

