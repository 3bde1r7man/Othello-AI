
import copy

# check if the move is in bounds of the board
def inBounds(x, y):
    if x >= 0 and x <= 7 and y >= 0 and y <= 7:
        return True
    return False

# check if the move is valid for the player and adjacent to the opponent
def validMove(Board, x, y, player):
    if inBounds(x, y) and Board[x][y] == 0 and (checkFlipDown(Board, x, y, player) or checkFlipUp(Board, x, y, player) or checkFlipLeft(Board, x, y, player) or checkFlipRight(Board, x, y, player)):
        if x - 1 >= 0 and Board[x - 1][y] != 0 and Board[x - 1][y] != player: # check up
            return True
        if x + 1 <= 7 and Board[x + 1][y] != 0 and Board[x + 1][y] != player: # check down
            return True
        if y - 1 >= 0 and Board[x][y - 1] != 0 and Board[x][y - 1] != player: # check left
            return True
        if y + 1 <= 7 and Board[x][y + 1] != 0 and Board[x][y + 1] != player: # check right
            return True
    return False

def checkFlipUp(Board, x, y, player):
    count = 0
    for i in range(x - 1, 0, -1):
        if Board[i][y] == player:
            if(count == (x - 1) - i):
                return True
            return False
        elif Board[i][y] != 0 and Board[i][y] != player:
            count += 1
    return False

def checkFlipDown(Board, x, y, player):
    count = 0
    for i in range(x + 1, 7):
        if Board[i][y] == player:
            if(count == i - (x + 1)):
                return True
            return False
        elif Board[i][y] != 0 and Board[i][y] != player:
            count += 1
    return False

def checkFlipLeft(Board, x, y, player):
    count = 0
    for i in range(y - 1, 0, -1):
        if Board[x][i] == player:
            if(count == (y - 1) - i):
                return True
            return False
        elif Board[x][i] != 0 and Board[x][i] != player:
            count += 1
    return False

def checkFlipRight(Board, x, y, player):
    count = 0
    for i in range(y + 1, 7):
        if Board[x][i] == player:
            if(count == i - (y + 1)):
                return True
            return False
        elif Board[x][i] != 0 and Board[x][i] != player:
            count += 1
    return False

# flip the opponent's pieces
def flipUp(Board, x, y, player):
    count = 0
    for i in range(x - 1, 0, -1):
        if Board[i][y] == player:
            if(count == (x - 1) - i):
                for j in range(i, x):
                    Board[j][y] = player
                break
        elif Board[i][y] != 0 and Board[i][y] != player:
            count += 1
    return Board

def flipDown(Board, x, y, player):
    count = 0
    for i in range(x + 1, 7):
        if Board[i][y] == player:
            if(count == i - (x + 1)):
                for j in range(x, i):
                    Board[j][y] = player
                break
        elif Board[i][y] != 0 and Board[i][y] != player:
            count += 1
    return Board

def flipLeft(Board, x, y, player):
    count = 0
    for i in range(y - 1, 0, -1):
        if Board[x][i] == player:
            if(count == (y - 1) - i):
                for j in range(i, y):
                    Board[x][j] = player
                break
        elif Board[x][i] != 0 and Board[x][i] != player:
            count += 1
    return Board

def flipRight(Board, x, y, player):
    count = 0
    for i in range(y + 1, 7):
        if Board[x][i] == player:
            if(count == i - (y + 1)):
                for j in range(y, i):
                    Board[x][j] = player
                break
        elif Board[x][i] != 0 and Board[x][i] != player:
            count += 1
    return Board

# get the new board after the move
def getMove(Board, x, y, player):
    newBoard = copy.deepcopy(Board)
    if validMove(newBoard, x, y, player):
        newBoard[x][y] = player
        newBoard = flipUp(newBoard, x, y, player)
        newBoard = flipDown(newBoard, x, y, player)
        newBoard = flipLeft(newBoard, x, y, player)
        newBoard = flipRight(newBoard, x, y, player)
    return newBoard


