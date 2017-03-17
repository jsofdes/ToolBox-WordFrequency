""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


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
            #print(lines)
    lines_total=''
    print('bb')
    #list1 = filter(lambda x: x != '\n', lines)
    print('so')
    #print(list1)
    for line in lines:
            #while line != str("End of Project Gutenberg's The Scarlet Letter, by Nathaniel Hawthorne\n"):
                if line != '\n':
                    lines_total = lines_total + line
    #print(lines_total)
    lines_total_split = lines_total.split()
    print(lines_total_split)

    for i in range(0, len(lines_total_split)):
        if (lines_total_split[i] == 'End') and (lines_total_split[i+1] == 'of') and (lines_total_split[i+2] == 'Project'):
                break
            #print(i)
    lines_total_s=lines_total_split[0:i]
    print(lines_total_s)
    final_set=[]
    for x in range (0,i):
        a = lines_total_s[x].strip(string.punctuation)
        b=a.lower()
        final_set.append(b)
    print (final_set)
    word_list = final_set
    return word_list


            # "End of Project Gutenberg's The Scarlet Letter, by Nathaniel Hawthorne\n"




def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    word_dict=dict()
    for word in word_list:
       word_dict[word] = word_dict.get(word, 0) + 1

    ordered_by_frequency = sorted(word_dict, key=word_dict.get, reverse=True)
    print(ordered_by_frequency[0: n])


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.punctuation)

    b= get_word_list('h_full.txt')
    get_top_n_words(b, 10)
