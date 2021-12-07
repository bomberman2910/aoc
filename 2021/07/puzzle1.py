TEST = False

def puzzle(filecontent):
    positions = [int(i) for i in filecontent[0].split(',')]
    maxposition = max(positions)
    minposition = min(positions)
    print(minposition, maxposition)
    fuelperposition = [0 for _ in range(maxposition + 1)]
    for i in range(minposition, maxposition + 1):
        fuelperposition[i] = sum([sum([j for j in range(abs(pos - i) + 1)]) for pos in positions])
    print(min(fuelperposition))
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