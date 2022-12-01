#!/usr/bin/env python

import sys

crabs = [ int(x) for x in open(sys.argv[1]).readline().strip().split(',') ]

costs = {}

for pos in range(min(crabs), max(crabs) +1):
    cost = 0
    for crab in crabs:
        cost += abs(crab - pos)
    costs[pos] = cost 

lowcost = min(list(costs.values()))
print("Lowest cost:", lowcost)
