TEST = True
TEST_SOLUTION = 35 # add solution for test input here

def puzzle(filecontent):
    result = 0
    # insert solution here
    
    print('Reading map data...')
    maps = filecontent.split('\n\n')
    seeds = maps[0].split(':')[1].strip().split(' ')
    maps = maps[1:]
    maps_dict = {}
    for map in maps:
        map_data = map.splitlines()
        map_id = map_data[0].split(' ')[0].split('-')[0]
        ranges = []
        for data in map_data[1:]:
            destination_start, source_start, length = data.split(' ')
            destination_start, source_start, length = int(destination_start), int(source_start), int(length)
            ranges.append((source_start, source_start + length, destination_start))
        maps_dict[map_id] = (map_data[0].split(' ')[0].split('-')[2], ranges)
    print('Map data reading finished')
    
    print('Mapping seeds')
    seed_locations = []
    for seed in seeds:
        mapped_value = int(seed)
        current_map = 'seed'
        while current_map != 'location':
            map = maps_dict[current_map]
            for mapped_range in map[1]:
                if mapped_value >= mapped_range[0] and mapped_value < mapped_range[1]:
                    offset = mapped_value - mapped_range[0]
                    mapped_value = mapped_range[2] + offset
                    break
            current_map = map[0]
        seed_locations.append(mapped_value)
        
    result = min(seed_locations)

    return result

def solve(input_filename):
    file = open(input_filename, "r")
    content = file.read()
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