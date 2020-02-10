"""
Implements a hash table using python dictionary
to allow for quick access to words containing
specific characters at specific indexes.
"""
from string import ascii_lowercase
from collections import defaultdict
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

# MASKS = {3:[], 4:[], 5:[]}
# LENGTH_TABLE = load_obj('length_table')

def generate_word_mask(mask, k): 
    '''
    '''
    n = len(mask)  
    generate_word_mask_rec(mask, "", n, k) 
  
def generate_word_mask_rec(mask, prefix, n, k): 
    '''
    '''  
    if (k == 0) : 
        MASKS[len(prefix)].append(prefix)
        return
  
    for i in range(n): 
        newPrefix = prefix + mask[i] 
        generate_word_mask_rec(mask, newPrefix, n, k - 1) 

def create_constraints(max_wordlength):
    '''
    '''
    constraint_table = defaultdict(list)

    for i in range(3, max_wordlength+1):
        generate_word_mask(['A','_'], i)

    for length in range(3, max_wordlength + 1):
        for word in LENGTH_TABLE[length]:
            for mask in MASKS[len(word[:-1])]:
                unmasked_word = list(word[:-1])
                for i in range(len(mask)):
                    if mask[i] == '_':
                        unmasked_word[i] = '_'
                    
                constraint_table[("").join(unmasked_word)].append(word[:-1])

    return constraint_table

# save_obj(create_constraints(5), "full_constraint_3_5")

# constraints = load_obj("full_constraint_3_5")


