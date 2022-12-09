TEST = True
TEST_SOLUTION = 13 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here

    movements = [(x.split(' ')[0], int(x.split(' ')[1])) for x in filecontent]
    
    head_x = 0
    head_y = 0
    tail_x = 0
    tail_y = 0
    
    visited_by_tail = [(0, 0)]
    
    for direction, distance in movements:
        for _ in range(distance):
            if(direction == 'U'):
                move_tail = tail_y > head_y
                head_y -= 1
                if(move_tail and tail_x < head_x):
                    tail_x += 1
                    tail_y -= 1
                elif(move_tail and tail_x == head_x):
                    tail_y -= 1
                elif(move_tail and tail_x > head_x):
                    tail_x -= 1
                    tail_y -= 1
            elif(direction == 'D'):
                move_tail = tail_y < head_y
                head_y += 1
                if(move_tail and tail_x < head_x):
                    tail_x += 1
                    tail_y += 1
                elif(move_tail and tail_x == head_x):
                    tail_y += 1
                elif(move_tail and tail_x > head_x):
                    tail_x -= 1
                    tail_y += 1
            elif(direction == 'L'):
                move_tail = tail_x > head_x
                head_x -= 1
                if(move_tail and tail_y < head_y):
                    tail_y += 1
                    tail_x -= 1
                elif(move_tail and tail_y == head_y):
                    tail_x -= 1
                elif(move_tail and tail_y > head_y):
                    tail_y -= 1
                    tail_x -= 1
            elif(direction == 'R'):
                move_tail = tail_x < head_x
                head_x += 1
                if(move_tail and tail_y < head_y):
                    tail_y += 1
                    tail_x += 1
                elif(move_tail and tail_y == head_y):
                    tail_x += 1
                elif(move_tail and tail_y > head_y):
                    tail_y -= 1
                    tail_x += 1
            visited_by_tail.append((tail_x, tail_y))
    
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