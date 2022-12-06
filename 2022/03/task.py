#!/usr/bin/env python
import sys

pri = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

common = ''

badges = ''

result = 0
secresult = 0

i = 0
lines = []

for line in open(sys.argv[1]).readlines():
    line = line.strip()
    if not line:
        continue

    lines.append(line)
    i += 1
    if not i % 3:
        for x in lines[0]:
            if (x in lines[1]) and (x in lines[2]):
                badges += x
                break
        i = 0
        lines = []


    one = line[0:int(len(line)/2)]
    two = line[int(len(line)/2):]

    for item in one:
        if item in two:
            common += item
            break

for item in common:
    result += pri.index(item) + 1

for badge in badges:
    secresult += pri.index(badge) +1


print("Solution part one:")
print(result)
print("Solution part two:")
print(secresult)



