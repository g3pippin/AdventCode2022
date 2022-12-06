from parse import *

test = False

if test:
    file_string = "test.txt"
else:
    file_string = "puzzle.txt"

input_file = open(file_string, "r")
input_string = input_file.read()
input_file.close()

map_input, moves_list = map(lambda x: x.splitlines(True), input_string.split("\n\n"))
map_list = [list(line[i:i + 4].strip() for i in range(0, len(line) + 1, 4)) for line in map_input]
stacks_part1 = [[cell.strip() for cell in row if cell.strip()] for row in list(zip(*reversed(map_list)))]
stacks_part2 = stacks_part1

# Part 1 Solution
for move in moves_list:
    num, source, dest = map(int, parse("move {} from {} to {}", move).fixed)
    for x in range(num):
        stacks_part1[dest - 1].append(stacks_part1[source - 1].pop())
print( "PART 1:", ''.join(stack[-1] for stack in stacks_part1).replace("[", "").replace("]", "") )

# Part 2 Solution
for move in moves_list:
    num, source, dest = map(int, parse("move {} from {} to {}", move).fixed)
    source_stack_after, stack_moving = stacks_part2[source - 1][:-num], stacks_part2[source - 1][-num:]
    stacks_part2[source - 1] = source_stack_after
    stacks_part2[dest - 1].extend(stack_moving)
print( "PART 2:", ''.join(stack[-1] for stack in stacks_part2).replace("[", "").replace("]", "") )