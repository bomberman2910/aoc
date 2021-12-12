TEST = True

def puzzle(filecontent):
    flashes = 0
    octopusses = [[(int(char), False) for char in list(line)] for line in filecontent]
    STEPS = 100
    for _ in range(STEPS):
        # reset flashes and do initial increment
        for y in range(octopusses):
            for x in range(octopusses[y]):
                lightlevel, _ = octopusses[y][x]
                octopusses[y][x] = (lightlevel + 1, False)
        # increase all lightlevels by one
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