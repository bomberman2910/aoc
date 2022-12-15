TEST = True
TEST_SOLUTION = 24 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here

    paths = [x.split(' -> ') for x in filecontent]
    
    all_x = []
    all_y = []
    for path in paths:
        for point in path:
            all_x.append(int(point.split(',')[0]))
            all_y.append(int(point.split(',')[1]))
            
    min_x = int(min(all_x))
    width = int(max(all_x)) - int(min(all_x)) + 1
    height = int(max(all_y)) + 1
    
    grid = [['.' for _ in range(width)] for _ in range(height)]
    grid[0][500 - min_x] = '+'
    
    for path in paths:
        for i in range(len(path) - 1):
            current_point = [int(x) for x in path[i].split(',')]
            next_point = [int(x) for x in path[i + 1].split(',')]
            if(current_point[0] == next_point[0]):
                x = current_point[0] - min_x
                if(current_point[1] > next_point[1]):
                    for y in range(next_point[1], current_point[1] + 1):
                        grid[y][x] = '#'
                elif(current_point[1] < next_point[1]):
                    for y in range(current_point[1], next_point[1] + 1):
                        grid[y][x] = '#'
            elif(current_point[1] == next_point[1]):
                if(current_point[0] > next_point[0]):
                    for x in range(next_point[0], current_point[0] + 1):
                        real_x = x - min_x
                        grid[current_point[1]][real_x] = '#'
                elif(current_point[0] < next_point[0]):
                    for x in range(current_point[0], next_point[0] + 1):
                        real_x = x - min_x
                        grid[current_point[1]][real_x] = '#'
    
    units_of_sand = 0
    while True:
        new_sand = [500 - min_x, 0]
        moving = True
        try:
            while moving:
                    if(grid[new_sand[1] + 1][new_sand[0]] == '.'):
                        new_sand[1] += 1
                    elif(grid[new_sand[1] + 1][new_sand[0] - 1] == '.'):
                        new_sand[0] -= 1
                        new_sand[1] += 1
                    elif(grid[new_sand[1] + 1][new_sand[0] + 1] == '.'):
                        new_sand[0] += 1
                        new_sand[1] += 1
                    else:
                        moving = False
                        units_of_sand += 1
                        grid[new_sand[1]][new_sand[0]] = 'o'
        except:
            result = units_of_sand
            break
    
    for row in grid:
        print(''.join(row))
    
    return result

def solve(input_filename):
    file = open(input_filename, "r")
    content = file.read().splitlines()
    return puzzle(content)

if(TEST):
    testsolution = solve("test.txt")
    if(testsolution == TEST_SOLUTION):
        print("Solution for test input correct")
        regularsolution = solve("input.txt")
        print("Answer for main input", regularsolution)
    else:
        print(f"Solution for test input incorrect! (expected: {TEST_SOLUTION}; is: {testsolution})")
else:
    solve("input.txt")