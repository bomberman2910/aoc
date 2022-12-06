from collections import Counter

TEST = True
TEST_SOLUTION = 2 # add solution for test input here

def check_for_double(word):
    for i in range(len(word) - 1):
        if(word[i] == word[i + 1]):
            return True
    return False

def puzzle(filecontent):
    result = 0
    # insert solution here

    for word in filecontent:
        if('ab' in word or 'cd' in word or 'pq' in word or 'xy' in word):
            continue
        if(not check_for_double(word)):
            continue
        count = Counter(word)
        if(count['a'] + count['e'] + count['i'] + count['o'] + count['u'] > 2):
            result += 1

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