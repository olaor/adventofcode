#!/usr/bin/env python

import sys

input = [ int(x) for x in open(sys.argv[1]).readlines() ]

larger = 0
index = 0
last = None

while index + 3 <= len(input):
    for slide in (0,1,2,3):
        value = sum(input[index + slide:index + slide + 3])
        if last and value > last:
            larger += 1
        last = value
    index += 4
    
print("Larger:", larger)
