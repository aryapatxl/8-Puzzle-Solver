#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Arya Patel
# email: aryaxrp@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Shruti Gajjar
# partner's email: shrutiga@bu.edu
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###

# Problem 1
    def __init__(self, depth_limit):
        ''' constructs a new Searcher object'''
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit

# Problem 2
    def add_state(self, new_state):
        '''takes a single State object called new_state and adds it to the 
        Searcher‘s list of untested states'''
        self.states += [new_state]

# Problem 3
    def should_add(self, state):
        '''takes a State object called state and returns True if the called 
        Searcher should add state to its list of untested states, and False otherwise'''
        if state.creates_cycle() == True:
            return False
        elif self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        return True

# Problem 4
    def add_states(self, new_states):
        '''takes a list State objects called new_states, and that processes the 
        elements of new_states one at a time if a given state s should be added to 
        the Searcher's list of untested states and if a given state s should not be added.'''
        for x in range(len(new_states)):
            if self.should_add(new_states[x]) == True:
                self.add_state(new_states[x])

                
# Problem 5
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s

# Problem 6
    def find_solution(self, init_state):
        '''performs a full state-space search that begins at the specified initial state init_state 
        and ends when the goal state is found or when the Searcher runs out of untested states'''
        self.add_state(init_state)
        while len(self.states) != 0:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())
        return None

    
    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


### Add your BFSeacher and DFSearcher class definitions below. ###

# Problem 1
class BFSearcher(Searcher):
    def next_state(self):
        '''Rather than choosing at random from the list of untested states, this 
        version of next_state should follow FIFO (first-in first-out) ordering – choosing 
        the state that has been in the list the longest.'''
        s = self.states[0]
        self.states.remove(s)
        return s
        
# Problem 2
class DFSearcher(Searcher):
    '''choosing one the untested states that has the largest depth (i.e., the largest number 
    of moves from the initial state).'''
    def next_state(self):
        s = self.states[-1]
        self.states.remove(s)
        return s
        
        
        
def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###
# Problem 1d
def h1(state):
    '''takes a State object called state, and that computes and returns an estimate of 
    how many additional moves are needed to get from state to the goal state. '''
    return state.board.num_misplaced()

# Problem 4
def h2(state):
    '''counts and returns the number of tiles who's row and/or col is in called Board object and not in the goal tiles'''
    count = 0
    
    for r in range(3):
        for c in range(3):
            if state.board.tiles[r][c] == '1':
                if r != 0:
                    count +=1
                if c != 1:
                    count += 1
            
            if state.board.tiles[r][c] == '2':
                if r != 0:
                    count +=1
                if c != 2:
                    count += 1
            
            if state.board.tiles[r][c] == '3':
                if r != 1:
                    count +=1
                if c != 0:
                    count += 1
                    
            if state.board.tiles[r][c] == '4':
                if r != 1:
                    count +=1
                if c != 1:
                    count += 1
            
            if state.board.tiles[r][c] == '5':
                if r != 1:
                    count +=1
                if c != 2:
                    count += 1
            
            if state.board.tiles[r][c] == '6':
                if r != 2:
                    count +=1
                if c != 0:
                    count += 1
                    
            if state.board.tiles[r][c] == '7':
                if r != 2:
                    count +=1
                if c != 1:
                    count += 1
            
            if state.board.tiles[r][c] == '8':
                if r != 2:
                    count +=1
                if c != 2:
                    count += 1
    return count
            

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###

# Problem 1b
    def __init__(self, heuristic):
        '''constructs a new GreedySearcher object.'''
        super().__init__(-1)

        self.heuristic = heuristic

# Problem 1c
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)

# Problem 1e
    def add_state(self, state):
        ''' adds a sublist that is a [priority, state] pair, where priority is the 
        priority of state that is determined by calling the priority method'''
        self.states += [[self.priority(state), state]]

# Problem 1f
    def next_state(self):
        '''chooses one of the states with the highest priority'''
        s = max(self.states)
        self.states.remove(s)
        return s[1]
        
    
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###

# Problem 2
class AStarSearcher(GreedySearcher):
        
    def priority(self, state):
        '''assigns a priority to a state, it also takes into account the cost that has 
        already been expended to get to that state'''
        return -1 * (self.heuristic(state) + state.num_moves)
    
    
    
    
    
    

