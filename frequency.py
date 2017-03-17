""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
#Scarlet Letter

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    print("hi")
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
            curr_line += 1
    lines = lines[curr_line+1:]
    lines_total = ''
    for line in lines:
                if line != '\n':
                    lines_total = lines_total + line
    lines_total_split = lines_total.split()
    # remove ending
    for i in range(0, len(lines_total_split)):
        if (lines_total_split[i] == 'End') and (lines_total_split[i+1] == 'of') and (lines_total_split[i+2] == 'Project'):
                break
    # create array
    lines_total_s = lines_total_split[0:i]
    final_set = []
    # change array so doesn't include end
    for x in range(0, i):
        a = lines_total_s[x].strip(string.punctuation)
        b = a.lower()
        final_set.append(b)
    # print (final_set)
    word_list = final_set
    return word_list


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    word_dict = dict()
    for word in word_list:
        word_dict[word] = word_dict.get(word, 0) + 1
    ordered_by_frequency = sorted(word_dict, key=word_dict.get, reverse=True)
    print(ordered_by_frequency[0: n])


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.punctuation)

    b = get_word_list('h_full.txt')
    get_top_n_words(b, 10)
