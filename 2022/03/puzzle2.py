TEST = False

def get_priority(c):
    if(c.islower()):
        return ord(c) - 96
    return ord(c) - 38

def puzzle(filecontent):
    prio_sum = 0
    for i in range(0, len(filecontent), 3):
        common_letter = list(set(filecontent[i])&set(filecontent[i+1])&set(filecontent[i+2]))[0]
        prio_sum += get_priority(common_letter)
    print(prio_sum)

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