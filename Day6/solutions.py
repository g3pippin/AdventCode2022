test = False

if test:
    file_string = "test.txt"
    # Part 1 = 7
    # Part 2 = 19
else:
    file_string = "puzzle.txt"
    # Part 1 = 1920
    # Part 2 = 2334

with open(file_string, "r") as input_string:
    buffer = input_string.read()
    print( "PART 1:", [len(set(buffer[subroutine:subroutine+4])) for subroutine in range(0, len(buffer)-4)].index(4)+4 )

    print( "PART 2:", [len(set(buffer[subroutine:subroutine+14])) for subroutine in range(0, len(buffer)-14)].index(14)+14 )