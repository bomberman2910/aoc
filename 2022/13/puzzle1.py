import ast


TEST = True
TEST_SOLUTION = 13 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here

    packet_pairs = []
    for i in range(0, len(filecontent), 3):
        packet_pairs.append((filecontent[i], filecontent[i + 1]))
        
    for pair in packet_pairs:
        left = eval(pair[0])
        right = eval(pair[1])
        if(compare(left, right) > -1):
            result += packet_pairs.index(pair) + 1
            
    return result

def compare(left, right):
    shorter = min(len(left), len(right))
    for i in range(shorter):
        if(type(left[i]) is list and type(right[i]) is not list):
            right[i] = [right[i]]
        if(type(left[i]) is not list and type(right[i]) is list):
            left[i] = [left[i]]
        if(type(left[i]) is list and type(right[i]) is list):
            result = compare(left[i], right[i])
            if(result == 0):
                continue
            return result
        if(left[i] == right[i]):
            continue
        if(left[i] < right[i]):
            return 1
        if(left[i] > right[i]):
            return -1
    
    if(len(left) < len(right)):
        return 1
    if(len(left) > len(right)):
        return -1
    
    return 0

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