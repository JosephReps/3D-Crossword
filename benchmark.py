"""
Tests crossword algorithm efficiency against multiple grid setups.
"""
import time
from puzzle_solver import solve_puzzle
# from collections import defaultdict
import json

def benchmark_algorithm(iterations=10):
    '''
    '''
    successful = 0
    times = []
    with open('grids/3/3_10.json') as f:
        grids = json.load(f)

    for grid in grids["10"]:
        
        for _ in range(iterations):
            start_time = time.clock()
            solved = solve_puzzle(grid, 3, 5)
            exec_time = time.clock() - start_time

            if solved:
                times.append(exec_time)
                successful += 1
            
    print("Attempted: ", len(grids["10"]))
    print("Successful: ", successful)

    print("Average time of success: ", sum(times)/len(times))

    return times


with open(f'benchmark_results/3.json', 'w') as fp:
    json.dump(benchmark_algorithm(), fp)

# benchmark_algorithm()


