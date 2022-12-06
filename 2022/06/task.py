#!/usr/bin/env python
import sys

line = open(sys.argv[1]).readline().strip()

uniques = int(sys.argv[2])

result = 0

buffer = []
i = 0
for c in line:
    i += 1
    buffer.append(c)
    if len(buffer) > uniques:
        buffer.pop(0)
    if len(buffer) < uniques:
        continue
    test = {}
    for x in buffer:
        test[x] = True
    print(test)
    if len(test.keys()) == uniques:
        result = i
        break

    
print("Solution part one:")
print(result)
#print("Solution part two:")
#print(partials)



