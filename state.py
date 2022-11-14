#
# state.py (Final project)
#
# A State class for the Eight Puzzle
#
# name: Arya Patel
# email: aryaxrp@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

from board import *

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###

# Problem 1
    def __init__(self, board, predecessor, move):
        '''constructs a new State object'''
        self.board = board
        self.predecessor = predecessor
        self.move = move
        if self.predecessor == None:
            self.num_moves = 0
        else: self.num_moves = predecessor.num_moves + 1
        
# Problem 2
    def is_goal(self):
        '''returns True if the called State object is a goal state, and False otherwise'''
        return self.board.tiles == GOAL_TILES
        
# Problem 3
    def generate_successors(self):
        '''creates and returns a list of State objects for all successor states of the called State object.'''
        successors = []
        for x in range(4):
            b = self.board.copy()
            if b.move_blank(MOVES[x]) == True:
                s = State(b, self, MOVES[x])
                successors += [s]
        return successors

# Problem 7
    def print_moves_to(self):
        ''' print the sequence of moves in the reverse order – from the initial state to the called State object.'''
        if self.num_moves == 0:
            print('initial state:')
            print(self.board)
        else:
            self.predecessor.print_moves_to()
            x = self.move + ':'
            print('move the blank', x)
            print(self.board)
        

    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True
    
    
    
    
    
    
    
    
    
    
    
    
    
    
