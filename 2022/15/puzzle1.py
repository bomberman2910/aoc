TEST = True
TEST_SOLUTION = 26 # add solution for test input here

def puzzle(filecontent, check_line):
    result = 0
    # insert solution here
    
    sensors = []
    beacons = []
    
    smallest_x, smallest_y, highest_x, highest_y = 0, 0, 0, 0
    
    for line in filecontent:
        sensor_text, beacon_text = line.split(': ')
        sensor_split = sensor_text.split(', ')
        sensor_x = int(sensor_split[0].split('=')[1])
        sensor_y = int(sensor_split[1].split('=')[1])
        beacon_split = beacon_text.split(', ')
        beacon_x = int(beacon_split[0].split('=')[1])
        beacon_y = int(beacon_split[1].split('=')[1])
        
        distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
        if(sensor_x - distance < smallest_x):
            smallest_x = sensor_x - distance
        if(sensor_x + distance > highest_x):
            highest_x = sensor_x + distance
        if(sensor_y - distance < smallest_y):
            smallest_y = sensor_y - distance
        if(sensor_y + distance > highest_y):
            highest_y = sensor_y + distance
            
        sensors.append([(sensor_x, sensor_y), distance])
        beacons.append([(beacon_x, beacon_y)])
        
    if(smallest_x < 0):
        for sensor in sensors:
            sensor[0] = (sensor[0][0] - smallest_x, sensor[0][1])
        for beacon in beacons:
            beacon[0] = (beacon[0][0] - smallest_x, beacon[0][1])
        highest_x -= smallest_x
        print('all shifted right by', smallest_x)
        smallest_x = 0
    if(smallest_y < 0):
        for sensor in sensors:
            sensor[0] = (sensor[0][0], sensor[0][1] - smallest_y)
        for beacon in beacons:
            beacon[0] = (beacon[0][0], beacon[0][1] - smallest_y)
        highest_y -= smallest_y
        check_line -= smallest_y
        print('all shifted down by', smallest_y)
        smallest_y = 0
    width = highest_x - smallest_x + 1
    height = highest_y - smallest_y + 1
    
    grid = [['.' for _ in range(width)] for _ in range(height)]
    
    for sensor in sensors:
        x, y = sensor[0]
        distance = sensor[1]
        
        grid[y][x] = 'S'
        for i in range(distance):
            for j in range(distance - i + 1):
                if(grid[y + i][x + j] == '.'):
                    grid[y + i][x + j] = '#'
                if(grid[y - i][x + j] == '.'):
                    grid[y - i][x + j] = '#'
                if(grid[y + i][x - j] == '.'):
                    grid[y + i][x - j] = '#'
                if(grid[y - i][x - j] == '.'):
                    grid[y - i][x - j] = '#'
                    
    for beacon in beacons:
        x, y = beacon[0]
        grid[y][x] = 'B'
        
    result = grid[check_line].count('#')

    return result

def solve(input_filename, line):
    file = open(input_filename, "r")
    content = file.read().splitlines()
    return puzzle(content, line)

if(TEST):
    testsolution = solve("test.txt", 10)
    if(testsolution == TEST_SOLUTION):
        print("Solution for test input correct")
        regularsolution = solve("input.txt", 2000000)
        print("Answer for main input", regularsolution)
    else:
        print(f"Solution for test input incorrect! (expected: {TEST_SOLUTION}; is: {testsolution})")
else:
    solve("input.txt", 2000000)