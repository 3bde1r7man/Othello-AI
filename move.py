
import copy

# check if the move is in bounds of the board
def inBounds(x, y):
    if x >= 0 and x <= 7 and y >= 0 and y <= 7:
        return True
    return False

# check if the move is valid for the player and adjacent to the opponent
def validMove(Board, x, y, player):
    if inBounds(x, y) and Board[x][y] == 0:
        if x - 1 >= 0 and Board[x - 1][y] != 0 and Board[x - 1][y] != player: # check up
            return True
        if x + 1 <= 7 and Board[x + 1][y] != 0 and Board[x + 1][y] != player: # check down
            return True
        if y - 1 >= 0 and Board[x][y - 1] != 0 and Board[x][y - 1] != player: # check left
            return True
        if y + 1 <= 7 and Board[x][y + 1] != 0 and Board[x][y + 1] != player: # check right
            return True
    return False

# flip the opponent's pieces
def flipUp(Board, x, y, player):
    count = 0
    for i in range(x - 1, 0, -1):
        if Board[i][y] == player:
            if(count == (x - 1) - i ):
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
    moves = getAllMoves(Board, 1)
    for move in moves:
        for i in range(8):
            print(move[i])
        print()

def main():
    # testGetMove()
    testGetAllMoves()

if __name__ == '__main__':
    main()