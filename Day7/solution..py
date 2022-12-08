test = False
file_string = "test.txt" if test else "puzzle.txt"

def get_structure(data):
    tree = {}
    path = []
    for line in data:
        command = line.split(" ")
        size = 0
        if 'dir' in command or ('$' in command and 'cd' not in command):
            continue
        elif 'cd' in command:
            if '..' in command:
                path.pop()
            else:
                branch = command[2] if '/' in command else ''.join([path[-1], command[2]])
                path.append(branch)
        else:
            size = int(command[0])
        if size > 0:
            for p in path:
                tree[p] = tree.get(p, 0) + size
    return tree


with open(file_string, "r") as input_string:
    data = input_string.read().splitlines()
    directory = get_structure(data)
    print('P1:', sum([v for v in directory.values() if v <= 100000]))
    print('P2:', min([v for v in directory.values() if v >= (30000000-(70000000-directory['/']))]) ) 

# Part 1 = 95437
# Part 1 = 1084134
# Part 2 = 24933642
# Part 2 = 6183184