import copy


class Helper:

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
        for i in range(x - 1, 0, -1):
            if Board[i][y] == player:
                if(count == (x - 1) - i):
                    return True
                return False
            elif Board[i][y] != 0 and Board[i][y] != player:
                count += 1
        return False
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    
    @staticmethod
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
    @staticmethod
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

    @staticmethod
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

def main():
    Helper.testGetMove()
    Helper.testGetAllMoves()

if __name__ == '__main__':
    main()