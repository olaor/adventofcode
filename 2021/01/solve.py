#!/usr/bin/env python

import sys

input = [ int(x) for x in open(sys.argv[1]).readlines() ]

larger = 0
measurement = None

for value in input:
    if measurement and (value > measurement):
        larger += 1
    measurement = value

print("Larger:", larger)
