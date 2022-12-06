from parse import *

test = False

if test:
    file_string = "test.txt"
    # 1 = 2
    # 2 = 4
else:
    file_string = "puzzle.txt"
    # 1 = 471
    # 2 = 888

with open(file_string, "r") as input_string:
    pairs = input_string.read().splitlines()

print( "PART 1:", sum([any([set(range(a, b+1)).issubset(set(range(c, d+1))) or set(range(c, d+1)).issubset(set(range(a, b+1)))]) for a, b, c, d, in [list(parse("{:d}-{:d},{:d}-{:d}", group)) for group in pairs]]) )
print( "PART 2:", sum([any([set(range(a, b+1)) & set(range(c, d+1)) or set(range(c, d+1)) & set(range(a, b+1))]) for a, b, c, d, in [list(parse("{:d}-{:d},{:d}-{:d}", group)) for group in pairs]]) )
