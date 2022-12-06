TEST = True
TEST_SOLUTION = 2 # add solution for test input here

def two_letters_twice(word):
    for i in range(len(word) - 3):
        pattern = word[i : i + 2]
        if(pattern in word[i + 2 : ]):
            return True
    return False

def repeat_with_distance(word):
    for i in range(len(word) - 2):
        if(word[i] == word[i + 2]):
            return True
    return False

def puzzle(filecontent):
    result = 0
    # insert solution here
    for word in filecontent:
        if(not two_letters_twice(word)):
            continue
        if(repeat_with_distance(word)):
            result += 1
    return result

def solve(input_filename):
    file = open(input_filename, "r")
    content = file.read().splitlines()
    return puzzle(content)

if(TEST):
    testsolution = puzzle(['qjhvhtzxzqqjkmpb','xxyxx','uurcxstgmygtbstg','ieodomkazucvgmuy'])
    if(testsolution == TEST_SOLUTION):
        print("Solution for test input correct")
        regularsolution = solve("input.txt")
        print("Answer for main input", regularsolution)
    else:
        print(f"Solution for test input incorrect! (expected: {TEST_SOLUTION}; is: {testsolution})")
else:
    solve("input.txt")