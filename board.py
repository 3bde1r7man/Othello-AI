class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(8)] for _ in range(8)]
        self.black = 30
        self.white = 30
        self.initialize_board()

    def initialize_board(self):
        self.grid[3][3] = 2
        self.grid[3][4] = 1
        self.grid[4][3] = 1
        self.grid[4][4] = 2
        # pass

    def make_move(self, x, y, color):
        # Update board state after move
        pass
