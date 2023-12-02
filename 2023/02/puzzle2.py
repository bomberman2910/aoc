TEST = True
TEST_SOLUTION = 2286 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here
    
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
        min_red = 0
        min_green = 0
        min_blue = 0
        for turn in game[1]:
            if 'red' in turn and turn['red'] > min_red:
                min_red = turn['red']
            if 'green' in turn and turn['green'] > min_green:
                min_green = turn['green']
            if 'blue' in turn and turn['blue'] > min_blue:
                min_blue = turn['blue']
        power = min_red * min_green * min_blue
        result += power

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