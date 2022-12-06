import string
test = False

if test:
    file_string = "test.txt"
    # 1 = 157
    # 2 = 70
else:
    file_string = "puzzle.txt"
    # 1 = 7997
    # 2 = 2545

with open(file_string, "r") as input_string:
    rucksacks = input_string.read().splitlines()
    
    print( "PART 1:", sum(int(string.ascii_letters.find(l)+1) for l in [set(a).intersection(set(b)).pop() for a, b in [[r[:int(len(r)/2)], r[int(len(r)/2):]] for r in rucksacks]]) )
    print( "PART 2:", sum(int(string.ascii_letters.find(l)+1) for l in [set(a).intersection(set(b)).intersection(set(c)).pop() for a, b, c in [rucksacks[r:r+3] for r in range(0, len(rucksacks), 3)]]) )