# get all possible moves for the player
def getAllMoves(Board, player):
    moves = []
    for i in range(8):
        for j in range(8):
            if validMove(Board, i, j, player):
                moves.append(getMove(Board, i, j, player))
    return moves


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
    newBoard = getMove(Board, 2, 3, 1)
    print("X = 2, Y = 3, Player = 1")
    for i in range(8):
        print(newBoard[i])
    print()
    print("X = 2, Y = 4, Player = 1")
    newBoard = getMove(Board, 2, 4, 1)
    for i in range(8):
        print(newBoard[i])
    print()
    print("X = 3, Y = 2, Player = 1")
    newBoard = getMove(Board, 3, 2, 1)
    for i in range(8):
        print(newBoard[i])
    print()
    print("X = 3, Y = 5, Player = 1")
    newBoard = getMove(Board, 3, 5, 1)
    for i in range(8):
        print(newBoard[i])
    print()
    print("X = 4, Y = 2, Player = 1")
    newBoard = getMove(Board, 4, 2, 1)
    for i in range(8):
        print(newBoard[i])
    print()
    print("X = 4, Y = 5, Player = 1")
    newBoard = getMove(Board, 4, 5, 1)
    for i in range(8):
        print(newBoard[i])
    print()


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
    moves = getAllMoves(Board, 2)
    for move in moves:
        for i in range(8):
            print(move[i])
        print()


infinity = 1000000000
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
def AlphaBeta(move, levels, is_max, alpha, beta, originalBoard, oldAlphaOrBeta, bestMove):
    player = 2
    if is_max:
        player =1    
    moves = getAllMoves(move, player)
    if levels == 0 or len(moves) == 0:
        return utility_fun(move)

    if is_max: 
        maxValue = -infinity
        for childMove in moves:
            value = AlphaBeta(childMove, levels - 1, False, alpha, beta, originalBoard, oldAlphaOrBeta, bestMove)
            maxValue = max(maxValue, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break
    
            if are_2d_lists_equal(move, originalBoard):
                if oldAlphaOrBeta == -infinity:
                    bestMove.clear()
                    bestMove.extend(childMove)
                    oldAlphaOrBeta = alpha
                    
                elif alpha > oldAlphaOrBeta:
                    bestMove.clear()
                    bestMove.extend(childMove)
                    oldAlphaOrBeta = alpha
                    
        return maxValue
    else:
        minValue = infinity
        for childMove in moves:
            value = AlphaBeta(childMove, levels - 1, True, alpha, beta, originalBoard, oldAlphaOrBeta, bestMove)
            minValue = min(minValue, value)
            beta = min(beta, value)
            if beta <= alpha:
                break
            
            if are_2d_lists_equal(move, originalBoard):
                if oldAlphaOrBeta == infinity:
                    bestMove.clear()
                    bestMove.extend(childMove)
                    oldAlphaOrBeta = beta
                    
                elif beta < oldAlphaOrBeta:
                    bestMove.clear()
                    bestMove.extend(childMove)
                    oldAlphaOrBeta = beta
                    
        return minValue

def testAlphaBeta():
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
    bestMove =copy.deepcopy(Board)
    
    AlphaBeta(Board, 3, False, -infinity, infinity, Board, infinity, bestMove )
    print("when depth is 3, best move for white player is ")
    for i in range(8):
        print(bestMove[i])
    print()
    
    AlphaBeta(Board, 3, True, -infinity, infinity, Board, -infinity, bestMove )
    print("when depth is 3, best move for black player is ")
    for i in range(8):
        print(bestMove[i])
    print()

    AlphaBeta(Board, 5, True, -infinity, infinity, Board, -infinity, bestMove )
    print("when depth is 5, best move for black player is ")
    for i in range(8):
        print(bestMove[i])
    print()

def main():
    # testGetMove()
    #testGetAllMoves()
    testAlphaBeta()

if __name__ == '__main__':
    main()