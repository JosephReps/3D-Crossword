"""
Selects word to fill the puzzle-grid.
"""
import random
from grid_locator import locate_grid
from grid_display import display_grid_to_console

GRID_SIZE = 5
TEST_GRID = [0,1,2,3,4,5,7,9,10,11,12,13,14,15,17,19,20,21,22,23,24,
             25,27,29,35,37,39,45,47,49,
             50,51,52,53,54,55,57,59,60,61,62,63,64,65,67,69,70,71,72,73,74,
             75,77,79,85,87,89,95,97,99,
             100,101,102,103,104,105,107,109,110,111,112,113,114,115,117,119,120,121,122,123,124,
            ]

def get_longest_word(grid_setup):
    '''
    Given a dictionary of lists of word spaces, determines
    the longest wordspace.
    '''
    combined_setup = []
    for row_col_leo in grid_setup:
        combined_setup += [each_wordspace for each_wordspace in grid_setup[row_col_leo]]

    longest_word_space = []
    for each_wordspace in combined_setup:
        if len(each_wordspace) > len(longest_word_space):
            longest_word_space = each_wordspace

    return longest_word_space

def select_word():
    '''
    '''
    letters = {}
    potential_words = []
    used_words = []
    filled_wordspaces = []

    grid_setup = locate_grid(TEST_GRID, GRID_SIZE)

    while grid_setup['columns'] or grid_setup['rows'] or grid_setup['leos']:

        longest_word = get_longest_word(grid_setup)

        intersecting_squares = check_wordspace_intersections(longest_word, letters)
        # print(intersecting_squares)

        with open('filtered_words.txt', 'r') as f:
            for each_word in f:

                # Last char is newline
                if each_word not in used_words:
                    if len(each_word[:-1]) == len(longest_word):
                        if intersecting_squares:
                            if check_word_fits(longest_word, letters, each_word, intersecting_squares):
                                potential_words.append(each_word[:-1])
                        else:
                            potential_words.append(each_word[:-1])

        if potential_words:
            selected_word = random.choice(potential_words)
        else:
            selected_word = None
        if selected_word:
            used_words.append(selected_word)
            potential_words = []
            print(selected_word)
            for each_square in longest_word:
                letters[each_square] = selected_word[longest_word.index(each_square)]

            if longest_word in grid_setup['columns']:
                filled_wordspaces.append([-1] + longest_word)
                grid_setup['columns'].remove(longest_word)
            elif longest_word in grid_setup['rows']:
                filled_wordspaces.append([-2] + longest_word)
                grid_setup['rows'].remove(longest_word)
            elif longest_word in grid_setup['leos']:
                filled_wordspaces.append([-3] + longest_word)
                grid_setup['leos'].remove(longest_word)
            else:
                break

        else:
            print("Removing last word")
            # print(filled_wordspaces)
            remove_previous_word(letters, grid_setup, filled_wordspaces)

    return letters

def check_wordspace_intersections(word_space, letters):
    '''
    Checks whether a word space intersects with a
    square which already has a letter in it.
    '''
    intersecting_squares = []
    for each_square in word_space:
        if each_square in letters:
            intersecting_squares.append(each_square)

    return intersecting_squares

def check_word_fits(word_space, letters, word, intersecting_squares):
    '''
    Checks whether a word will fit into a wordspace,
    and format with other already-filled intersecting squares
    appropriatley.
    '''
    word_fits = True
    for each_square in intersecting_squares:
        if letters[each_square] != word[word_space.index(each_square)]:
            word_fits = False
            break

    return word_fits

def remove_previous_word(letters, grid_setup, filled_wordspaces):
    '''
    Removes last word that was entered into puzzle.
    '''
    last_word = filled_wordspaces[-1]

    last_intersecting = []
    for each_wordspace in filled_wordspaces[:-1]:
        for each_square in each_wordspace:
            if each_square in last_word:
                last_intersecting.append(each_square)

    for each_square in last_word[1:]:
        if each_square not in last_intersecting:
            del letters[each_square]

    if last_word[0] == -1:
        grid_setup['columns'].append(last_word[1:])
    if last_word[0] == -2:
        grid_setup['rows'].append(last_word[1:])
    else:
        grid_setup['leos'].append(last_word[1:])

    filled_wordspaces.remove(last_word)

    # print("Removed last word")

display_grid_to_console(select_word(), GRID_SIZE)
