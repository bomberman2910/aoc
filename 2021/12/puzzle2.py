from collections import defaultdict, deque

TEST = False

def trace(map, dbls):
    ct = 0
    tracker = deque([("start", set(["start"]), False)])
    while tracker:
        p, seen, visited = tracker.popleft()
        if p == "end":
            ct += 1
            continue
        for c in map[p]:
            if c not in seen:
                seen_cp = set(seen)
                if c.islower():
                    seen_cp.add(c)
                tracker.append((c, seen_cp, visited))
            elif c in seen and not visited and c not in ["start", "end"] and dbls:
                tracker.append((c, seen, c))
    return ct

def puzzle(filecontent):
    map = defaultdict(list)
    for line in filecontent:
        p, c = line.split('-')
        map[p].append(c)
        map[c].append(p)
    print(trace(map, True))
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