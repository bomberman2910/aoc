inputfile = open("input_1.txt", "r")
rawfilecontent = inputfile.readlines()
filecontent = []
for line in rawfilecontent:
    filecontent.append(line.removesuffix("\n"))

mostcommonincolumn = []

for i in range(len(filecontent[0])):
    ones = 0
    zeros = 0
    for element in filecontent:
        if(element[i] == "1"):
            ones += 1
        else:
            zeros += 1
    if(ones > zeros):
        mostcommonincolumn.append((i, "1"))
    elif(zeros > ones):
        mostcommonincolumn.append((i, "0"))

gammastring = ""
epsilonstring = ""
for _, v in mostcommonincolumn:
    gammastring += v
    if(v=="0"):
        epsilonstring += "1"
    else:
        epsilonstring += "0"

gamma = int(gammastring, 2)
epsilon = int(epsilonstring, 2)

print(gammastring, gamma)
print(epsilonstring, epsilon)
print(epsilon * gamma)
