test = False
# file_string = "test1.txt" if test else "puzzle.txt"
file_string = "test2.txt" if test else "puzzle.txt"


def layout(track, visit):
    grid = 50
    print(''.join(['.' for a in range(-grid, grid)]))
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
        if '#' in list(layout_row) or 's' in list(layout_row):
            print(layout_row)
    print(''.join(['.' for a in range(-grid, grid)]))


def check_rope(check):
    for num in range(0, len(check)-1):
        surroundings = []
        for i in [i for i in range(check[num+1][0]-1, check[num+1][0]+2)]:
            for j in [j for j in range(check[num+1][1]-1, check[num+1][1]+2)]:
                surroundings.append([i, j])
        if check[num] not in surroundings:
            for row, column in [[h - t for h, t in zip(check[num], check[num+1])]]:
                if row > 1:
                    check[num+1][0] += 1
                    if column > 0:
                        check[num+1][1] += 1
                    elif column < 0:
                        check[num+1][1] -= 1
                elif row < -1:
                    check[num+1][0] -= 1
                    if column > 0:
                        check[num+1][1] += 1
                    elif column < 0:
                        check[num+1][1] -= 1
                elif column > 1:
                    check[num+1][1] += 1
                    if row < 0:
                        check[num+1][0] -= 1
                    elif row > 0:
                        check[num+1][0] += 1
                elif column < -1:
                    check[num+1][1] -= 1
                    if row < 0:
                        check[num+1][0] -= 1
                    elif row > 0:
                        check[num+1][0] += 1
    return check


def get_locations(data_input, rope_length, print_layout):
    rope = [[0, 0] for x in range(0, rope_length)]
    locations = [[0, 0]]
    for d, m in [line.split(" ") for line in data_input]:
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
    if print_layout:
        layout(rope, locations)
    return len(locations)


with open(file_string, "r") as input_string:
    data = input_string.read().splitlines()
    for length in [2, 5, 10, 15]:
        # Change boolean for picture of travel
        results = get_locations(data, length, True)
        print(f'The rope with length {length} visited {results} locations')
