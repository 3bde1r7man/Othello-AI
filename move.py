
import copy

def flipUp(Board, x, y, player):
    count = 0
    newBoard = copy.deepcopy(Board)
    for i in range(x - 1, 0, -1):
        if newBoard[i][y] == player:
            if(count == (x - 1) - i ):
                for j in range(i, x):
                    newBoard[j][y] = player
                break
        elif newBoard[i][y] != 0 and newBoard[i][y] != player:
            count += 1
    return newBoard

def flipDown(Board, x, y, player):
    count = 0
    newBoard = copy.deepcopy(Board)
    for i in range(x + 1, 7):
        if newBoard[i][y] == player:
            if(count == i - (x + 1)):
                for j in range(x, i):
                    newBoard[j][y] = player
                break
        elif newBoard[i][y] != 0 and newBoard[i][y] != player:
            count += 1
    return newBoard

def flipLeft(Board, x, y, player):
    count = 0
    newBoard = copy.deepcopy(Board)
    for i in range(y - 1, 0, -1):
        if newBoard[x][i] == player:
            if(count == (y - 1) - i):
                for j in range(i, y):
                    newBoard[x][j] = player
                break
        elif newBoard[x][i] != 0 and newBoard[x][i] != player:
            count += 1
    return newBoard

def flipRight(Board, x, y, player):
    count = 0
    newBoard = copy.deepcopy(Board)
    for i in range(y + 1, 7):
        if newBoard[x][i] == player:
            if(count == i - (y + 1)):
                for j in range(y, i):
                    newBoard[x][j] = player
                break
        elif newBoard[x][i] != 0 and newBoard[x][i] != player:
            count += 1
    return newBoard


def getMove(Board, x, y, player):
    newBoard = copy.deepcopy(Board)
    if newBoard[x][y] == 0:
        newBoard[x][y] = player
        newBoard = flipUp(newBoard, x, y, player)
        newBoard = flipDown(newBoard, x, y, player)
        newBoard = flipLeft(newBoard, x, y, player)
        newBoard = flipRight(newBoard, x, y, player)
    return newBoard



def getAllMoves(Board):
    moves = []
    for i in range(8):
        for j in range(8):
            if Board[i][j] == 0:
                moves.append(getMove(Board, i, j, 1))
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
    moves = getAllMoves(Board)
    for move in moves:
        for i in range(8):
            print(move[i])
        print()

def main():
    # testGetMove()
    testGetAllMoves()

if __name__ == '__main__':
    main()