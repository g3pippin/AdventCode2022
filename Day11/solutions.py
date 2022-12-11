from parse import *
import math


class Monkey:
    def __init__(self, items, operation, value, divisible, true, false):
        self.inspections = 0
        self.items = items
        self.op = operation
        self.opval = value
        self.div = divisible
        self.true = true
        self.false = false

    def process_item(self, f, bored):
        self.inspections += 1
        update = self.items[0] if self.opval == 'old' else int(self.opval)
        if self.op == '+':
            self.items[0] = self.items[0] + update
        elif self.op == '*':
            self.items[0] = self.items[0] * update
        self.items[0] = math.floor(self.items[0] / 3) if bored else self.items[0] % f
        return self.true if self.items[0] % self.div == 0 else self.false


test = False
file_string = "test.txt" if test else "puzzle.txt"
with open(file_string, "r") as input_string:
    data = input_string.read().split("\n\n")

monkeys = []
for line in [i.splitlines() for i in data]:
    operation, value = list(parse('Operation: new = old {} {}', line[2].strip()))
    monkeys.append(Monkey(
        [int(l) for l in line[1][line[1].find(':') + 1:].strip().split(", ")],
        operation,
        value,
        parse('Test: divisible by {:d}', line[3].strip())[0],
        parse('If true: throw to monkey {:d}', line[4].strip())[0],
        parse('If false: throw to monkey {:d}', line[5].strip())[0]
    ))
factor = math.prod([m.div for m in monkeys])

boredom = False
rounds = 20 if boredom else 10000
for r in range(rounds):
    for m in range(len(monkeys)):
        for _ in range(len(monkeys[m].items)):
            next_monkey = monkeys[m].process_item(factor, boredom)
            monkeys[next_monkey].items.append(monkeys[m].items.pop(0))
print(math.prod(sorted([monkeys[x].inspections for x in range(len(monkeys))], reverse=True)[:2]))
# 10605 / 69918
# 2713310158 / 19573408701