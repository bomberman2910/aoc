from queue import SimpleQueue


TEST = True
TEST_SOLUTION = 31 # add solution for test input here

def flip(direction):
    if(direction == 0):
        return 2
    if(direction == 1):
        return 3
    if(direction == 2):
        return 0
    if(direction == 3):
        return 1

def search(grid, point_queue, x, y, direction):
    if((direction == 0 and y == 0) or (direction == 1 and x == len(grid[0]) - 1) or (direction == 2 and y == len(grid) - 1) or (direction == 3 and x == 0)):
        return
    
    to_x = 0
    to_y = 0
    
    if(direction == 0):
        to_x = x
        to_y = y - 1
    elif(direction == 1):
        to_x = x + 1
        to_y = y
    elif(direction == 2):
        to_x = x
        to_y = y + 1
    elif(direction == 3):
        to_x = x - 1
        to_y = y
        
    if(grid[to_y][to_x][1]):
        return
    
    current = grid[y][x]
    next = grid[to_y][to_x]
    if(current[0] - next[0] > 1):
        return
    
    grid[to_y][to_x][1] = True
    grid[to_y][to_x][2] = flip(direction)
    point_queue.put((to_x, to_y))
        

def puzzle(filecontent):
    result = 0
    # insert solution here

    grid = []
    point_queue = SimpleQueue()

    for y in filecontent:
        row = []
        for x in y:
            row.append([ord(x), False, -1])
        grid.append(row)
    
    end_x, end_y = 0, 0
    for y in range(len(filecontent)):
        if('E' not in filecontent[y]):
            continue
        end_x = filecontent[y].index('E')
        end_y = y
        break
    start_x, start_y = 0, 0
    for y in range(len(filecontent)):
        if('S' not in filecontent[y]):
            continue
        start_x = filecontent[y].index('S')
        start_y = y
        break
    
    grid[end_y][end_x][0] = ord('z')
    grid[start_y][start_x][0] = ord('a')
    
    point_queue.put((end_x, end_y))
    grid[end_y][end_x][1] = True
    
    while not point_queue.empty():
        point_x, point_y = point_queue.get()
        
        search(grid, point_queue, point_x, point_y, 0)
        search(grid, point_queue, point_x, point_y, 1)
        search(grid, point_queue, point_x, point_y, 2)
        search(grid, point_queue, point_x, point_y, 3)
        
    current_point = (start_x, start_y)
    while(current_point != (end_x, end_y)):
        next_direction = grid[current_point[1]][current_point[0]][2]
        if(next_direction == 0):
            current_point = (current_point[0], current_point[1] - 1)
        elif(next_direction == 1):
            current_point = (current_point[0] + 1, current_point[1])
        elif(next_direction == 2):
            current_point = (current_point[0], current_point[1] + 1)
        elif(next_direction == 3):
            current_point = (current_point[0] - 1, current_point[1])
        result += 1

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