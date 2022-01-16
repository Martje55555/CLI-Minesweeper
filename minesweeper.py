import random

# let's create a board object to represent the game
class Board:
    def __init__(self, dim_size, num_bombs):
        # parameters
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #create the board & plant bombs
        self.board = self.make_new_board(self)

        #initialize a set to keep track of which locations
        #we've uncovered, saving (row, col) tuples into this set
        self.dug = set() # if we dig at 0,0, then self.dug = {(0,0)}

        def make_new_board(self):
            # construct a new board based on the dim size and num bombs
            # we should construct the list of lists here
            #generate new board
            board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

            bombs_planted = 0
            while bombs_planted < self.num_bombs:
                loc = random.randint(0, self.dim_size**2 - 1) # random int N such that a <= N <= b
                row = loc // self.dim_size
                col = loc % self.dim_size

                if board[row][col] == '*':
                    # bomb already here
                    continue
                board[row][col] = '*'
                bombs_planted += 1

            return board
        
        def assign_values_to_empty_board(self):
            for r in range(self.dim_size):
                for c in range(self.dim_size):
                    if self.board[r][c] == '*':
                        continue
                    self.board[r][c] = self.get_num_neighboring_bombs(r,c)

        def get_num_neighboring_bombs(self, row, col):
            num_neighboring_bombs = 0
            for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                    if r == row and c == col:
                        continue
                    if self.board[r][c] == '*':
                        num_neighboring_bombs += 1
            return num_neighboring_bombs

        pass

# play the game
def playGame(dim_size = 10, num_bombs = 10):
    #Step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)
    #Step 2: show the user the board and ask for where they want to dig
    
    #Step 3a: if location is a bomb, show game over message
    #Step 3b: if location is not a bomb, dig recursively until each
    # square is at least next to a bomb
    
    #Step 4: repeat steps 2 and 3a/b until there are no more places to dig
    # -> VICTORY!!!
    pass 