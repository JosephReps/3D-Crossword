"""
Selects word to fill the puzzle-grid.
"""
import random
from copy import deepcopy, copy
from intersection_table import load_obj

INTERSECTION_TABLE = load_obj('intersection_table')
LENGTH_TABLE = load_obj('length_table')
FULL_CONSTRAINT_TABLE = load_obj('full_constraint_3_5')

def get_combined_grid_setup(grid_setup):
    '''
    Returns a list of all wordspaces, disregarding orientation.

    Parameters:
        grid_setup | <dict><str>:<list><int> | Dictionary containing all wordspaces.

    Returns:
        combined_setup | <list><int> | A list containing each 'active' grid square.
    '''
    combined_setup = []
    for row_col_leo in grid_setup:
        combined_setup += [each_wordspace for each_wordspace in grid_setup[row_col_leo]]

    return combined_setup

def get_longest_word(grid_setup):
    '''
    Given a dictionary of lists of word spaces, determines
    the longest wordspace. If there are multiple longest word spaces, 
    returns random selection from them.

    Parameters:
        grid_setup | <dict><str>:<list><int> | Dictionary containing all wordspaces.

    Returns:
        longest_word_space | <list><int> | Longest wordspace (List of grid squares
                                                              which make up wordspace).
    '''
    combined_setup = get_combined_grid_setup(grid_setup)

    longest_word_space = [[0]]
    for each_wordspace in combined_setup:
        if len(each_wordspace) > len(longest_word_space[0]):
            longest_word_space = [each_wordspace]

        elif len(each_wordspace) == len(longest_word_space[0]):
            longest_word_space.append(each_wordspace)

    return random.choice(longest_word_space)

def get_current_intersections(word_space, letters):
    '''
    Checks whether a word space intersects with a
    square which already has a letter in it.

    Parameters:
        wordspace | <list><int> | A list of square numbers which make up the word space.
        letters | <dict><int>:<str> | A dictionary which contains square numbers as keys
                                      and corresponding characters as values.

    Returns:
        intersecting_squares | <list><int> | A list of grid squares which intersect from 
                                             word_space. 
    '''
    intersecting_squares = []
    for each_square in word_space:
        if each_square in letters:
            intersecting_squares.append(each_square)

    return intersecting_squares

def create_constraint_key(wordspace, constraints, letters):
    '''
    Creates a constraint key from given constraints.

    Parameters:
        wordspace | <list><int> | A list of square numbers which make up the word space.
        letters | <dict><int>:<str> | A dictionary which contains square numbers as keys
                                      and corresponding characters as values.
        constraints | <list><int> | A list of squares which have intersected, therefore becoming
                                    a constraint.

    Returns: 
        constraint_key | <str> | A string where '_' represents a position in a wordspace which 
                                 can be any character, and all other characters represent 
                                 characters which are already present (due to intersections).
                                 
    '''
    constraint_key = ['_']*len(wordspace)

    if constraints:
        for constraint in constraints:
            constraint_key[wordspace.index(constraint)] = letters[constraint]

    return ("").join(constraint_key)

# I don't like how I've used longest word here but it was convinient. If this was
# not a personal project, I would definitley change this.
def update_letters(letters, longest_word, selected_word):
    '''
    Updates letters with new letters/squares from selected word.

    Parameters:
        letters | <dict><int>:<str> | A dictionary which contains square numbers as keys
                                      and corresponding characters as values.
        longest_word_space | <list><int> | Longest wordspace (in this case it is the wordspace
                                           we have already selected to fill).
        selected_word | <str> | The word we have chosen to fill the selected wordspace (longest_word).

    Returns:
        letters | <dict><int>:<str> | A dictionary which contains square numbers as keys
                                      and corresponding characters as values.
    '''
    for each_square in longest_word:

        letters[each_square] = selected_word[longest_word.index(each_square)]

    return letters

# Definitley a better way to do this.
def update_grid_setup(longest_word, grid_setup):
    '''
    Updates the grid setup by removing the wordspace we have just filled.

    Parameters:
        longest_word_space | <list><int> | Longest wordspace (in this case it is the wordspace
                                           we have already selected to fill).
        grid_setup | <dict><str>:<list><int> | Dictionary containing all wordspaces.
    
    Returns:
        grid_setup | <dict><str>:<list><int> | Dictionary containing all wordspaces.
    '''
    if longest_word in grid_setup['columns']:
        grid_setup['columns'].remove(longest_word)
    elif longest_word in grid_setup['rows']:
        grid_setup['rows'].remove(longest_word)
    elif longest_word in grid_setup['hoes']:
        grid_setup['hoes'].remove(longest_word)
    
    return grid_setup


