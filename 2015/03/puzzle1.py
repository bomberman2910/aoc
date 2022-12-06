TEST = True
TEST_SOLUTION = 4 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here
    movements = filecontent[0]
    visited = []
    current_x, current_y = 0, 0
    for move in movements:
        visited.append((current_x, current_y))
        if(move == '^'):
            current_y -= 1
        elif(move == 'v'):
            current_y += 1
        elif(move == '<'):
            current_x -= 1
        elif(move == '>'):
            current_x += 1
    
    result = len(set(visited))

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