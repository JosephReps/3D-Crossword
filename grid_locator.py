"""
Locates word-spaces in a given grid.
"""
GRID_SIZE = 3
TEST_GRID = [0,1,2,3,6,7,8,9,11,15,17,18,20,21,24,26]

def search_rows(grid):
    '''
    Searches for word-spaces in the 'across' direction.
    '''
    local_square = 0

    potential_row = []
    rows = []
    rows_squares = []

    edge_squares = []
    edge_square = -1
    for each_square in range(GRID_SIZE**2):
        edge_square += GRID_SIZE
        edge_squares.append(edge_square)
    
    for square in range(GRID_SIZE**GRID_SIZE):
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


def search_columns(grid):
    '''
    Searches for word-spaces in the 'down' direction.
    '''
    local_square = 0

    potential_column = []
    columns = []
    columns_squares = []

    # We don't need to iterate over last to layers of the puzzle
    # as we are searching 'down' and the words must be >2 length.
    for square in range(GRID_SIZE**GRID_SIZE - (GRID_SIZE**2)*2):
        local_square = square
        while local_square in grid: #squares[local_square].active
            if local_square not in columns_squares: 
                potential_column.append(local_square)
                local_square += GRID_SIZE**2
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

def search_leos(grid):
    '''
    Searches for word-spaces in the 'leo' direction.
    '''
    local_square = 0

    potential_leo = []
    leos = []
    leos_squares = []

    first_layer_edge_squares = []
    edge_squares = []
    for i in range(GRID_SIZE):
        first_layer_edge_squares.append(GRID_SIZE**2 - i - 1)

    for each_square in first_layer_edge_squares:
        for layer in range(GRID_SIZE):
            edge_squares.append(each_square + layer*(GRID_SIZE**2))

    for square in range(GRID_SIZE**GRID_SIZE):
        local_square = square
        while local_square in grid: #squares[local_square].active
            if local_square not in leos_squares: 
                potential_leo.append(local_square)
                if local_square in edge_squares:
                    break

                local_square += GRID_SIZE

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

def locate_grid(grid):
    '''
    Locates grid (word-spaces of columns/rows/...).
    '''
    grid_setup = {'columns':[], 'rows':[], 'leos':[]}

    grid_setup['columns'] += search_columns(grid)
    grid_setup['rows'] += search_rows(grid)
    grid_setup['leos'] += search_leos(grid)

    return grid_setup

def get_layer_squares(grid):
    '''
    '''
    current_layer = 1

    layers = {}
    for each_layer in range(GRID_SIZE):
        layers[current_layer] = list(range((GRID_SIZE**2)*current_layer))
        current_layer += 1

    return layers

print(get_layer_squares(TEST_GRID))


