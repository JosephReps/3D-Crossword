"""
Creates word list of valid words from the 'words.txt' file.
"""
import re

word_list = []
with open('words.txt', 'r') as f:
    i = 0

    for line in f:
        if re.match("^[a-z]+$", line[:-1]) and len(line[:-1]) > 2:
            word_list.append(line[:-1])

with open('filtered_words.txt', 'w') as f:
    for item in word_list:
        f.write("%s\n" % item)

