from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    open_file = open(file_path)
    # giant_string = ''

    # for line in open_file: 
    #     giant_string = giant_string + line.rstrip() + " "
    # return giant_string

    return open_file.read()



def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    words = text_string.split()
    chains = {}

    # keys: tuples
    # for index in range(0, len(words)-2):
    #     word1, word2, word3 = words[index], words[index + 1], words[index + 2]
    #     key, value = tuple([word1, word2]), word3
    #     if key in chains:
    #         chains[key].append(word3)
    #     else:
    #         chains[key] = [word3]

    # key, value = tuple([word1, word2]), word3
    #     if key in chains:
    #         chains[key].append(word3)
    #     else:
    #         chains[key] = [word3]

    # wrap1_key = tuple([words[-2],words[-1]])
    # chains[wrap1_key] = chains.get(warp1_key, [words[0]])

    # wrap2_key = tuple([words[-1],words[0]])
    # chains[wrap2_key] = chains.get(warp2_key, [words[1]])

    for index in range(-2, len(words)-2):
        key = tuple([words[index],words[index+1]])
        chains[key] = chains.get(key,[]).append(words[index+2])

    return chains

print make_chains(open_and_read_file("green-eggs.txt"))


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
