TEST = False

def puzzle(filecontent):
    onefourseveneight = 0
    for line in filecontent:
        patterns, code = line.split('|')[0].strip().split(), line.split('|')[1].strip().split()
        for digit in code:
            if(len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7):
                onefourseveneight += 1
    print(onefourseveneight)
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