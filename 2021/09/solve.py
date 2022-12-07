#!/usr/bin/python

import sys

map = []
for line in open(sys.argv[1]).readlines():
    line = line.strip()
    values = []
    for chr in line:
        values.append(int(chr))
    map.append(values)

lowpoints = []
ln = 0
for line in map:
    i = 0
    for loc in line:
        adjacent = [True,True,True,True]
        if ln > 0:
            adjacent[0] = map[ln - 1][i] > loc
        if ln < (len(map) - 1 ):
            adjacent[1] = map[ln + 1][i] > loc
        if i > 0:
            adjacent[2] = map[ln][i-1] > loc
        if i < len(line) -1 :
            adjacent[3] = map[ln][i+1] > loc

        if len(set(adjacent)) == 1 and set(adjacent).pop() == True:
            lowpoints.append(loc + 1)



        i += 1
    ln += 1

print(sum(lowpoints), lowpoints)

