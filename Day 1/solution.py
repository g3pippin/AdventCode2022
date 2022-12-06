test = False

if test:
    file_string = "test.txt"
else:
    file_string = "puzzle.txt"

with open(file_string, "r") as second_input:
    calories = second_input.read()
    print( "PART 1:", sum(sorted([sum([int(cal) for cal in s.split("\n")]) for s in calories.split("\n\n")], reverse=True)[:1]) )
    print( "PART 2:", sum(sorted([sum([int(cal) for cal in s.split("\n")]) for s in calories.split("\n\n")], reverse=True)[:3]) )