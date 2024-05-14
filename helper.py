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
        if Helper.inBounds(x, y) and Board[x][y] == 0 and (Helper.checkFlipCol(Board, x, y, player, x - 1, -1, -1) or Helper.checkFlipCol(Board, x, y, player, x + 1, 8, 1) or Helper.checkFlipRow(Board, x, y, player, y - 1, -1, -1) or Helper.checkFlipRow(Board, x, y, player, y + 1, 8, 1)):
            if x - 1 >= 0 and Board[x - 1][y] != 0 and Board[x - 1][y] != player:
                return True
            if x + 1 <= 7 and Board[x + 1][y] != 0 and Board[x + 1][y] != player:
                return True
            if y - 1 >= 0 and Board[x][y - 1] != 0 and Board[x][y - 1] != player:
                return True
            if y + 1 <= 7 and Board[x][y + 1] != 0 and Board[x][y + 1] != player:
                return True
        return False
    
    @staticmethod
    def checkFlipRow(Board, x, y, player, i, j, inc):
        count = 0
        for k in range(i, j, inc):
            if Board[x][k] == player:
                if(count == abs(k - i) and count != 0):
                    return True
                return False
            elif Board[x][k] != 0 and Board[x][k] != player:
                count += 1
        return False
    
    @staticmethod
    def checkFlipCol(Board, x, y, player, i, j, inc):
        count = 0
        for k in range(i, j, inc):
            if Board[k][y] == player:
                if(count == abs(k - i) and count != 0):
                    return True
                return False
            elif Board[k][y] != 0 and Board[k][y] != player:
                count += 1
        return False
    
    @staticmethod
    def flipCol(Board, x, y, player, i, j, inc):
        count = 0
        for k in range(i, j, inc):
            if Board[k][y] == player:
                if(count == abs(k - i) and count != 0):
                    for l in range(i, k, inc):
                        Board[l][y] = player
                    break
            elif Board[k][y] != 0 and Board[k][y] != player:
                count += 1
        return Board
    
    @staticmethod
    def flipRow(Board, x, y, player, i, j, inc):
        count = 0
        for k in range(i, j, inc):
            if Board[x][k] == player:
                if(count == abs(k - i) and count != 0):
                    for l in range(i, k, inc):
                        Board[x][l] = player
                    break
            elif Board[x][k] != 0 and Board[x][k] != player:
                count += 1
        return Board

    # get the new board after the move
    @staticmethod
    def getMove(Board, x, y, player):
        newBoard = copy.deepcopy(Board)
        if Helper.validMove(newBoard, x, y, player):
            newBoard[x][y] = player
            newBoard = Helper.flipCol(newBoard, x, y, player, x - 1, -1, -1) # flip up
            newBoard = Helper.flipCol(newBoard, x, y, player, x + 1, 8, 1) # flip down
            newBoard = Helper.flipRow(newBoard, x, y, player, y - 1, -1, -1) # flip left
            newBoard = Helper.flipRow(newBoard, x, y, player, y + 1, 8, 1) # flip right
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
    def check_winner(Board):
        res = Helper.utility_fun(Board)
        if res > 0:
            return "Black is winner!"
        elif res < 0:
            return "White is winner!"
        else:
            return "Draw!"

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

