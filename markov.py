from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # Solution 2
    open_file = open(file_path)

    ## Solution 1
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

    ## Solution 1
    # for index in range(0, len(words)-2):
    #     word1, word2, word3 = words[index], words[index + 1], words[index + 2]
    #     key, value = tuple([word1, word2]), word3
    #     if key in chains:
    #         chains[key].append(word3)
    #     else:
    #         chains[key] = [word3]

    # Solution 2
    for index in range(0, len(words)-2):
        key = tuple([words[index], words[index+1]])
        chains.setdefault(key, []).append(words[index+2])
    chains.setdefault((words[-2], words[-1]), []).append(None)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    output_text = ""

    # made key list and then choise the first key random
    keys = chains.keys()
    new_key = choice(keys)

    # add the first tuple key to the output_text
    output_text = output_text + new_key[0] + " " + new_key[1]

    # from index 2 to end which is none, the code runs
    while True:
        random_value = choice(chains[new_key])
        if random_value is None:
            break
        output_text += " %s" % random_value
        new_key = tuple([new_key[1], random_value])

    return output_text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