def select_word(grid_setup, letters, used_words):
    '''
    Selects the best possible (see Readme for how I've defined 'best possible') word 
    for a given wordspace, taking into account current constraints, from a wordlist.

    Parameters:
        grid_setup | <dict><str>:<list><int> | Dictionary containing all wordspaces.
        letters | <dict><int>:<str> | A dictionary which contains square numbers as keys
                                      and corresponding characters as values.
        used_words | <list><str> | A list of words which have been used, or unsuccessful 
                                   during the solve. 

    Returns: 
        letters | <dict><int>:<str> | A dictionary which contains square numbers as keys
                                    and corresponding characters as values.
    '''
    letters = deepcopy(letters)
    used_words = copy(used_words)
    longest_word = get_longest_word(grid_setup)

    intersecting_squares = get_current_intersections(longest_word, letters)

    constraint_key = create_constraint_key(longest_word, intersecting_squares, letters)

    potential_words = [word for word in FULL_CONSTRAINT_TABLE[constraint_key] if word not in used_words]
    # print(len(potential_words))
    selected_word = None
    if potential_words:
        if intersecting_squares:
            selected_word = optimize_word_selection(potential_words, longest_word, grid_setup)

        else:
            selected_word = random.choice(potential_words)

        # print(selected_word)

        used_words.append(selected_word)

        letters = update_letters(letters, longest_word, selected_word)

        grid_setup = update_grid_setup(longest_word, grid_setup)

    if selected_word:
        return [letters, used_words, grid_setup]
    else:
        return [longest_word, intersecting_squares]


def optimize_word_selection(potential_words, longest_word, grid_setup):
    '''
    Determines the best possible word from a list of potential words.

    Parameters:
        potential_words | <list><str> | A list of word which fit the wordspace (longest_word) constraints.  
        longest_word_space | <list><int> | Longest wordspace (in this case it is the wordspace
                                           we have already selected to fill).
        grid_setup | <dict><str>:<list><int> | Dictionary containing all wordspaces.

    Returns:
        max(potential_word_dict) | <str> | The best possible word from potential_words.
    '''
    empty_neighbours = get_empty_neighbours(grid_setup, longest_word)

    potential_word_dict = {}
    for each_word in potential_words:
        potential_word_dict[assign_word_value(each_word, empty_neighbours, longest_word)] = each_word

    return potential_word_dict[max(potential_word_dict.keys())]

def get_empty_neighbours(grid_setup, word_space):
    '''
    Returns the wordspaces which intersect with selected wordspace
    and have not yet been filled.

    Parameters:
        grid_setup <dict>{str:<list>[int]}: Dictionary containing the wordspaces
                                            of all the columns, rows and ....
        wordspace <list><int>: A list of square numbers which make up the word space.
    
    Returns:
        neighbours | <list><list><int> | A list of wordspaces which have not been filled
                                         and intersect with current word_space (the one
                                         we are trying to fill right now).
    '''
    combined_setup = get_combined_grid_setup(grid_setup)

    neighbours = []
    for each_wordspace in combined_setup:
        if bool(set(each_wordspace) & set(word_space)):
            if each_wordspace != word_space:
                neighbours.append(tuple(each_wordspace))

    return neighbours

# Multiply rather than add so as to ensure the maximum 'balance'.
def assign_word_value(each_word, empty_neighbours, longest_word):
    '''
    Assigns a value to each_word based on the probability of the puzzle being
    succsefully solved given the selection.

    Parameters:
        each_word | <str> | A word from the list of potential words which fit 
                            the constraints of the current wordspace (the wordspace
                            we are trying to fill right now).
        empty_neighbours | <list><list><int> | A list of wordspaces which have not been filled
                                         and intersect with current word_space (the one
                                         we are trying to fill right now).
        longest_word_space | <list><int> | Longest wordspace (in this case it is the wordspace
                                           we have already selected to fill).

    Returns:
        value | <int> | A value which determines the 'quality' of each_word. Higher = better.
    '''
    neighbour_intersections = {}

    for neighbour in empty_neighbours:
        neighbour_intersections[neighbour] = [square for square in neighbour if square in longest_word][0]

    value = 0
    for neighbour in empty_neighbours:
        constraint_key = create_neigbour_key(neighbour, neighbour_intersections[neighbour], each_word)

        value *= len(FULL_CONSTRAINT_TABLE[constraint_key])

    return value

def create_neigbour_key(wordspace, constraint, each_word):
    # Lazy docu
    '''
    Creates a contraint key for each neighbour.
    See create_constraint_key() for more information.
    '''
    constraint_key = ['_']*len(wordspace)
    constraint = wordspace.index(constraint)

    constraint_key[constraint] = each_word[constraint]

    return ('').join(constraint_key)
