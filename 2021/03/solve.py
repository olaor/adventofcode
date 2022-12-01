#!/usr/bin/env python

import sys

input = [ x.strip() for x in open(sys.argv[1]).readlines() ]

index = 0
matrix = [''] * len(input[0]) 

# Find ALL the bits!
for value in input:
    index = 0
    for bit in value:
        matrix[index] += bit
        index += 1

# Determine gamma and epsilon values
gammabits = ''
epsilonbits = ''
for bitstream in matrix:
    ones = bitstream.count('1')
    zeroes = bitstream.count('0')

    if ones > zeroes:
        gammabits += '1'
        epsilonbits += '0'

    if ones < zeroes:
        gammabits += '0'
        epsilonbits += '1'

gammarate = int(gammabits, 2)
epsilonrate = int(epsilonbits, 2)

consumption = gammarate * epsilonrate

print("Power consumption:", consumption)
