TEST = False
TEST_SOLUTION = 0 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here
    
    commands = [x.split(' ')[-4:] for x in filecontent]
    
    grid = [[False for x in range(1000)] for y in range(1000)]
    for command in commands:
        start = command[1].split(',')
        start_x = int(start[0])
        start_y = int(start[1])
        end = command[3].split(',')
        end_x = int(end[0])
        end_y = int(end[1])
        for y in range(start_y, end_y + 1):
            for x in range(start_x, end_x + 1):
                action = command[0]
                if(action == 'on'):
                    grid[y][x] = True
                elif(action == 'off'):
                    grid[y][x] = False
                elif(action == 'toggle'):
                    grid[y][x] = not grid[y][x]
        
    row_sums = []
    for row in grid:
        switched_on = [x for x in row if x]
        row_sums.append(len(switched_on))
    
    print(sum(row_sums))
    
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