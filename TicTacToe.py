import random
class Move:
    def __init__(self):
        self.position = -1
        self.score = 0

    def setPosition(self, position):
        self.position = position

    def setScore(self, score):
        self.score = score

    def __gt__(self, other):
        return self.score > other

    def __lt__(self, other):
        return self.score < other


player = "O"
computer = "X"
def printBoard(board):
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("     |     |")
    print()
    print()

def checkForMatch(board, player):
    if (board[0] == board[1] == board[2] == player or board[3] == board[4] == board[5] == player or
        board[6] == board[7] == board[8] == player or board[1] == board[4] == board[7] == player or
        board[2] == board[5] == board[8] == player or board[0] == board[4] == board[8] == player or
        board[2] == board[4] == board[6] == player):
        return True
    else:
        return False

def setBoard(board, position, player):
    board[position] = player

def getAvailableMoves(board):
    return [i for i in range(9) if board[i] not in ["X", "O"]]

def minMax(board, curPlayer):
    #print("CURRENT PLAYER = ", curPlayer)
    availableMoves = getAvailableMoves(board)
    #print("Available moves = ", availableMoves)

    if (checkForMatch(board, player)):
        endMove = Move()
        endMove.setScore(-10)
        return endMove
    elif (checkForMatch(board, computer)):
        endMove = Move()
        endMove.setScore(10)
        return endMove
    elif (len(availableMoves) == 0):
        endMove = Move()
        endMove.setScore(0)
        return endMove

    moves = []

    for position in availableMoves:
        #print("CHECKING POSITION = ", position)
        move = Move()
        move.setPosition(position)

        setBoard(board, position, curPlayer)
        #printBoard(board)

        if (curPlayer == player):
            highestValueMove = minMax(board, computer)
            #print("SCORE = ", highestValueMove.score)
            move.setScore(highestValueMove.score)
        else:
            highestValueMove = minMax(board, player)
            #print("SCORE = ", highestValueMove.score)
            move.setScore(highestValueMove.score)

        #print("END IF")
        setBoard(board, position, " ")
        #printBoard(board)
        moves.append(move)

    bestMove = []
    if curPlayer == player:
        score = 10000000
        for i in range(0, len(moves)):
            if moves[i].score == score:
                bestMove.append(i)
            if moves[i].score < score:
                bestMove = [i]
                score = moves[i].score
    else:
        score = -10000000
        for i in range(0, len(moves)):
            if moves[i].score == score:
                bestMove.append(i)
            elif moves[i].score > score:
                bestMove = [i]
                score = moves[i].score
    return moves[bestMove[random.randint(0, len(bestMove) - 1)]]

if __name__ == "__main__":
    board = [" " for i in range(9)]
    availablePositions = [i for i in range(9)]
    win = False
    currentPlayer = computer
    while not win and not all(i in ["X","O"] for i in board):
        printBoard(board)
        if currentPlayer == player:
            position = int(input("Enter Position "))
            while position not in availablePositions or position < 0 or position > 8:
                print("Available positions ", availablePositions )
                position = int(input("Invalid position. Enter again "))
            availablePositions[position] = " "
            setBoard(board, position, currentPlayer)
            win = checkForMatch(board, currentPlayer)
            currentPlayer = computer
        else:
            move = minMax(board, computer)
            setBoard(board, move.position, currentPlayer)
            availablePositions[move.position] = " "
            win = checkForMatch(board, currentPlayer)
            currentPlayer = player

    printBoard(board)
    if not win:
        print("It's a draw!")
    else:
        if (currentPlayer == player):
            print("Computer wins!")
        else:
            print("Player wins!")