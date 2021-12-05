TEST = False

def puzzle(filecontent):
    floor = 0
    position = 1
    for i in filecontent[0]:
        if(i == '('):
            floor += 1
        else:
            floor -= 1
        if(floor == -1):
            break
        position += 1
    print(floor)
    print(position)
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