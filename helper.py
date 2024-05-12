import copy
class Helper:
    infinity = 1000000000
    negative_infinity = -1000000000

    # check if the move is in bounds of the board
    @staticmethod
    def inBounds(x, y):
        if x >= 0 and x <= 7 and y >= 0 and y <= 7:
            return True
        return False

    # check if the move is valid for the player and adjacent to the opponent
    @staticmethod
    def validMove(Board, x, y, player):
        if Helper.inBounds(x, y) and Board[x][y] == 0 and (Helper.checkFlipDown(Board, x, y, player) or Helper.checkFlipUp(Board, x, y, player) or Helper.checkFlipLeft(Board, x, y, player) or Helper.checkFlipRight(Board, x, y, player)):
            if x - 1 >= 0 and Board[x - 1][y] != 0 and Board[x - 1][y] != player: # check up
                return True
            if x + 1 <= 7 and Board[x + 1][y] != 0 and Board[x + 1][y] != player: # check down
                return True
            if y - 1 >= 0 and Board[x][y - 1] != 0 and Board[x][y - 1] != player: # check left
                return True
            if y + 1 <= 7 and Board[x][y + 1] != 0 and Board[x][y + 1] != player: # check right
                return True
        return False

    @staticmethod
    def checkFlipUp(Board, x, y, player):
        count = 0
        for i in range(x - 1, -1, -1):
            if Board[i][y] == player:
                if(count == (x - 1) - i and count != 0):
                    return True
                return False
            elif Board[i][y] != 0 and Board[i][y] != player:
                count += 1
        return False
    @staticmethod
    def checkFlipDown(Board, x, y, player):
        count = 0
        for i in range(x + 1, 8):
            if Board[i][y] == player:
                if(count == i - (x + 1) and count != 0):
                    return True
                return False
            elif Board[i][y] != 0 and Board[i][y] != player:
                count += 1
        return False
    @staticmethod
    def checkFlipLeft(Board, x, y, player):
        count = 0
        for i in range(y - 1, -1, -1):
            if Board[x][i] == player:
                if(count == (y - 1) - i and count != 0):
                    return True
                return False
            elif Board[x][i] != 0 and Board[x][i] != player:
                count += 1
        return False
    @staticmethod
    def checkFlipRight(Board, x, y, player):
        count = 0
        for i in range(y + 1, 8):
            if Board[x][i] == player:
                if(count == i - (y + 1) and count != 0):
                    return True
                return False
            elif Board[x][i] != 0 and Board[x][i] != player:
                count += 1
        return False

    # flip the opponent's pieces
    @staticmethod
    def flipUp(Board, x, y, player):
        count = 0
        for i in range(x - 1, -1, -1):
            if Board[i][y] == player:
                if(count == (x - 1) - i and count != 0):
                    for j in range(i, x):
                        Board[j][y] = player
                    break
            elif Board[i][y] != 0 and Board[i][y] != player:
                count += 1
        return Board
    
    @staticmethod
    def flipDown(Board, x, y, player):
        count = 0
        for i in range(x + 1, 8):
            if Board[i][y] == player:
                if(count == i - (x + 1) and count != 0):
                    for j in range(x, i):
                        Board[j][y] = player
                    break
            elif Board[i][y] != 0 and Board[i][y] != player:
                count += 1
        return Board
    @staticmethod
    def flipLeft(Board, x, y, player):
        count = 0
        for i in range(y - 1, -1, -1):
            if Board[x][i] == player:
                if(count == (y - 1) - i and count != 0):
                    for j in range(i, y):
                        Board[x][j] = player
                    break
            elif Board[x][i] != 0 and Board[x][i] != player:
                count += 1
        return Board

    @staticmethod
    def flipRight(Board, x, y, player):
        count = 0
        for i in range(y + 1, 8):
            if Board[x][i] == player:
                if(count == i - (y + 1) and count != 0):
                    for j in range(y, i):
                        Board[x][j] = player
                    break
            elif Board[x][i] != 0 and Board[x][i] != player:
                count += 1
        return Board

    # get the new board after the move
    @staticmethod
    def getMove(Board, x, y, player):
        newBoard = copy.deepcopy(Board)
        if Helper.validMove(newBoard, x, y, player):
            newBoard[x][y] = player
            newBoard = Helper.flipUp(newBoard, x, y, player)
            newBoard = Helper.flipDown(newBoard, x, y, player)
            newBoard = Helper.flipLeft(newBoard, x, y, player)
            newBoard = Helper.flipRight(newBoard, x, y, player)
        return newBoard


    # get all possible moves for the player
    @staticmethod
    def getAllMoves(Board, player):
        moves = []
        for i in range(8):
            for j in range(8):
                if Helper.validMove(Board, i, j, player):
                    moves.append(Helper.getMove(Board, i, j, player))
        return moves

    @staticmethod
    def testGetMove():
        Board = [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 2, 0, 0, 0],
                [0, 0, 0, 2, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]
                ]
        for i in range(8):
            print(Board[i])
        print()
        newBoard = Helper.getMove(Board, 2, 3, 1)
        print("X = 2, Y = 3, Player = 1")
        for i in range(8):
            print(newBoard[i])
        print()
        print("X = 2, Y = 4, Player = 1")
        newBoard = Helper.getMove(Board, 2, 4, 1)
        for i in range(8):
            print(newBoard[i])
        print()
        print("X = 3, Y = 2, Player = 1")
        newBoard = Helper.getMove(Board, 3, 2, 1)
        for i in range(8):
            print(newBoard[i])
        print()
        print("X = 3, Y = 5, Player = 1")
        newBoard = Helper.getMove(Board, 3, 5, 1)
        for i in range(8):
            print(newBoard[i])
        print()
        print("X = 4, Y = 2, Player = 1")
        newBoard = Helper.getMove(Board, 4, 2, 1)
        for i in range(8):
            print(newBoard[i])
        print()
        print("X = 4, Y = 5, Player = 1")
        newBoard = Helper.getMove(Board, 4, 5, 1)
        for i in range(8):
            print(newBoard[i])
        print()

    @staticmethod
    def testGetAllMoves():
        Board = [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 2, 0, 0, 0],
                [0, 0, 0, 2, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]
                ]
        for i in range(8):
            print(Board[i])
        print()
        moves = Helper.getAllMoves(Board, 2)
        for move in moves:
            for i in range(8):
                print(move[i])
            print()

    @staticmethod
    def utility_fun(Board):
        black_count = 0
        white_count = 0
        for i in range(len(Board)):
            for j in range(len(Board[0])):
                if Board[i][j] == 1: #black
                    black_count += 1
                elif Board[i][j] == 2: #white
                    white_count += 1

        return black_count - white_count

    @staticmethod
    def are_2d_lists_equal(list1, list2):
        # Check if the lists have the same dimensions
        if len(list1) != len(list2) or len(list1[0]) != len(list2[0]):
            return False
        
        # Iterate through each element and compare
        for i in range(len(list1)):
            for j in range(len(list1[0])):
                if list1[i][j] != list2[i][j]:
                    return False
        
        # If all elements are equal, return True
        return True

    # Max is always set to represent the black player.
    # initial values for:
    # - move: the current board state,
    # - levels: the depth of the search,
    # - is_max: indicates whether it's the maximizing player's turn (True for black, False for white),
    # - alpha: the best value found so far for the maximizing player its initial value is negative infinity,
    # - beta: the best value found so far for the minimizing player its initial value is infinity,
    # - originalBoard: always equals the initial board state before any moves,
    # - oldAlphaOrBeta: the value of the best found alpha or beta, depending on the type of player (black or white),
    # - bestMove: initially equals the current board state; if there is a valid move, it will represent the best move found.

    # Max we will make it always to be for the black player 
    # initial values for:
        # move is Board, levels are depth of search, alpha is negative infinity, beta ,
        # originalBoard always equals the initial Board before any moves,
        # oldAlphaOrBeta is the value of best found alpha or beta depends on the type of player black or white,
        # bestMove is initialy equals board then if there is a valid moves it will equal the best move of them.  
    @staticmethod
    def AlphaBeta(move, levels, is_max, alpha, beta, originalBoard, oldAlphaOrBeta, bestMove):
        player = 2
        if is_max:
            player =1    
        moves = Helper.getAllMoves(move, player)
        if levels == 0 or len(moves) == 0:
            return Helper.utility_fun(move)

        if is_max: 
            maxValue = Helper.negative_infinity
            for childMove in moves:
                value = Helper.AlphaBeta(childMove, levels - 1, False, alpha, beta, originalBoard, oldAlphaOrBeta, bestMove)
                maxValue = max(maxValue, value)
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
        
                if Helper.are_2d_lists_equal(move, originalBoard):
                    if oldAlphaOrBeta == Helper.negative_infinity:
                        bestMove.clear()
                        bestMove.extend(childMove)
                        oldAlphaOrBeta = alpha
                        
                    elif alpha > oldAlphaOrBeta:
                        bestMove.clear()
                        bestMove.extend(childMove)
                        oldAlphaOrBeta = alpha
                        
            return maxValue
        else:
            minValue = Helper.infinity
            for childMove in moves:
                value = Helper.AlphaBeta(childMove, levels - 1, True, alpha, beta, originalBoard, oldAlphaOrBeta, bestMove)
                minValue = min(minValue, value)
                beta = min(beta, value)
                if beta <= alpha:
                    break
                
                if Helper.are_2d_lists_equal(move, originalBoard):
                    if oldAlphaOrBeta == Helper.infinity:
                        bestMove.clear()
                        bestMove.extend(childMove)
                        oldAlphaOrBeta = beta
                        
                    elif beta < oldAlphaOrBeta:
                        bestMove.clear()
                        bestMove.extend(childMove)
                        oldAlphaOrBeta = beta
                        
            return minValue



def main():
    Helper.testGetMove()
    Helper.testGetAllMoves()

if __name__ == '__main__':
    main()