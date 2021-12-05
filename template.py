TEST = True

def puzzle(filecontent):
    pass

def test():
    testfile = open("test.txt", "r")
    content = testfile.readlines().splitlines()
    puzzle(content)

if(TEST):
    test()
else:
    inputfile = open("input.txt", "r")
    filecontent = inputfile.readlines().splitlines()
    puzzle(filecontent)