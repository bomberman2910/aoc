import copy

inputfile = open("input_1.txt", "r")
rawfilecontent = inputfile.readlines()
filecontent = []
for line in rawfilecontent:
    filecontent.append(line.removesuffix("\n"))

def getmostcommonvalueincolumn(collection, column):
    ones = 0
    zeros = 0
    for element in collection:
        if(element[column] == "1"):
            ones += 1
        else:
            zeros += 1
    if(ones >= zeros):
        return "1"
    elif(zeros > ones):
        return "0"

oxygenlist = copy.deepcopy(filecontent)
columncounter = 0
while(len(oxygenlist) > 1):
    if(getmostcommonvalueincolumn(oxygenlist, columncounter) == "0"):
        hasnozeroincolumn = lambda e: e[columncounter] != "0"
        oxygenlist = list(filter(hasnozeroincolumn, oxygenlist))
    else:
        hasnooneincolumn = lambda e: e[columncounter] != "1"
        oxygenlist = list(filter(hasnooneincolumn, oxygenlist))
    columncounter += 1

oxygencounter = int(oxygenlist[0], 2)

co2list = copy.deepcopy(filecontent)
columncounter = 0
while(len(co2list) > 1):
    if(getmostcommonvalueincolumn(co2list, columncounter) == "0"):
        hasnozeroincolumn = lambda e: e[columncounter] != "1"
        co2list = list(filter(hasnozeroincolumn, co2list))
    else:
        hasnooneincolumn = lambda e: e[columncounter] != "0"
        co2list = list(filter(hasnooneincolumn, co2list))
    columncounter += 1

co2counter = int(co2list[0], 2)

print(oxygencounter)
print(co2counter)
print(oxygencounter * co2counter)
