"""
Generates random crossword grids.
"""
import itertools
import json

# STILL IN PROGRESS# STILL IN PROGRESS
# STILL IN PROGRESS
# STILL IN PROGRESS
# STILL IN PROGRESS

def generate_random_grids(grid_size, number_empty_squares):
    '''
    Generates a list of valid grids.

    Parameters:
        grid_size |<int>| Size of the puzzle grid.
        number_empty_squares |<int>| Number of empty (black) squares.

    Returns:
        filtered_grids |<list**2><int>| A list of lists containing all potential valid grids.
    '''
    unfiltered_grids = generate_unfiltered_grids(grid_size, number_empty_squares)
    print(len(unfiltered_grids))

    filtered_grids = filter_grids(grid_size, unfiltered_grids)

    return filtered_grids

def generate_unfiltered_grids(grid_size, number_empty_squares):
    '''
    Generates all possible permutations of the list of grid squares
    with respect to number of empty squares constraint. 

    Parameters:
        grid_size |<int>| Size of the puzzle grid.
        number_empty_squares |<int>| Number of empty (black) squares.

    Returns:
        permutations_list |<list**2><int>| A list of lists containing all possible permutations of the 
                                           list of grid squares with respect to number of empty squares 
                                           constraint. 
    '''
    nes_permutations_list = set(itertools.combinations(range(grid_size**grid_size), grid_size**grid_size - number_empty_squares))

    if number_empty_squares > 0:
        nes_minus_1_permutations_list = set(itertools.combinations(range(grid_size**grid_size), grid_size**grid_size - number_empty_squares + 1))
        exclusive_permutations_list = nes_permutations_list - nes_minus_1_permutations_list

        return exclusive_permutations_list

    return nes_permutations_list


def filter_grids(grid_size, unfiltered_grids):
    '''
    An invalid grid consists of having a wordspace < 3 squares long. 
    
    Parameters:
        grid_size |<int>| Size of the puzzle grid.

    Returns:
        valid_grids |<list**2><int>| A list of lists containing all potential valid grids.
    '''
    valid_grids = [grid for grid in unfiltered_grids if is_valid_grid(grid_size, grid)]

    return valid_grids

def is_valid_grid(grid_size, grid):
    '''
    Determines whether a grid is valid (all wordspaces are >3 in length).

    Parameters:
        grid_size |<int>| Size of the puzzle grid.
        grid |<list><int>| List of active (white) grid square numbers.

    Returns:
        True if valid.
        False if not valid.
    '''
    rows = valid_rows(grid_size, grid)
    hoes = valid_hoes(grid_size, grid)
    columns = valid_columns(grid_size, grid)

    if any(type(i) == bool for i in [rows, hoes, columns])\
        or all(bool(i) == False for i in [rows, hoes, columns]):
        return False

    return True

def valid_rows(grid_size, grid):
    '''
    '''
    local_square = 0

    potential_row = []
    rows = []
    rows_squares = []

    edge_squares = []
    edge_square = -1
    for _ in range(grid_size**2):
        edge_square += grid_size
        edge_squares.append(edge_square)
    
    for square in range(grid_size**grid_size):
        local_square = square
        while local_square in grid: 
            if local_square not in rows_squares: 
                potential_row.append(local_square)
                if local_square in edge_squares:
                    break

                local_square += 1

            else:
                break

        if len(potential_row) >= 3:
            rows_squares += potential_row
            rows.append(potential_row)
            potential_row = []

        elif len(potential_row) == 2:
            return False

        else:
            potential_row = []

    return rows

def valid_columns(grid_size, grid):
    '''
    '''
    local_square = 0

    potential_column = []
    columns_squares = []
    columns = []

    for square in range(grid_size**grid_size):
        local_square = square
        while local_square in grid: 
            if local_square not in columns_squares: 
                potential_column.append(local_square)
                local_square += grid_size**2
            else:
                break

        if len(potential_column) >= 3:
            columns_squares += potential_column
            columns.append(potential_column)

        elif len(potential_column) == 2:
            return False

        potential_column = []

    return columns

def locate_hoe_edge_squares(grid_size):
    '''
    Locates all edge squares relative to hoe direction.

    Parameters:
        grid_size |<int>| The size of the grid.
        grid |<list><int>| List of active (white) grid square numbers.

    Returns:
        edge_squares |<list><int>| List of edge squares relative to hoe
                                  direction.
    '''
    first_layer_edge_squares = []
    edge_squares = []
    for i in range(grid_size):
        first_layer_edge_squares.append(grid_size**2 - i - 1)

    for each_square in first_layer_edge_squares:
        for layer in range(grid_size):
            edge_squares.append(each_square + layer*(grid_size**2))
    
    return edge_squares

def valid_hoes(grid_size, grid, ):
    '''
    Searches for word-spaces in the 'hoe' direction.

    Parameters:
        grid_size |<int>| The size of the grid.
        grid |<list><int>| List of active (white) grid square numbers.

    Returns:
        rows |<list><list><int>| A 2D array containing hoes, made up of grid
                                 grid square numbers.
    '''
    local_square = 0

    potential_hoe = []
    hoes_squares = []
    hoes = []

    edge_squares = locate_hoe_edge_squares(grid_size)

    for square in range(grid_size**grid_size):
        local_square = square
        while local_square in grid: 
            if local_square not in hoes_squares: 
                potential_hoe.append(local_square)
                if local_square in edge_squares:
                    break

                local_square += grid_size

            else:
                break

        if len(potential_hoe) >= 3:
            hoes_squares += potential_hoe
            hoes.append(potential_hoe)

        elif len (potential_hoe) == 2:
            return False

        potential_hoe = []

    return hoes

def save_grids(grid_size):
    '''
    Saves a dictionary of potential valid grids.

    Parameters:
        grid_size |<int>| The size of the grid.
    '''
    for i in range(12, grid_size**grid_size - 3):
        grid_dictionary = {}

        print(i)
        grid_dictionary[i] = generate_random_grids(grid_size, i)

        print(len(grid_dictionary[i]))

        with open(f'grids/3/{grid_size}_{i}.json', 'w') as fp:
            json.dump(grid_dictionary, fp)

    return grid_dictionary
    
# save_obj(save_grids(3), "potential_valid_grids_3")

save_grids(3)

# print(valid_columns(3, [3, 0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 4]))

















