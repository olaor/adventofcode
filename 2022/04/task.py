#!/usr/bin/env python
import sys

overlaps = 0
partials = 0

def intit(s):
    return [ int(x) for x in s ]


for line in open(sys.argv[1]).readlines():
    line = line.strip()
    if not line:
        continue

    overlapped = False

    one, two = line.split(",")

    startone, endone = intit(one.split("-"))
    starttwo, endtwo = intit(two.split("-"))

    
    if (startone <= starttwo) and (endone >= endtwo): 
        overlaps += 1 
        overlapped = True
        #print(line+" first")
    if (starttwo <= startone) and (endtwo >= endone): 
        if not overlapped:
            overlaps += 1 
        #print(line+" second")        
        

    onerange = list(range(startone, endone + 1))
    tworange = list(range(starttwo, endtwo + 1))
    result = [ True for x in onerange if x in tworange ]
    if bool(result):
        partials += 1


print("Solution part one:")
print(overlaps)
print("Solution part two:")
print(partials)



