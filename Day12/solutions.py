import string


class Map:
    def __init__(self, data):
        self.layout = data
        self.trail = [[['.'] for _ in range(len(data[0]))] for _ in range(len(data))]
        self.start = []
        self.position = []
        self.end = []
        self.elevation = 0
        self.visited = []
        self.moves = 0

        for i in range(len(data)):
            for j in range(len(data[0])):
                if self.layout[i][j] == 'S':
                    self.start = [i, j]
                elif self.layout[i][j] == 'E':
                    self.end = [i, j]
            if self.start and self.end:
                break
        self.position = self.end.copy()
        self.elevation = self.get_elevation(self.position[0], self.position[1])

    def print_layout(self):
        for r in range(len(self.layout)):
            line = ''
            for c in range(len(self.layout[0])):
                line += '*' if [r, c] == self.position else self.layout[r][c]
            print(line)

    def print_trail(self):
        for r in range(len(self.trail)):
            line = ''
            for c in range(len(self.trail[0])):
                if [r, c] == self.start:
                    line += 'S'
                elif [r, c] == self.end:
                    line += 'E'
                elif [r, c] == self.position:
                    line += '*'
                else:
                    last_move = self.trail[r][c][-1]
                    if last_move == 'up':
                        line += '^'
                    elif last_move == 'down':
                        line += 'V'
                    elif last_move == 'left':
                        line += '<'
                    elif last_move == 'right':
                        line += '>'
                    else:
                        line += self.layout[r][c]
            print(line)
        print(f"Climbs made {self.moves}")

    def get_elevation(self, x, y):
        return ('S' + string.ascii_lowercase + 'E').find(self.layout[x][y])

    def get_surroundings(self):
        return {'up': self.get_elevation(self.position[0] - 1, self.position[1]) if self.position[0] > 0 else -1,
                'down': self.get_elevation(self.position[0] + 1, self.position[1]) if self.position[0] < len(self.layout) - 1 else -1,
                'left': self.get_elevation(self.position[0], self.position[1] - 1) if self.position[1] > 0 else -1,
                'right': self.get_elevation(self.position[0], self.position[1] + 1) if self.position[1] < len(self.layout[0]) - 1 else -1}

    def move(self):
        next_moves = dict(sorted(self.get_surroundings().items(), key=lambda i: i[1]))
        old_pos = self.position.copy()
        new_pos = old_pos.copy()
        moved = False
        
        print(f'Checking {next_moves} against {self.elevation}')
        print(f'Trail for {self.position}: {self.trail[self.position[0]][self.position[1]]}')
        
        
        
        for k, v in next_moves.items():
            if k in self.trail[old_pos[0]][old_pos[-1]]:
                continue
            if v in [self.elevation, self.elevation-1]:
                if k == 'up':
                    new_pos[0] -= 1
                    if new_pos in self.visited:
                        new_pos[0] += 1
                        continue
                elif k == 'down':
                    new_pos[0] += 1
                    if new_pos in self.visited:
                        new_pos[0] -= 1
                        continue
                elif k == 'right':
                    new_pos[0] += 1
                    if new_pos in self.visited:
                        new_pos[1]-= 1
                        continue
                    new_pos[1] += 1
                elif k == 'left':
                    new_pos[1] -= 1
                    if new_pos in self.visited:
                        new_pos[1] += 1
                        continue
                    
                    
                print(f'Moving {k} from {old_pos}({self.layout[old_pos[0]][old_pos[1]]}) to {new_pos}({self.layout[new_pos[0]][new_pos[1]]})')
                moved = True
                self.moves += 1
                self.visited.append(old_pos)
                self.position = new_pos
                self.elevation = self.get_elevation(new_pos[0], new_pos[1])
                self.trail[old_pos[0]][old_pos[1]].append(k)
                self.print_trail()
                break
        if not moved:
            self.moves -= 1
            print(f'{self.visited}')
            last = self.visited.pop()
            print(f'Backtracking from {self.position}({self.layout[self.position[0]][self.position[1]]}) to {last}({self.layout[last[0]][last[1]]})')
            
            self.position = [last[0], last[1]]
            self.move()
        return


test = False
file_string = "test.txt" if test else "puzzle.txt"
with open(file_string, "r") as input_string:
    map = Map([[*i] for i in input_string.read().splitlines()])
    print(f'Starting position {map.position} with elevation {map.elevation}')
    while map.position != map.start:
        map.move()
    map.print_trail()
# 31 / <385
# 