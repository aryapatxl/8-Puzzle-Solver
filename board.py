#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Arya Patel
# email: aryaxrp@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1
        
# Problem 1
        for c in range(3):
            for r in range(3):
                self.tiles[r][c] = digitstr[3*r + c]
                
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c
        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.


    ### Add your other method definitions below. ###
# Problem 2
    def __repr__(self):
        '''returns a string representation of a Board object.'''
        s = ''
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    s += '_ '
                else: s += self.tiles[r][c] + ' '
            s += '\n'
        return s
            
# Problem 3
    def move_blank(self, direction):
        '''that takes as input a string direction that specifies the direction in which the blank should move, 
        and that attempts to modify the contents of the called Board object accordingly.'''
        row = ''
        col = ''

        if direction not in 'downuprightleft':
            return False
        else:
            for r in range(3):
                for c in range(3):
                    if self.tiles[r][c] == '0':
                        row = r
                        col = c
            if direction == 'down':
                if row == 2:
                    return False
                else:
                    y = self.tiles[row+1][col]
                    self.tiles[row+1][col] = '0'
                    self.tiles[row][col] = y
                    self.blank_r = row + 1
                    self.blanl_c = col
                    return True
           
            if direction == 'up':
                if row == 0:
                    return False
                else:
                    y = self.tiles[row-1][col]
                    self.tiles[row-1][col] = '0'
                    self.tiles[row][col] = y
                    self.blank_r = row - 1
                    self.blanl_c = col
                    return True
            
            if direction == 'left':
                if col == 0:
                    return False
                else:
                    y = self.tiles[row][col-1]
                    self.tiles[row][col-1] = '0'
                    self.tiles[row][col] = y
                    self.blank_r = row
                    self.blank_c = col - 1
                    return True
                
            if direction == 'right':
                if col == 2:
                    return False
                else:
                    y = self.tiles[row][col+1]
                    self.tiles[row][col+1] = '0'
                    self.tiles[row][col] = y
                    self.blank_r = row
                    self.blanl_c = col + 1
                    return True

            else: return False

# Problem 4
    def digit_string(self):
        '''creates and returns a string of digits that 
        corresponds to the current contents of the called Board object’s 
        tiles attribute. '''
        s = ''
        for x in range(3):
            for y in range(3):
                s += self.tiles[x][y]
        return s
                
# Problem 5
    def copy(self):
        '''returns a newly-constructed Board object that is a deep copy 
        of the called object (i.e., of the object represented by self).'''
        copy1 = Board(self.digit_string())
        return copy1

# Problem 6
    def num_misplaced(self):
        '''counts and returns the number of tiles in the called Board object 
        that are not where they should be in the goal state.'''
        count = 0
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != '0':
                    if self.tiles[r][c] != GOAL_TILES[r][c]:
                        count += 1
                    
        return count

# Problem 7
    def __eq__(self, other):
        '''return True if the called object (self) and the argument (other) have 
        the same values for the tiles attribute, and False otherwise'''
        if self.tiles == other.tiles:
            return True
        else: return False
        
            
        
                        
    
                    
        































