TEST = False

def get_priority(c):
    if(c.islower()):
        return ord(c) - 96
    return ord(c) - 38

def puzzle(filecontent):
    prio_sum = 0
    for rucksack in filecontent:
        compartment1, compartment2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        prio_sum += get_priority(list(set(compartment1) & set(compartment2))[0])
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