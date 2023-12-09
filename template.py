TEST = True
TEST_SOLUTION = 0 # add solution for test input here

def puzzle(filecontent : list[str]) -> int:
    result = 0
    # insert solution here

    return result

def solve(input_filename : str) -> int:
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
    regularsolution = solve("input.txt")
    print("Answer for main input", regularsolution)