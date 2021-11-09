"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text = ""

    with open(file_path) as file:
        for line in file:
            line = line.rstrip()
            text += line + " "

    return text




def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words_collection = text_string.split(" ")
    print(len(words_collection))
    words_collection.pop()
    # print(words_collection)
    # looping through words_collection and assign 3 variable[1] first [2] 2nd [3]3rd as a tuple
    # Does the key exist in chain {} if not, assign third word as a list value
        # If yes, append to new variable list
        # If no, then it will create a new key/ toop

    for i in range(len(words_collection)-2):
        first_word = words_collection[i]
        second_word = words_collection[i+1]
        third_word = words_collection[i+2]

        toop = (first_word,second_word)

        if toop not in chains:
            chains[toop] = [third_word]
        else:
            chains[toop].append(third_word)

    return chains




def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

