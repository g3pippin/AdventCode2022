test = False
# file_string = "test1.txt" if test else "puzzle.txt"
file_string = "test2.txt" if test else "puzzle.txt"


def layout(track, visit):
    grid = 50
    check_row = ''.join(['.' for a in range(-grid, grid)])
    last_row = ''
    for r in range(-grid, grid):
        layout_row = ''
        for c in range(-grid, grid):
            if [r, c] in track:
                layout_row += str(track.index([r, c])) if track.index([r, c]) > 0 else 'H'
            elif [r, c] == [0, 0]:
                layout_row += 's'
            elif [r, c] in visit:
                layout_row += '#'
            else:
                layout_row += '.'
        if check_row != last_row != layout_row:
            print(layout_row)
        last_row = layout_row


def check_rope(check):
    for num in range(0, len(check)-1):
        head_loc = check[num]
        tail_loc = check[num+1]
        surroundings = []
        for i in [i for i in range(tail_loc[0]-1, tail_loc[0]+2)]:
            for j in [j for j in range(tail_loc[1]-1, tail_loc[1]+2)]:
                surroundings.append([i, j])
        if head_loc not in surroundings:
            for row, column in [[h - t for h, t in zip(head_loc, tail_loc)]]:
                if row > 1:
                    tail_loc[0] += 1
                    if column > 0:
                        tail_loc[1] += 1
                    elif column < 0:
                        tail_loc[1] -= 1
                elif row < -1:
                    tail_loc[0] -= 1
                    if column > 0:
                        tail_loc[1] += 1
                    elif column < 0:
                        tail_loc[1] -= 1
                elif column > 1:
                    tail_loc[1] += 1
                    if row < 0:
                        tail_loc[0] -= 1
                    elif row > 0:
                        tail_loc[0] += 1
                elif column < -1:
                    tail_loc[1] -= 1
                    if row < 0:
                        tail_loc[0] -= 1
                    elif row > 0:
                        tail_loc[0] += 1
        check[num] = head_loc
        check[num+1] = tail_loc
    return check


def get_locations(input, rope_length, print):
    rope = [[0,0] for x in range(0, rope_length)]
    locations = [[0,0]]

    for d, m in [line.split(" ") for line in input]:
        for x in range(int(m)):
            if d == 'R':
                rope[0][1] += 1
            elif d == 'L':
                rope[0][1] -= 1
            elif d == 'U':
                rope[0][0] -= 1
            elif d == 'D':
                rope[0][0] += 1
            
            rope = check_rope(rope)
            if rope[rope_length-1] not in locations:
                locations.append([rope[rope_length-1][0], rope[rope_length-1][1]])
    if print:
        layout(rope, locations)
    return len(locations)


with open(file_string, "r") as input_string:
    data = input_string.read().splitlines()

    # Change boolean for picture of travel
    rope_2 = get_locations(data, 2, True)
    rope_10 = get_locations(data, 10, True)

    print(f'The rope with length {2} visited {rope_2} locations') # 6494
    print(f'The rope with length {10} visited {rope_10} locations') # 2691