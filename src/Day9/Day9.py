import io
import re
import sys

with open("input.txt") as file:
    points = 0
    tags = 0
    garbage = False
    garbageCount = 0
    skip = False
    for char in file.read():
        if skip:
            skip = False
            continue
        elif char == '{' and garbage == False:
            tags += 1
        elif char == '}' and garbage == False:
            points += tags
            tags -= 1
        elif char == '!':
            skip = True
        elif char != '>' and garbage == True:
            garbageCount += 1
        elif char == '<':
            garbage = True
        elif char == '>':
            garbage = False

    print('Amount of points: ', points)
    print('Amount of non-canceled characters in the garbage: ',  garbageCount)
    file.close()