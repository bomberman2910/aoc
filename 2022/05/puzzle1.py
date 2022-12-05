TEST = True
TEST_SOLUTION = 'CMZ' # add solution for test input here

def puzzle(filecontent):
    result = ''
    # insert solution here

    # build stacks
    end_of_crates = next((i for i, e in enumerate(filecontent) if e.startswith(' 1')))
    num_stacks = max([int(x) for x in filecontent[end_of_crates].split(' ') if x])
    stacks = []
    for i in range(num_stacks):
        stacks.append([])
    for i in range(end_of_crates - 1, -1, -1):
        layer = filecontent[i]
        for x in range(0, num_stacks * 4, 4):
            position = layer[x : x + 4]
            if(position.strip() != ''):
                stacks[x // 4].append(position.strip().lstrip('[').rstrip(']'))
        
    # parse movement instructions
    instructions_start_line = end_of_crates + 2
    raw_instructions = filecontent[instructions_start_line:]
    parsed_instructions = []
    for raw_instruction in raw_instructions:
        instruction_parts = raw_instruction.split(' ')
        amount, source, destination = int(instruction_parts[1]), int(instruction_parts[3]) - 1, int(instruction_parts[5]) - 1
        parsed_instructions.append((amount, source, destination))

    # perform movements
    for amount, source, destination in parsed_instructions:
        for i in range(amount):
            item = stacks[source].pop()
            stacks[destination].append(item)

    # get uppermost crate letters
    uppermost_crates = []
    for stack in stacks:
        uppermost_crates.append(stack[-1:][0])

    result = ''.join(uppermost_crates)

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