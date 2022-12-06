from parse import *

test = False

if test:
    file_string = "test.txt"
    # CMZ
    # MCD
else:
    file_string = "puzzle.txt"
    # VJSFHWGFT
    # LCTQFBVZV

with open(file_string, "r") as input_string:
    map_input, moves_list = map(lambda x: x.splitlines(), input_string.read().split("\n\n"))

# Split map into chunks of 4 to capture column value
map_list = [[line[i:i + 4].strip().replace("[", "").replace("]", "") for i in range(0, len(line) + 1, 4)] for line in map_input]

# Reverse, transpose and strip whitespace of map; shoutout to reddit for assistance
stack1 = [[cell.strip() for cell in row if cell.strip()] for row in list(zip(*reversed(map_list)))]
stack2 = [[cell.strip() for cell in row if cell.strip()] for row in list(zip(*reversed(map_list)))]
stack2_test = [[cell.strip() for cell in row if cell.strip()] for row in list(zip(*reversed(map_list)))]

moves = [[x, y, z] for x, y, z in [parse("move {:d} from {:d} to {:d}", move) for move in moves_list]]

[[stack1[t-1].append(stack1[f-1].pop()) for x in range(m)] for m, f, t in moves]
print("P1:", ''.join(s.pop() for s in stack1) )

for m, f, t in moves:
    stack2[t-1].extend(stack2[f-1][-m:])
    stack2[f-1] = stack2[f-1][:-m]
print( "P2:", ''.join(s[-1] for s in stack2) )