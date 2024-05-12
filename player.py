class Player:
    def __init__(self, color, strategy):
        self.color = color
        self.strategy = strategy

    def make_move(self, board, params=None):
        return self.strategy.make_move(board)
