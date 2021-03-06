"""
Creates word list of valid words from the 'words.txt' file.
"""
import re

def filter_wordlist():
    '''
    Filters the word list, removing invalid words.
    '''
    word_list = []
    with open('words.txt', 'r') as f:

        for line in f:
            if re.match("^[a-z]+$", line[:-1]) and len(line[:-1]) > 2:
                word_list.append(line[:-1])

    with open('filtered_words.txt', 'w') as f:
        for item in word_list:
            f.write("%s\n" % item)

def find_longest_word():
    '''
    Finds the longest word in the filtered word list.

    Returns:
        longest_word |<str>| The longest string in 'filtered_words.txt'.
    '''
    longest_word = ''
    with open('filtered_words.txt', 'r') as f:

        for line in f: 
            if len(line) > len(longest_word):
                longest_word = line

    return longest_word

def filter_length_3():
    '''
    Creates a file of words of length 3.
    '''
    with open('new/filtered_words.txt', 'r') as f:
        with open('new/filtered_words_3.txt', 'w') as f2:
            for line in f: 
                if len(line) == 4:
                    f2.write(line)
