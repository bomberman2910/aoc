import math

TEST = True
TEST_SOLUTION = 6 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here
    
    instructions = filecontent.pop(0)
    filecontent.pop(0)
    nodes = {}
    for line in filecontent:
        node = line.split(' = ')[0]
        left, right = line.split(' = (')[1].rstrip(')').split(', ')[0], line.split(' = (')[1].rstrip(')').split(', ')[1]
        nodes[node] = (left, right)
        
    current_nodes = [x for x in nodes.keys() if x[-1] == 'A']
    current_nodes_steps = {}
    for i in range(len(current_nodes)):
        current_nodes_steps[i] = 0
    instruction_pointer = 0
    for i in range(len(current_nodes)):
        while current_nodes[i][-1] != 'Z':
            instruction = instructions[instruction_pointer]
            instruction_pointer += 1
            if instruction_pointer >= len(instructions):
                instruction_pointer = 0
            if instruction == 'L':
                current_nodes[i] = nodes[current_nodes[i]][0]
            else:
                current_nodes[i] = nodes[current_nodes[i]][1]
            current_nodes_steps[i] += 1
    
    factors = {x: find_factors(x) for x in current_nodes_steps.values()}
    common = list(factors.values())[0][1]
    result = 1
    for factor in factors:
        result *= factors[factor][0]
    result *= common

    return result

def find_factors(number : int) -> list[int]:
    factors = []
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:
                factors.append(number // i)
    return factors

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