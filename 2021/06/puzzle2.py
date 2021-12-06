from collections import Counter


TEST = False

def puzzle(filecontent):
    fishstrings = filecontent[0].split(',')
    fishes = [int(i) for i in fishstrings]
    popcount = []
    for i in range(9):
        popcount.append(fishes.count(i))

    for i in range(256):
        popcountnextday = [0 for _ in range(9)]
        for day in range(1, 9):
            popcountnextday[day - 1] = popcount[day]
        popcountnextday[8] = popcount[0]
        popcountnextday[6] += popcount[0]
        popcount = popcountnextday
    print(sum(popcount))
    pass

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