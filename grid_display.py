"""
Displays the crossword grid.
"""
from math import sqrt  
from grid_locator import get_layer_squares

def display_grid_to_console(letters, grid_size):
    '''
    Displays the puzzle grid to the console, printing each layer
    seperatley.

    Parameters:
        grid_size |<int>| The size of the grid.
        letters |<dict><int><str>| A dictionary which contains square numbers as keys
                                   and corresponding characters as values.
    '''
    layer_squares = get_layer_squares(grid_size)

    for each_layer in layer_squares:
        for each_square in layer_squares[each_layer]:
            if each_square in letters:
                layer_squares[each_layer][
                              layer_squares[each_layer].index(each_square)] = letters[each_square]

            else:
                layer_squares[each_layer][layer_squares[each_layer].index(each_square)] = ' '

    for each_layer in layer_squares:
        print(f"\nLAYER {each_layer}----")

        row = 0
        for each_row in range(1, int(sqrt(len(layer_squares[each_layer]))) + 1):
            print(layer_squares[each_layer][row:each_row*grid_size])
            row = each_row*grid_size

