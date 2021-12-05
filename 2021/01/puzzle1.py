inputfile = open("Puzzle1_Input.txt", "r")
rawfilecontent = inputfile.readlines()
filecontent = []
for num in rawfilecontent:
    filecontent.append(int(num.removesuffix("\n")))
increased = 0
decreased = 0
for i in range(1, len(filecontent)):
    if(filecontent[i] < filecontent[i - 1]):
        decreased += 1
    elif(filecontent[i] > filecontent[i-1]):
        increased += 1

print("Increased: ", increased)
print("Decreased: ", decreased)