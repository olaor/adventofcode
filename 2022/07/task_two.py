#!/usr/bin/env python
import sys


stacks = [[]]


for line in open(sys.argv[1]).readlines():
    line = line.replace("\n", "")
    if not line:
        continue

    parts = line.split()
    #print(parts)
    if parts[0] == "1":
        continue
    if parts[0] == "move":
        what = int(parts[1])
        fr = int(parts[3]) - 1
        to = int(parts[5])- 1
        moves = list(range(what))
        moves.reverse()
        print(moves)
        for crate in moves:
            item = stacks[fr].pop(crate)
            stacks[to].insert(0,item)
        #sys.exit()
        continue



    incrate = False
    stack = 0
    for i in range(len(line)-1):
        if ((i+1) % 4) == 0:
            stack += 1
            if len(stacks) < (stack + 1):
                stacks.append([])
            
            
        
        if line[i] == "[":
            incrate = True
            continue
        if line[i] == "]":
            incrate = False
        if incrate:
            stacks[stack].append(line[i])

    

print(stacks)

result = ""
for stack in stacks:
    if len(stack) > 0:
        result += stack[0]


print("Solution part one:")
print(result)
#print("Solution part two:")
#print(partials)



