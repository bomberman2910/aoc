from queue import LifoQueue

TEST = False

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
                    score += 3
                    print("Error in line", i, "at position", j, "(expected ( from stack, got", laststart, "instead) 17")
                    break
            elif(chars[j] == ']'):
                laststart = chunkstarts.get()
                if(laststart != '['):
                    score += 57
                    print("Error in line", i, "at position", j, "(expected [ from stack, got", laststart, "instead) 23")
                    break
            elif(chars[j] == '}'):
                laststart = chunkstarts.get()
                if(laststart != '{'):
                    score += 1197
                    print("Error in line", i, "at position", j, "(expected { from stack, got", laststart, "instead) 29")
                    break
            elif(chars[j] == '>'):
                laststart = chunkstarts.get()
                if(laststart != '<'):
                    score += 25137
                    print("Error in line", i, "at position", j, "(expected < from stack, got", laststart, "instead) 35")
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