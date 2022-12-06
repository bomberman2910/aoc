import hashlib
import threading

TEST = False
TEST_SOLUTION = 0 # add solution for test input here

def is_condition_met(hash):
    return hash[:6] == '000000'

def check_range(start, key):
    for i in range(start, start + 1000000):
        input = f"{key}{i}"
        hash = hashlib.md5(input.encode()).hexdigest()
        if(is_condition_met(hash)):
            print(f"Found one: {i}")
            return
    print(f"Found nothing in range ({start}, {start + 1000000 - 1})")

def puzzle(filecontent):
    result = 0
    # insert solution here
    
    key = filecontent[0]

    i = -1
    hash = '      '

    for i in range(0, 1000000000, 1000000):
        threading.Thread(target=check_range, args=(i,key)).start()

    result = i
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