#!/usr/bin/env python

import sys

input = [ x.strip() for x in open(sys.argv[1]).readlines() ]


def countbits(input):
    matrix = [''] * len(input[0]) 

    index = 0
    # Find ALL the bits!
    for value in input:
        index = 0
        for bit in value:
            matrix[index] += bit
            index += 1
    return matrix


# Yes yes, it's manual and tedious and I should make a function. Yes yes, I suck.
oxy = input[:]

index = 0
while len(oxy) > 1:
    matrix = countbits(oxy)
    
    ones = matrix[index].count('1')
    zeroes = matrix[index].count('0')

    if ones >= zeroes:
        oxy = [ num for num in oxy if num[index] == '1' ]
    else:
        oxy = [ num for num in oxy if num[index] == '0' ]

    index += 1


co2 = input[:]

index = 0
while len(co2) > 1:
    matrix = countbits(co2)
    
    ones = matrix[index].count('1')
    zeroes = matrix[index].count('0')

    if zeroes <= ones:
        co2 = [ num for num in co2 if num[index] == '0' ]
    else:
        co2 = [ num for num in co2 if num[index] == '1' ]

    index += 1

print("Oxygen", oxy)    
print("CO2", co2)    
print("Life support rating", int(oxy[0],2) * int(co2[0],2))
