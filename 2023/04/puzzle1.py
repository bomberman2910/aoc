TEST = True
TEST_SOLUTION = 13 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here
    
    cards = []
    for line in filecontent:
        card_number = line.split(':')[0].split(' ')[-1]
        winning_numbers = list(filter(None, line.split(':')[1].split('|')[0].split(' ')))
        drawn_numbers = list(filter(None, line.split(':')[1].split('|')[1].split(' ')))
        cards.append((card_number, winning_numbers, drawn_numbers))
    
    for card in cards:
        value = 0
        for number in card[2]:
            if number in card[1]:
                if value == 0:
                    value = 1
                else:
                    value *= 2
        result += value

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