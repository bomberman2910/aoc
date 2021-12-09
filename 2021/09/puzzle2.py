TEST = False

def check_for_basin(heightmap, x, y):
    belongstobasin = [(x, y, heightmap[y][x])]
    if(x == 0 and y == 0): # top left
        right = heightmap[y][x + 1]
        down = heightmap[y + 1][x]
        if(down != 9 and down > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x, y + 1))
        if(right != 9 and right > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x + 1, y))
    elif (x == len(heightmap[y]) - 1 and y == 0): # top right
        down = heightmap[y + 1][x]
        left = heightmap[y][x - 1]
        if(down != 9 and down > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x, y + 1))
        if(left != 9 and left > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x - 1, y))
    elif (x == 0 and y == len(heightmap) - 1): # bottom left
        up = heightmap[y - 1][x]
        right = heightmap[y][x + 1]
        if(up != 9 and up > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x, y - 1))
        if(right != 9 and right > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x + 1, y))
    elif (x == len(heightmap[y]) - 1 and y == len(heightmap) - 1): # bottom right
        up = heightmap[y - 1][x]
        left = heightmap[y][x - 1]
        if(up != 9 and up > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x, y - 1))
        if(left != 9 and left > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x - 1, y))
    elif (y == 0): # top row
        left = heightmap[y][x - 1]
        down = heightmap[y + 1][x]
        right = heightmap[y][x + 1]
        if(down != 9 and down > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x, y + 1))
        if(left != 9 and left > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x - 1, y))
        if(right != 9 and right > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x + 1, y))
    elif (y == len(heightmap) - 1): # bottom row
        left = heightmap[y][x - 1]
        up = heightmap[y - 1][x]
        right = heightmap[y][x + 1]
        if(up != 9 and up > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x, y - 1))
        if(left != 9 and left > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x - 1, y))
        if(right != 9 and right > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x + 1, y))
    elif (x == 0): # left column
        up = heightmap[y - 1][x]
        down = heightmap[y + 1][x]
        right = heightmap[y][x + 1]
        if(up != 9 and up > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x, y - 1))
        if(down != 9 and down > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x, y + 1))
        if(right != 9 and right > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x + 1, y))
    elif (x == len(heightmap[y]) - 1): # right column
        left = heightmap[y][x - 1]
        up = heightmap[y - 1][x]
        down = heightmap[y + 1][x]
        if(up != 9 and up > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x, y - 1))
        if(down != 9 and down > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x, y + 1))
        if(left != 9 and left > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x - 1, y))
    else:
        up = heightmap[y - 1][x]
        left = heightmap[y][x - 1]
        down = heightmap[y + 1][x]
        right = heightmap[y][x + 1]
        if(up != 9 and up > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x, y - 1))
        if(down != 9 and down > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x, y + 1))
        if(left != 9 and left > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x - 1, y))
        if(right != 9 and right > heightmap[y][x]):
            belongstobasin.extend(check_for_basin(heightmap, x + 1, y))
    return belongstobasin

def puzzle(filecontent):
    heightmap = []
    for y in range(len(filecontent)):
        heightmap.append([int(i) for i in list(filecontent[y])])
    lowpoints = []
    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            if (x == 0 and y == 0): # top left
                down = heightmap[y + 1][x]
                right = heightmap[y][x + 1]
                current = heightmap[y][x]
                if(current < down and current < right):
                    lowpoints.append((x, y, current))
            elif (x == len(heightmap[y]) - 1 and y == 0): # top right
                down = heightmap[y + 1][x]
                left = heightmap[y][x - 1]
                current = heightmap[y][x]
                if(current < down and current < left):
                    lowpoints.append((x, y, current))
            elif (x == 0 and y == len(heightmap) - 1): # bottom left
                up = heightmap[y - 1][x]
                right = heightmap[y][x + 1]
                current = heightmap[y][x]
                if(current < up and current < right):
                    lowpoints.append((x, y, current))
            elif (x == len(heightmap[y]) - 1 and y == len(heightmap) - 1): # bottom right
                up = heightmap[y - 1][x]
                left = heightmap[y][x - 1]
                current = heightmap[y][x]
                if(current < up and current < left):
                    lowpoints.append((x, y, current))
            elif (y == 0): # top row
                left = heightmap[y][x - 1]
                down = heightmap[y + 1][x]
                right = heightmap[y][x + 1]
                current = heightmap[y][x]
                if(current < left and current < down and current < right):
                    lowpoints.append((x, y, current))
            elif (y == len(heightmap) - 1): # bottom row
                left = heightmap[y][x - 1]
                up = heightmap[y - 1][x]
                right = heightmap[y][x + 1]
                current = heightmap[y][x]
                if(current < left and current < up and current < right):
                    lowpoints.append((x, y, current))
            elif (x == 0): # left column
                up = heightmap[y - 1][x]
                down = heightmap[y + 1][x]
                right = heightmap[y][x + 1]
                current = heightmap[y][x]
                if(current < up and current < down and current < right):
                    lowpoints.append((x, y, current))
            elif (x == len(heightmap[y]) - 1): # right column
                left = heightmap[y][x - 1]
                up = heightmap[y - 1][x]
                down = heightmap[y + 1][x]
                current = heightmap[y][x]
                if(current < left and current < up and current < down):
                    lowpoints.append((x, y, current))
            else:
                up = heightmap[y - 1][x]
                left = heightmap[y][x - 1]
                down = heightmap[y + 1][x]
                right = heightmap[y][x + 1]
                current = heightmap[y][x]
                if(current < up and current < left and current < down and current < right):
                    lowpoints.append((x, y, current))

    basins = []
    for lowpoint_x, lowpoint_y, _ in lowpoints:
        basins.append(set(check_for_basin(heightmap, lowpoint_x, lowpoint_y)))
    basinsizes = [len(basin) for basin in basins]
    threebiggest = sorted(basinsizes, reverse=True)[:3]
    print(threebiggest[0] * threebiggest[1] * threebiggest[2])
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