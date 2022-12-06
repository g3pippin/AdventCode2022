test = False

if test:
    file_string = "test.txt"
else:
    file_string = "puzzle.txt"

input_file = open(file_string, "r")
input_string = input_file.read()
input_file.close()

print( "Test Results:", test )
print( "PART 1:", sum(sorted([sum([int(cal) for cal in s.split("\n")]) for s in input_string.split("\n\n")], reverse=True)[:1]) )
print( "PART 2:", sum(sorted([sum([int(cal) for cal in s.split("\n")]) for s in input_string.split("\n\n")], reverse=True)[:3]) )