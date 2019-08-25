"""
Implements a hash table using python dictionary
to allow for quick access to words containing
specific characters at specific indexes.
"""
from string import ascii_lowercase
import collections
import pickle

def create_intersection_table():
    '''
    Creates a dictionary grouping words into character index position.
    Longest word in list is 31 (excluding longass one).
    '''
    intersection_table = collections.defaultdict(list)
    for each_index in range(31):
        for each_char in ascii_lowercase:
            with open('filtered_words.txt', 'r') as f:
                for line in f:
                    if len(line[:-1]) - 1 >= each_index:
                        if line[each_index] == each_char:
                            intersection_table[each_char 
                                                + '_'   
                                                + str(each_index)].append(line)

    return intersection_table

def create_length_table():
    '''
    Creates a dictionary grouping words by length.

    Words are saved with the newline char still included.
    '''
    length_table = collections.defaultdict(list)
    with open('filtered_words.txt', 'r') as f:
        for line in f:
            length_table[len(line[:-1])].append(line)
        
    return length_table

def save_obj(obj, name):
    '''
    Saves a python object to file.
    '''
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    '''
    Loads python object from file.
    '''
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

# save_obj(create_length_table(), 'length_table')
# intersection_table = load_obj('intersection_table')

# print(intersection_table['x_4'])
