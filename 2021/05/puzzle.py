inputfile = open("input.txt", "r")
rawfilecontent = inputfile.readlines()
filecontent = []
for line in rawfilecontent:
    filecontent.append(line.removesuffix("\n"))

MAP_SIZE = 1000

# get lines
lines = []
for line in filecontent:
    points = line.split(' -> ')
    start = points[0].split(',')
    end = points[1].split(',')
    lines.append((int(start[0]), int(start[1]), int(end[0]), int(end[1])))

onedimmap = [0 for i in range(MAP_SIZE * MAP_SIZE)]

for line in lines:
    startx, starty, endx, endy = line
    if(startx != endx and starty != endy):
        stepx = -1 if endx < startx else 1
        stepy = -1 if endy < starty else 1
        posx = startx
        posy = starty
        length = abs(startx - endx) + 1
        for i in range(length):
            onedimmap[posy * MAP_SIZE + posx] += 1
            posx += stepx
            posy += stepy
    if(startx == endx): # vertical
        step = -1 if endy < starty else 1
        end = endy + 1 if step == 1 else endy - 1
        for i in range(starty, end, step):
            onedimmap[i * MAP_SIZE + startx] += 1
    elif(starty == endy): # horizontal
        step = -1 if endx < startx else 1
        end = endx + 1 if step == 1 else endx - 1
        for i in range(startx, end, step):
            onedimmap[starty * MAP_SIZE + i] += 1

dangerouspoints = 0
for i in onedimmap:
    if(i >= 2):
        dangerouspoints += 1

print(dangerouspoints)

# for y in range(MAP_SIZE):
#     line = ''
#     for x in range(MAP_SIZE):
#         point = str(onedimmap[y * MAP_SIZE + x])
#         if(point == '0'):
#             line += '.'
#         else:
#             line += point
#     print(line)