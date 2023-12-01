TEST = True
TEST_SOLUTION = 142 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here

    for line in filecontent:
        numbers = [x for x in line if x.isdigit()]
        number_string = numbers[0] + numbers[-1]
        result += int(number_string)

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