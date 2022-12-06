#!/usr/bin/env python
import sys

pri = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

common = ''

result = 0

for line in open(sys.argv[1]).readlines():
    line = line.strip()
    if not line:
        continue

    one = line[0:int(len(line)/2)]
    two = line[int(len(line)/2):]

    for item in one:
        if item in two:
            common += item
            break

for item in common:
    result += pri.index(item) + 1



print("Solution part one:")
print(common,result)
#print("Solution part two:")
#print(parttwopoints)



