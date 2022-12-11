import re


TEST = True
TEST_SOLUTION = 12 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here

    sum_literal = 0
    sum_memory = 0
    
    for line in filecontent:
        sum_literal += len(line)
        processed = line[1 : -1].replace('\\\\', '\\').replace('\\\"', '\"')
        pattern = re.compile(r'(\\x[0-9a-fA-F]{2})', re.MULTILINE)
        matches = re.findall(pattern, line)
        for match in matches:
            start = processed.index(match)
            complete_hex = processed[start : start + 4]
            processed = processed.replace(match, chr(int(complete_hex[2 : ] , 16)))
        sum_memory += len(processed)

    result = sum_literal - sum_memory

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