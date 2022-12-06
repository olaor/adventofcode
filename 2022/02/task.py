#!/usr/bin/env python
import sys


shapes = { "X": 1,
    "Y": 2,
    "Z": 3 
    }


orock = "A"
mrock = "X"
opaper = "B"
mpaper = "Y"
oscissors = "C"
mscissors = "Z"

mdraw = "Y"
mlose = "X"
mwin = "Z"

points = 0
parttwopoints = 0

lose = 0
draw = 3
win = 6

for line in open(sys.argv[1]).readlines():
    line = line.strip()
    if not line:
        continue
    omove, mmove = line.split()
    
    result = 0
    secresult = 0

    if omove == orock:
        if mmove == mrock: result = draw
        if mmove == mpaper: result = win
        if mmove == mscissors: result = lose

        if mmove == mdraw: secresult, secmove = (draw, mrock)
        if mmove == mlose: secresult, secmove = (lose, mscissors)
        if mmove == mwin: secresult, secmove = (win, mpaper)


    if omove == opaper:
        if mmove == mrock: result = lose
        if mmove == mpaper: result = draw
        if mmove == mscissors: result = win

        if mmove == mdraw: secresult, secmove = (draw, mpaper)
        if mmove == mlose: secresult, secmove = (lose, mrock)
        if mmove == mwin: secresult, secmove = (win, mscissors)

    if omove == oscissors:
        if mmove == mrock: result = win
        if mmove == mpaper: result = lose
        if mmove == mscissors: result = draw

        if mmove == mdraw: secresult, secmove = (draw, mscissors)
        if mmove == mlose: secresult, secmove = (lose, mpaper)
        if mmove == mwin: secresult, secmove = (win, mrock)
    

    points += result + shapes[mmove]
    parttwopoints += secresult + shapes[secmove]

print("Solution part one:")
print(points)
print("Solution part two:")
print(parttwopoints)



