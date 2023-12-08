TEST = True
TEST_SOLUTION = 6 # add solution for test input here

def puzzle(filecontent : list[str]) -> int:
    result = 0
    # insert solution here
    
    instructions = filecontent.pop(0)
    filecontent.pop(0)
    nodes = {}
    for line in filecontent:
        node = line.split(' = ')[0]
        left, right = line.split(' = (')[1].rstrip(')').split(', ')[0], line.split(' = (')[1].rstrip(')').split(', ')[1]
        nodes[node] = (left, right)
    
    current_node = 'AAA'
    instruction_pointer = 0
    while current_node != 'ZZZ':
        instruction = instructions[instruction_pointer]
        instruction_pointer += 1
        if instruction_pointer >= len(instructions):
            instruction_pointer = 0
        if instruction == 'L':
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
        result += 1

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
    solve("input.txt")