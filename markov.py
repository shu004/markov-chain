"""Generate Markov text from text files."""

from random import choice
import random


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
    words_collection.pop()


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

    list_of_keys = sorted(chains.keys())
    first_two_words = choice(list_of_keys)
    word1, word2 = first_two_words
    words.append(word1)
    words.append(word2)
    list_of_value = chains.get(first_two_words)
    word = choice(list_of_value)
    words.append(word)

    new_key = (words[1],words[2])
    

    while new_key in list_of_keys:
        random_value = chains.get(new_key)
        random_word = choice(random_value) #random word for new list
        words.append(random_word)
        new_key = (new_key[1], random_word)


    return ' '.join(words)



input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

