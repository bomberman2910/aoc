TEST = False

def puzzle(filecontent):
    elfcalories = []
    currentcalories = 0
    for line in filecontent:
        if (line == ''):
            elfcalories.append(currentcalories)
            currentcalories = 0
        else:
            currentcalories += int(line)
    elfcalories.append(currentcalories)
    print(max(elfcalories))

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