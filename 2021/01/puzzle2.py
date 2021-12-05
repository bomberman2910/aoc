inputfile = open("Puzzle1_Input.txt", "r")
rawfilecontent = inputfile.readlines()
filecontent = []
for num in rawfilecontent:
    filecontent.append(int(num.removesuffix("\n")))

groups = []
for i in range(len(filecontent) - 2):
    groups.append((i, filecontent[i] + filecontent[i + 1] + filecontent[i + 2]))

increased = 0
decreased = 0
for i in range(1, len(groups)):
    _, thisgroup = groups[i]
    _, prevgroup = groups[i - 1]
    if(thisgroup < prevgroup):
        decreased += 1
    elif(thisgroup > prevgroup):
        increased += 1

print("Increased: ", increased)
print("Decreased: ", decreased)