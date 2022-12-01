#!/usr/bin/env python
import sys

class elfin:
    def __init__(self):
        self.calories = []
        self.total = 0
    
    def new(self, item):
        item = int(item)
        self.calories.append(item)
        self.total += item

elves = []
elf = elfin()
for line in open(sys.argv[1]).readlines():
    line = line.strip()
    if not line:
        elves.append(elf)
        elf = elfin()
        continue
    elf.new(line)


print("Part one:")
print(max([x.total for x in elves]))
print("Part two:")
calories = [x.total for x in elves]
calories.sort()
print(sum(calories[-3:]))

    
