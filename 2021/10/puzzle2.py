from queue import LifoQueue

TEST = False

def puzzle(filecontent):
    scores = []
    for i in range(len(filecontent)):
        chunkstarts = LifoQueue()
        chars = list(filecontent[i])
        error = False
        for j in range(len(chars)):
            if(chars[j] == '(' or chars[j] == '[' or chars[j] == '{' or chars[j] == '<'):
                chunkstarts.put(chars[j])
            elif(chars[j] == ')'):
                laststart = chunkstarts.get()
                if(laststart != '('):
                    print("Error in line", i, "at position", j, "(expected ( from stack, got", laststart, "instead)")
                    error = True
                    break
            elif(chars[j] == ']'):
                laststart = chunkstarts.get()
                if(laststart != '['):
                    print("Error in line", i, "at position", j, "(expected [ from stack, got", laststart, "instead)")
                    error = True
                    break
            elif(chars[j] == '}'):
                laststart = chunkstarts.get()
                if(laststart != '{'):
                    print("Error in line", i, "at position", j, "(expected { from stack, got", laststart, "instead)")
                    error = True
                    break
            elif(chars[j] == '>'):
                laststart = chunkstarts.get()
                if(laststart != '<'):
                    print("Error in line", i, "at position", j, "(expected < from stack, got", laststart, "instead)")
                    error = True
                    break
        if(not error and not chunkstarts.empty()):
            missing = list(chunkstarts.queue)
            print("Line", i, "incomplete (Missing", missing, "in endings)")
            score = 0
            while not chunkstarts.empty():
                char = chunkstarts.get()
                score *= 5
                if(char == '('):
                    score += 1
                elif(char == '['):
                    score += 2
                elif(char == '{'):
                    score += 3
                elif(char == '<'):
                    score += 4
            scores.append(score)
    scores = sorted(scores)
    middleindex = (len(scores) - 1) // 2
    print(scores, middleindex)
    print(scores[middleindex])
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