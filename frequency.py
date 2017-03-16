""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import pickle


def setup():
    import requests
    h_full_text = requests.get('http://www.gutenberg.org/cache/epub/33/pg33.txt').text
    #import pickle
    # Save data to a file (will be part of your data fetching script)
    f = open('h_texts.pickle', 'wb')
    pickle.dump(h_full_text, f)
    f.close()


def get_word_list():
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    #import pickle
    input_file = open('h_texts.pickle', 'rb')
    copy_of_texts = pickle.load(input_file)
    #changed this line
    f = open(copy_of_texts, 'r')
    lines = f.readlines()
    curr_line = 0
    print("hi")
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
        lines = lines[curr_line+1:]
        #print(lines)



def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    pass

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.punctuation)
    setup()
    get_word_list()
