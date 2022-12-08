TEST = True
TEST_SOLUTION = 21 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here

    grid = []
    for row in filecontent:
        row_as_ints = []
        for column in row:
            row_as_ints.append(int(column))
        grid.append(row_as_ints)
        
    result = len(grid) * 2 + (len(grid[0]) - 2) * 2
    
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            is_visible_from_left = check_left(grid, x, y)
            is_visible_from_right = check_right(grid, x, y)
            is_visible_from_top = check_top(grid, x, y)
            is_visible_from_bottom = check_bottom(grid, x, y)
            if(is_visible_from_left or is_visible_from_right or is_visible_from_top or is_visible_from_bottom):
                result += 1

    return result

def check_left(grid, x, y):
    height = grid[y][x]
    for left in range(x - 1, -1, -1):
        if(grid[y][left] >= height):
            return False
    return True

def check_right(grid, x, y):
    height = grid[y][x]
    for right in range(x + 1, len(grid[y]), 1):
        if(grid[y][right] >= height):
            return False
    return True

def check_top(grid, x, y):
    height = grid[y][x]
    for top in range(y - 1, -1, -1):
        if(grid[top][x] >= height):
            return False
    return True

def check_bottom(grid, x, y):
    height = grid[y][x]
    for bottom in range(y + 1, len(grid), 1):
        if(grid[bottom][x] >= height):
            return False
    return True

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