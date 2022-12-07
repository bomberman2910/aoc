TEST = True
TEST_SOLUTION = 95437 # add solution for test input here

SIZE_LIMIT = 100000

directory_sizes = []

class node(object):
    def __init__(self):
        self.name=None
        self.node=[]
        self.otherInfo = []
        self.prev=None
    def nex(self,child):
        "Gets a node by number"
        return self.node[child]
    def prev(self):
        return self.prev
    def goto(self,data):
        "Gets the node by name"
        for child in range(0,len(self.node)):
            if(self.node[child].name==data):
                return self.node[child]
    def has_child(self, name):
        for child in range(0,len(self.node)):
            if(self.node[child].name==name):
                return True
    def get_sizes(self):
        size = 0
        for file_size, _ in self.otherInfo:
            size += file_size
        for node in self.node:
            size += node.get_sizes()
        directory_sizes.append(size)
        return size
    def add(self):
        node1=node()
        self.node.append(node1)
        node1.prev=self
        return node1

def puzzle(filecontent):
    result = 0
    # insert solution here

    directory_sizes.clear()

    commands = []
    current_command = ('', [])
    for i in range(len(filecontent)):
        if(filecontent[i].startswith('$')):
            commands.append(current_command)
            current_command = (filecontent[i].lstrip('$').strip(), [])
        else:
            current_command[1].append(filecontent[i])
    commands = commands[1 : ]

    filesystem = None
    current_position = None

    for command, output in commands:
        if(command.startswith('cd')):
            destination = command.split(' ')[1]
            if(filesystem is None):
                filesystem = node()
                current_position = filesystem
                current_position.name = destination
            elif(destination == '..'):
                current_position = current_position.prev
            else:
                current_position = current_position.goto(destination)
        elif(command.startswith('ls')):
            for line in output:
                type_size, name = line.split(' ')
                if(type_size == 'dir'):
                    new_folder = current_position.add()
                    new_folder.name = name
                else:
                    current_position.otherInfo.append((int(type_size), name))

    filesystem.get_sizes()

    for size in directory_sizes:
        if(size <= 100000):
            result += size

    return result

def solve(input_filename):
    file = open(input_filename, "r")
    content = file.read().splitlines()
    return puzzle(content)

if(TEST):
    testsolution = solve("test.txt")
    if(testsolution == TEST_SOLUTION):
        print("Solution for test input correct")
        regularsolution = solve("input.txt")
        print("Answer for main input", regularsolution)
    else:
        print(f"Solution for test input incorrect! (expected: {TEST_SOLUTION}; is: {testsolution})")
else:
    solve("input.txt")