test = False

if test:
    file_string = "test.txt"
    # 1 = 15
    # 2 = 12
else:
    file_string = "puzzle.txt"
    # 1 = 12586
    # 2 = 13193

input_file = open(file_string, "r")
input_string = input_file.read().splitlines()
input_file.close()

score = [3, 0, 6]
guide1 = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}

code = [1, 2, 3]
guide2 = {"A": 1, "X": -2, "B": 2, "Y": -1, "C": 3, "Z": -3}

print("PART 1:", sum([score[x - y] + y for x, y in [[guide1.get(h, h) for h in match.split(" ")] for match in input_string]]))
print("PART 2:", sum([score[x-code[x+y]] + code[x+y] for x, y in [[guide2.get(h, h) for h in match.split(" ")] for match in input_string]]) )