TEST = False

# A = Rock
# B = Paper
# C = Scissors
# X = Lose
# Y = Draw
# Z = Win
# A-C -> Opponent
# X-Z -> Me

# Scores:
# Rock = 1, Paper = 2, Scissors = 3
# Lose = 0, Draw = 3, Win = 6

ROCK = 1
PAPER = 2
SCISSORS = 3
LOSE = 0
DRAW = 3
WIN = 6

def get_score(opponent, me):
    if(opponent == 'A'):
        if(me == 'X'):
            return SCISSORS + LOSE
        elif(me == 'Y'):
            return ROCK + DRAW
        elif(me == 'Z'):
            return PAPER + WIN
    elif(opponent == 'B'):
        if(me == 'X'):
            return ROCK + LOSE
        elif(me == 'Y'):
            return PAPER + DRAW
        elif(me == 'Z'):
            return SCISSORS + WIN
    elif(opponent == 'C'):
        if(me == 'X'):
            return PAPER + LOSE
        elif(me == 'Y'):
            return SCISSORS + DRAW
        elif(me == 'Z'):
            return ROCK + WIN
    return 0

def puzzle(filecontent):
    score = 0
    for line in filecontent:
        (opponent, me) = line.split(' ')
        score += get_score(opponent, me)
    print(score)

def test():
    testfile = open("test.txt", "r")
    content = testfile.read().splitlines()
    puzzle(content)

if(TEST):
    test()
else:
    inputfile = open("input.txt", "r")
    filecontent = inputfile.read().splitlines()
    puzzle(filecontent)