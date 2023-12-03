TEST = True
TEST_SOLUTION = 4361 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here
    
    parts = []
    
    y = 0
    for line in filecontent:
        x = 0
        number_mode = False
        current_number = ''
        for char in line:
            if char.isdigit():
                number_mode = True
                current_number += char
            else:
                if char != '.':
                    parts.append((char, (x, y)))
                if number_mode:
                    parts.append((current_number, (x - len(current_number), y)))
                    number_mode = False
                    current_number = ''
            x += 1
        if number_mode:
            parts.append((current_number, (x - len(current_number), y)))
        y += 1
    
    for part in parts:
        if part[0][0].isdigit():
            positions = []
            for i in range(len(part[0])):
                if i == 0:
                    positions.append((part[1][0] - 1, part[1][1] - 1))  # top left
                    positions.append((part[1][0] - 1, part[1][1]))      # left
                    positions.append((part[1][0] - 1, part[1][1] + 1))  # bottom left
                positions.append((part[1][0] + i, part[1][1] - 1))          # top
                positions.append((part[1][0] + i, part[1][1] + 1))          # bottom
                if i == len(part[0]) - 1:
                    positions.append((part[1][0] + i + 1, part[1][1] - 1))  # top right
                    positions.append((part[1][0] + i + 1, part[1][1]))      # right
                    positions.append((part[1][0] + i + 1, part[1][1] + 1))  # bottom right
            for inner_part in parts:
                if not inner_part[0][0].isdigit() and inner_part[1] in positions:
                    result += int(part[0])
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