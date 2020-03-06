"""
Solves crossword puzzles.
"""
# from grid_display import display_grid_to_console
from grid_locator import locate_grid
from copy import deepcopy
import word_selector
import time

# Example grid and size
# g = [0, 1, 2, 3, 4, 5, 7, 9, 10, 12, 14, 15, 17, 19, 20, 21, 22, 23, 24, 25, 27, 29, 
#       45, 49, 50, 51, 52, 53, 54, 55, 57, 59, 60, 61, 62, 63, 64, 65, 67, 69, 70, 71, 72, 
#       73, 74, 75, 77, 78, 79, 95, 97, 99, 100, 101, 102, 103, 104, 105, 107, 109, 110, 112, 
#       114, 115, 117, 119, 120, 121, 122, 123, 124, 47]
# s = 5

def solve_puzzle(grid, grid_size, allocated_time, benchmarking=False):
    '''
    Attempts to solve a 3D crossword puzzle grid within an allocated time.

    Algorithm explanation can be found in the Readme.

    Parameters:
        grid_size |<int>| The size of the grid.
        grid |<list><int>| List of active (white) grid square numbers.
        allocated_time |<int>| The amount of time allocated for the puzzle 
                               to solve the given grid.

    Returns:
        letters |<dict><int><str>| A dictionary which contains square numbers as keys
                                   and corresponding characters as values.
    '''
    letters = {}
    used_words = []
    grid_setup = locate_grid(grid, grid_size)
    best_solution = [[0]]

    partial_stack = [[deepcopy(letters), used_words, grid_setup]]

    start_time = time.clock()
    while grid_setup['columns'] or grid_setup['rows'] or grid_setup['hoes']:

        new_partial_solution = word_selector.select_word(deepcopy(partial_stack[-1][2]), partial_stack[-1][0], partial_stack[-1][1])
        
        # Success
        if len(new_partial_solution) == 3:
            partial_stack.append(new_partial_solution)
            if len(new_partial_solution[0]) > len(best_solution[0]):
                best_solution = new_partial_solution

        # Failure
        elif len(new_partial_solution) == 2:
            
            for each_solution in reversed(partial_stack):
                
                # Remove solutions until we reach problem area
                if set(new_partial_solution[1]).intersection(each_solution[0].keys()):
                    last_removed_solution = each_solution
                    partial_stack.remove(each_solution)

                else:
                    # Make sure to not re use the word giving us problem
                    partial_stack[-1][1] = last_removed_solution[1]
                    break

        if len(partial_stack) > 0:
            if len(partial_stack[-1]) > 2:
                grid_setup = partial_stack[-1][2]

        if time.clock() > start_time + allocated_time:
            # print(best_solution)
            if benchmarking:
                return 0
                
            return best_solution[0]

    # print("solved")
    if benchmarking:
        return 1

    return partial_stack[-1][0]


# display_grid_to_console(solve_puzzle(g, s, 5), s)
