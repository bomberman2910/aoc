TEST = True
TEST_SOLUTION = 6440 # add solution for test input here

ranks = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
hands = [['12345'], ['11234', '12234', '12334', '12344'], ['11223', '11233', '12233'], ['11123', '12223', '12333'], ['11122', '11222'], ['11112', '12222'], ['11111']]

def puzzle(filecontent):
    result = 0
    # insert solution here
    
    parsed_hands = {}
    hands_and_bids = {}
    for line in filecontent:
        hand, bid = line.split()
        
        # parse hand
        card_map = {}
        next_map = 1
        parsed_hand = []
        for card in hand:
            if not card in card_map:
                card_map[card] = next_map
                next_map += 1
            parsed_hand.append(card_map[card])
        parsed_hand.sort()
        parsed_hand = ''.join([str(x) for x in parsed_hand])
        
        rank_in_hands = 0
        for i in range(len(hands)):
            if parsed_hand in hands[i]:
                break
            rank_in_hands += 1 
        
        if rank_in_hands not in parsed_hands:
            parsed_hands[rank_in_hands] = []
        parsed_hands[rank_in_hands].append(hand)
        hands_and_bids[hand] = int(bid)
    parsed_hands = dict(sorted(parsed_hands.items()))
    
    final_hands_ranked = []
    for _, disputed_hands in parsed_hands.items():
        valued_hands = []
        for hand in disputed_hands:
            valued_hand = []
            for card in hand:
                valued_hand.append(ranks[card])
            valued_hands.append((valued_hand, hand))
        valued_hands.sort()
        for _, hand in valued_hands:
            final_hands_ranked.append(hand)
    
    for i in range(len(final_hands_ranked)):
        result += (i + 1) * hands_and_bids[final_hands_ranked[i]]

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