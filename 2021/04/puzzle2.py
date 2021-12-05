inputfile = open("input.txt", "r")
rawfilecontent = inputfile.readlines()
filecontent = []
for line in rawfilecontent:
    filecontent.append(line.removesuffix("\n"))

inputnumbers = [int(number) for number in filecontent[0].split(',')]
boards = []

def make_board(boardlines):
    board = []
    assert len(boardlines) == 5
    for line in boardlines:
        for number in line.split():
            board.append((int(number.removesuffix(' ').removeprefix(' ')), False))
    boards.append(board)

def mark_number_on_board(number, board):
    for i in range(len(board)):
        cell = list(board[i])
        if(cell[0] == number and not cell[1]):
            cell[1] = True
            board[i] = tuple(cell)

def mark_number(number):
    for board in boards:
        mark_number_on_board(number, board)

def check_board(board):
    # check horizontal
    for i in range(0, 25, 5):
        _, marked1 = board[i]
        _, marked2 = board[i + 1]
        _, marked3 = board[i + 2]
        _, marked4 = board[i + 3]
        _, marked5 = board[i + 4]
        if(marked1 and marked2 and marked3 and marked4 and marked5):
            return True
    # check vertical
    for i in range(5):
        _, marked1 = board[i]
        _, marked2 = board[5 + i]
        _, marked3 = board[10 + i]
        _, marked4 = board[15 + i]
        _, marked5 = board[20 + i]
        if(marked1 and marked2 and marked3 and marked4 and marked5):
            return True
    return False

def check_boards():
    winningboards = len(boards)
    for board in boards:
        if(check_board(board)):
            winningboards -= 1
    return winningboards

def find_losing_board():
    for board in boards:
        if(not check_board(board)):
            return board

for i in range(2, len(filecontent) - 4, 6):
    make_board(filecontent[i:i+5])

assert boards[len(boards) - 1][0] == (57, False)

losingboard = None
winningnumber = -1
sumofunmarked = -1

for number in inputnumbers:
    mark_number(number)
    boardsleft = check_boards()
    if(boardsleft == 1):
        winningnumber = number
        losingboard = find_losing_board()
        sumofunmarked = 0
        for cellnumber, marked in losingboard:
            if(not marked):
                sumofunmarked += cellnumber
        break

winningnumberindex = inputnumbers.index(winningnumber)
for i in range(winningnumberindex + 1, len(inputnumbers)):
    mark_number_on_board(inputnumbers[i], losingboard)
    if(check_board(losingboard)):
        winningnumber = inputnumbers[i]
        break

sumofunmarked = 0
for cellnumber, marked in losingboard:
    if(not marked):
        sumofunmarked += cellnumber


print(losingboard)
print(sumofunmarked)
print(winningnumber)
print(sumofunmarked * winningnumber)
