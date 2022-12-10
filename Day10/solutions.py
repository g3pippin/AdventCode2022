test = False
file_string = "test.txt" if test else "puzzle.txt"

with open(file_string, "r") as input_string:
    data = input_string.read().splitlines()

    signal, sprite, reg, cycle = [], [], 1, 1
    for line in [row.split() for row in data]:
        count = 1 if line[0] == 'noop' else 2
        for _ in range(count):
            if cycle in [20, 60, 100, 140, 180, 220]:
                signal.append(cycle * reg)
            if (cycle-1) % 40 in [reg - 1, reg, reg + 1]:
                sprite.append(cycle-1)
            cycle += 1
        reg += 0 if line[0] == 'noop' else int(line[1])
    
    print('P1:', sum(signal)) # 13140 / 12540
    for i in range(6):
        crt = ''
        for j in range(40):
            crt += '#' if j+(i*40) in sprite else '.'
        print(crt) # FECZELHE
