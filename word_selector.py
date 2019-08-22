"""
Selects word to fill the puzzle-grid.
"""
from grid_locator import locate_grid

GRID_SIZE = 3
TEST_GRID = [0,1,2,3,6,7,8,9,11,15,17,18,20,21,24,26]

GRID_SETUP = locate_grid(TEST_GRID)

def longest_empty_word(grid_setup):
    '''
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

    with open('filtered_words.txt', 'r') as f:
        



print(longest_empty_word(GRID_SETUP))