TEST = True
TEST_SOLUTION = 8 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here

    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    games = []
    for line in filecontent:
        game_id = int(line.split(':')[0].split(' ')[1])
        turns = line.split(':')[1].split(';')
        turns_analyzed = []
        for turn in turns:
            colors = {}
            color_info = turn.split(',')
            for color in color_info:
                colors[color.strip().split(' ')[1]] = int(color.strip().split(' ')[0])
            turns_analyzed.append(colors)
        games.append((game_id, turns_analyzed))
    
    for game in games:
        is_game_possible = True
        for turn in game[1]:
            if 'red' in turn and turn['red'] > MAX_RED:
                is_game_possible = False
                break
            elif 'green' in turn and turn['green'] > MAX_GREEN:
                is_game_possible = False
                break
            elif 'blue' in turn and turn['blue'] > MAX_BLUE:
                is_game_possible = False
                break
        if is_game_possible:
            result += game[0]

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