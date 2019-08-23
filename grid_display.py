"""
Displays the crossword grid.
"""
from grid_locator import get_layer_squares
from math import sqrt

## TEST DATA
GRID_SIZE = 5
TEST_GRID = [0,1,2,3,4,5,7,9,10,11,12,13,14,15,17,19,20,21,22,23,24,
             25,27,29,35,37,39,45,47,49,
             50,51,52,53,54,55,57,59,60,61,62,63,64,65,67,69,70,71,72,73,74,
             75,77,79,85,87,89,95,97,99,
             100,101,102,103,104,105,107,109,110,111,112,113,114,115,117,119,120,121,122,123,124,
            ]
            
LAYER_SQUARES = get_layer_squares(GRID_SIZE)

# LETTERS = {0: 'a', 9: 'a', 18: 'a', 
#             2: 'h', 11: 'a', 20: 'h', 
#             6: 'h', 15: 'a', 24: 'h', 
#             8: 'h', 17: 'a', 26: 'h', 
#             1: 'a', 7: 'a', 3: 'a', 21: 'a'
#             }
##

# print(LAYER_SQUARES)

def display_grid_to_console(letters, grid_size):
    '''
    Displays the puzzle grid to the console, printing each layer
    seperatley.
    '''
    for each_layer in LAYER_SQUARES:
        for each_square in LAYER_SQUARES[each_layer]:
            if each_square in letters:
                LAYER_SQUARES[each_layer][LAYER_SQUARES[each_layer].index(each_square)] = letters[each_square]

            else:
                LAYER_SQUARES[each_layer][LAYER_SQUARES[each_layer].index(each_square)] = ' '

    for each_layer in LAYER_SQUARES:
        print(f"\nLAYER {each_layer}----")

        row = 0
        for each_row in range(1, int(sqrt(len(LAYER_SQUARES[each_layer]))) + 1):
            print(LAYER_SQUARES[each_layer][row:each_row*grid_size])
            row = each_row*GRID_SIZE
        

# print(LAYER_SQUARES)
# display_grid_to_console(LETTERS, GRID_SIZE)
