import regex as re


TEST = True
TEST_SOLUTION = 281 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here

    for line in filecontent:
        numbers = re.findall('\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
        number_string = ''
        for number in [numbers[0], numbers[-1]]:
            if number == 'one':
                number_string += '1'
            elif number == 'two':
                number_string += '2'
            elif number == 'three':
                number_string += '3'
            elif number == 'four':
                number_string += '4'
            elif number == 'five':
                number_string += '5'
            elif number == 'six':
                number_string += '6'
            elif number == 'seven':
                number_string += '7'
            elif number == 'eight':
                number_string += '8'
            elif number == 'nine':
                number_string += '9'
            else:
                number_string += number
        result += int(number_string)
    
    return result

def solve(input_filename):
    file = open(input_filename, "r")
    content = file.read().splitlines()
    return puzzle(content)

if(TEST):
    testsolution = solve("test2.txt")
    if(testsolution == TEST_SOLUTION):
        print("Solution for test input correct")
        regularsolution = solve("input.txt")
        print("Answer for main input", regularsolution)
    else:
        print(f"Solution for test input incorrect! (expected: {TEST_SOLUTION}; is: {testsolution})")
else:
    solve("input.txt")