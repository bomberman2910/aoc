TEST = True
TEST_SOLUTION = 467835 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here
    
    parts = []
    gears = []
    
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
                if char == '*':
                    gears.append((char, (x, y)))
                if number_mode:
                    part = (current_number, (x - len(current_number), y))
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
                    parts.append(((current_number), (x - len(current_number), y), positions))
                    number_mode = False
                    current_number = ''
            x += 1
        if number_mode:
            part = (current_number, (x - len(current_number), y))
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
            parts.append(((current_number), (x - len(current_number), y), positions))
        y += 1
        
    for gear in gears:
        adjacent_parts = []
        for part in parts:
            if gear[1] in part[2]:
                adjacent_parts.append(part)
        if len(adjacent_parts) == 2:
            result += int(adjacent_parts[0][0]) * int(adjacent_parts[1][0])

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