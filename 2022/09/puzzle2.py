TEST = True
TEST_SOLUTION = 1 # add solution for test input here

def sign(x):
    return (x > 0) - (x < 0)

def puzzle(filecontent):
    result = 0
    # insert solution here

    movements = [(x.split(' ')[0], int(x.split(' ')[1])) for x in filecontent]
    
    elements = [[0, 0] for _ in range(10)]
    
    visited_by_tail = [(elements[9][0], elements[9][1])]
    
    for direction, distance in movements:
        for _ in range(distance):
            if(direction == 'U'):
                elements[0][1] -= 1
            elif(direction == 'D'):
                elements[0][1] += 1
            elif(direction == 'L'):
                elements[0][0] -= 1
            elif(direction == 'R'):
                elements[0][0] += 1
                
            for i in range(1, 10):
                xdelta = elements[i -1][0] - elements[i][0]
                ydelta = elements[i -1][1] - elements[i][1]
                if abs(xdelta) > 1 or abs(ydelta) > 1:
                    elements[i][0] += sign(xdelta)
                    elements[i][1] += sign(ydelta)
            
            visited_by_tail.append((elements[9][0], elements[9][1]))

    result = len(set(visited_by_tail))

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