TEST = False

def puzzle(filecontent):
    totallength = 0
    for box in filecontent:
        measurementstrings = box.split('x')
        width, length, height = int(measurementstrings[0]), int(measurementstrings[1]), int(measurementstrings[2])
        volume = width * length * height
        band = 0
        if(max(width, length, height) == width):
            band = length + length + height + height
        elif(max(width, length, height) == length):
            band = width + width + height + height
        elif(max(width, length, height) == height):
            band = length + length + width + width
        totallength += band + volume
    print(totallength)
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