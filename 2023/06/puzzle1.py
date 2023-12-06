TEST = True
TEST_SOLUTION = 288 # add solution for test input here

def puzzle(filecontent):
    result = 1
    # insert solution here
    
    time_raw, distance_raw = filecontent[0].split(':')[1], filecontent[1].split(':')[1]
    times = list(filter(None, time_raw.split()))
    distances = list(filter(None, distance_raw.split()))
    races = list(zip(times, distances))
    
    for race in races:
        min_distance = int(race[1])
        charge_time = int(race[0])
        ways_to_win = 0
        for i in range(1, charge_time):
            distance = (charge_time - i) * i
            if(distance > min_distance):
                ways_to_win += 1
        result *= ways_to_win

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