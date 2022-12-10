test = False
file_string = "test.txt" if test else "puzzle.txt"


def check_reg(v, s, r, c):
    if c%40 in [r-1, r, r+1]:
        s.append(c)
        
    if c in [20, 60, 100, 140, 180, 220]:
        v.append(c * r)
    return v, s


with open(file_string, "r") as input_string:
    data = input_string.read().splitlines()

signals = []
sprite = []

reg = 1
cycle = 0

for update in [line.split() for line in data]:
    if update[0] == 'noop':
        signals, sprite = check_reg(signals, sprite, reg, cycle)
        cycle += 1
    elif update[0] == 'addx':
        for i in range(2):
            signals, sprite = check_reg(signals, sprite, reg, cycle)
            cycle += 1
        reg += int(update[1])

print('P1:', sum(signals)) # 13140 / 12540
# Part 2
print('P2') # FECZELHE
for i in range(6):
    crt = ''
    for j in range(40):
        if j+(i*40) in sprite:
            crt += '#'
        else:
            crt += '.'
    print(crt)