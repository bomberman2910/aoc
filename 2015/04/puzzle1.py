import hashlib

TEST = True
TEST_SOLUTION = 609043 # add solution for test input here

def is_condition_met(hash):
    return hash[:5] == '00000'

def puzzle(filecontent):
    result = 0
    # insert solution here
    
    key = filecontent[0]

    i = -1
    hash = '     '

    while (not is_condition_met(hash)):
        i += 1
        input = f"{key}{i}"
        hash = hashlib.md5(input.encode()).hexdigest()

    result = i
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