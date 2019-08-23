"""
Locates word-spaces in a given grid.
"""
GRID_SIZE = 5
TEST_GRID = [0,1,2,3,4,5,7,9,10,11,12,13,14,15,17,19,20,21,22,23,24,
             25,27,29,35,37,39,45,47,49,
             50,51,52,53,54,55,57,59,60,61,62,63,64,65,67,69,70,71,72,73,74,
             75,77,79,85,87,89,95,97,99,
             100,101,102,103,104,105,107,109,110,111,112,113,114,115,117,119,120,121,122,123,124,
            ]

def search_rows(grid, grid_size):
    '''
    Searches for word-spaces in the 'across' direction.
    '''
    local_square = 0

    potential_row = []
    rows = []
    rows_squares = []

    edge_squares = []
    edge_square = -1
    for each_square in range(grid_size**2):
        edge_square += grid_size
        edge_squares.append(edge_square)
    
    for square in range(grid_size**grid_size):
        local_square = square
        while local_square in grid: #squares[local_square].active
            if local_square not in rows_squares: 
                potential_row.append(local_square)
                if local_square in edge_squares:
                    break

                local_square += 1

            else:
                break

        if len(potential_row) >= 3:
            # print(f"appended{potential_row}")
            rows.append(potential_row)
            rows_squares += potential_row
            potential_row = []

        else:
            potential_row = []

    return rows

def search_columns(grid, grid_size):
    '''
    Searches for word-spaces in the 'down' direction.
    '''
    local_square = 0

    potential_column = []
    columns = []
    columns_squares = []

    # We don't need to iterate over last to layers of the puzzle
    # as we are searching 'down' and the words must be >2 length.
    for square in range(grid_size**grid_size - (grid_size**2)*2):
        local_square = square
        while local_square in grid: #squares[local_square].active
            if local_square not in columns_squares: 
                potential_column.append(local_square)
                local_square += grid_size**2
            else:
                break

        if len(potential_column) >= 3:
            # print(f"appended{potential_column}")
            columns.append(potential_column)
            columns_squares += potential_column
            potential_column = []

        else:
            potential_column = []


    return columns

def search_leos(grid, grid_size):
    '''
    Searches for word-spaces in the 'leo' direction.
    '''
    local_square = 0

    potential_leo = []
    leos = []
    leos_squares = []

    first_layer_edge_squares = []
    edge_squares = []
    for i in range(grid_size):
        first_layer_edge_squares.append(grid_size**2 - i - 1)

    for each_square in first_layer_edge_squares:
        for layer in range(grid_size):
            edge_squares.append(each_square + layer*(grid_size**2))

    for square in range(grid_size**grid_size):
        local_square = square
        while local_square in grid: #squares[local_square].active
            if local_square not in leos_squares: 
                potential_leo.append(local_square)
                if local_square in edge_squares:
                    break

                local_square += grid_size

            else:
                break

        if len(potential_leo) >= 3:
            # print(f"appended{potential_leo}")
            leos.append(potential_leo)
            leos_squares += potential_leo
            potential_leo = []

        else:
            potential_leo = []

    return leos

def locate_grid(grid, grid_size):
    '''
    Locates grid (word-spaces of columns/rows/...).
    '''
    grid_setup = {'columns':[], 'rows':[], 'leos':[]}

    grid_setup['columns'] += search_columns(grid, grid_size)
    grid_setup['rows'] += search_rows(grid, grid_size)
    grid_setup['leos'] += search_leos(grid, grid_size)

    return grid_setup

def get_layer_squares(grid_size):
    '''
    '''
    current_layer = 1

    layers = {}
    for each_layer in range(grid_size):
        layers[current_layer] = list(range(each_layer*(grid_size**2), (grid_size**2)*current_layer))
        current_layer += 1

    return layers

# print(locate_grid(TEST_GRID, GRID_SIZE))

