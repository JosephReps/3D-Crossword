# 3D-Crossword

# [LIVE DEMO](http://li2085-168.members.linode.com/)

# Disclaimer:
This is a personal project. There are a couple functions which are slightly complex as a result of this. I've kept the documentation fairly clear. 

# The main puzzle solving action can be found in:
 - [puzzle_solver.py](https://github.com/JosephReps/3D-Crossword/blob/master/puzzle_solver.py)
 - [word_selector.py](https://github.com/JosephReps/3D-Crossword/blob/master/word_selector.py)
 
 
# How it works:
 - Create a stack which will contain partial solutions.

 - At each iteration of the solve, we select the longest wordspace.
   (This helps reach local minimums as fast as possible so we dont waste as much time reaching dead ends).
 
 - We then determine the constraints of the wordspace (intersections + length).
 
 - Using these constraints we find a list of possible words.
   (This is done using a full-constraint hash table makes this constant time).
   
 - Using 'one-step-lookahead' we determine the best word from the list of potential words. 
   (See [this paper](https://www.researchgate.net/publication/224362845_A_Fully_Automatic_Crossword_Generator) for more information on this process).
   
 - Update the grid, used words, and wordspaces.
 
 - Save this as a partial solution on the stack.
 
 - If we reach a local minimum (no possible words), use 'selective-backjumping' to back track to the source of the problem.
   (See [this paper](https://www.aaai.org/Papers/AAAI/1999/AAAI99-023.pdf) for more information on this process).
   
 - If the allocated solve time expires or we fill all the wordspaces, return the last partial solution from the stack.
 

# Whats next:

 - Adding random grid generation will not only be a nice feature for users, it will allow us to properly benchmark our crosswords, to      get a better idea of the impact of changes to the algorithm.
 
 - Restrict wordlist to only use most common english words (currently contains large amount of obscure words + abbr.)
 
 
