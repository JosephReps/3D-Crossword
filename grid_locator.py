"""
Locates word-spaces in a given grid.
"""
# Could probably clean this up
def search_rows(grid, grid_size):
    '''
    Searches for word-spaces in the 'across' direction in a grid.

    Parameters:
        grid_size |<int>| The size of the grid.
        grid |<list><int>| List of active (white) grid square numbers.

    Returns:
        rows |<list><list><int>| A 2D array containing rows, made up of grid
                                 grid square numbers.
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
            rows.append(potential_row)
            rows_squares += potential_row
            potential_row = []

        else:
            potential_row = []

    return rows

def search_columns(grid, grid_size):
    '''
    Searches for word-spaces in the 'down' direction.

    Parameters:
        grid_size |<int>| The size of the grid.
        grid |<list><int>| List of active (white) grid square numbers.

    Returns:
        rows |<list><list><int>| A 2D array containing columns, made up of grid
                                 grid square numbers.
    '''
    local_square = 0

    potential_column = []
    columns, columns_squares = [], []

    for square in range(grid_size**grid_size - (grid_size**2)*2):
        local_square = square
        while local_square in grid: 
            if local_square not in columns_squares: 
                potential_column.append(local_square)
                local_square += grid_size**2
            else:
                break

        if len(potential_column) >= 3:
            columns.append(potential_column)
            columns_squares += potential_column
        
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

def search_hoes(grid, grid_size):
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
    hoes = []
    hoes_squares = []

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
            hoes.append(potential_hoe)
            hoes_squares += potential_hoe
        
        potential_hoe = []

    return hoes

def locate_grid(grid, grid_size):
    '''
    Locates grid (word-spaces of columns/rows/hoes).

    Parameters:
        grid_size |<int>| The size of the grid.

    Returns:
        grid_setup |<dict><list><list><int>| A dict containing the structure
                                             of the puzzle.
                                            
    '''
    grid_setup = {'columns':[], 'rows':[], 'hoes':[]}

    grid_setup['columns'] += search_columns(grid, grid_size)
    grid_setup['rows'] += search_rows(grid, grid_size)
    grid_setup['hoes'] += search_hoes(grid, grid_size)

    return grid_setup

def get_layer_squares(grid_size):
    '''
    Locates the squares corresponding to each 'layer' (horizontal) of
    the puzzle.

    Parameters:
        grid_size |<int>| The size of the grid.
    
    Returns:
        layers |<dict><list><int>| A dict containing list of square numbers
                                   corresponding to each layer (key).
    '''
    current_layer = 1

    layers = {}
    for each_layer in range(grid_size):
        layers[current_layer] = list(range(each_layer*(grid_size**2), (grid_size**2)*current_layer))
        current_layer += 1

    return layers




