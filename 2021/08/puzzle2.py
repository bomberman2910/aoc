TEST = False

def puzzle(filecontent):
    codesum = 0
    for line in filecontent:
        patterns, code = line.split('|')[0].strip().split(), line.split('|')[1].strip().split()
        # find 1
        one = list(next(filter(lambda digit: len(digit) == 2, patterns), None))
        # find 7
        seven = list(next(filter(lambda digit: len(digit) == 3, patterns), None))
        # find element in seven that is not in one for segment A
        segment_a = list(set(seven) - set(one))[0]
        # find 4
        four = list(next(filter(lambda digit: len(digit) == 4, patterns), None))
        segments_bd = list(set(four) - set(one))
        twothreefive = list(filter(lambda digit: len(digit) == 5, patterns))
        three = list(list(filter(lambda digit: all(item in list(digit) for item in one), twothreefive))[0])
        segment_b = list(set(segments_bd) - set(three))[0]
        segment_d = list(set(segments_bd) - set(segment_b))[0]
        five = list(list(filter(lambda digit: segment_b in digit, twothreefive))[0])
        eight = list(next(filter(lambda digit: len(digit) == 7, patterns), None))
        segment_c = list(set(three) - set(five))[0]
        segment_f = list(set(one) - set(segment_c))[0]
        segment_g = list(set(three) - set((segment_a, segment_c, segment_d, segment_f)))[0]
        segment_e = list(set(eight) - set((segment_a, segment_b, segment_c, segment_d, segment_f, segment_g)))[0]
        
        # print(segment_a, segment_b, segment_c, segment_d, segment_e, segment_f, segment_g)

        new_zero = [segment_a, segment_b, segment_c, segment_e, segment_f, segment_g]
        new_one = [segment_c, segment_f]
        new_two = [segment_a, segment_c, segment_d, segment_e, segment_g]
        new_three = [segment_a, segment_c, segment_d, segment_f, segment_g]
        new_four = [segment_b, segment_c, segment_d, segment_f]
        new_five = [segment_a, segment_b, segment_d, segment_f, segment_g]
        new_six = [segment_a, segment_b, segment_d, segment_e, segment_f, segment_g]
        new_seven = [segment_a, segment_c, segment_f]
        new_eight = [segment_a, segment_b, segment_c, segment_d, segment_e, segment_f, segment_g]
        new_nine = [segment_a, segment_b, segment_c, segment_d, segment_f, segment_g]

        codenumbers = []
        for digit in code:
            if(all(item in new_one for item in list(digit))):
                codenumbers.append(1)
                continue
            if(all(item in new_seven for item in list(digit))):
                codenumbers.append(7)
                continue
            if(all(item in new_four for item in list(digit))):
                codenumbers.append(4)
                continue
            if(all(item in new_two for item in list(digit))):
                codenumbers.append(2)
                continue
            if(all(item in new_three for item in list(digit))):
                codenumbers.append(3)
                continue
            if(all(item in new_five for item in list(digit))):
                codenumbers.append(5)
                continue
            if(all(item in new_zero for item in list(digit))):
                codenumbers.append(0)
                continue
            if(all(item in new_six for item in list(digit))):
                codenumbers.append(6)
                continue
            if(all(item in new_nine for item in list(digit))):
                codenumbers.append(9)
                continue
            if(all(item in new_eight for item in list(digit))):
                codenumbers.append(8)
                continue
        codesum += int(''.join(str(i) for i in codenumbers))
        print(int(''.join(str(i) for i in codenumbers)))
    print(codesum)
    pass

def test():
    testfile = open("test.txt", "r")
    content = testfile.read().splitlines()
    puzzle(content)

if(TEST):
    test()
else:
    inputfile = open("input.txt", "r")
    filecontent = inputfile.read().splitlines()
    puzzle(filecontent)