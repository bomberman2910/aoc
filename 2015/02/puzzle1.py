TEST = False

def puzzle(filecontent):
    totalpaper = 0
    for box in filecontent:
        measurementstrings = box.split("x")
        width, length, height = int(measurementstrings[0]), int(measurementstrings[1]), int(measurementstrings[2])
        side1 = width * length
        side2 = width * height
        side3 = height * length
        paperforbox = (2 * side1) + (2 * side2) + (2 * side3) + min(side1, side2, side3)
        totalpaper += paperforbox
    print(totalpaper)
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