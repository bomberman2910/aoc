TEST = True
TEST_SOLUTION = 13140 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here

    total_cycles = 0
    for command in filecontent:
        if(command == 'noop'):
            total_cycles += 1
        elif(command.startswith('addx')):
            total_cycles += 2
        
    register_x = 1
    is_in_add = False
    current_add_value = 0
    instruction_pointer = 0
    for current_cycle in range(total_cycles):
        if((current_cycle + 1) % 40 == 20):
            result += (current_cycle + 1) * register_x
        if(is_in_add):
            register_x += current_add_value
            instruction_pointer += 1
            is_in_add = False
            continue
        if(filecontent[instruction_pointer].startswith('addx')):
            current_add_value = int(filecontent[instruction_pointer].split(' ')[1])
            is_in_add = True
        else:
            instruction_pointer += 1

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