from parse import *
import math


def init_monkeys(data):
    data_set = {}
    for line in [i.splitlines() for i in data]:
        num = parse('Monkey {:d}:', line[0].strip())[0]
        data_set[num] = {'inspect': 0, 'items':[], 'op': '', 'opval': 0, 'test': 0, 'true': 0, 'false': 0}
        
        data_set[num]['items'] = [int(l) for l in line[1][line[1].find(':') + 1:].strip().split(", ")]
        data_set[num]['op'], data_set[num]['opval'] = list(parse('Operation: new = old {} {}', line[2].strip()))
        data_set[num]['test'] = parse('Test: divisible by {:d}', line[3].strip())[0]
        data_set[num]['true'] = parse('If true: throw to monkey {:d}', line[4].strip())[0]
        data_set[num]['false'] = parse('If false: throw to monkey {:d}', line[5].strip())[0]
    return data_set
    

def inspect_worry(item_worry, monkey_operation, operation_value, modifier):
    update = item_worry if operation_value == 'old' else int(operation_value)
    if monkey_operation == "+":
        item_worry = item_worry + update
    elif monkey_operation == "*":
        item_worry = item_worry * update
    item_worry = item_worry % modifier
    return item_worry


def print_output(data):
    top = [v for v in sorted([data[k]['inspect'] for k in data.keys()])]
    print(f"Generated Answer {top[-2] * top[-1]}")


test = False
file_string = "test.txt" if test else "puzzle.txt"

with open(file_string, "r") as input_string:
    input_data = input_string.read().split("\n\n")

monkeys = init_monkeys(input_data).copy()
mod = math.prod([monkeys[m]['test'] for m in monkeys])

for _ in range(10000):
    for m in monkeys:
        for item in monkeys[m]['items']:
            monkeys[m]['inspect'] += 1
            item = inspect_worry(item, monkeys[m]['op'], monkeys[m]['opval'], mod)
            next_monkey = monkeys[m]['true'] if item % monkeys[m]['test'] == 0 else monkeys[m]['false']
            monkeys[next_monkey]['items'] += [item]
        monkeys[m]['items'] = []
print_output(monkeys)
