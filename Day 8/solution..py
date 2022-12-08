test = False
file_string = "test.txt" if test else "puzzle.txt"

def getTreeData(row, column):
    report = {}
    left = [*reversed(forest[row][:column])]
    left_score = len(left) \
        if [x+1 for x, val in enumerate(left) if val >= forest[row][column]] == [] \
        else [x+1 for x, val in enumerate(left) if val >= forest[row][column]][0]
    
    right = forest[row][column+1:]
    right_score = len(right) \
        if [x + 1 for x, val in enumerate(right) if val >= forest[row][column]] == [] \
        else [x + 1 for x, val in enumerate(right) if val >= forest[row][column]][0]
    
    top = [*reversed(forest_transpose[column][:row])]
    top_score = len(top)\
        if [x + 1 for x, val in enumerate(top) if val >= forest[row][column]] == [] \
        else [x + 1 for x, val in enumerate(top) if val >= forest[row][column]][0]
    
    bot = forest_transpose[column][row+1:]
    bot_score = len(bot) \
        if [x + 1 for x, val in enumerate(bot) if val >= forest[row][column]] == [] \
        else [x + 1 for x, val in enumerate(bot) if val >= forest[row][column]][0]

    report['left'] = forest[row][column] > max(left)
    report['right'] = forest[row][column] > max(right)
    report['top'] = forest[row][column] > max(top)
    report['bot'] = forest[row][column] > max(bot)
    report['score'] = left_score * right_score * top_score * bot_score
    return report


with open(file_string, "r") as input_string:
    data = input_string.read()
    forest = [[*t] for t in data.splitlines()]
    forest_transpose = list(map(list, zip(*forest)))
    
    visible = len(forest)*2 + len(forest[0])*2 - 4
    max_score = 0
    for r, c in [[x,y] for y in range(1, len(forest)-1) for x in range(1, len(forest[0])-1)]:
        tree = getTreeData(r, c)
        visible += 1 if (tree['left'] or tree['right'] or tree['top'] or tree['bot']) else 0
        max_score = tree['score'] if tree['score'] > max_score else max_score
    print(f'P1: visible trees {visible}')
    print(f'P2: top scenic score {max_score}')
