TEST = True
TEST_SOLUTION = 114 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here

    sequences = [[int(y) for y in x.split()] for x in filecontent]
    sequences_analyzed = []
    for sequence in sequences:
        sequence_analyzed = [sequence]
        sequence_analyzed.extend(find_differences(sequence))
        sequences_analyzed.append(sequence_analyzed)
    
    for analyzed in sequences_analyzed:
        result += next_in_sequence(analyzed)

    return result

def next_in_sequence(analyzed_sequence : list[list[int]]) -> int:
    analyzed_sequence.reverse()
    analyzed_sequence[0].append(0)
    for i in range(1, len(analyzed_sequence)):
        analyzed_sequence[i].append(analyzed_sequence[i][-1] + analyzed_sequence[i - 1][-1])
    print(analyzed_sequence)
    return analyzed_sequence[-1][-1]

def find_differences(row : list[int]) -> list[list[int]]:
    differences = []
    for i in range(len(row) - 1):
        differences.append(row[i + 1] - row[i])
    if len([x for x in differences if x != 0]) == 0:
        return [differences]
    including_following = [differences]
    including_following.extend(find_differences(differences))
    return including_following

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