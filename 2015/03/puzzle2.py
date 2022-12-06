TEST = True
TEST_SOLUTION = 11 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here
    movements = filecontent[0]
    visited = []
    current_x, current_y = 0, 0
    robo_x, robo_y = 0, 0
    for i in range(0, len(movements), 2):
        visited.append((current_x, current_y))
        visited.append((robo_x, robo_y))
        if(movements[i] == '^'):
            current_y -= 1
        elif(movements[i] == 'v'):
            current_y += 1
        elif(movements[i] == '<'):
            current_x -= 1
        elif(movements[i] == '>'):
            current_x += 1
        if(movements[i + 1] == '^'):
            robo_y -= 1
        elif(movements[i + 1] == 'v'):
            robo_y += 1
        elif(movements[i + 1] == '<'):
            robo_x -= 1
        elif(movements[i + 1] == '>'):
            robo_x += 1

    visited.append((current_x, current_y))
    visited.append((robo_x, robo_y))

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