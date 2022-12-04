TEST = False

def puzzle(filecontent):
    overlapping = 0
    for pair in filecontent:
        elf1, elf2 = pair.split(',')
        elf1_start, elf1_end = elf1.split('-')
        elf2_start, elf2_end = elf2.split('-')
        if((int(elf1_start) >= int(elf2_start) and int(elf1_end) <= int(elf2_end)) or (int(elf2_start) >= int(elf1_start) and int(elf2_end) <= int(elf1_end))):
            overlapping += 1
    print(overlapping)


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