TEST = False

def flash_wave(r, c, octopusses):
    flashed = []
    for i, j in ((r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), 
                 (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)):
        if 0 <= i < 10 and 0 <= j < 10 and octopusses[i][j] != 10:
            octopusses[i][j] += 1
            if octopusses[i][j] == 10:
                flashed.append((i, j))
    return flashed

def puzzle(filecontent):
    octopusses = [[int(char) for char in list(line)] for line in filecontent]
    flashes = 0
    steps = 0

    while True:
        flashed = []
        for r in range(10):
            for c in range(10):
                octopusses[r][c] += 1
                if octopusses[r][c] == 10:
                    flashed.append((r, c))
        for (r, c) in flashed:
            flashed += flash_wave(r, c, octopusses)
        flashes += len(flashed)
        steps += 1
    
        if steps == 100:
            pt1_flashes = flashes
    
        if all(sum(row) == 100 for row in octopusses):
            print(pt1_flashes, steps)
            return
        for r, c in flashed:
            octopusses[r][c] = 0

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