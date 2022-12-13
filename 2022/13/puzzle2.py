TEST = True
TEST_SOLUTION = 140 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here

    packet_pairs = []
    for i in range(len(filecontent)):
        if(filecontent[i] != ''):
            packet_pairs.append(eval(filecontent[i]))
    packet_pairs.append([2])
    packet_pairs.append([6])
    
    n = len(packet_pairs)
    while True:
        swapped = False
        for i in range(n - 1):
            if (compare(packet_pairs[i], packet_pairs[i + 1]) == -1):
                packet_pairs[i], packet_pairs[i + 1] = packet_pairs[i + 1], packet_pairs[i]
                swapped = True
        n = n - 1
        if(not swapped):
            break
    
    index_2 = packet_pairs.index([2]) + 1
    index_6 = packet_pairs.index([6]) + 1
    
    result = index_2 * index_6
            
    return result

def compare(left, right):
    shorter = min(len(left), len(right))
    for i in range(shorter):
        current_left = left[i]
        current_right = right[i]
        if(type(current_left) is list and type(current_right) is not list):
            current_right = [current_right]
        if(type(current_left) is not list and type(current_right) is list):
            current_left = [current_left]
        if(type(current_left) is list and type(current_right) is list):
            result = compare(current_left, current_right)
            if(result == 0):
                continue
            return result
        if(current_left == current_right):
            continue
        if(current_left < current_right):
            return 1
        if(current_left > current_right):
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