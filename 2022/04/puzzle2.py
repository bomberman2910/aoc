TEST = False

def includes(start1, start2, end1, end2):
    return (int(start1) >= int(start2) and int(end1) <= int(end2)) or (int(start2) >= int(start1) and int(end2) <= int(end1))

def overlap_end1(start1, start2, end1, end2):
    return (int(end1) >= int(start2) and int(end1) < int(end2))

def overlap_end2(start1, start2, end1, end2):
    return (int(end2) >= int(start1) and int(end2) < int(end1))

def puzzle(filecontent):
    overlapping = 0
    for pair in filecontent:
        elf1, elf2 = pair.split(',')
        elf1_start, elf1_end = elf1.split('-')
        elf2_start, elf2_end = elf2.split('-')
        if(includes(elf1_start, elf2_start, elf1_end, elf2_end) or overlap_end1(elf1_start, elf2_start, elf1_end, elf2_end) or overlap_end2(elf1_start, elf2_start, elf1_end, elf2_end)):
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