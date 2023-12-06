TEST = True
TEST_SOLUTION = 71503 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here
    
    time_raw, distance_raw = filecontent[0].split(':')[1].replace(' ', ''), filecontent[1].split(':')[1].replace(' ', '')
    charge_time, min_distance = int(time_raw), int(distance_raw)
    
    for i in range(1, charge_time):
        distance = (charge_time - i) * i
        if(distance > min_distance):
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