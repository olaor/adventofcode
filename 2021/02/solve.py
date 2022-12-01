#!/usr/bin/env python

import sys

h = 0
d = 0

for line in open(sys.argv[1]).readlines():
    move, num = line.split()
    num = int(num)

    if move == "forward":
        h += num
    if move == "down":
        d += num
    if move == "up":
        d -= num


print("Horizontal:", h)
print("Depth:", d)
print("Answer:", h * d)
