from queue import LifoQueue

TEST = True

def puzzle(filecontent):
    score = 0
    for i in range(len(filecontent)):
        chunkstarts = LifoQueue()
        chars = list(filecontent[i])
        for j in range(len(chars)):
            if(chars[j] == '(' or chars[j] == '[' or chars[j] == '{' or chars[j] == '<'):
                chunkstarts.put(chars[j])
            elif(chars[j] == ')'):
                laststart = chunkstarts.get()
                if(laststart != '('):
                    if(j < len(chars) - 1):
                        print("Error in line", i, "at position", j, "(expected ( from stack, got", laststart, "instead)")
                    else:
                        print("Line", i, "incomplete")
                    score += 3
                    break
            elif(chars[j] == ']'):
                laststart = chunkstarts.get()
                if(laststart != '['):
                    if(j < len(chars) - 1):
                        print("Error in line", i, "at position", j, "(expected [ from stack, got", laststart, "instead)")
                    else:
                        print("Line", i, "incomplete")
                    score += 57
                    break
            elif(chars[j] == '}'):
                laststart = chunkstarts.get()
                if(laststart != '{'):
                    if(j < len(chars) - 1):
                        print("Error in line", i, "at position", j, "(expected { from stack, got", laststart, "instead)")
                    else:
                        print("Line", i, "incomplete")
                    score += 1197
                    break
            elif(chars[j] == '>'):
                laststart = chunkstarts.get()
                if(laststart != '<'):
                    if(j < len(chars) - 1):
                        print("Error in line", i, "at position", j, "(expected < from stack, got", laststart, "instead)")
                    else:
                        print("Line", i, "incomplete")
                    score += 25137
                    break
    print(score)
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