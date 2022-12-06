TEST = True
TEST_SOLUTION = 19 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here
    message = filecontent[0]
    for i in range(14, len(message) + 1):
        if(len(set(message[i - 14 : i])) == 14):
            result = i
            break
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