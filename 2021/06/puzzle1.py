TEST = False

def puzzle(filecontent):
    fishstrings = filecontent[0].split(',')
    fishes = [int(i) for i in fishstrings]
    for i in range(80):
        newfishes = 0
        for i, e in enumerate(fishes):
            if(e == 0):
                fishes[i] = 6
                newfishes += 1
            else:
                fishes[i] -= 1
        for i in range(newfishes):
            fishes.append(8)
    print(len(fishes))
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