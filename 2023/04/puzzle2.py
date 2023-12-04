from collections import deque

TEST = True
TEST_SOLUTION = 30 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here
    
    cards = []
    for line in filecontent:
        card_number = line.split(':')[0].split(' ')[-1]
        winning_numbers = list(filter(None, line.split(':')[1].split('|')[0].split(' ')))
        drawn_numbers = list(filter(None, line.split(':')[1].split('|')[1].split(' ')))
        cards.append((int(card_number), winning_numbers, drawn_numbers))
        
    card_queue = deque(cards)
    while len(card_queue) > 0:
        card = card_queue.popleft()
        result += 1
        winning = 0
        for number in card[2]:
            if number in card[1]:
                winning += 1
        if winning == 0:
            continue
        next_index = card[0]
        for i in range(winning):
            if next_index + i > len(cards):
                continue
            card_queue.append(cards[next_index + i])

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