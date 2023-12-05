TEST = True
TEST_SOLUTION = 46 # add solution for test input here

def puzzle(filecontent):
    result = 10000000000000000000000
    # insert solution here
    
    print('Reading map data...')
    maps = filecontent.split('\n\n')
    seeds_ranges = maps[0].split(':')[1].strip().split(' ')
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
    for i in range(0, len(seeds_ranges), 2):
        range_start = int(seeds_ranges[i])
        range_length = int(seeds_ranges[i + 1])
        
        starting_map = 'seed'
        intersect_found = False
        while not intersect_found:
            # check for first map to intersect
            map_to_check = maps_dict[starting_map]
            for map_range in map_to_check[1]:
                if (range_start > map_range[0] and range_start <= map_range[1]) or (range_start + range_length > map_range[0] and range_start + range_length <= map_range[1]):
                    intersect_found = True
                    break
            if not intersect_found:
                starting_map = map_to_check[0]
        
        for seed in range(range_start, range_start + range_length - 2):
            mapped_value = int(seed)
            current_map = starting_map
            while current_map != 'location':
                map = maps_dict[current_map]
                for mapped_range in map[1]:
                    if mapped_value >= mapped_range[0] and mapped_value < mapped_range[1]:
                        offset = mapped_value - mapped_range[0]
                        mapped_value = mapped_range[2] + offset
                        break
                current_map = map[0]
            if mapped_value < result:
                result = mapped_value
        print(f'Finished mapping group {int(i / 2) + 1}/{int(len(seeds_ranges) / 2)}')

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