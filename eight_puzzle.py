#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: Arya Patel
# email: aryaxrp@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Shruti Gajjar
# partner's email: shrutiga@bu.edu
#

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
            
            
            
# Problem 1
def process_file(filename, algorithm, param):
    '''takes in a file, algorithm and its paramater. Processes the digitstring in the file to report the 
    number of moves, number of states tested, number of puzzles solves, average number of states tested and average 
    number of moves in the solutions'''
    f = open(filename, 'r')
    moves_average = 0
    solved = 0
    tested_average = 0
    for line in f:
        line = line[:-1]
    
        init_board = Board(line)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)
        
        if searcher == None:
            return
        soln = None
        try:
            soln = searcher.find_solution(init_state)
        
            if soln == None:
                print(line +  ':' + ' no solution')
            else:
                solved += 1
                moves_average += soln.num_moves
                tested_average += searcher.num_tested
                print(line + ': ' + str(soln.num_moves) + ' moves, ' + str(searcher.num_tested) + ' states tested ')

        except KeyboardInterrupt:
            print(line + ': ' + 'search terminated, no solution')
        
        
    print()

    if solved > 0:
        print('solved', str(solved), 'puzzles')
        print('averages: ', str(moves_average/solved), ' moves, ', str(tested_average/solved), ' stated tested')
    else:
        print('solved 0 puzzles')
        
        
        
        
        
        
        
        
        

