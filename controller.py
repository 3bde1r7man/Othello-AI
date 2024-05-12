import move


class OthelloController:
    def __init__(self, players):
        self.board = OthelloController.init_board()
        self.players = players
        self.current_player_index = 0

    @staticmethod
    def init_board():
        return [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 2, 0, 0, 0],
                [0, 0, 0, 2, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]
                ]
    
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
    
    def play_turn(self):
        player = self.players[self.current_player_index]
        move_valid = False
        
        while not move_valid:
            row, col = player.make_move(self.board)
            move_valid = move.validMove(self.board, row, col, player)
            if move_valid:
                self.board = move.getMove(self.board, row, col, player)
            else:
                print("Invalid move, try again.")
        
        self.switch_player()
        self.check_game_end()
    
    def check_game_end(self):
        if not self.board.has_valid_moves(self.players[0].color) and not self.board.has_valid_moves(self.players[1].color):
            print("Game Over")
            self.board.calculate_scores()
    
    def run(self):
        while True:
            self.play_turn()
            if self.check_game_end():
                break

# Example usage
# players = [HumanPlayer('Black'), ComputerPlayer('White')]
# game = OthelloController(board, players)
# game.run()
