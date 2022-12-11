import math


TEST = True
TEST_SOLUTION = 10605 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here

    split_by_monkeys = []
    current_monkey_lines = None
    for i in range(len(filecontent)):
        if(filecontent[i].startswith('Monkey')):
            split_by_monkeys.append(current_monkey_lines)
            current_monkey_lines = []
        current_monkey_lines.append(filecontent[i].strip())
    split_by_monkeys.append(current_monkey_lines)
    split_by_monkeys = split_by_monkeys[1 : ]
    
    monkey_data = []
    for monkey in split_by_monkeys:
        starting_items = monkey[1].split(':')[1].strip().split(', ')
        important_part_of_operation = monkey[2].split(' = ')[1].lstrip(' old ').split(' ')
        operation_data = (important_part_of_operation[0], important_part_of_operation[1])
        test = int(monkey[3].split(' by ')[1])
        if_true = int(monkey[4][-1])
        if_false = int(monkey[5][-1])
        monkey_data.append([starting_items, operation_data, test, if_true, if_false, 0])
    
    for _ in range(20):
        for i in range(len(monkey_data)):
            if(len(monkey_data[i][0]) == 0):
                continue
            for item in monkey_data[i][0]:
                worry_level = int(item)
                monkey_data[i][5] += 1
                operation, count = monkey_data[i][1]
                if(count == 'old'):
                    count = worry_level
                else:
                    count = int(count)
                if(operation == '+'):
                    worry_level += count
                elif(operation == '*'):
                    worry_level *= count
                worry_level = math.floor(worry_level / 3)
                if(worry_level % monkey_data[i][2] == 0):
                    monkey_data[monkey_data[i][3]][0].append(worry_level)
                else:
                    monkey_data[monkey_data[i][4]][0].append(worry_level)
            monkey_data[i][0].clear()
    
    inspections_counters = [x[5] for x in monkey_data]
    inspections_counters.sort(reverse=True)
    result = inspections_counters[0] * inspections_counters[1]
    
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