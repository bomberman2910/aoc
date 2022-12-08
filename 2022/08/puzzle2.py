from itertools import chain


TEST = True
TEST_SOLUTION = 8 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here

    grid = []
    for row in filecontent:
        row_as_ints = []
        for column in row:
            row_as_ints.append(int(column))
        grid.append(row_as_ints)
        
    view_distances = []
    for y in range(1, len(grid) - 1):
        view_distances_row = []
        for x in range(1, len(grid[y]) - 1):
            view_distance_left = check_left(grid, x, y)
            view_distance_right = check_right(grid, x, y)
            view_distance_top = check_top(grid, x, y)
            view_distance_bottom = check_bottom(grid, x, y)
            view_distances_row.append(view_distance_left * view_distance_right * view_distance_top * view_distance_bottom)
        view_distances.append(view_distances_row)
            
    result = max(chain.from_iterable(view_distances))

    return result

def check_left(grid, x, y):
    height = grid[y][x]
    distance = 0
    for left in range(x - 1, -1, -1):
        distance += 1
        if(grid[y][left] >= height):
            break
    return distance

def check_right(grid, x, y):
    height = grid[y][x]
    distance = 0
    for right in range(x + 1, len(grid[y]), 1):
        distance += 1
        if(grid[y][right] >= height):
            break
    return distance

def check_top(grid, x, y):
    height = grid[y][x]
    distance = 0
    for top in range(y - 1, -1, -1):
        distance += 1
        if(grid[top][x] >= height):
            break
    return distance

def check_bottom(grid, x, y):
    height = grid[y][x]
    distance = 0
    for bottom in range(y + 1, len(grid), 1):
        distance += 1
        if(grid[bottom][x] >= height):
            break
    return distance

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