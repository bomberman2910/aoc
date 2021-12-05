inputfile = open("input_1.txt", "r")
rawfilecontent = inputfile.readlines()
filecontent = []
for rawmovement in rawfilecontent:
    filecontent.append(rawmovement.removesuffix("\n"))

movements = []
for movement in filecontent:
    split = movement.split()
    movements.append((split[0], int(split[1])))

horizontal = 0
depth = 0

for movement in movements:
    direction, distance = movement
    if (direction == "forward"):
        horizontal += distance
    elif (direction == "up"):
        depth -= distance
    elif (direction == "down"):
        depth += distance

print(horizontal * depth)